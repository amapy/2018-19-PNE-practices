with open("cplx2.txt", "r") as info:

    for line in info:
        if line[0] != ">":
            print(line)

