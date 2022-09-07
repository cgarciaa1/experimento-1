from base import app, api, ma, r, Resource, Flask, request
import time
import logging
import threading

event = ""
logging.warning("-------EJECUTANDO ANTES DE LOG")
subcription = r.pubsub()    
logging.warning("-------EJECUTANDO DESPUES DE LOG ----------")
subcription.subscribe("signal-channel") 

class SignalProcessorResource(Resource):

    def get(self):
        return {"status":"Ok", "event": event }, 200

api.add_resource(SignalProcessorResource, '/api-queries/signals')


def thread_function(p):
    
    while True:
        logging.warning("Subscrition")
        message = subcription.get_message()
        logging.warning("-------")
        logging.warning(message)
        logging.warning("-------")
        if message:
            logging.warning("Evento obtenido: {}".format(message))
            event = message
        time.sleep(10)


if __name__ == '__main__':
  
    x = threading.Thread(target=thread_function, args=(0,))
    x.start()

    app.run(debug=True, host='0.0.0.0')