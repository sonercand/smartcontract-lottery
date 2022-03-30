from brownie import Lottery, accounts, config, network
from web3 import Web3

# current value of usd ~ 0.015
current_value_of_usd = 0.015
delta = 0.03
global current_value_of_usd_hb
current_value_of_usd_hb = current_value_of_usd + delta
global current_value_of_usd_lb
current_value_of_usd_lb = current_value_of_usd - delta


def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    val = lottery.getEnteranceFee()
    val = Web3.fromWei(val, "ether")
    assert val > current_value_of_usd_lb
    assert val < current_value_of_usd_hb
