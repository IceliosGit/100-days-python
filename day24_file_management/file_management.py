with open("/Users/anton/Desktop/test_absolute.txt", mode="w") as file:  # absolute path
    file.write("Hello world")

with open("../../../Desktop/test_relative.txt", mode="w") as file:  # relative path
    file.write("Hello world")

with open("./text.txt", mode="w") as file:
    file.write("hello world")

with open("text.txt", mode="r") as file:  # can also omit the ./
    print(file.read())
