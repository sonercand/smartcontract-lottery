from scripts.helpers import get_account, get_contract, fund_with_link
from brownie import Lottery, network, config
import time


def deploy_lottery():

    account = get_account()
    lottery = Lottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deployed lottery")
    return lottery


def start_lottery():
    account = get_account()
    lottery = Lottery[-1]
    st_txn = lottery.startLottery({"from": account})
    st_txn.wait(1)
    print("lottery started")


def enter_lottery():
    account = get_account()
    lottery = Lottery[-1]
    val = lottery.getEnteranceFee() + 10000000
    tx = lottery.enter({"from": account, "value": val})


def end_lottery():
    account = get_account()
    lottery = Lottery[-1]
    tx = fund_with_link(lottery.address)
    tx.wait(1)
    end_txn = lottery.endLottery({"from": account})
    end_txn.wait(1)
    time.sleep(60)
    print(f"{lottery.recentWinner()} is the winner!")


def main():
    deploy_lottery()
    start_lottery()
    enter_lottery()
    end_lottery()
