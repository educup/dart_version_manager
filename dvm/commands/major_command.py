from pathlib import Path
from typing import Optional

import typer

from dvm.core import DartVersion, NoVersionError
from dvm.utils import filename_option

app = typer.Typer(help='Manage "major" version')


NO_VERSION = (
    "The provided pubspec don't have a version defined. Please define it first."
)


@app.command(name="get", help='Get "major" version')
def major_get(
    filename: Optional[Path] = filename_option,
    verbose: bool = True,
):
    try:
        version = DartVersion.from_pubspec(str(filename))
        if verbose:
            typer.echo(f"Major: {version.major}")
        else:
            typer.echo(version.major)
    except NoVersionError:
        typer.echo(NO_VERSION)
        raise typer.Exit(code=1)


VERSION_CHANGED = 'Version changed from "%s" to "%s".'


@app.command(name="up", help='Increase "major" version by 1')
def major_up(
    filename: Optional[Path] = filename_option,
    verbose: bool = True,
    keep_pre_release: bool = False,
    keep_build: bool = False,
):
    try:
        new_ver = DartVersion.from_pubspec(str(filename))
        old_ver = DartVersion.copy(new_ver)
        new_ver.increase_major_up(
            keep_build=keep_build,
            keep_pre_release=keep_pre_release,
        )
        new_ver.to_pubspec(str(filename))
        if verbose:
            typer.echo(VERSION_CHANGED % (str(old_ver), str(new_ver)))
        else:
            typer.echo(new_ver)
    except NoVersionError:
        typer.echo(NO_VERSION)
        raise typer.Exit(code=1)


INVALID_INT = "Invalid integer."


@app.command(name="set", help='Set "major" version')
def major_set(
    major: int = typer.Argument(..., help='"major" version'),
    filename: Optional[Path] = filename_option,
    verbose: bool = True,
):
    try:
        new_ver = DartVersion.from_pubspec(str(filename))
        old_ver = DartVersion.copy(new_ver)
        major = int(major)
        new_ver.set_major(major)
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
