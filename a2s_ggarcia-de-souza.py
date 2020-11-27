from fabric.api import *
import tempfile
'''
OPS435 Assignment 2S - Fall 2020
Program: a2r_ggarcia-de-souza.py
Author: Guilherme Garcia de Souza
The python code in this file a2s_ggarcia-de-souza.py is original work written by
Guilherme Garcia de Souza. No code in this file is copied from any other source 
including any person, textbook, or on-line resource except those provided
by the course instructor. I have not shared this python file with anyone
or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and violators 
will be reported and appropriate action will be taken.
'''

env.user = "student"



def addUser(name):
    '''add a user with given user name to remote system'''
    

    sudo(('useradd -m {}').format(name))
    sudo(('echo "password" | passwd {} --stdin').format(name))

 
def listUser():
    '''return a list of shell user on a remote system'''

    user_list = []

    #Creating a temporary file to store the /etc/passwd file from remote system
    #This file will be automatically deleted once the script ends
    
    with tempfile.TemporaryFile() as file_temp:
        get("/etc/passwd", file_temp)

        file_temp.seek(0)
        
        
        users = file_temp.readlines()

        for item in users:
            if "/bin/bash" in item:

                user_list.append(item.split(":")[0])

        print(user_list)

 


def listSysUser():
    '''return a list of system (non-shell) user'''


    user_list = []
    with tempfile.TemporaryFile() as file_temp:
        get("/etc/passwd", file_temp)

        file_temp.seek(0)


        users = file_temp.readlines()

        for item in users:
            if "nologin" in item:

                user_list.append(item.split(":")[0])

        print(user_list)

def findUser(name):
    '''find user with a given user name'''

    flag = 0
    with tempfile.TemporaryFile() as file_temp:
        get("/etc/passwd", file_temp)

        file_temp.seek(0)


        users = file_temp.readlines()
               
 
        for item in users:
            username = item.split(":")[0]

            if username == name:
                flag = 1
                break
            else:
                flag = 0

        if flag == 1:
            print("Found user " + name + " on the system.")
        else:
            print("User " + name + " is not on the system.")


