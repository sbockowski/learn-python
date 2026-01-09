def simple_generator():
    yield 1
    yield 2
    yield 3

# Using the generator
gen = simple_generator()
for value in gen:
    print(value)