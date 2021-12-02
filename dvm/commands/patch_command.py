from pathlib import Path
from typing import Optional

import typer

from dvm.core import DartVersion, NoVersionError
from dvm.utils import filename_option

app = typer.Typer(help='Manage "patch"')


NO_VERSION = (
    "The provided pubspec don't have a version defined. Please define it first."
)


@app.command(name="get", help='Get "patch"')
def patch_get(
    filename: Optional[Path] = filename_option,
    verbose: bool = True,
):
    try:
        version = DartVersion.from_pubspec(str(filename))
        if verbose:
            typer.echo(f"Patch: {version.patch}")
        else:
            typer.echo(version.patch)
    except NoVersionError:
        typer.echo(NO_VERSION)
        raise typer.Exit(code=1)


VERSION_CHANGED = 'Version changed from "%s" to "%s".'


@app.command(name="up", help='Increase "patch" by 1')
def patch_up(
    filename: Optional[Path] = filename_option,
    verbose: bool = True,
):
    try:
        new_ver = DartVersion.from_pubspec(str(filename))
        old_ver = DartVersion.copy(new_ver)
        new_ver.increase_patch_up()
        new_ver.to_pubspec(str(filename))
        if verbose:
            typer.echo(VERSION_CHANGED % (str(old_ver), str(new_ver)))
        else:
            typer.echo(new_ver)
    except NoVersionError:
        typer.echo(NO_VERSION)
        raise typer.Exit(code=1)


INVALID_INT = "Invalid integer."


@app.command(name="set", help='Set "patch"')
def patch_set(
    patch: int = typer.Argument(..., help='"patch" number'),
    filename: Optional[Path] = filename_option,
    verbose: bool = True,
):
    try:
        new_ver = DartVersion.from_pubspec(str(filename))
        old_ver = DartVersion.copy(new_ver)
        patch = int(patch)
        new_ver.set_patch(patch)
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
