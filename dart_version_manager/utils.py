from os.path import join

import typer

filename_option = typer.Argument(
    join(".", "pubspec.yaml"),
    exists=True,
    file_okay=True,
    dir_okay=False,
    writable=True,
    readable=True,
    resolve_path=True,
    help="Path to the pubspec file of the Dart project",
    envvar=["DVM_FILENAME"],
)
