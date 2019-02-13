from Seq import Seq

seq_1 = Seq("ACAGTATAGCTTAGC")
seq_2 = Seq("GTCCCTTTAACGATTTAG")
seq_3 = seq_1.complement()
seq_3 = Seq(seq_3)
seq_4 = seq_3.reverse()
seq_4 = Seq(seq_4)

my_seq = [seq_1, seq_2, seq_3, seq_4]

number = 0

for sequence in my_seq:
    number += 1
    print("SEQUENCE: ", number)
    print("Length: ", sequence.len()
    print(sequence.count_base())
    print(sequence.perc())
