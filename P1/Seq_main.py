from Seq import Seq

seq_1 = Seq("ACAGTATAGCTTAGC")
seq_2 = Seq("GTCCCTTTAACGATTTAG")
seq_3 = seq_1.complement()
seq_4 = seq_3.reverse()

my_seq = [seq_1, seq_2, seq_3, seq_4]

number = 0

for sequence in my_seq:
    print(sequence)
    len(sequence)
    count_base(sequence)
    perc(sequence)

    number += 1
