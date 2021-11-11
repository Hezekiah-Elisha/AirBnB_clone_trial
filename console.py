#!/usr/bin/python3
import cmd
import sys


class ConsoleShell(cmd.Cmd):
    intro = 'Welcome to the AirBnB clone. Type help or ? to list commands. \n'
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, arg):
        'Check if it is End-Of-File: EOF'
        # something to be done here
        print('EOF')

    def do_quit(self, arg):
        'close the turtle window, and exit:  EXIT'
        print('Thank you for AirBnB clone shell;-)')
        self.close()
        # bye()
        return True

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    ConsoleShell().cmdloop()
