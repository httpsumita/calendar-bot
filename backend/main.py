from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timedelta
import sys, os
import json
from backend.calendar_utils import create_event
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from agent import extract_booking_details

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

class BookingRequest(BaseModel):
    user_input: str

def safe_json_parse(response):
    if isinstance(response, str):
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            print(f"Could not parse JSON: {response}")
            return {}
    return response

@app.post("/extract")
def get_booking_details(data: BookingRequest):
    response = extract_booking_details(data.user_input)
    response = safe_json_parse(response)

    if "intent" in response and response["intent"] == "booking":
        try:
            # Parse datetime from model output
            # start_str = response["date"] + "T" + response["time"]  # → "2025-07-08T22:00"
            start_time = datetime.fromisoformat("time")
            duration = int(response["duration"])
            end_time = start_time + timedelta(minutes=duration)

            # Format to RFC3339 (Google Calendar expects this format)
            start_time_str = start_time.isoformat()
            end_time_str = end_time.isoformat()

            # Call calendar event creator
            event = create_event(start_time_str, end_time_str, response["title"])

            return {
                "response": response,
                "event_created": True,
                "event_id": event.get("id")
            }

        except Exception as e:
            return {
                "response": response,
                "event_created": False,
                "error": str(e)
            }
    else:
        return {
            "response": response,
            "event_created": False,
            "reason": "Intent was not 'booking'"
        }
