import subprocess
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

subprocess.run(
    [
        "ffmpeg",
        "-y",
        "-f",
        "s16le",
        "-ar",
        "16000",
        "-i",
        str(BASE_DIR / "demo.pcm"),
        str(BASE_DIR / "aa.wav"),
    ],
    check=True,
)