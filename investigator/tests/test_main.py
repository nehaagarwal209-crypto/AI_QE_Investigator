"""Tests for the investigator entry point."""

from app.main import __version__, main


def test_main_returns_versioned_banner():
    banner = main()
    assert banner.startswith("investigator")
    assert __version__ in banner


def test_version_is_set():
    assert __version__