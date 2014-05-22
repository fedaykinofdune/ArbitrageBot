from PyRock import PyRock
from time import sleep

rock = PyRock('username','password', 'apikey')

# EURO -> LTC -> BTC -> EURO
LtcEurData = rock.MarketData('ltceur')
LtcBtcData = rock.MarketData('ltcbtc')
BtcEurData = rock.MarketData('btceur')

LTC = 5

print 'Euro -> Ltc -> Btc -> Euro'
print 'Trading 5 LTC'
EuroSpentForLtc = float(LtcEurData['result'][0]['ask']) * LTC * 1.01
print 'Euro spent for 5 LTC: '+str(EuroSpentForLtc)
BtcAmount = float(LtcBtcData['result'][0]['bid']) * LTC * 0.99
print 'Buying BTC for LTC: '+str(BtcAmount)
EuroEnd = float(BtcEurData['result'][0]['bid']) * BtcAmount * 0.99
print 'Euro at the end: '+str(EuroEnd)+'\n'

# -------- #
sleep(2)
# -------- #

# EURO -> XRP -> BTC -> EURO
EurXrpData = rock.MarketData('eurxrp')
BtcXrpData = rock.MarketData('btcxrp')
BtcEurData = rock.MarketData('btceur')

EUR = 35

print 'Euro -> Xrp -> Btc -> Euro'
print 'Trading euro: '+str(EUR)
XrpAmount = float(EurXrpData['result'][0]['bid']) * EUR * 0.99
print 'Ottengo Xrp: '+str(XrpAmount)
BtcAmount = XrpAmount * 0.99 / float(BtcXrpData['result'][0]['ask']) 
print 'Compro Btc per Xrp: '+str(BtcAmount)
EuroEnd = float(BtcEurData['result'][0]['bid']) * BtcAmount * 0.99
print 'Euro alla fine: '+str(EuroEnd)+'\n'

