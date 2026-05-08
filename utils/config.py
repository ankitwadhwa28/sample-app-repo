import os
from dotenv import load_dotenv

load_dotenv()

PRACTICE_BASE_URL = os.getenv("PRACTICE_BASE_URL", "https://practice.expandtesting.com")
BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
SLOW_MO = int(os.getenv("SLOW_MO", "0"))
TIMEOUT = int(os.getenv("TIMEOUT", "30000"))
