import cmd

class MyCLI(cmd.Cmd):
    prompt = '<BestCLI> '
    intro = "Simple CLI example"

    def do_greet(self, name):
        """Greets the person"""
        if name:
            print(f"Hello, {name}!")
        else:
            print("Hello!")

    def do_exit(self, inp):
        """Exit the application"""
        print("Bye")
        return True
    
    def do_thing(self, thing):
        if thing:
            print(f"{thing} is a thing!")
        else:
            print("A call for things.")
    
    def do_add(self, args):
        try:
            num1, num2 = map(float, args.split())
            print(f"The sum is: {num1 + num2}")
        except ValueError:
            print("Invalid input. Please provide two numbers.")
    
    def default(self, inp):
        print("Invalid command")

    def emptyline(self):
        pass

if __name__ == '__main__':
    MyCLI().cmdloop()