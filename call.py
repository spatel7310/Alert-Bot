from twilio.rest import Client
import xml.etree.ElementTree as ET

tree = ET.parse('script.xml')
root = tree.getroot()
script = ET.tostring(root)

account_sid = 'account_sid'
auth_token = 'auth_token' 
client = Client(account_sid, auth_token)

message = client.messages.create(
        body="Hey Dad, time to take your meds!",
        to='+12482141104',
        from_='+17207436230',
    )

call = client.calls.create(
    twiml=script,
    to='+12482141104',
    from_='+17207436230',
)

