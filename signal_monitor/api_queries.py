from base import app, api, ma, r, Resource, Flask, request
import requests

class SignalMonitorResource(Resource):

    def get(self):
        response = requests.get("http://192.168.1.145/api-queries/monitor")
        return response, 200

     

api.add_resource(SignalMonitorResource, '/api-queries/monitor')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
