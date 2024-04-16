import requests
import json

''' Fill in the following information '''
# General information
YOUR_EMAIL = "" # <put your coursera account email>,
YOUR_SECRET = "" # <put your secret token from coursera>

# <To submit your solution to be graded for both sections 1 and 2, leave this blank. It will run both section 1 and section 2 tests>
SECTION = "" # <put "1" to test section 1 in isolation; put "2" to test section 2 in isolation>
# For example, SECTION = "1" tests only section 1.

# Section 1
IP_ADDRESS1 = "" # <put your first EC2 instance's IP address:port>
# For example, IP_ADDRESS1 = "18.208.152.40:8000"

IP_ADDRESS2 = "" # <put your second instance's IP address:port>
# For example, IP_ADDRESS2 = "52.91.26.84:8000"

# Do not add "https://" to your loadbalancer address.
YOUR_LOAD_BALANCER1 = "" # <put your load_balancer address for section 1 (explicitly add :port if port is not 80)>
# For example, YOUR_LOAD_BALANCER1 = "mp2LoadBalancerSection1-xxxx.us-east-1.elb.amazonaws.com:5000"

# Section 2
YOUR_LOAD_BALANCER2 = "" # <put your load_balancer address for section 2 (explicitly add :port if port is not 80)>, 
# For example, YOUR_LOAD_BALANCER1 = "mp2LoadBalancerSection2-xxxx.us-east-1.elb.amazonaws.com:5000"

''' Don't change the following '''
url = "https://ekwygde36j.execute-api.us-east-1.amazonaws.com/alpha/execution"
input = {
            'ip_address1': IP_ADDRESS1,
            'ip_address2': IP_ADDRESS2,
			'load_balancer1': YOUR_LOAD_BALANCER1, 
            'load_balancer2': YOUR_LOAD_BALANCER2,
			'submitterEmail': YOUR_EMAIL, 
			'secret': YOUR_SECRET, 
			'section': SECTION
		}
payload = { "input": json.dumps(input),
    		"stateMachineArn": "arn:aws:states:us-east-1:913708708374:stateMachine:mp2grader"
        }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)
