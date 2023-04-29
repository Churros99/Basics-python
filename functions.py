def hello_world():
    print("Hello, world!")

def hello_world_name(first_name):
    print(f"Hello, {first_name}!")

def hello_world_args(*args):
    first_name = args[0]
    second_name = args[1]
    third_name = args[2]

    print(f"Hello, {first_name} / {second_name} / {third_name} !")

def hello_world_keyword_args(first_person, second_person):
    print(f"Hello, {first_person} / {second_person}")


def hello_world_arbitrary_keyword_args(**kwargs):
    if kwargs.get('second_person') is None:
        print("No hay segunda persona")
    else:
        print(f"Hello, {kwargs['first_person']} / {kwargs['second_person']}!")


# hello_world()
# hello_world_name("Obed")
# hello_world_name("Jose")
# hello_world_args("Omar", "Jose", "Irving")
# hello_world_keyword_args(first_person="Omar", second_person="Irving")
hello_world_arbitrary_keyword_args(first_person="Bandy", second_person="Luis")
hello_world_arbitrary_keyword_args(first_person="Luis")