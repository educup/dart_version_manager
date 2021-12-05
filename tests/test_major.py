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


def test_major_get(tmpdir):
    pubspec = prepare_tmp_pubspec(tmpdir)
    result = runner.invoke(app=app, args=["major", "get", pubspec, "--no-verbose"])
    assert result.exit_code == 0
    assert f"{MAJOR}\n" == result.stdout


def test_major_set(tmpdir):
    pubspec = prepare_tmp_pubspec(tmpdir)
    new_major = 2
    new_version = build_version(new_major, MINOR, PATCH, PRE_RELEASE, BUILD)
    result = runner.invoke(
        app=app, args=["major", "set", str(new_major), pubspec, "--no-verbose"]
    )
    assert result.exit_code == 0
    assert f"{new_version}\n" == result.stdout
    ensure_edit(pubspec, new_version)


def test_major_up(tmpdir):
    pubspec = prepare_tmp_pubspec(tmpdir)
    new_version = build_version(MAJOR + 1, 0, 0, "", "")
    result = runner.invoke(app=app, args=["major", "up", pubspec, "--no-verbose"])
    assert result.exit_code == 0
    assert f"{new_version}\n" == result.stdout
    ensure_edit(pubspec, new_version)
