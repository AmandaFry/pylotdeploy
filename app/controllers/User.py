from system.core.controller import *

class User(Controller):
    def __init__(self, action):
        super(User, self).__init__(action)

        self.load_model('UserModel')


    def index(self):
        return self.load_view('index.html')

    def dashboard(self):
    	return self.load_view('dashboard.html')

    def two(self):
    	return self.load_view('twodown.html')
 