with open("sourav.txt", mode="r") as s_file:
    all_words = []
    for line in s_file.readlines():
        # print(line, end="")
        # print(line.strip(), end="")
        # words = line.split(" ")
        striped_line = line.strip()
        words = striped_line.split(" ")
        # print(words)
        all_words += words
    # print(all_words)
    unique_words = set(all_words)
    print(len(all_words))
    print(len(unique_words))
print("***Finished***")
