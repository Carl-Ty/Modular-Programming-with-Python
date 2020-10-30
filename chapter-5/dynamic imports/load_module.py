import importlib

def main():
    modules = {1:"module_a",2:"module_b",3:"module_c"}
    prompt = f"Select the module to load\n{string_dict(modules)}5Enter> "
    module_number = input(prompt)
    selected_module = modules.get(int(module_number),None)
    if selected_module != "":
        module = importlib.import_module(selected_module)
        module.say_hello()
def string_dict(dictionary):
    result = ""
    for k,v in dictionary.items():
        result = result + f"{str(k):5s} {v}\n"
    return result

if __name__ == '__main__':
    main()

