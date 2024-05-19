#pip install requests
#client code which can be a mobile app , or web site, or windows app, or backened service
import requests

def fetch_employees_data():
  url = f'http://localhost:5000/employees'
  response = requests.get(url)

  if response.status_code == 200:
    return response.json()
  else:
    return f'Error: {response.status_code}'




def create_employee():
  url = f'http://localhost:5000/employees'
  data = { 'id': 4, 'name': 'Amit' }
  headers = {"Content-Type": "application/json; charset=utf-8"}
  response = requests.post(url, json=data,headers=headers)
  if response.status_code == 201:
    return response.json()
  else:
    return f'Error: {response.status_code}'

# Example usage - GET CALL
emp_data = fetch_employees_data()
print(emp_data)

print(create_employee())


