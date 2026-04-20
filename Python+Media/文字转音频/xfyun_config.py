import os
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
AUDIO_DIR = BASE_DIR / "audio"


def require_env(name):
    value = os.getenv(name)
    if value:
        return value
    raise RuntimeError(
        f"Missing environment variable: {name}. "
        f"Export it before running this script."
    )


def load_websocket_credentials():
    return {
        "APPID": require_env("XFYUN_APPID"),
        "APIKey": require_env("XFYUN_API_KEY"),
        "APISecret": require_env("XFYUN_API_SECRET"),
    }


def load_webapi_credentials():
    return {
        "APPID": require_env("XFYUN_APPID"),
        "API_KEY": require_env("XFYUN_API_KEY"),
    }


def ensure_audio_dir():
    AUDIO_DIR.mkdir(exist_ok=True)
    return AUDIO_DIR


def safe_output_name(text, default="output"):
    cleaned = re.sub(r"[^\w\-. ]+", "_", text).strip(" ._")
    return (cleaned[:80] or default)
