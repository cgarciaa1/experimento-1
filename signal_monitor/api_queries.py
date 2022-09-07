from base import app, api, ma, Resource, Flask, request
import requests
import time
import logging
import threading

number_requests = 0

class SignalMonitorResource(Resource):

    def get(self):
        global number_requests
        return {"status":"Ok", "response": number_requests}, 200

     

api.add_resource(SignalMonitorResource, '/api-queries/monitor')

def thread_function(p):
    global number_requests
    
    while True:
        response = requests.get("http://signals-queries:5000/api-queries/signals")
        number_requests += 1
        health = response.json
        logging.warning("Respuesta obtenida: {}".format(health))

        time.sleep(5)


if __name__ == '__main__':
  
    x = threading.Thread(target=thread_function, args=(0,))
    x.start()

    app.run(debug=True, host='0.0.0.0')
