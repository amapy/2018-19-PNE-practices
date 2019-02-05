class Seq:
    """A class for representing sequences."""
    def __init__(self, strbases): #Siempre que defina una clase tengo que hacer esta definición, es la definición constructora.
    #Dentro de los paréntesis se pueden poner más variables.
    #strbases es un atributo.
        print("New empty sequence created.")

        self.strbases = strbases

    def len(self):
        return len(self.strbases)

class Gene(Seq):
    #This class is derived from the Seq. All the objects of cass Gene will inheritage the methods from Seq class.
    pass

#s1 y s2 son objetos de tipo Seq.
s1 = Gene("AAGCTTC")
s2 = Seq("AAGAT")

str1 = s1.strbases
str2 = s2.strbases

l1 = s1.len()
l2 = s2.len()

print("Sequence 1: {}".format(str1))
print("Sequence 2: {}".format(str2))

print("Length of the sequence 1 is: {}".format(l1))
print("Length of the sequence 2 is: {}".format(l2))

