# Classdecorator.py

class decorator_class():
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("call method executed this before {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class
def message():
    return "Message"

@decorator_class
def new_message(message, newmessage):
    print("{} VS {}".format(message, newmessage))

new_message(message(), "New Message")
