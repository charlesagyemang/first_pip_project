# import json
from witty_flow_sms import WittyFlowSms

client = WittyFlowSms('1f41908b-a9d7-4408-a0bf-4ee4665b3276', 'CvAILbsSdfjGAVVZr6RG0zgBv5jHUioh88vCuHu914')
# res = client.send_sms('0507565349', 'Possitech', 'Test')
# res = client.send_sms('0507565349', 'Possitech', 'Test')

# res = client.get_account_balance()
res = client.check_sms_status('21776c6f-3c84-40c0-b0a5-14c3b0c6f514')

print (res)

# print(test.test("keli"))

# print(json.dumps({"hey":"memmss"}))
