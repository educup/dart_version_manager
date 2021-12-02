from dvm.commands.build_command import app as build_app
from dvm.commands.major_command import app as major_app
from dvm.commands.minor_command import app as minor_app
from dvm.commands.patch_command import app as patch_app
from dvm.commands.pre_release_command import app as pre_release_app

__all__ = [build_app, major_app, minor_app, patch_app, pre_release_app]
