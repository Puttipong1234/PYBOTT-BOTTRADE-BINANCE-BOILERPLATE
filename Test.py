from BinanceTrade.FutureTrade import *
from BinanceTrade.Trade import ReceiveSignals

if __name__ == "__main__":
    data = {
        "ACTION" : "TPSL LONG",
        "LEV" : "50",
        "SYMBOL":"BTCUSDT",
        }


    msg = ReceiveSignals(signal_data_dict= data )

    # from line.notify import notify
    # notify.send("TEST")


    # res = get_market_data_by_symbol(symbol = "BTCUSDT")
    # print(res["markPrice"])

    # change_leverage(symbol="BTCUSDT", lev=5)

    # balance = getAssetUSDT()
    # print(balance)

    # PlaceOrderAtMarket(
    #     position='SHORT',
    #     symbol='SOLUSDT', # 0.000....
    #     amount=15,
    # )

    # res = getPositionbySymbol(Symbol="BTCUSDT")
    # print(res['positionAmt'])

    # ClosePositionAtMarket(symbol="BTCUSDT", positionSide="SHORT")
