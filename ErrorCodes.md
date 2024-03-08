All error cases captured in the lambdas and propogated to Coursera via error codes for MP2

Section 1:

1) Submission payload is incorrect. (Missing fields or invalid values)
-> lb should not contain “http” prefix
-> If lb is not hosted on port 80, mention the port number specifically in the url using :[PORT]
2) EC2 (one of the two, can’t propagate that to Coursera) is not responding
-> Security group is blocking inbound traffic
-> Server not running
3) LoadBalancer is not responding
-> Security group is blocking inbound requests.
-> loadbalancer is not able to send requests to EC2 via the target group. (Fix the Port mapping)
4) LB returned an invalid seed value. 
-> Either the value was not updated properly (Check post request logic) or the value returned was not in the right format (Get req should return the seed as a string. str(seed))
5) LB only sends requests to 1 EC2.
-> Ensure that you have 2 EC2 instances registered on the target group and LB is able to distribute requests across the two successfully. 

Section 2:

Test 1 (ASG should have 1 EC2 instances up)

1) LoadBalancer is not responding
-> Security group is blocking inbound requests.
-> loadbalancer is not able to send requests to EC2 via the target group. (Fix the Port mapping)
2) Number of running EC2 is not 1

Stress CPU

1) LoadBalancer is not responding to POST stress requests
-> LB should return success message within 2-3 seconds and run the stress cpu script in the background as a detached process (subprocess.POPEN())
-> Security group is blocking inbound requests. (Unlikely, since Test 1 passed)


Test 2 (ASG should have 2 EC2 instances up)

1) LoadBalancer is not responding
-> Security group is blocking inbound requests.
-> loadbalancer is not able to send requests to EC2 via the target group. (Fix the Port mapping)
2) Number of running EC2 is not 2

Stress CPU

1) Same as before but failures are unlikely as it worked in the previous stage.

Test 3 (ASG should have 3 EC2 instances up)

1) LoadBalancer is not responding
-> Security group is blocking inbound requests.
-> loadbalancer is not able to send requests to EC2 via the target group. (Fix the Port mapping)
2) Number of running EC2 is not 3
