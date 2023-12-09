#0x00. AirBnB clone - The console
#This is an alx team project that clones AirBnB.

This project is the first step to deploy a simple copy of the AirBnB website on a server. We are tasked to implement only some of the features of the website, and it is a test of our knowledge on the fundamental concepts of higher level programming.

#The Console
This project adopts the Object-oriented data model for this project and sets classes (both parent and derived) to represent objects of the website.
Also, it requires that a command interpreter called the console is created by which various manipulations like create, update, store, destroy etc are performed on the objects.
The state of objects are stored to file in human-readable and machine-readable format for use later.

#How to start it
The console is started byy running the script using "./console.py. After running the script, the command interpreter is started and a custom prompt "(hbnb)" appears waiting for commands.

#How t use it
To exit the console, type "quit":
...	(hbnb) quit

To create an instance of any class or object, type "create followed by the class name as shown in the example below:
...	(hbnb) create User

To show details of a stored instance, type the "show" followed by the name of the class of the instance followed by the its unique identifier:
...	(hbnb) show User 123

To update an attribute of an instance, type "update" followed by the class of the instanc, the unique id, the attribute to update and the update string:
...	(hbnb) update User 123 name "New Name"

To destroy an instance, type "destroy", followed by the class name, follwed by the unique id of the instance:
...	(hbnb) destroy User 123

To display all instances stored in the console, type "all":
...	(hbnb) all
