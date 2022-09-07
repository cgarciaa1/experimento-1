from base import app, api, ma, Resource, Flask, request
import requests
import time
import logging
import threading

number_requests = 0
number_errors = 0

class SignalMonitorResource(Resource):

    def get(self):
        global number_requests
        return {"status":"Ok", "number_requests_monitor": number_requests, "founded_errors_monitor" : number_errors}, 200 

api.add_resource(SignalMonitorResource, '/api-queries/monitor')

def thread_function(p):
    global number_requests
    global number_errors
    real_time_error = False
    while True:
        response = requests.get("http://signals-queries:5000/api-queries/signals")
        number_requests += 1
        health = response.json["status"]
        logging.warning("Respuesta obtenida: {}".format(health))
        if health == "ERROR" & real_time_error == False:
            number_errors += 1
            real_time_error = True
        elif health == "OK":
            real_time_error = False    


        time.sleep(5)


if __name__ == '__main__':
  
    x = threading.Thread(target=thread_function, args=(0,))
    x.start()

    app.run(debug=True, host='0.0.0.0')
