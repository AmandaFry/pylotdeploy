from system.core.controller import *
from flask import Flask, session, flash, request, redirect

class User(Controller):
	def __init__(self, action):
		super(User, self).__init__(action)
		self.load_model('UserModel')
		self.db = self._app.db #not sure if it is needed

	def index(self):
		#It is needed for inital page load
		return self.load_view('index.html')

	def process_login(self):
		#informaiton collected at login
		user_info ={
			'email' : request.form['email'],
			'passw' : request.form['passw']
		}
		#sending informaiton to model
		user_login = self.models['UserModel'].login_user(user_info)

		#information returned from model
		if user_login['status'] == False:
			for messages in errorMessages
				flash(messages)
			# return self.load_view('index.html')
			return redirect('/')
		else:
			session['id'] = users['users']['id']
			session['name'] = users['users']['first_name'] + ' ' + users['users']['last_name']
			return redirect('/dashboard')

	def process_registration(self):
		user_info = {
			'f_name' : request.form['f_name'],
			'l_name' : request.form['l_name'],
			'alias' : request.form['alais'],
			'email' : request.form['email'],
			'passw' : request.form['passw'],
			'conf_passw' : request.form['conf_passw'],
			'birthday' : request.form['birthday']
		}
		pass

