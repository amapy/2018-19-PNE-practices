def count_bases(seq):
    """This function is for counting the number of a's in the sequence."""

    #Counter for bases


    result_a = 0
    result_c = 0
    result_g = 0
    result_t = 0

    for b in seq:
        if b == "A":
            result_a += 1
        if b == "C":
            result_c += 1
        if b == "G":
            result_g += 1
        if b == "T":
            result_t += 1

    dict_bases = dict(zip(["A", "C", "G", "T"], [result_a, result_c, result_g, result_t]))

    #Return the dictionary with the number


    return dict_bases

#Main program


s = input("Please, introduce a sequence: ").lower()

na = s.count("a")
nc = s.count("c")
ng = s.count("g")
nt = s.count("t")

print("The number of a's is: {}".format(na), "\nThe number of c's is: {}".format(nc),
      "\nThe number of g's is: {}".format(ng), "\nThe number of t's is: {}".format(nt))

#Calculate the total sequence lenght


tl = len(s)

#Calculate the percentage of a's in the series


print("The total lenght of the sequence is: {}".format(tl))
print("The percentages of a's is {}%".format(round(100.0 * na / tl, 1)),
      "\nThe percentage of c's is: {}".format(round(100.0 * nc / tl, 1)),
       "\nThe percentage of g's is: {}".format(round(100.0 * ng / tl)),
      "\nThe percentage of t's is: {}".format(round(100.0 * nt / tl)))
