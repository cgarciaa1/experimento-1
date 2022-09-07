from base import app, api, ma, r, Resource, Flask, request
import time
import logging
import threading

event = ""
requests= 0
status= "Ok"

subcription = r.pubsub()    
subcription.subscribe("signal-channel") 

class SignalProcessorResource(Resource):

    def get(self):
        return {"status": status, "event": event }, 200

api.add_resource(SignalProcessorResource, '/api-queries/signals')


def thread_function(p):
    global event
    global requests
    global status
    while True:
        message = subcription.get_message()
        logging.warning("-------")
        logging.warning(message)
        logging.warning("-------")
        if message:
            logging.warning("Evento obtenido: {}".format(message))
            requests += 1
            if requests % 5 == 0 :
                status = "Ok"
            else: 
                status = "Error"
                event = ""
        time.sleep(10)


if __name__ == '__main__':
  
    x = threading.Thread(target=thread_function, args=(0,))
    x.start()

    app.run(debug=True, host='0.0.0.0')