import os

def get_api_key():
    key = os.getenv("OPENWEATHER_API_KEY")
    if not key:
        raise RuntimeError(
            "Set the OPENWEATHER_API_KEY environment variable first."
        )
    return key