import os
from dotenv import load_dotenv

def load_env():
    # Load environment variables from the .env file
    load_dotenv()
    api_key = os.getenv("API")
    api_hash = os.getenv("API_HASH")
    bot_token = os.getenv("BOT_API_TOKEN")
    debug_mode = os.getenv("DEBUG")

    return api_key, api_hash, bot_token, debug_mode

