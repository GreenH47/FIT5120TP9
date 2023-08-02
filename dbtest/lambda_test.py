import deploy_demo as dp
import json
input = {"Subarea":"Subarea 4","Electricity":2,"Gas":3,"Carbon":5.36}
event = {"body": json.dumps(input)}
dp.lambda_handler(event)
# dp.lambda_handler()