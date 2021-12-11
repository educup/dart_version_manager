from typer.testing import CliRunner

from dart_version_manager.main import app

from .config import VERSION, build_version, ensure_edit, prepare_tmp_pubspec

runner = CliRunner()


def test_get(tmpdir):
    pubspec = prepare_tmp_pubspec(tmpdir)
    result = runner.invoke(app=app, args=["get", pubspec, "--no-verbose"])
    assert result.exit_code == 0
    assert f"{VERSION}\n" == result.stdout


def test_set(tmpdir):
    pubspec = prepare_tmp_pubspec(tmpdir)
    new_version = build_version(2, 0, 4, "alpha", 56)
    result = runner.invoke(app=app, args=["set", new_version, pubspec, "--no-verbose"])
    assert result.exit_code == 0
    assert f"{new_version}\n" == result.stdout
    ensure_edit(pubspec, new_version)
