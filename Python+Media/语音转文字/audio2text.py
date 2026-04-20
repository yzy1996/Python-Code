import argparse
from pathlib import Path

try:
    import whisper
except ImportError as exc:  # pragma: no cover
    raise RuntimeError(
        "Missing dependency: openai-whisper. Install with `pip install openai-whisper`."
    ) from exc


DEFAULT_MODEL = "small"


def transcribe_offline(audio_file, model, language=None, prompt=None, temperature=None):
    whisper_model = whisper.load_model(model)
    kwargs = {}
    if language:
        kwargs["language"] = language
    if prompt:
        kwargs["initial_prompt"] = prompt
    if temperature is not None:
        kwargs["temperature"] = temperature

    result = whisper_model.transcribe(str(audio_file), **kwargs)
    text = result.get("text", "")
    return text.strip()


def parse_args():
    parser = argparse.ArgumentParser(description="Speech-to-text with offline OpenAI Whisper models.")
    parser.add_argument("audio_file", help="Path to input audio file (wav/mp3/m4a/mp4, etc).")
    parser.add_argument("-o", "--output", help="Path to save transcript text. Default: <audio_file_stem>.txt")
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=(
            "Whisper model size/name, e.g. tiny, base, small, medium, large "
            f"(default: {DEFAULT_MODEL})"
        ),
    )
    parser.add_argument("--language", help="Optional language hint, e.g. zh or en.")
    parser.add_argument("--prompt", help="Optional initial prompt to guide transcription style.")
    parser.add_argument(
        "--temperature",
        type=float,
        help="Optional sampling temperature.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    audio_file = Path(args.audio_file).expanduser().resolve()
    if not audio_file.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_file}")

    transcript = transcribe_offline(
        audio_file=audio_file,
        model=args.model,
        language=args.language,
        prompt=args.prompt,
        temperature=args.temperature,
    )

    output_path = Path(args.output).expanduser().resolve() if args.output else audio_file.with_suffix(".txt")
    output_path.write_text(transcript, encoding="utf-8")
    print(transcript)
    print(f"Saved transcript to: {output_path}")


if __name__ == "__main__":
    main()
