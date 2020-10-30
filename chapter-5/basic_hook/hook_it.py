import get_hooked


def hooked_print():
    print(f"{hooked_print.__name__} got hooked")


get_hooked.set_hook(hooked_print)

