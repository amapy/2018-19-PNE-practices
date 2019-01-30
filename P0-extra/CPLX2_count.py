info = open("cplx2.txt", "r")

lines = info.readlines()

info.close()

info = open("cplx2.txt", "w")

for line in lines:
    if line[0] !=">":
        info.write(line)
        line = line.lower()

print("- A: ", line.count("a"), "\n- C: ", line.count("c"), "\n- G: ", line.count("g"), "\n- T: ", line.count("t"))

info.close()



