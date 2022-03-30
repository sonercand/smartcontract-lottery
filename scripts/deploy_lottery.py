from operator import ge
from scripts.helpers import get_account, get_contract
from brownie import Lottery


def deploy_lottery():

    account = get_account()
    lottery = Lottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
    )


def main():
    deploy_lottery()
