import requests
import json

''' Fill in the following information '''
# General information
YOUR_EMAIL = "" # <put your coursera account email>,
YOUR_SECRET = "" # <put your secret token from coursera>

# <To get full credits, leave this blank. It will run both section 1 and section 2 tests>
SECTION = "1" # <put "1" to test section 1 in isolation; put "2" to test section 2 in isolation>

# Section 1
IP_ADDRESS1 = "" # <put your first EC2 instance's IP address:port> for receiver service
IP_ADDRESS2 = "" # <put your second instance's IP address:port> for receiver service
IP_ADDRESS3 = "" # <put your data access service instance's IP address> DO NOT INCLUDE PORT HERE
NACL_ID = "" # put NACL ID here
DATA_SERVICE_SUBNET_ID = "" # put subnet ID for data access service here
RECEIVER_APPLICATION_CIDR_RANGE = "" # put CIDR block range for the subnet associated to receiver service instances


# Do not add "https://" to your loadbalancer address.
YOUR_LOAD_BALANCER1 = "" # <put your load_balancer address for section 1 (explicitly add :port if port is not 80)>
# Section 2
YOUR_LOAD_BALANCER2 = "" # <put your load_balancer address for section 2 (explicitly add :port if port is not 80)>,

''' Don't change the following '''
url = "https://ekwygde36j.execute-api.us-east-1.amazonaws.com/alpha/execution"
input = {
	'ip_address1': IP_ADDRESS1,
	'ip_address2': IP_ADDRESS2,
	'ip_address3': IP_ADDRESS3,
	'load_balancer1': YOUR_LOAD_BALANCER1,
	'load_balancer2': YOUR_LOAD_BALANCER2,
	'submitterEmail': YOUR_EMAIL,
	'secret': YOUR_SECRET,
	'section': SECTION,
	'NACL_ID': NACL_ID,
	'data-service-subnet-id': DATA_SERVICE_SUBNET_ID,
	'receiver-application-cidr-range': RECEIVER_APPLICATION_CIDR_RANGE
}
payload = { "input": json.dumps(input),
			"stateMachineArn": "arn:aws:states:us-east-1:913708708374:stateMachine:mp2grader"
			}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)
