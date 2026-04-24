from ai_automation_lab.main import build_message


def test_build_message() -> None:
    assert build_message() == "AI Automation Lab is ready."
