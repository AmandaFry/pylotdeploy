from system.core.controller import *

class User(Controller):
    def __init__(self, action):
        super(User, self).__init__(action)

        self.load_model('UserModel')


    def index(self):
        return self.load_view('index.html')