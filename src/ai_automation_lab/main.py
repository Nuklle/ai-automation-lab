"""Project entry point."""


def build_message() -> str:
    """Return a simple startup message for the CLI."""
    return "AI Automation Lab is ready."


def main() -> None:
    """Print the default startup message."""
    print(build_message())


if __name__ == "__main__":
    main()
