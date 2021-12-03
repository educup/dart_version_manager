# `Dart Package Manager`

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Test](https://github.com/educup/dvm/workflows/CI/badge.svg)](https://github.com/educup/dvm/actions?query=workflow%3ACI)
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
$ dvm [OPTIONS] COMMAND [ARGS]...
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

## `dvm build`

Manage "build" tag

**Usage**:

```console
$ dvm build [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Get "build" tag
* `set`: Set "build" tag
* `up`: Increase "build" tag's first detected number...

### `dvm build get`

Get "build" tag

**Usage**:

```console
$ dvm build get [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `dvm build set`

Set "build" tag

**Usage**:

```console
$ dvm build set [OPTIONS] BUILD [FILENAME]
```

**Arguments**:

* `BUILD`: "build" tag  [required]
* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `dvm build up`

Increase "build" tag's first detected number by 1

**Usage**:

```console
$ dvm build up [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

## `dvm get`

Get project version

**Usage**:

```console
$ dvm get [OPTIONS] [PUBSPEC_FILE]
```

**Arguments**:

* `[PUBSPEC_FILE]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

## `dvm major`

Manage "major" version

**Usage**:

```console
$ dvm major [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Get "major" version
* `set`: Set "major" version
* `up`: Increase "major" version by 1

### `dvm major get`

Get "major" version

**Usage**:

```console
$ dvm major get [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `dvm major set`

Set "major" version

**Usage**:

```console
$ dvm major set [OPTIONS] MAJOR [FILENAME]
```

**Arguments**:

* `MAJOR`: "major" version  [required]
* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `dvm major up`

Increase "major" version by 1

**Usage**:

```console
$ dvm major up [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--keep-pre-release / --no-keep-pre-release`: [default: False]
* `--keep-build / --no-keep-build`: [default: False]
* `--help`: Show this message and exit.

## `dvm minor`

Manage "minor" version

**Usage**:

```console
$ dvm minor [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Get "minor" version
* `set`: Set "minor" version
* `up`: Increase "minor" version by 1

### `dvm minor get`

Get "minor" version

**Usage**:

```console
$ dvm minor get [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `dvm minor set`

Set "minor" version

**Usage**:

```console
$ dvm minor set [OPTIONS] MINOR [FILENAME]
```

**Arguments**:

* `MINOR`: "minor" version  [required]
* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `dvm minor up`

Increase "minor" version by 1

**Usage**:

```console
$ dvm minor up [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--keep-pre-release / --no-keep-pre-release`: [default: False]
* `--keep-build / --no-keep-build`: [default: False]
* `--help`: Show this message and exit.

## `dvm patch`

Manage "patch"

**Usage**:

```console
$ dvm patch [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Get "patch"
* `set`: Set "patch"
* `up`: Increase "patch" by 1

### `dvm patch get`

Get "patch"

**Usage**:

```console
$ dvm patch get [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `dvm patch set`

Set "patch"

**Usage**:

```console
$ dvm patch set [OPTIONS] PATCH [FILENAME]
```

**Arguments**:

* `PATCH`: "patch" number  [required]
* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `dvm patch up`

Increase "patch" by 1

**Usage**:

```console
$ dvm patch up [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--keep-pre-release / --no-keep-pre-release`: [default: False]
* `--keep-build / --no-keep-build`: [default: False]
* `--help`: Show this message and exit.

## `dvm pre-release`

Manage "pre-release" tag

**Usage**:

```console
$ dvm pre-release [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `get`: Get "pre-release" tag
* `set`: Set "pre-release" tag
* `up`: Increase "pre-release" tag's first detected...

### `dvm pre-release get`

Get "pre-release" tag

**Usage**:

```console
$ dvm pre-release get [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `dvm pre-release set`

Set "pre-release" tag

**Usage**:

```console
$ dvm pre-release set [OPTIONS] PRE_RELEASE [FILENAME]
```

**Arguments**:

* `PRE_RELEASE`: "pre-release" tag  [required]
* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

### `dvm pre-release up`

Increase "pre-release" tag's first detected number by 1

**Usage**:

```console
$ dvm pre-release up [OPTIONS] [FILENAME]
```

**Arguments**:

* `[FILENAME]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.

## `dvm set`

Set project version

**Usage**:

```console
$ dvm set [OPTIONS] VERSION [PUBSPEC_FILE]
```

**Arguments**:

* `VERSION`: The version to set in format "\<major\>.\<minor\>.\<patch\>-\<pre-release\>+\<build\>". The "major", "minor" and "patch" must be all integers. The "pre-release" and "build" are words splited by ".".  [required]
* `[PUBSPEC_FILE]`: Path to the pubspec file of the Dart project  [env var: DVM_FILENAME;default: .\pubspec.yaml]

**Options**:

* `--verbose / --no-verbose`: [default: True]
* `--help`: Show this message and exit.
