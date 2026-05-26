from sandboas.main import run


def test_run_returns_ready_message() -> None:
    assert run() == "sandboas template is ready"

