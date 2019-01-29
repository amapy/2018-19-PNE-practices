dna_code = str(input("Please, introduce a DNA sequence to get information from it: "))

dna_code = dna_code.lower()

print("- Total length: ", len(dna_code), "\n- A: ", dna_code.count("a"), "\n- C: ", dna_code.count("c"), "\n- G: ", dna_code.count("g"), "\n- T: ", dna_code.count("t"))

