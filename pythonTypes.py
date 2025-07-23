def add(firstname: str | list, lastname: str):

    return firstname +' '+ lastname

firstname = 'laksh'
lastname = 'lukhi'
print(add(firstname, lastname))

def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

say_hi('laksh')
say_hi()