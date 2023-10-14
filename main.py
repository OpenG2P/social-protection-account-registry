#!/usr/bin/env python3

# ruff: noqa: I001

from social_payments_account_registry.app import Initializer as SparInitializer
from openg2p_fastapi_auth.app import Initializer as AuthInitializer
from spar_mapper_g2p_connect.app import Initializer as SparG2pConnectMapperInitializer
from openg2p_common_g2pconnect_id_mapper.app import (
    Initializer as G2pConnectMapperInitializer,
)
from openg2p_fastapi_common.ping import PingInitializer

# from spar_mapper_g2p_connect.app import Initializer as SparG2PConnectMapperInitializer

main_init = SparInitializer()
AuthInitializer()
G2pConnectMapperInitializer()
SparG2pConnectMapperInitializer()
PingInitializer()

main_init.main()
