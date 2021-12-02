from pathlib import Path
from typing import Optional

import typer

from dvm.core import DartVersion, NoVersionError
from dvm.utils import filename_option

app = typer.Typer(help='Manage "minor" version')


NO_VERSION = (
    "The provided pubspec don't have a version defined. Please define it first."
)


@app.command(name="get", help='Get "minor" version')
def minor_get(
    filename: Optional[Path] = filename_option,
    verbose: bool = True,
):
    try:
        version = DartVersion.from_pubspec(str(filename))
        if verbose:
            typer.echo(f"Minor: {version.minor}")
        else:
            typer.echo(version.minor)
    except NoVersionError:
        typer.echo(NO_VERSION)
        raise typer.Exit(code=1)


VERSION_CHANGED = 'Version changed from "%s" to "%s".'


@app.command(name="up", help='Increase "minor" version by 1')
def minor_up(
    filename: Optional[Path] = filename_option,
    verbose: bool = True,
):
    try:
        new_ver = DartVersion.from_pubspec(str(filename))
        old_ver = DartVersion.copy(new_ver)
        new_ver.increase_minor_up()
        new_ver.to_pubspec(str(filename))
        if verbose:
            typer.echo(VERSION_CHANGED % (str(old_ver), str(new_ver)))
        else:
            typer.echo(new_ver)
    except NoVersionError:
        typer.echo(NO_VERSION)
        raise typer.Exit(code=1)


INVALID_INT = "Invalid integer."


@app.command(name="set", help='Set "minor" version')
def minor_set(
    minor: int = typer.Argument(..., help='"minor" version'),
    filename: Optional[Path] = filename_option,
    verbose: bool = True,
):
    try:
        new_ver = DartVersion.from_pubspec(str(filename))
        old_ver = DartVersion.copy(new_ver)
        minor = int(minor)
        new_ver.set_minor(minor)
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
