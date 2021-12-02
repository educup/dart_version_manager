import re
import yaml


class NoVersionError(ValueError):
    def __init__(
        self,
    ) -> None:
        super().__init__("No version detected.")


class InvalidDataError(ValueError):
    def __init__(
        self,
    ) -> None:
        super().__init__("Invalid data.")


class Version:
    def __init__(
        self,
        major: int = 0,
        minor: int = 0,
        patch: int = 0,
        pre_release: str = "",
        build: str = "",
    ) -> None:
        self.set_major(major)
        self.set_minor(minor)
        self.set_patch(patch)
        self.set_pre_release(pre_release)
        self.set_build(build)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        pre = f"-{self.pre_release}" if self.pre_release else ""
        build = f"+{self.build}" if self.build else ""
        return f"{self.major}.{self.minor}.{self.patch}{pre}{build}"

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Version) and str(self) == str(o)

    def increase_major_up(self) -> None:
        self.major += 1
        self.minor = 0
        self.patch = 0
        self.pre_release = ""
        self.build = ""
        return self

    def increase_minor_up(self) -> None:
        self.minor += 1
        self.patch = 0
        self.pre_release = ""
        self.build = ""
        return self

    def increase_patch_up(self) -> None:
        self.patch += 1
        self.pre_release = ""
        self.build = ""
        return self

    def set_major(self, major) -> None:
        try:
            self.major = int(major)
        except TypeError:
            self.major = 0

    def set_minor(self, minor) -> None:
        try:
            self.minor = int(minor)
        except TypeError:
            self.minor = 0

    def set_patch(self, patch) -> None:
        try:
            self.patch = int(patch)
        except TypeError:
            self.patch = 0

    def set_pre_release(self, pre_release: str = "") -> None:
        self.pre_release = pre_release if pre_release is not None else ""

    def set_build(self, build: str = "") -> None:
        self.build = build if build is not None else ""

    @classmethod
    def copy(cls, original):
        copy = cls.parse_version(str(original))
        return copy

    @classmethod
    def parse_version(cls, data: str):
        data = data.strip()

        if not data:
            return cls()

        expr = r"^([0-9]+)\.([0-9]+)\.([0-9]+)(-[\w|\.]+)?(\+[\w|\.]+)?$"
        major = 0
        minor = 0
        patch = 1
        build = ""
        pre_release = ""
        try:
            major, minor, patch, pre_release, build = re.findall(expr, data)[0]
            pre_release = pre_release[1:]
            build = build[1:]
            return cls(
                major=major,
                minor=minor,
                patch=patch,
                build=build,
                pre_release=pre_release,
            )
        except Exception:
            raise InvalidDataError()


class DartVersion(Version):
    def increase_pre_release_up(self):
        nums = re.findall(r"[0-9]+", self.pre_release)
        first_num = 1
        if nums:
            first_num = int(nums[0])
            new_num = first_num + 1
            parts = self.pre_release.split(str(first_num), 1)
            self.pre_release = str(new_num).join(parts)
        else:
            self.pre_release = (
                f"{self.pre_release}.{first_num}"
                if self.pre_release
                else str(first_num)
            )
        return self

    def increase_build_up(
        self,
    ):
        nums = re.findall(r"[0-9]+", self.build)
        first_num = 1
        if nums:
            first_num = int(nums[0])
            new_num = first_num + 1
            parts = self.build.split(str(first_num), 1)
            self.build = str(new_num).join(parts)
        else:
            self.build = f"{self.build}.{first_num}" if self.build else str(first_num)
        return self

    def to_pubspec(self, file_name):
        with open(file_name, "r") as pubspec:
            pubspec_raw_data = pubspec.read()

        version_raw_data = re.findall(r"version:(.*)", pubspec_raw_data)[:1]

        if not version_raw_data:
            raise NoVersionError()

        pubspec_raw_data_edited = pubspec_raw_data.replace(
            f"version:{version_raw_data[0]}", f"version: {self}", 1
        )

        with open(file_name, "w") as new_pubspec:
            new_pubspec.write(pubspec_raw_data_edited)

    @classmethod
    def from_pubspec(cls, file_name):
        version_data = ""
        with open(file_name, "r") as pubspec:
            pubspec_data = yaml.safe_load(pubspec)
            if "version" in pubspec_data:
                version_data = pubspec_data["version"]
            else:
                raise NoVersionError()
        return cls.parse_version(version_data)
