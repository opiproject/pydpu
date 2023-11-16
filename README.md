# pydpu

[![License](https://img.shields.io/github/license/opiproject/pydpu?style=flat&color=blue&label=License)](https://github.com/opiproject/pydpu/blob/main/LICENSE)
[![Pulls](https://img.shields.io/docker/pulls/opiproject/pydpu.svg?logo=docker&style=flat&label=Pulls)](https://hub.docker.com/r/opiproject/pydpu)
[![PyPI](https://img.shields.io/pypi/v/pydpu)](https://pypi.org/project/pydpu/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/opiproject/pydpu/branch/main/graph/badge.svg)](https://codecov.io/gh/opiproject/pydpu)
[![Linters](https://github.com/opiproject/pydpu/actions/workflows/linters.yml/badge.svg)](https://github.com/opiproject/pydpu/actions/workflows/linters.yml)
[![CodeQL](https://github.com/opiproject/pydpu/actions/workflows/codeql.yml/badge.svg)](https://github.com/opiproject/pydpu/actions/workflows/codeql.yml)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/opiproject/pydpu/badge)](https://securityscorecards.dev/viewer/?platform=github.com&org=opiproject&repo=pydpu)
[![Docker](https://github.com/opiproject/pydpu/actions/workflows/docker.yaml/badge.svg)](https://github.com/opiproject/pydpu/actions/workflows/docker.yaml)
[![Tests](https://github.com/opiproject/pydpu/actions/workflows/python.yaml/badge.svg)](https://github.com/opiproject/pydpu/actions/workflows/python.yaml)
[![GitHub stars](https://img.shields.io/github/stars/opiproject/pydpu.svg?style=flat-square&label=github%20stars)](https://github.com/opiproject/pydpu)
[![GitHub Contributors](https://img.shields.io/github/contributors/opiproject/pydpu.svg?style=flat-square)](https://github.com/opiproject/pydpu/graphs/contributors)

Python library and cli to communicate with DPUs and IPUs

## I Want To Contribute

This project welcomes contributions and suggestions.  We are happy to have the Community involved via submission of **Issues and Pull Requests** (with substantive content or even just fixes). We are hoping for the documents, test framework, etc. to become a community process with active engagement.  PRs can be reviewed by by any number of people, and a maintainer may accept.

See [CONTRIBUTING](https://github.com/opiproject/opi/blob/main/CONTRIBUTING.md) and [GitHub Basic Process](https://github.com/opiproject/opi/blob/main/doc-github-rules.md) for more details.

## Installation

There are several ways of running this CLI.

### Docker

```sh
docker pull opiproject/pydpu:<version>
```

You can specify a version like `0.1.1` or use `latest` to get the most up-to-date version.

Run latest version of the CLI in a container:

```sh
docker run -it --rm --network=host opiproject/pydpu:latest --help
```

Replace `--help` with any `pydpu` command, without `pydpu` itself.

### PyPI

```sh
pip install pydpu
```

## Usage

### Version

To get version, run:

```sh
$ pydpu --version
dpu, version 0.1.1
```

### Redfish

To communicate over redfish, run:

```sh
pydpu --address=10.10.10.10 redfish --username root --password 0penBmc test
```

### Inventory

To get inventory, run:

```sh
pydpu --address=localhost:50151 inventory get
```

### Ipsec

To create a tunnel, run:

```sh
pydpu --address=localhost:50151 ipsec create-tunnel
```

To get statistics, run:

```sh
pydpu --address=localhost:50151 ipsec stats
```

### Storage

To create a subsystem, run:

```sh
pydpu --address=localhost:50151 storage subsystem
```

To create a controller, run:

```sh
pydpu --address=localhost:50151 storage controller
```

To create a namespace, run:

```sh
pydpu --address=localhost:50151 storage namespace
```

### Evpn

To create a logical bridge, run:

```sh
pydpu --address=localhost:50151 evpn bridge
```

To create a bridge port, run:

```sh
pydpu --address=localhost:50151 evpn port
```

To create a vrf, run:

```sh
pydpu --address=localhost:50151 evpn vrf
```

To create a svi, run:

```sh
pydpu --address=localhost:50151 evpn svi
```

## Packaging

This project uses [poetry](https://python-poetry.org/) to manage dependencies, build, etc.

## Releasing new versions

```sh
# Make sure you have dev dependencies installed
$ poetry install --group dev
# Use bump2version to update version strings and create a new tag
$ bump2version <patch|minor|major>
# Push new tag
$ git push --tags
# Create GitHub release
$ gh release create v$(poetry version -s) --generate-notes
```
