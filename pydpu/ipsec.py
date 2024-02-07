# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2022 Dell Inc, or its subsidiaries.

import grpc

from .proto.v1 import ipsec_pb2, ipsec_pb2_grpc


def get_stats(address):
    with grpc.insecure_channel(address) as channel:
        stub = ipsec_pb2_grpc.IPsecServiceStub(channel)
        a = stub.IPsecVersion(ipsec_pb2.IPsecVersionRequest())
        b = stub.IPsecStats(ipsec_pb2.IPsecStatsRequest())
        c = stub.IPsecListConns(ipsec_pb2.IPsecListConnsRequest(ike="tun1_0_0"))
        d = stub.IPsecListSas(ipsec_pb2.IPsecListSasRequest(ike="tun1_0_0"))
        e = stub.IPsecListCerts(ipsec_pb2.IPsecListCertsRequest())
        print(a, b, c, d, e)


def create_new_tunnel(address):
    with grpc.insecure_channel(address) as channel:
        stub = ipsec_pb2_grpc.IPsecServiceStub(channel)
        # connection_1 = stub.IPsecLoadConn(tun1_0_0)
        # connection_2 = stub.IPsecLoadConn(tun1_0_1)
        print(
            "tbd",
            stub,
            grpc.StatusCode.UNIMPLEMENTED,
            ipsec_pb2.IPsecStatsRequest(),
        )
