#!/usr/bin/python3
"""create a console that contains
    a command interpreter"""

import models
import cmd
import json
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """a command class that inherits from cmd"""
    prompt = '(hbnb) '
    classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        exit(0)

    def do_EOF(self, arg):
        """EOF exits the program"""
        print("")
        exit(0)

    def emptyline(self):
        """execute nothing"""
        pass

    def do_create(self, arg):
        """create a new instance of Basemodel"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg not in self.classes:
            print("** class doesn't exist **")

        else:
            new_inst = eval(arg)()
            new_inst.save()
            print(new_inst.id)

        if cmd == "all":
            self.do_all(args)
            classes.all()

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        cls = args[0]
        if cls not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        ids = args[1]
        key = cls + '.' + ids
        all_instances = storage.all()
        if key not in all_instances:
            print("** no instance found **")
        else:
            print("[{}] ({}) {}".format(cls, ids, str(all_instances[key])))

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        cls = args[0]
        if cls not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        ids = args[1]
        all_instances = storage.all()
        key = cls + "." + ids
        if key in all_instances:
            del all_instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """print all string representation of instances"""
        args = shlex.split(arg)
        all_instances = storage.all()

        if len(args) == 0:
            print([str(value) for value in all_instances.values()])

        cls = args[0]
        if cls not in self.classes:
            print("* class doesn't exist *")
        else:
            print([str(value) for key, value in all_instances.items()
                   if cls in key])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        all_instances = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return

        cls = args[0]
        if cls not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        ids = args[1]
        key = cls + '.' + ids
        if key not in all_instances:
            print("** no instance found **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        instance = all_instances[key]
        attribute_name = args[2]
        attribute_value = args[3]
        if hasattr(instance, attribute_name):
            attribute_value = type(getattr(instance, attribute_name))(
                    attribute_value)
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if _name_ == '_main_':
    HBNBCommand().cmdloop()
