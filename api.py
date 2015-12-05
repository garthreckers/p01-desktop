""" simple api calls to the server """

import json
import http.client

from localstore import LocalStore

class ApiCall:
    """ simple api calls to the server """
    def __init__(self):
        self.api_host = "104.236.161.75"
        self.api_path = "/api/v1"
        self.login_url = self.api_path + "/login"
        self.boxes_url = self.api_path + "/getboxes"

    def login(self, email, password):
        """ log user in and store token """
        login_dict = {"email": str(email), "password": str(password)}
        login_json = json.dumps(login_dict)
        login_header = {"Content-type": "application/json"}

        # Make request
        conn = http.client.HTTPConnection(self.api_host, 80)
        conn.request('POST', self.login_url, login_json, login_header)

        # Get response and parse
        res = conn.getresponse()
        res_read = res.read().decode('utf-8')
        res_decode = json.loads(res_read)

        if res.status == 401:
        	print("FUCKKKKK")
        	return False

        # Add token to local store
        store = LocalStore()
        store.set_token(res_decode['token'])

        conn.close()
        return True

    def boxes(self):
        """ check token and get all boxes """
        # Get token from local store
        store = LocalStore()
        token = store.get_token()

        # Make request
        conn = http.client.HTTPConnection(self.api_host, 80)
        conn.request('POST', self.boxes_url + "?token=" + token)

        # Get response and parse
        res = conn.getresponse()
        res_read = res.read().decode('utf-8')
        res_decode = json.loads(res_read)

        print(res_decode)

        conn.close()
