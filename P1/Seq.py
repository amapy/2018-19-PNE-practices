class Seq:
    def __init__(self, strbase):
        self.strbase = strbase
        pass

    def len(self):
        return len(self.strbase)

    def complement(self):
        my_complement = self.complement()
        return "Original sequence: {}".format(self), "Complement sequence: {}".format(my_complement)

    def reverse(self):
        my_reverse = self.reverse()
        return my_reverse

    def count_base(self):
        abase = 0
        cbase = 0
        g_base = 0
        tbase = 0
        for base in self.strbase:
            if base == "A":
                abase += 1
            elif base == "C":
                cbase += 1
            elif base == "G":
                g_base += 1
            elif base == "T":
                tbase += 1
        return ("- Number of A's: {}".format(abase),
                "\n- Number of C's: {}".format(cbase),
                "\n- Number of G's: {}".format(g_base),
                "\n- Number of T's: {}".format(tbase))

    def perc(self):
        length = len(self.strbase)
        return ("- The percentage of A's is: {}%".format(round(100.0 * self.strbase.count("A") / length, 1)),
                "- The percentage of C's is: {}%".format(round(100.0 * self.strbase.count("C") / length, 1)),
                "- The percentage of G's is; {}%".format(round(100.0 * self.strbase.count("G") / length, 1)),
                "- The percentage of T's is; {}%".format(round(100.0 * self.strbase.count("T") / length, 1)))
