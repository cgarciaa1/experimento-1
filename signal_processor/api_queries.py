from base import app, api, ma, r, Resource, Flask, request
import time
import logging

event = ""

class SignalProcessorResource(Resource):

    def get(self):
        logging.warning("-------EJECUTANDO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        return {"status":"Ok", "event": event }, 200

     

api.add_resource(SignalProcessorResource, '/api-queries/signals')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    p = r.pubsub()
    p.subscribe("signal-channel")       
    logging.warning("-------EJECUTANDO ANTES DE LOG")
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