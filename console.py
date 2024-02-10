#!/usr/bin/python3
"""
Defines the console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""
    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        return

    def do_EOF(self, line):
        """End of file"""
        return True

    def do_create(self, line):
        pass

    def do_show(self, line):
        pass

    def do_destroy(self, line):
        pass

    def do_all(self, line):
        pass

    def do_update(self, line):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
