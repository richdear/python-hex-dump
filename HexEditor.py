
with open("test.txt", "rb") as file:
    while True:
        chunk = file.read(2)
        if len(chunk)==0:
            break
        print(type(chunk))
        print(hex(chunk[0]))


