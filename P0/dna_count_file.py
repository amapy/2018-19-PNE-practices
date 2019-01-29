with open("file_dna_test.txt", "r") as file:

    for line in file:
        line = line.lower()
        line = line.replace('\n', '')

        print("- Total length: ", len(line), "\n- A: ", line.count("a"), "\n- C: ", line.count("c"), "\n- G: ", line.count("g"), "\n- T: ", line.count("t"))

    file.close()


