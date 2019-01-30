with open("file_dna_test.txt", "r") as file:

    dna_seq = []

    for line in file:
        line = line.lower()
        line = line.replace('\n', '')
        dna_seq.append(line)

    total_seq = []

    for chain in dna_seq:
        total_seq += chain

    print("- Total length: ", len(total_seq), "\n- A: ", total_seq.count("a"), "\n- C: ", total_seq.count("c"), "\n- G: ", total_seq.count("g"), "\n- T: ", total_seq.count("t"))

    file.close()



