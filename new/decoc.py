def star(func):
    def inner(arg):
        print("*" * 5)
        func(arg)
        print("*" * 30)

    return inner


def percent(func):
    def inner(arg):
        print("%" * 5)
        func(arg)
        print("%" * 30)

    return inner


@star
@percent
def printer(x):
    print(x)


printer("Decoraters are wonoderful")
