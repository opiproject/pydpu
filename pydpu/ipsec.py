# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.

import grpc

from .proto.v1 import ipsec_pb2, ipsec_pb2_grpc


def get_stats(address):
    channel = grpc.insecure_channel(address)
    stub = ipsec_pb2_grpc.IPsecStub(channel)
    a = stub.IPsecVersion(ipsec_pb2.IPsecVersionReq())
    b = stub.IPsecStats(ipsec_pb2.IPsecStatsReq())
    c = stub.IPsecListConns(ipsec_pb2.IPsecListConnsReq(ike="tun1_0_0"))
    d = stub.IPsecListSas(ipsec_pb2.IPsecListSasReq(ike="tun1_0_0"))
    e = stub.IPsecListCerts(ipsec_pb2.IPsecListCertsReq())
    print(a, b, c, d, e)


def create_new_tunnel(address):
    channel = grpc.insecure_channel(address)
    stub = ipsec_pb2_grpc.IPsecStub(channel)
    # connection_1 = stub.IPsecLoadConn(tun1_0_0)
    # connection_2 = stub.IPsecLoadConn(tun1_0_1)
    print(
        "tbd",
        stub,
        grpc.StatusCode.UNIMPLEMENTED,
        ipsec_pb2.IPsecStatsReq(),
    )
