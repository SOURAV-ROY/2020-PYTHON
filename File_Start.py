with open("sourav.txt", mode="r") as s_file:
    for line in s_file.readlines():
        # print(line, end="")
        # print(line.strip(), end="")
        # words = line.split(" ")
        striped_line = line.strip()
        words = striped_line.split(" ")
        print(words)
print("***Finished***")
