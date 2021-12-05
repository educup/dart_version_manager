from dart_version_manager.main import app
from typer.testing import CliRunner

from .config import (
    BUILD,
    MAJOR,
    MINOR,
    PATCH,
    PRE_RELEASE,
    PRE_RELEASE_NUM,
    PRE_RELEASE_TEMPLATE,
    build_version,
    ensure_edit,
    prepare_tmp_pubspec,
)

runner = CliRunner()


def test_pre_release_get(tmpdir):
    pubspec = prepare_tmp_pubspec(tmpdir)
    result = runner.invoke(
        app=app, args=["pre-release", "get", pubspec, "--no-verbose"]
    )
    assert result.exit_code == 0
    assert f"{PRE_RELEASE}\n" == result.stdout


def test_pre_release_set(tmpdir):
    pubspec = prepare_tmp_pubspec(tmpdir)
    new_pre_release = "beta"
    new_version = build_version(MAJOR, MINOR, PATCH, new_pre_release, BUILD)
    result = runner.invoke(
        app=app, args=["pre-release", "set", new_pre_release, pubspec, "--no-verbose"]
    )
    assert result.exit_code == 0
    assert f"{new_version}\n" == result.stdout
    ensure_edit(pubspec, new_version)


def test_pre_release_up(tmpdir):
    pubspec = prepare_tmp_pubspec(tmpdir)
    new_version = build_version(
        MAJOR, MINOR, PATCH, PRE_RELEASE_TEMPLATE % (PRE_RELEASE_NUM + 1), BUILD
    )
    result = runner.invoke(app=app, args=["pre-release", "up", pubspec, "--no-verbose"])
    assert result.exit_code == 0
    assert f"{new_version}\n" == result.stdout
    ensure_edit(pubspec, new_version)
