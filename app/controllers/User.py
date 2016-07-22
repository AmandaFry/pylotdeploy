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

    def register(self):
        #information collected to register
        user_info = {
            'f_name' : request.form['f_name'],
            'l_name' : request.form['l_name'],
            'alias' : request.form['alias'],
            'email' : request.form['email'],
            'passw' : request.form['passw'],
            'conf_passw' : request.form['conf_passw'],
            'birthday' : request.form['birthday']
        }

        #sending information to model
        user_register = self.models['UserModel'].register_user(user_info)

        #process returned information
        if user_register['status'] == False:
            for message in user_register['errors']:
                flash(message)
            return self.load_view('index.html')
        else:
            flash('SUCCESFULLY REGISTERED, PLEASE LOGIN!')
            return redirect('/')