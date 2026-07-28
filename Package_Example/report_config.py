from dotenv import load_dotenv
import os
load_dotenv() # reads .env into environment variables

def get_config():
    return {
        "title": os.getenv("APP_TITLE", "Untitled"),
        "author": os.getenv("AUTHOR", "Unknown")
    }
if __name__ == "__main__":
    print(get_config())