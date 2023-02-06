# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.
FROM python:3.11.1-alpine

WORKDIR /src
COPY . /src/
RUN python3 -m pip install --no-cache-dir /src
