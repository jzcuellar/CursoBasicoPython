"""
In DNA strings, symbols "A" and "T" are complements of each other,
as "C" and "G". Your function receives one side of the DNA (string, except for Haskell);
you need to return the other complementary side. DNA strand is never empty or 
there is no DNA at all (again, except for Haskell).

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"

"""

# Using dictionaries and the map function
# Mejor practica para este caso ya que es mas legible y mejor mantenimiento con el tiempo 
# def DNA_strand(dna):
#     pairs = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
#     dna_pairs = list(map(lambda x: pairs.get(x,x), dna))
#     return ''.join(dna_pairs)

# Using List comprehension
# def DNA_strand(dna):
#     return ''.join(['A' if i == 'T' else 'T' if i == 'A' 
#                     else 'C' if i == 'G' else 'G' if i == 'C' else i for i in dna])

# #Clever One
# import string
# def DNA_strand(dna):
#     return dna.translate(string.maketrans("ATCG","TAGC")) #Transslate replaces a Character for other
#     # Python 3.4 solution || you don't need to import anything :)
#     # return dna.translate(str.maketrans("ATCG","TAGC"))

# Using dictionary comprehencion -> solution Chat GTP
def DNA_strand(dna):
    complements = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return "".join(complements[nucleotide] for nucleotide in dna)

print(DNA_strand("ATTGC"))

