import os
from dotenv import load_dotenv,dotenv_values,find_dotenv
#loads .env file from the current directory or any parent directory
load_dotenv()
config = dotenv_values(".env")
api_key = config.get("GEMINI_API_KEY")
api_key = config.getenv("GEMINI_API_KEY","")
api_key = os.environ.get("GEMINI_API_KEY","")
