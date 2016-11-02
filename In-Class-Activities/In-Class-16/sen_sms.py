from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC239793e553d0d3f72b153ebceac9b564"
auth_token = "ccecc4d920331e39a82e6fc445afe710"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+16175648766", from_="+16176525814",
                                     body="Hello there! My Name is Mark Oh. Testing text message sent from python :) ")



