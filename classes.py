# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:40:02 2017

@author: Teun
"""

def main():
    gc1 = GC(file_input())
    print("Hier volgt de standaard data voor de sequentie met het hoogste GC%")
    print("Transcript naar RNA: ",gc1.get_Transcript())
    print("Lengte sequentie: ", gc1.get_Lenth()) 
    print("GC percentage: ", gc1.get_GC())
    

def file_input():
    name = input("Geef bestandsnaam in")
    file = open(name, "r")
    fasta_list = []
    fasta = ""
    top_GC = 0
    for line in file:
        if ">"not in line:
            fasta += line.replace("\n","")
        else:
            fasta_list, top_GC = check_GC(fasta, top_GC, fasta_list)
    fasta_list, top_GC = check_GC(fasta, top_GC, fasta_list)
    return fasta_list

def check_GC(fasta, top_GC, fasta_list):
    gc = 0
    for item in fasta:
        if item != "G":
            gc -= 1
        elif item != "C":
            gc -= 1
        else:
            gc += 1
    if gc >= top_GC:
        fasta_list = []
        fasta_list.append(fasta)
        top_GC = gc
    elif top_GC == 0:
        fasta_list = []
        fasta_list.append(fasta)
        top_GC = gc
    return fasta_list, top_GC

class GC:
    RNA_sequence = ""
    seq_Length = 0
    GC_percentage = 0
    
    def __init__(self, list_DNA):
        gc = 0
        top = 0
        self.item = []
        print(list_DNA)
        for item in list_DNA:
            for letter in item:
                if letter == "G":
                    gc += 1
                elif letter == "C":
                    gc += 1
            if gc/len(item) >= top:
                self.item = item
            gc = 0
    
    def get_Transcript(self):
        for letter in self.item:
            if letter == "T":
                GC.RNA_sequence += "U"
            else:
                GC.RNA_sequence += letter
        return GC.RNA_sequence

    def get_Lenth(self):
        GC.seq_Length = len(self.item)
        return GC.seq_Length        
    
    def get_GC(self):
        gc = 0
        for letter in self.item:
            if letter == "G":
                gc += 1
            elif letter == "C":
                gc += 1
        GC.GC_percentage = (100/len(self.item))*gc
        return GC.GC_percentage
main()
    