from binance.client import Client
from BinanceTrade.FutureTrade import *

try : 
    from config_dev import API_BINANCE_KEY , API_BINANCE_SECRET
except Exception:
    from config_prod import API_BINANCE_KEY , API_BINANCE_SECRET

# from DB.Firebasedb import GetDataBotsetting

client = Client( API_BINANCE_KEY , API_BINANCE_SECRET )

def ReceiveSignals(signal_data_dict):

    """
    Example Data
    signal_data_dict
    {
        "message" : "CLOSE LONG",  ----> CLOSE or OPEN / LONG or SHORT
        "symbol" : "BTCUSDT"
    }
    """

    Signal_Type = signal_data_dict["ACTION"].split(" ")[0]
    Signal_Side = signal_data_dict["ACTION"].split(" ")[1]
    Signal_Size = 50
    Signal_Symbol = "BTCUSDT"

    msg = ""

    # ให้เป็น USDT 
    amount = Signal_Size

    if Signal_Type == "OPEN":
        PlaceOrderAtMarket(position=Signal_Side, symbol=Signal_Symbol, amount=amount, lev = 5)
        msg = "ทำการ {} Position ในฝั่ง {} คู่สินค้า {} ".format(Signal_Type,Signal_Side,Signal_Symbol)
    
    elif Signal_Type == "CLOSE":
        ClosePositionAtMarket(symbol=Signal_Symbol, positionSide=Signal_Side)
        msg = "ทำการ {} Position ในฝั่ง {} คู่สินค้า {} ".format(Signal_Type,Signal_Side,Signal_Symbol)
    
    return msg