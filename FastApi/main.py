def smart_divide(func):
    def inner(a, b):
        print("Dividing", a, "by", b)
        if b == 0:
            print("Connot divide by 0!")
            return
        return func(a, b)

    return inner


@smart_divide
def divided(a, b):
    return a / b


Value1 = divided(15, 3)
print(Value1)

Value2 = divided(5, 0)
print(Value2)
