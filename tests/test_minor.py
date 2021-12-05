from dart_version_manager.main import app
from typer.testing import CliRunner

from .config import (
    BUILD,
    MAJOR,
    MINOR,
    PATCH,
    PRE_RELEASE,
    build_version,
    ensure_edit,
    prepare_tmp_pubspec,
)

runner = CliRunner()


def test_minor_get(tmpdir):
    pubspec = prepare_tmp_pubspec(tmpdir)
    result = runner.invoke(app=app, args=["minor", "get", pubspec, "--no-verbose"])
    assert result.exit_code == 0
    assert f"{MINOR}\n" == result.stdout


def test_minor_set(tmpdir):
    pubspec = prepare_tmp_pubspec(tmpdir)
    new_minor = 2
    new_version = build_version(MAJOR, new_minor, PATCH, PRE_RELEASE, BUILD)
    result = runner.invoke(
        app=app, args=["minor", "set", str(new_minor), pubspec, "--no-verbose"]
    )
    assert result.exit_code == 0
    assert f"{new_version}\n" == result.stdout
    ensure_edit(pubspec, new_version)


def test_minor_up(tmpdir):
    pubspec = prepare_tmp_pubspec(tmpdir)
    new_version = build_version(MAJOR, MINOR + 1, 0, "", "")
    result = runner.invoke(app=app, args=["minor", "up", pubspec, "--no-verbose"])
    assert result.exit_code == 0
    assert f"{new_version}\n" == result.stdout
    ensure_edit(pubspec, new_version)
