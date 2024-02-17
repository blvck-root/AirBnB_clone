#!/usr/bin/python3
"""define class"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """custom prompt (hbnb)"""

    prompt = "(hbnb) "

    def do_quit(self, ln):
        """quit program"""
        return (True)

    def do_EOF(self, ln):
        """exit program"""
        print()
        return True

    def emptyline(self):
        """shouldnt execute anything"""
        pass

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_create(self, ln):
        """creating new instances"""
        if not ln:
            print("** class name missing **")
        elif ln not in storage.classes:
            print("** class doesn't exist **")
        else:
            new = storage.classes[ln]()
            new.save()
            print(new.id)

    def do_show(self, ln):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = ln.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            k = args[0] + "." + args[1]
            i = storage.all().get(k)
            if not i:
                print("** no instance found **")
            else:
                print(i)

    def do_destroy(self, ln):
        """Deletes an instance based on the class name and id"""
        args = ln.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            k = args[0] + "." + args[1]
            if k not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[k]
                storage.save()

    def do_all(self, ln):
        """Prints all string representation of all instances
        based or not on the class name
        """
        if not ln:
            for n in storage.all().values():
                print(n)
        elif ln not in storage.classes:
            print("** class doesn't exist **")
        else:
            for n in storage.all().values():
                if n.__class__.__name__ == ln:
                    print(n)

    def do_update(self, ln):
        args = ln.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            k = args[0] + "." + args[1]
            n = storage.all().get(k)
            if not n:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                a, v = args[2], args[3]
                setattr(n, a, v)
                n.save()
                print(f"{k} {a} = {v}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
