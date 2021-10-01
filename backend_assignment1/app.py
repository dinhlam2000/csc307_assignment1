from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin
import uuid
import json


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


users = {
   'users_list' :
   [
      {
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123',
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222',
         'name': 'Mac',
         'job': 'Professor',
      },
      {
         'id' : 'yat999',
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555',
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/users/<id>', methods=['DELETE'])
@app.route('/users', methods=['GET', 'POST', 'DELETE'])
@cross_origin()
def get_users(id=None):

   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      subdict = {'users_list': []}
      if search_username and search_job:
          for user in users['users_list']:
              if user['name'] == search_username and user['job'] == search_job:
                  subdict['users_list'].append(user)
          return subdict
      elif search_username :
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id']= str(uuid.uuid4())
      users['users_list'].append(userToAdd)
      #resp.status_code = 200 #optionally, you can always set a response code.
      # 200 is the default code for a normal response

      return Response(json.dumps(users),status=201)
   elif request.method == 'DELETE':
      for index, user in enumerate(users['users_list']):
        if user['id'] == id:
            users['users_list'].pop(index)
            return Response(json.dumps(users), status=204)
      return Response(status=404)



app.run(port=5000)