# Arbitrage Bot #

This project works on a simple idea: maybe, on some of the biggest exchanges, is possible to do some arbitrage and gain fiat currencies or bitcoin with no risk. By saying that, I mean some arbitrage on bids/asks on a single exchange: maybe if you buy LTC with BTC, then some AUR with LTC, then some BTC with AUR you may have more bitcoins than at the start of the trades!

This bot is far from completed: I want to make it run as a cron job almost every one/two minutes, and make it write a .txt file with some details only if it finds some arbitrage opportunity.
For now I have split the bot in some parts that do NOT work together, each of them is relative to one of the websites. 

While the Cryptsy part is almost complete (I have to test it properly, but it's working), I still have to add the write-file function to the The Rock Trading part. I'll do it soon. 

Be careful, there may be some errors in the code (specially with fees); I'll check everything as soon as I can.


# Project Schedule #

- Add write-file function to therocktrading.com part. 
- Add Mintpal scanning.
- Add Bittrex scanning. 
- Test everything and make it run together.
- Add automatic buy&sell orders in case of arbitrage opportunity. 
- Add other websites (maybe BTC-e and others..)
