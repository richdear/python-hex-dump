file = open("test.tar.gz", mode="rb")

data=file.read()

print(type(data))

print(data.hex())

file.close()

