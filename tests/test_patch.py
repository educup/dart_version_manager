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


def test_patch_get(tmpdir):
    pubspec = prepare_tmp_pubspec(tmpdir)
    result = runner.invoke(app=app, args=["patch", "get", pubspec, "--no-verbose"])
    assert result.exit_code == 0
    assert f"{PATCH}\n" == result.stdout


def test_patch_set(tmpdir):
    pubspec = prepare_tmp_pubspec(tmpdir)
    new_patch = 2
    new_version = build_version(MAJOR, MINOR, new_patch, PRE_RELEASE, BUILD)
    result = runner.invoke(
        app=app, args=["patch", "set", str(new_patch), pubspec, "--no-verbose"]
    )
    assert result.exit_code == 0
    assert f"{new_version}\n" == result.stdout
    ensure_edit(pubspec, new_version)


def test_patch_up(tmpdir):
    pubspec = prepare_tmp_pubspec(tmpdir)
    new_version = build_version(MAJOR, MINOR, PATCH + 1, "", "")
    result = runner.invoke(app=app, args=["patch", "up", pubspec, "--no-verbose"])
    assert result.exit_code == 0
    assert f"{new_version}\n" == result.stdout
    ensure_edit(pubspec, new_version)
