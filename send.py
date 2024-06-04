from twilio.rest import Client

account_sid = 'ACCOUNTID'
auth_token = 'AUTHTOKEN'
client = Client(account_sid, auth_token)
def SendSms():
    message = client.messages.create(
    from_='+14795525792',
    body='Intruder Alert',
    to='YOUR_NUMBER'
    )

    print(message.sid)