from base import app, api, ma, Resource, Flask, request
import requests

class SignalMonitorResource(Resource):

    def get(self):
        print("Preparando request Monitor")
        response = requests.get("http://signals-queries:5000/api-queries/signals")
        #response = "Ok-1"
        print("Respuesta: {}".format(response))
        return response, 200

     

api.add_resource(SignalMonitorResource, '/api-queries/monitor')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

