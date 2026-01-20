def simple_generator():
    yield 1
    yield 2
    yield 3

# Using the generator
gen = simple_generator()
for value in gen:
    print(value)

def get_doubles(my_list: list):
    for element in my_list:
        print(f"Zwracam wartość {element * 2}")
        yield element * 2

for double in get_doubles([5,6,7,8,9]):
    print(f"Przetwarzam {double}.")