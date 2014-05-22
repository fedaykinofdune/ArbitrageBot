import urllib, json
import time
from collections import Counter
import datetime



def MarketDataCryptsy():
    Url = "http://pubapi.cryptsy.com/api.php?method=marketdatav2"
    response = urllib.urlopen(Url)
    MarketData = json.loads(response.read())
    return MarketData

Cryptsy = MarketDataCryptsy()
codes = []
for market in Cryptsy['return']['markets']:
    code = Cryptsy['return']['markets'][market]['label']
    codes.append(code[:code.index('/')])
ListCryptsy = [k for k,v in Counter(codes).items() if v>1]
print 'list of currency on /BTC market AND /LTC market on MINTPAL'
for i in range(len(ListCryptsy)):
    try:
        print '\033[1;42m'+ListCryptsy[i]+'\033[1;m'
        # parto con 1 BTC
        BTC = 1
        print 'START: BTC -> LTC -> '+ListCryptsy[i]+' -> BTC'
        Ltc = BTC/float(Cryptsy['return']['markets']['LTC/BTC']['sellorders'][0]['price'])
        FeeLtcBtc = float(Cryptsy['return']['markets']['LTC/BTC']['sellorders'][0]['price']) * Ltc * 0.002
        Coins = Ltc/float(Cryptsy['return']['markets'][ListCryptsy[i]+'/LTC']['sellorders'][0]['price'])
        FeeCoinsLtcInBtc = float(Cryptsy['return']['markets'][ListCryptsy[i]+'/LTC']['sellorders'][0]['price']) * Coins * 0.002 * float(Cryptsy['return']['markets']['LTC/BTC']['lasttradeprice'])
        BtcForCoin = float(Cryptsy['return']['markets'][ListCryptsy[i]+'/BTC']['buyorders'][0]['price'])*Coins
        FeeCoinsBtc = BtcForCoin * 0.003
        TotalFee = FeeLtcBtc + FeeCoinsLtcInBtc + FeeCoinsBtc
        print str(BTC)+' BTC traded with '+str(Ltc)+' LTC at price: '+str(Cryptsy['return']['markets']['LTC/BTC']['sellorders'][0]['price'])
        print str(Ltc)+' Ltc traded with '+str(Coins)+' '+ListCryptsy[i]+' at price: '+str(Cryptsy['return']['markets'][ListCryptsy[i]+'/LTC']['sellorders'][0]['price'])
        print 'Total BTC received: '+str(BtcForCoin)
        print 'Total Fee: '+str(TotalFee)
        print str(Coins)+' '+ListCryptsy[i]+' traded with '+str(BtcForCoin-TotalFee)+' BTC at price: '+str(Cryptsy['return']['markets'][ListCryptsy[i]+'/BTC']['sellorders'][0]['price'])
        
        if BtcForCoin - TotalFee > BTC:
            print '\033[1;42mPossibility of arbitrage\033[1;m'
            timestamp = int(time.time())
            myfile = open(str(timestamp)+'.txt', 'w')
            myfile.write('ON CRYPTSY \n'+'At time: '+str(datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))+'\n'+'Trading arbitrage on '+ListCryptsy[i]+', with a possible gain of '+str(BtcForCoin-TotalFee-BTC)+' if '+str(BTC)+' BTC traded.')
            myfile.close()
            
        print ''
    except:
        print 'pay attention to '+ListCryptsy[i]
        print ''



        
