import json
from flask import Flask, jsonify, request
app = Flask(__name__)

employees = [
 { 'id': 1, 'name': 'Ashley' },
 { 'id': 2, 'name': 'Kate' },
 { 'id': 3, 'name': 'Joe' }
] 


@app.route('/employees',methods=['get'])
def get_employees():
   return jsonify({'data':employees}), 200



@app.route('/employees', methods=['POST'])
def create_employee(): 
   print("Received Post Call")
   content_type = request.headers.get('Content-Type')
   if (content_type == 'application/json; charset=utf-8'):
      employeeJson = request.json 
      print(employeeJson)  
      employees.append(employeeJson)
   return jsonify({'data':employees}), 201


if __name__ == '__main__':
   app.run(port=5000)