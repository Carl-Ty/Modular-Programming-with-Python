hooked_function = None
def set_hook(hook):
    global hooked_function
    hooked_function = hook
    hooked_function

def do_it():
    if hooked_function != None:
        hooked_function()
    else:
        print("Did not get hooked")
