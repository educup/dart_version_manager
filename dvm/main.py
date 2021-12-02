from pathlib import Path
from typing import Optional

import typer

from dvm.core import DartVersion, NoVersionError, InvalidDataError
from dvm.commands import major_app, minor_app, patch_app
from dvm.utils import filename_option

app = typer.Typer(help="Dart Version Manager CLI implemented with Python and Typer")

app.add_typer(major_app, name="major")
app.add_typer(minor_app, name="minor")
app.add_typer(patch_app, name="patch")


NO_VERSION = (
    "The provided pubspec don't have a version defined. Please define it first."
)


@app.command(name="get", help="Get project version")
def get(
    pubspec_file: Optional[Path] = filename_option,
    verbose: bool = True,
):
    try:
        version = DartVersion.from_pubspec(str(pubspec_file))
        if verbose:
            typer.echo(f"Version: {version}")
        else:
            typer.echo(version)
    except NoVersionError:
        typer.echo(NO_VERSION)
        raise typer.Exit(code=1)


SET_ARG_HELP_1 = (
    'The version to set in format "<major>.<minor>.<patch>-<pre-release>+<build>". '
)
SET_ARG_HELP_2 = 'The "major", "minor" and "patch" must be all integers. '
SET_ARG_HELP_3 = 'The "pre-release" and "build" are words splited by ".".'
SET_ARG_HELP = SET_ARG_HELP_1 + SET_ARG_HELP_2 + SET_ARG_HELP_3

INVALID_FORMAT = 'The version format is invalid. See "dvm set --help".'

VERSION_CHANGED = 'Version changed from "%s" to "%s".'


@app.command(name="set", help="Set project version")
def set(
    version: str = typer.Argument(
        ...,
        help=SET_ARG_HELP,
    ),
    pubspec_file: Optional[Path] = filename_option,
    verbose: bool = True,
):
    try:
        new_ver = DartVersion.parse_version(version)
        old_ver = DartVersion.from_pubspec(pubspec_file)
        new_ver.to_pubspec(pubspec_file)
        if verbose:
            typer.echo(VERSION_CHANGED % (str(old_ver), str(new_ver)))
        else:
            typer.echo(new_ver)
    except InvalidDataError:
        typer.echo(INVALID_FORMAT)
        raise typer.Exit(code=1)
    except NoVersionError:
        typer.echo(NO_VERSION)
        raise typer.Exit(code=1)
