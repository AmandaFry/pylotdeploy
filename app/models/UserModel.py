from system.core.model import Model
from flask import Flask, session, request, redirect
from datetime import datetime
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]*$')
NOSPACE_REGEX = re.compile(r'^[a-zA-Z0-9]*$')
                        #is there upper case, number, at least 8 charater
PW_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?\d)[A-Za-z\d]{8,}$')

class UserModel(Model):
    def __init__(self):
        super(UserModel, self).__init__()


     def register_user(self, user_info):
        errors=[]

        #setting up todays date to use it for date validation
        # today = datetime.now().strftime("%Y-%m-%d")
        # however I am using at least 1 year back to use this application
        valid_date = '2015-01-01'

        #validation prior to inserting data to db
        if len(user_info['f_name']) < 2:
            errors.append("First name cannot be empty")
        elif not NOSPACE_REGEX.match(user_info['f_name']):
            errors.append("Please enter a valid first name")
        elif len(user_info['l_name']) < 2 :
            errors.append("Last name cannot be empty")
        elif len(user_info['alias']) < 2 :
            errors.append("Alias cannot be empty")
        elif not NOSPACE_REGEX.match(user_info['f_name']):
            errors.append("Please enter a valid last name")
        elif len(user_info['email']) < 2 :
            errors.append("Email cannot be empty")
        elif not EMAIL_REGEX.match(user_info['email']):
            errors.append("Please enter a valid email format")
        elif not PW_REGEX.match(user_info['passw']):
            errors.append("Please enter a valid password. It must be 8 charater long, at must include least one upper case and number")
        elif len(user_info['conf_passw']) < 2 :
            errors.append("Confirm password cannot be empty")
        elif not (user_info['passw'] == user_info['conf_passw']):
            errors.append("Password and confirm password must match")   
        # elif today < user_info['birthday']:
        elif valid_date < user_info['birthday']:
            errors.append("You must been born 2014 or before to use this application")

        if errors:
            return {"status": False, "errors": errors}
        else:
            #check to see if email already in use
            query = "SELECT * FROM users WHERE email = :email"
            data = {'email': user_info['email']}
            email_inuse = self.db.query_db(query, data)

            if email_inuse:
                errors.append("Email account already in use")
                return {"status": False, "errors": errors}
            else:
                query = "INSERT INTO users (first_name, last_name, alias, email, password, birthday, created_at, updated_at) VALUES (:f_name, :l_name, :alias, :email, :passw, :birthday, NOW(), NOW())"
                #password needs to be converted from plain text before can be part of data
                password = user_info['passw']
                hashed_pw = self.bcrypt.generate_password_hash(password)
                data = {
                    'f_name':user_info['f_name'],
                    'l_name':user_info['l_name'],
                    'alias' :user_info['alias'],
                    'email':user_info['email'],
                    'passw':hashed_pw,
                    'birthday':user_info['birthday'],
                }
                registered_user = self.db.query_db(query, data)
                # print ('%' * 25)
                # print registered_user
                # print ('%' * 25)
                return {"status": True }
                