class Seq:
    def __init__(self, strbase):
        self.strbase = strbase
        pass

    def len(self):
        return len(self.strbase)

    def complement(self):
        my_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
        my_sequence = ""
        for base in self.strbase:
            if base == "A":
                my_sequence += my_dict.get("A")
            elif base == "T":
                my_sequence += my_dict.get("T")
            elif base == "C":
                my_sequence += my_dict.get("C")
            elif base == "G":
                my_sequence += my_dict.get("G")
        return my_sequence

    def reverse(self):
        my_reverse = self.strbase[::-1]
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
        my_out = "A's: {}".format(abase),"C's: {}".format(cbase),"G's: {}".format(g_base),"T's: {}".format(tbase)
        return my_out

    def perc(self):
        length = len(self.strbase)
        my_out2 = ("- The percentage of A's is: {}%".format(round(100.0 * self.strbase.count("A") / length, 1)),
                "- The percentage of C's is: {}%".format(round(100.0 * self.strbase.count("C") / length, 1)),
                "- The percentage of G's is; {}%".format(round(100.0 * self.strbase.count("G") / length, 1)),
                "- The percentage of T's is; {}%".format(round(100.0 * self.strbase.count("T") / length, 1)))
        return my_out2
