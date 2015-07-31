#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#----Standard library imports----

from random import randint

#--------------------------------


# Generating a mutation

def replace_base_randomly(base_seq):
    """Return a sequence with the base at a randomly selected position
    of base_seq replaced by a base chosen randmly from the three bases
    that are not at that position."""

    position = randint(0, len(base_seq)-1)
    base = base_seq[position]
    bases = 'TCAG'

    bases.replace(base, '')  # Replace base with empty string, not in choice
    newbase = bases[randint(0,2)]
    beginning = base_seq[0:position]
    end = base_seq[position+1:]
    return beginning + newbase + end


# Validating a sequence

def validate_base_sequence(base_sequence, RNAflag=False): 
    """Return True if the string base_sequence contains only upper
    or lowercase T (U if RNAflag), C, A, G characters, otherwise False"""

    seq = base_sequence.upper()
    return len(seq) == (seq.count('U'if RNAflag else 'T')
                        + seq.count('C') + seq.count('A') 
                        + seq.count('G'))


def validate_base_sequence_by_set(base_sequence, RNAflag=False):
    """Return True if the string base_sequence contains only upper
    or lowercase T (U if RNAflag), C, A, G characters, otherwise False"""

    DNAbases = set('ATCGatcg')
    RNAbases = set('AUCGaucg')
    return set(base_sequence) <= (RNAbases if RNAflag else DNAbases)

def validate_base_sequence_by_comprehension(base_sequence, RNAflag=False):
    """Return True if the string base_sequence contains only upper
    or lowercase T (U if RNAflag), C, A, G characters, otherwise False"""

    valid_bases = 'UCAG' if RNAflag else 'TCAG'
    return all ([(base in valid_bases)
                for base in base_sequence.upper()])

        
# Generating a random sequence (first a base, then a codon)    
        
def random_base(RNAflag=False):
    """Return a base randomly. True=RNA, False=DNA"""

    return ('UCAG' if RNAflag else 'TCAG')[randint(0,3)]  
    
    
#def random_codon(RNAflag=False):
    """Return a codon randomly. True=RNA, False=DNA"""

    return random_base(RNAflag) + random_base(RNAflag) + random_base(RNAflag)
         


# Percentage of GC
    
def gc_content(base_seq):
    """Return the percentage of bases in base_seq that are C or G"""

    seq = base_seq.upper()
    return (seq.count('G') + seq.count('C')) / len(seq)
    
# Fastq : number of sequences

def fastq_nb_seq(filename):
    """Return the number of sequences in fastq file"""

    with open(filename, 'r') as fastq:
        t = fastq.readlines()
        return(print(len(t)/4))


# Writing a file by input

def writing():
    """ Create a new file if necessary and write in it by input"""
    
    print("Nom du fichier :")
    filename=input()
    f = open(filename, 'a')
    f.close()
    print("Nouvelles lignes de commandes ? O/N ?")
    a = input()

    while a == "O" :
        print("Ecrire les nouvelles lignes de commandes :")
        with open(filename, 'a') as f:
            f.write(input())
            print("Nouvelles lignes de commandes ? O/N ?")
            a = input()
    
    print("Affichage du contenu du fichier :")
    with open(filename, 'r') as f:
        print(f.read())

# Compare two files
        
def compare(filename1, filename2):
    """Return if the two files are equals or not"""

    f1 = open(filename1, 'r')
    f2 = open(filename2, "r")
    if f1.read() == f2.read() :
        print("They are equal.")
    else :
        print("They are different.")
    f1.close()
    f2.close()

           

# Assertion

def test():
    
    assert .5 == gc_content('ATGC')
    assert not validate_base_sequence('ACUG', True)
    print('All tests passed.')
    
        
