# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.

import grpc

from .proto.v1 import ipsec_pb2


def get_stats():
    print(
        "tbd",
        grpc.StatusCode.UNIMPLEMENTED,
        ipsec_pb2.IPsecStatsReq(),
    )


def create_new_tunnel():
    print(
        "tbd",
        grpc.StatusCode.UNIMPLEMENTED,
        ipsec_pb2.IPsecStatsReq(),
    )
