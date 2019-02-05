def count_a(seq):
    """This function is for counting the number of a's in the sequence."""

    #Counter for a's
    result = 0

    for b in seq:
        if b == "A":
            result += 1

    #Return result
    return result

#Main program

s = "AGATAGAGATAGCCCAGATCCACAGATACA"

na = count_a(s)

print("The number of a's is: {}".format(na))

#Calculate the total sequence lenght
tl = len(s)

#Calculate the percentage of a's in the series
perc = round(1000.0 * na / tl, 1)

print("The total lenght of the sequence is: {}".format(tl))
print("The percentages of As is {}%".format(round(100.0 * na / tl, 1)))
