# Defining a new class for sequences
class Seq:
    def __init__(self, strbase):
        self.strbase = strbase
        pass

    # Function for length
    def len(self):
        return len(self.strbase)

    # Function for building the complement sequence
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

    # Function for getting the sequ3ence in reverse
    def reverse(self):
        my_reverse = self.strbase[::-1]
        return my_reverse

    # Function for getting the number of bases in the sequence
    def count_base(self, base):
        base_count = 0
        for letter in self.strbase:
            if letter == base:
                base_count += 1
        return base_count

    # Function for obtaining the percentage of bases inside the sequence
    def perc(self, base):
        return round(self.count(base) * 100 / self.length(), 1)


seq = Seq("ACGT")
potato = seq.complement()
print(potato)