# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:32:18 2017

@author: Teun
"""

class DNA:
    "basis info dna sequentie bereken"
    is_DNA = False
    length_DNA = 0
    DNA_sequence = ""
    RNA_sequence = ""
    GC_percentage = 0
    
    def __init__(self, name):
        self.name = name
        seq = open(self.name,"r")
        for line in seq:
            if ">" not in line:
                line.replace("\n","")
                DNA.DNA_sequence += line
        
    def get_DNA(self):
        return DNA.DNA_sequence
    
    def get_Length(self):
        DNA.length_DNA = len(DNA.DNA_sequence)
        return DNA.length_DNA
    
    def get_Transcript(self):
        for letter in DNA.DNA_sequence:
            if letter != "T":
                DNA.RNA_sequence += letter
            else:
                DNA.RNA_sequence += "U"
        return DNA.RNA_sequence
    
    def get_GC(self):
        gc = 0
        for letter in DNA.DNA_sequence:
            print(letter)
            if letter == "C":
                gc += 1
            elif letter == "G":
                gc += 1
        DNA.GC_percentage = gc*(100/len(DNA.DNA_sequence))
        return DNA.GC_percentage              

dna1 = DNA("Test dna.txt")
print(dna1.get_GC())
print(dna1.get_DNA())
print(dna1.get_Length())
print(dna1.get_Transcript())