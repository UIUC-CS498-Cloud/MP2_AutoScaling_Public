import requests
import json

# Fill in the following information
YOUR_LOAD_BALANCER = "mp2LoadBalancer-1890294852.us-east-1.elb.amazonaws.com" # <put your load_balancer address>, 
YOUR_EMAIL = "" # <put your coursera account email>,
YOUR_SECRET = "" # <put your secret token from coursera>

# Don't change the following
url = "https://ekwygde36j.execute-api.us-east-1.amazonaws.com/alpha/execution"
input = {
			'load_balancer': YOUR_LOAD_BALANCER, 
			'submitterEmail': YOUR_EMAIL, 
			'secret': YOUR_SECRET, 
		}
payload = { "input": json.dumps(input),
    		"stateMachineArn": "arn:aws:states:us-east-1:913708708374:stateMachine:mp2grader"
        }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)