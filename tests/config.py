def build_version(
    major,
    minor,
    patch,
    pre_release,
    build,
):
    version = f"{major}.{minor}.{patch}"
    version += f"-{pre_release}" if pre_release else ""
    version += f"+{build}" if build else ""
    return version


def ensure_edit(pubspec, new_version):
    with open("tests/pubspec.yaml", "r") as template:
        original = template.read()
    original = original % new_version
    with open(pubspec, "r") as file:
        new = file.read()
    assert original == new


MAJOR = 1
MINOR = 2
PATCH = 3
PRE_RELEASE_NUM = 4
PRE_RELEASE_TEMPLATE = "alpha.%s"
PRE_RELEASE = PRE_RELEASE_TEMPLATE % PRE_RELEASE_NUM
BUILD_NUM = 5
BUILD_TEMPLATE = "%s"
BUILD = BUILD_TEMPLATE % BUILD_NUM
VERSION = build_version(MAJOR, MINOR, PATCH, PRE_RELEASE, BUILD)


def prepare_tmp_pubspec(tmpdir):
    pubspec = tmpdir / "pubspec.yaml"
    with open("tests/pubspec.yaml", "r") as file:
        data = file.read()
    with open(pubspec, "w") as file:
        file.write(data % VERSION)
    return str(pubspec)
