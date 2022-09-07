from base import app, api, ma, r, Resource, Flask, request
import time
import logging
import threading

event = ""
logging.warning("-------EJECUTANDO ANTES DE LOG"
subcription = r.pubsub()    
logging.warning("-------EJECUTANDO DESPUES DE LOG ----------"
subcription.subscribe(channel)  

class SignalProcessorResource(Resource):

    def get(self):
        return {"status":"Ok", "event": event }, 200

api.add_resource(SignalProcessorResource, '/api-queries/signals')


def thread_function(channel, p):
    
    while True:
        logging.warning("Subscrition")
        message = p.get_message()
        logging.warning("-------")
        logging.warning(message)
        logging.warning("-------")
        if message:
            logging.warning("Evento obtenido: {}".format(message))
            event = message
        time.sleep(0.01)


if __name__ == '__main__':
 
    x = threading.Thread(target=thread_function, args=("signal-channel", subcription))
    x.start()

    app.run(debug=True, host='0.0.0.0')