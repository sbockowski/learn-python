# import time

# def measuretime(func):
#     def wrapper():
#         starttime = time.perf_counter()
#         func()
#         endtime = time.perf_counter()
#         print(f"Time needed: {endtime - starttime} seconds")
#     return wrapper

# def startstop(func):
#     def wrapper():
#         print("Starting...")
#         func()
#         print("Finished!")
#     return wrapper
# # def roll():
# #     print("Rolling on the floor laughing XD")

# # rotfl = startstop(roll)

# # rotfl()
# @measuretime
# @startstop
# def roll():
#     print("Rolling on the floor laughing XD")

# roll()

def debug(func):
    def wrapper():
        print(f"Calling function name: {func.__name__}")
    return wrapper

@debug
def scare():
    print("Boo!")
scare()

def babbys_first_deco(func):
    return print
@babbys_first_deco 
def do_stuff(a, b, c):
    return a, b, c

# decorated_function = babbys_first_deco(do_stuff)
# decorated_function("foo", "bar", "baz")
do_stuff("foo", "bar", "baz")