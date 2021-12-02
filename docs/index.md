# `Dart Package Manager`

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Test](https://github.com/educup/dvm/workflows/CI/badge.svg)](https://github.com/educup/dvm/actions?query=workflow%3ACI)
<!-- [![codecov](https://codecov.io/gh/educup/dvm/branch/main/graph/badge.svg?token=Z1MEEL3EAB)](https://codecov.io/gh/educup/dvm) -->
<!-- [![DeepSource](https://deepsource.io/gh/educup/dvm.svg/?label=active+issues)](https://deepsource.io/gh/educup/dvm/?ref=repository-badge) -->
[![Version](https://img.shields.io/pypi/v/dvm?color=%2334D058&label=Version)](https://pypi.org/project/dvm)
[![Last commit](https://img.shields.io/github/last-commit/educup/dvm.svg?style=flat)](https://github.com/educup/dvm/commits)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/educup/dvm)](https://github.com/educup/dvm/commits)
[![Github Stars](https://img.shields.io/github/stars/educup/dvm?style=flat&logo=github)](https://github.com/educup/dvm/stargazers)
[![Github Forks](https://img.shields.io/github/forks/educup/dvm?style=flat&logo=github)](https://github.com/educup/dvm/network/members)
[![Github Watchers](https://img.shields.io/github/watchers/educup/dvm?style=flat&logo=github)](https://github.com/educup/dvm)
[![Website](https://img.shields.io/website?up_message=online&url=https%3A%2F%2Feducup.github.io/dvm)](https://educup.github.io/dvm)
[![GitHub contributors](https://img.shields.io/github/contributors/educup/dvm)](https://github.com/educup/dvm/graphs/contributors)

Dart Version Manager CLI implemented with Python and Typer

**Usage**:

```console
$ Dart Package Manager [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `build`: Manage "build" tag
* `get`: Get project version
* `major`: Manage "major" version
* `minor`: Manage "minor" version
* `patch`: Manage "patch"
* `pre-release`: Manage "pre-release" tag
* `set`: Set project version

## `Dart Package Manager build`

Manage "build" tag

**Usage**:

```console
$ Dart Package Manager build [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Get "build" tag
* `set`: Set "build" tag
* `up`: Increase "build" tag's first detected number...

### `Dart Package Manager build get`

Get "build" tag

**Usage**:

```console
$ Dart Package Manager build get [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `Dart Package Manager build set`

Set "build" tag

**Usage**:

```console
$ Dart Package Manager build set [OPTIONS] BUILD [FILENAME]
```

**Arguments**:

* `BUILD`: "build" tag  [required]
* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `Dart Package Manager build up`

Increase "build" tag's first detected number by 1

**Usage**:

```console
$ Dart Package Manager build up [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

## `Dart Package Manager get`

Get project version

**Usage**:

```console
$ Dart Package Manager get [OPTIONS] [PUBSPEC_FILE]
```

**Arguments**:

* `[PUBSPEC_FILE]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

## `Dart Package Manager major`

Manage "major" version

**Usage**:

```console
$ Dart Package Manager major [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Get "major" version
* `set`: Set "major" version
* `up`: Increase "major" version by 1

### `Dart Package Manager major get`

Get "major" version

**Usage**:

```console
$ Dart Package Manager major get [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `Dart Package Manager major set`

Set "major" version

**Usage**:

```console
$ Dart Package Manager major set [OPTIONS] MAJOR [FILENAME]
```

**Arguments**:

* `MAJOR`: "major" version  [required]
* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `Dart Package Manager major up`

Increase "major" version by 1

**Usage**:

```console
$ Dart Package Manager major up [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

## `Dart Package Manager minor`

Manage "minor" version

**Usage**:

```console
$ Dart Package Manager minor [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Get "minor" version
* `set`: Set "minor" version
* `up`: Increase "minor" version by 1

### `Dart Package Manager minor get`

Get "minor" version

**Usage**:

```console
$ Dart Package Manager minor get [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `Dart Package Manager minor set`

Set "minor" version

**Usage**:

```console
$ Dart Package Manager minor set [OPTIONS] MINOR [FILENAME]
```

**Arguments**:

* `MINOR`: "minor" version  [required]
* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `Dart Package Manager minor up`

Increase "minor" version by 1

**Usage**:

```console
$ Dart Package Manager minor up [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

## `Dart Package Manager patch`

Manage "patch"

**Usage**:

```console
$ Dart Package Manager patch [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Get "patch"
* `set`: Set "patch"
* `up`: Increase "patch" by 1

### `Dart Package Manager patch get`

Get "patch"

**Usage**:

```console
$ Dart Package Manager patch get [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `Dart Package Manager patch set`

Set "patch"

**Usage**:

```console
$ Dart Package Manager patch set [OPTIONS] PATCH [FILENAME]
```

**Arguments**:

* `PATCH`: "patch" number  [required]
* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `Dart Package Manager patch up`

Increase "patch" by 1

**Usage**:

```console
$ Dart Package Manager patch up [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

## `Dart Package Manager pre-release`

Manage "pre-release" tag

**Usage**:

```console
$ Dart Package Manager pre-release [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Get "pre-release" tag
* `set`: Set "pre-release" tag
* `up`: Increase "pre-release" tag's first detected...

### `Dart Package Manager pre-release get`

Get "pre-release" tag

**Usage**:

```console
$ Dart Package Manager pre-release get [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `Dart Package Manager pre-release set`

Set "pre-release" tag

**Usage**:

```console
$ Dart Package Manager pre-release set [OPTIONS] PRE_RELEASE [FILENAME]
```

**Arguments**:

* `PRE_RELEASE`: "pre-release" tag  [required]
* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `Dart Package Manager pre-release up`

Increase "pre-release" tag's first detected number by 1

**Usage**:

```console
$ Dart Package Manager pre-release up [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

## `Dart Package Manager set`

Set project version

**Usage**:

```console
$ Dart Package Manager set [OPTIONS] VERSION [PUBSPEC_FILE]
```

**Arguments**:

* `VERSION`: The version to set in format "<major>.<minor>.<patch>-<pre-release>+<build>". The "major", "minor" and "patch" must be all integers. The "pre-release" and "build" are words splited by ".".  [required]
* `[PUBSPEC_FILE]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.
