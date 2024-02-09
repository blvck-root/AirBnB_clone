#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    """custom prompty (hbnb)"""

    def do_quit(self, ln):
        """quit program"""
        return (True)

    def do_EOF(self, ln):
        """exit program"""
        return True

    def emptyline(self):
        """shouldnt execute anything"""
        pass

    def do_create(self, ln):
        """creating new instances"""
        if not ln :
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            new = storage.classes()[ln]().save()
            print(new.id)

    def do_show(self, ln)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
