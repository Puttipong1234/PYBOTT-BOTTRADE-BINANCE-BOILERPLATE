from flask import Flask , request , abort 
from linebot.exceptions import (
    InvalidSignatureError
)
import json

from BinanceTrade.Trade import ReceiveSignals
from line.notify import sendmsg

app = Flask(__name__)

#@app.route("/START/REBALANCEBOT/SYMBOL")

#@app.route("/STOP/REBALANCEBOT/SYMBOL")

@app.route("/SIGNALS" , methods=['POST'])
def SIGNALS_RECEIVER():
    if request.method == "POST":
        msg = request.data.decode("utf-8")
        json_msg = json.loads(msg)
        print(json_msg) # <-- dictionary

        # if GetDataBotsetting(key="run") == True:
        #     # get data firebase เพื่อดูว่า Autotrading = True??
        msg = ReceiveSignals(signal_data_dict = json_msg)

        sendmsg(msg=json_msg)
        sendmsg(msg=msg)

    return "200"

if __name__== "__main__":
    app.run(debug=True,port=8080)