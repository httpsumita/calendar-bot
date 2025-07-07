🗓️ AI Calendar Bot
An intelligent calendar booking assistant that uses natural language processing to automatically schedule appointments in Google Calendar. Simply tell the bot what you want to book, and it will handle the rest!
✨ Features

Natural Language Processing: Book appointments using everyday language
Google Calendar Integration: Seamlessly creates events in your Google Calendar
Smart Intent Recognition: Automatically detects booking, canceling, or checking requests
Flexible Date/Time Parsing: Understands various time formats and relative dates
AI-Powered: Uses Mistral AI through OpenRouter for intelligent text processing

🚀 Quick Start
Prerequisites

Python 3.8 or higher
Google Cloud Platform account
OpenRouter API account
Google Calendar API enabled

Installation

Clone the repository
git clone https://github.com/yourusername/ai-calendar-bot.git
cd ai-calendar-bot

Install dependencies
pip install -r requirements.txt

Set up environment variables


Run the backend
uvicorn backend.main:app --reload
Run the frontend
streamlit run frontend/app.py




🛠️ Setup Guide
1. Google Calendar API Setup

Create a Google Cloud Project

Go to Google Cloud Console
Create a new project or select an existing one


Enable Google Calendar API

Navigate to APIs & Services → Library
Search for "Google Calendar API"
Click "Enable"


Create Service Account

Go to APIs & Services → Credentials
Click "Create Credentials" → "Service Account"
Fill in the details and create
Download the JSON key file


Share Calendar with Service Account

Open Google Calendar
Go to Settings → Settings for my calendars
Click on your calendar → "Share with specific people"
Add your service account email with "Make changes to events" permission



2. OpenRouter API Setup

Create an account at OpenRouter
Get your API key from the dashboard
Add credits to your account for API usage

3. Environment Configuration
Create a .env file in your project root:
bash# Google Calendar Configuration
GOOGLE_CALENDAR_ID=your-calendar-id@gmail.com
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account-key.json

# OpenRouter Configuration
OPENROUTER_API_KEY=your_openrouter_api_key_here
