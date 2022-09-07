from base import app, api, ma, r, Resource, Flask, request
import time



class SignalProcessorResource(Resource):

    def get(self):

        return "Ok", 200

     

api.add_resource(SignalProcessorResource, '/api-queries/signals')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

p = r.pubsub()
p.subscribe("signal-channel")       

while True:
    message = p.get_message()
    if message:
        print(message)
    time.sleep(0.01)