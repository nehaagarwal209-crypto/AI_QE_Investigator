"""Minimal entry point for the investigator app.

The real investigation workflow (driving test-world, collecting evidence,
persisting it under data/) lands here as it is designed.
"""

__version__ = "0.0.1"


def main() -> str:
    """Return the investigator status banner."""
    return f"investigator {__version__}: stub entry point - no investigation configured yet"


if __name__ == "__main__":
    print(main())