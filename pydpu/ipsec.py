# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.

import grpc

from .proto.ipsec import ipsec_pb2, ipsec_pb2_grpc


def get_stats():
    print(
        "tbd",
        grpc.StatusCode.UNIMPLEMENTED,
        ipsec_pb2.IPsecStatsReq(),
        ipsec_pb2_grpc.IPsecStub(),
    )


def create_new_tunnel():
    print(
        "tbd",
        grpc.StatusCode.UNIMPLEMENTED,
        ipsec_pb2.IPsecStatsReq(),
        ipsec_pb2_grpc.IPsecStub(),
    )
