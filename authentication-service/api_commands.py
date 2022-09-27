from base import app, api, Resource, request
from model import *

class AuthenticationResource(Resource):
    def __init__(self, monitor):
        self.__login_monitor__ = monitor       
        super().__init__()

    def post(self):
        username=request.json['username']
        password=request.json['password']
        if self.__login_monitor__.authenticate_user(username, password):
            return {"status":"Ok", "response": "Usuario {} autenticado".format(username,)}, 200
        return {"status":"Error", "response": "Error"}, 401


if __name__ == '__main__':
    # monitor configuration
    MAX_USER_LOGGIN_ATTEMPS = 3
    
    # data setup
    admin_user = User("admin", "supersecret", LoginTracker())
    sensor1_user = User("sensor_1", "sensor1", LoginTracker())
    monitor = LoginMonitor([admin_user, sensor1_user], MAX_USER_LOGGIN_ATTEMPS)

    # endpoint handlers
    api.add_resource(AuthenticationResource, '/api-commands/authenticate', resource_class_kwargs={'monitor': monitor})

    # app run
    app.run(debug=True, host='0.0.0.0')