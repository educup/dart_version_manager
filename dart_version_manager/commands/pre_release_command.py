from pathlib import Path
from typing import Optional

import typer

from dart_version_manager.core import DartVersion, NoVersionError
from dart_version_manager.utils import filename_option

app = typer.Typer(help='Manage "pre-release" tag')


NO_VERSION = (
    "The provided pubspec don't have a version defined. Please define it first."
)


@app.command(name="get", help='Get "pre-release" tag')
def pre_release_get(
    filename: Optional[Path] = filename_option,
    verbose: bool = True,
):
    try:
        version = DartVersion.from_pubspec(str(filename))
        if verbose:
            typer.echo(f"pre-release: {version.pre_release}")
        else:
            typer.echo(version.pre_release)
    except NoVersionError:
        typer.echo(NO_VERSION)
        raise typer.Exit(code=1)


VERSION_CHANGED = 'Version changed from "%s" to "%s".'


@app.command(name="up", help='Increase "pre-release" tag\'s first detected number by 1')
def pre_release_up(
    filename: Optional[Path] = filename_option,
    verbose: bool = True,
):
    try:
        new_ver = DartVersion.from_pubspec(str(filename))
        old_ver = DartVersion.copy(new_ver)
        new_ver.increase_pre_release_up()
        new_ver.to_pubspec(str(filename))
        if verbose:
            typer.echo(VERSION_CHANGED % (str(old_ver), str(new_ver)))
        else:
            typer.echo(new_ver)
    except NoVersionError:
        typer.echo(NO_VERSION)
        raise typer.Exit(code=1)


INVALID_INT = "Invalid integer."


@app.command(name="set", help='Set "pre-release" tag')
def pre_release_set(
    pre_release: str = typer.Argument(..., help='"pre-release" tag'),
    filename: Optional[Path] = filename_option,
    verbose: bool = True,
):
    try:
        new_ver = DartVersion.from_pubspec(str(filename))
        old_ver = DartVersion.copy(new_ver)
        new_ver.set_pre_release(pre_release)
        new_ver.to_pubspec(str(filename))
        if verbose:
            typer.echo(VERSION_CHANGED % (str(old_ver), str(new_ver)))
        else:
            typer.echo(new_ver)
    except NoVersionError:
        typer.echo(NO_VERSION)
        raise typer.Exit(code=1)
    except ValueError:
        typer.echo(INVALID_INT)
        raise typer.Exit(code=1)
