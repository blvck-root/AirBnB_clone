#!/usr/bin/python3
"""define class"""

import cmd


class HBNBCommand(cmd.Cmd):
    """custom prompt (hbnb)"""

    prompt = "(hbnb)"

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
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            new = storage.classes()[ln]()
            new.save()
            print(new.id)

    def do_show(self, ln):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = ln.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            k = args[0] + "." + args[1]
            if k not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[k])

    def do_destroy(self, ln):
        """Deletes an instance based on the class name and id"""
        args = ln.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing**")
        else:
            k = args[0] + "." + args[1]
            if k not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[k]

    def do_all(self, ln):
        """Prints all string representation of all instances
        based or not on the class name
        """
        if not ln:
            print("** class doesn't exist **")
        else:
            d = []
            for n in d:
                if n.__class__.__name__ == ln:
                    print(n)

    def do_update(self, ln):
        args = ln.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            k = args[0] + "." + args[1]
            if k not in storage.all():
                print("** no instance found **")
            else:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    a = args[2]
                    v = args[3]
                    print(f"{k} {a} = {v}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
