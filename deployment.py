import requests

API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=64e64ce2a72bbd5c43bbe450&org=69421cc0-0d23-4f09-87d0-84f2fdc3e524"
headers = {'Authorization':
			 'Bearer XXXXXXXXXXXXXXX',
			 'Content-Type': 'application/json'
		}

def query(payload):
 response = requests.post(API_URL, headers=headers, json=payload)
 return response.json()

output = query({"in-0": """Hi Karios I want to learn about Python"""})
