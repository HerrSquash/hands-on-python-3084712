RUN_INDENTED = True

message = "running unindented"

if RUN_INDENTED:
    message = "running indented"

print(message)


def my_function():
    greet = "Hello, dude!"
    return greet


print(my_function())
