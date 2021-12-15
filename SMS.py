


import requests

def send_sms(message,mob_no):
	url = "https://www.fast2sms.com/dev/bulk"
	payload = "sender_id=FSTSMS&message="+ message +"&language=english&route=p&numbers="+ mob_no +""
	headers = {
	 'authorization': "AUTHORIZATION_KEY FAST2SMS",
	 'Content-Type': "application/x-www-form-urlencoded",
	 'Cache-Control': "no-cache",
	 }
	response = requests.request("POST", url, data=payload, headers=headers)
	print("SMS Sent !")


