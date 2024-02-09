#!/usr/bin/python3
"""module for consule"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    """cmd class"""
    prompt = "(hbnb) "

    def empty(self):
        """do nothing when enter empty line"""
        pass

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        print("")
        return True

    def do_create(self, arg):
        """create a new class instance"""
        if not arg:
            print("** class name missing **")
            return
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """print string rep of instance based on cls name & id"""
        if not arg:
            print("class name missing")
            return
        args = arg.split()
        if args[0] not in storage.classes.keys():
            print("class doesn't exist")
            return
        if len(args) < 2:
            print("instance id missing")
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("no instance found")

    def do_destroy(self, arg):
        """delete instance based on cls name & id"""
        if not arg:
            print("class name missing")
            return
        args = arg.split()
        if args[0] not in storage.classes.keys():
            print("class doesn't exist")
            return
        if len(args) < 2:
            print("instance id missing")
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("no instance found")

    def do_all(self, arg):
        """Prints all string rep of all instances"""
        args = arg.split()
        if not arg or args[0] == "":
            objects = storage.all().values()
        elif args[0] in storage.classes.keys():
            objects = [obj for obj in storage.all().values()
                       if type(obj).__name__ == args[0]]
        else:
            print("class doesn't exist")
            return
        print([str(obj) for obj in objects])

    def do_update(self, arg):
        """update and instance based on cls name & id"""
        if not arg:
            print("class name missing")
            return
        args = arg.split()
        if args[0] not in storage.classes.keys():
            print("class doesn't exist")
            return
        if len(args) < 2:
            print("instance id missing")
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key not in objects:
            print("no instance found")
            return
        if len(args) < 3:
            print("attribute name missing")
            return
        if len(args) < 4:
            print("value missing")
            return
        setattr(objects[key], args[2], eval(args[3]))
        objects[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
