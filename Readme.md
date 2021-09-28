## Procedure Production
ใช้ Command line ในการใส่คำสั่งตามเนื้อหานะครับ

### STEP 1 
- ติดตั้ง gitscm และ heroku cli : https://devcenter.heroku.com/articles/heroku-cli
- สร้างโฟลเดอแล้ว Clone Project
```
git clone https://github.com/Puttipong1234/PYBOTT-BOTTRADE-BINANCE-BOILERPLATE.git
cd PYBOTT-BOTTRADE-BINANCE-BOILERPLATE
```

### STEP 2

- ทำการ Deploy ไปที่ Heroku

```
heroku login
heroku create
```

- ทำการ Push Code ขึ้นไปบน Heroku

```
git branch //ดูชื่อ Branch
git add .
git commit -m "New Project"
git push heroku <ชื่อbranch (main , master)>
```

### STEP 3
SET ENV VAR พิมพ์คำสั่งใน Commandline โดยนำ ค่ามาใส่แทนตัว xxx

```
heroku config:set API_BINANCE_KEY=xxx
heroku config:set API_BINANCE_SECRET=xxx
heroku config:set LINE_NOTIFY_TOKEN=UPb02B1GXPIxerGrE6ivMy0Rt24XZN8cR9yz73rlYDD
```

### STEP 4
นำ URL ที่ได้ /SIGNALS ไปวางไว้ที่ ช่องสัญญาณ webhook Tradingview
ใส่ alerts message ไว้ดังนี้ (LEV,SYMBOL ปรับเปลี่ยนค่าได้)

```
{"ACTION":"{{strategy.order.comment}}","LEV":"10","SYMBOL":"BTCUSDT"}
```

เพิ่ม code ในการ alert สัญญาณ
- strategy entry ให้เพิ่ม arguement [comment = "OPEN LONG" or "OPEN SHORT" ]กรณีเปิดสัญญาณ บอทจะทำการปิด position binance ที่เปิดอยู่ก่อนเปิดใหม่เสมอ

- strategy exit ให้เพิ่ม [comment = "TPSL LONG" or "TPSL SHORT" ]
กรณีราคาวิ่งไปชน order ใน tradingivew จะสั่งให้บอทปิด position ใน binance

### STEP 5
รอสัญญาณเข้า เช็คข้อผิดพลาดต่างๆได้โดยใช้คำสั่ง
```
heroku logs --tail
```


## References - 
* binance API : https://python-binance.readthedocs.io/en/latest/
* binance Future Ref : https://binance-docs.github.io/apidocs/futures/en/#change-log
* binance Future SDK python with Example : https://github.com/Binance-docs/Binance_Futures_python