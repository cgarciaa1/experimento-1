from base import app, api, ma, r, Resource, Flask, request



class SignalPublisherResource(Resource):

    def post(self):
        
        name=request.json['evento']
        r.publish('signal-channel', name)
        return "Mensaje publicado", 200

api.add_resource(SignalPublisherResource, '/api-commands/signal')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')