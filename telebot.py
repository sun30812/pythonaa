import telegram

telegram_token='939951841:AAEDClm-J9J2Ao2p8twJTisUEMLZOf1sLJ8'

myBot=telegram.Bot(token = telegram_token)
updates = myBot.get_updates()
print(updates)

for i in updates:
	print(i)
