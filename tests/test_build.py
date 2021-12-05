from dart_version_manager.main import app
from typer.testing import CliRunner

from .config import (
    BUILD,
    BUILD_NUM,
    BUILD_TEMPLATE,
    MAJOR,
    MINOR,
    PATCH,
    PRE_RELEASE,
    build_version,
    ensure_edit,
    prepare_tmp_pubspec,
)

runner = CliRunner()


def test_build_get(tmpdir):
    pubspec = prepare_tmp_pubspec(tmpdir)
    result = runner.invoke(app=app, args=["build", "get", pubspec, "--no-verbose"])
    assert result.exit_code == 0
    assert f"{BUILD}\n" == result.stdout


def test_build_set(tmpdir):
    pubspec = prepare_tmp_pubspec(tmpdir)
    new_build = "web"
    new_version = build_version(MAJOR, MINOR, PATCH, PRE_RELEASE, new_build)
    result = runner.invoke(
        app=app, args=["build", "set", new_build, pubspec, "--no-verbose"]
    )
    assert result.exit_code == 0
    assert f"{new_version}\n" == result.stdout
    ensure_edit(pubspec, new_version)


def test_build_up(tmpdir):
    pubspec = prepare_tmp_pubspec(tmpdir)
    new_version = build_version(
        MAJOR, MINOR, PATCH, PRE_RELEASE, BUILD_TEMPLATE % (BUILD_NUM + 1)
    )
    result = runner.invoke(app=app, args=["build", "up", pubspec, "--no-verbose"])
    assert result.exit_code == 0
    assert f"{new_version}\n" == result.stdout
    ensure_edit(pubspec, new_version)
