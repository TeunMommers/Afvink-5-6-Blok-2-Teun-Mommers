# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 07:54:28 2018

@author: Teun
"""
import time
import re
def get_seq(name):
    seq = []
    seq_list = []
    file = open(name, "r")
    for item in file:
        if ">" not in item:
            item = item.replace("\n", "")
            seq.append(item)
    for item in seq:
        for letter in item:
            seq_list.append(letter)
    return seq, seq_list
            
def main():
    name = input("Welke bestand wilt u openen")
    seq, seq_list = get_seq(name)
    part = int(input("Deel 1 of Deel 2 van de opdracht."))
    if part == 1:
        start_time = time.time()
        print("fibinaci iteratie vanaf 11")
        iteratie_1(11)
        print("--- %s in secondes ---" %  (time.time() - start_time))
        start_time = time.time()
        print("fibinaci recursief vanaf 11")
        for i in range(1,11):
            print(recursief_1(i))
        print("--- %s in secondes ---" %  (time.time() - start_time))
    elif part == 2:
        start_time = time.time()
        print("recursief vind ",recursief_2(seq_list, len(seq)))
        print("--- %s in secondes ---" %  (time.time() - start_time))
        start_time = time.time()
        print("regex vind ",regex_1(seq))
        print("--- %s in secondes ---" %  (time.time() - start_time))
        start_time = time.time()
        print("interatie vind ",iteratie_2(seq_list))
        print("--- %s in secondes ---" %  (time.time() - start_time))
        
def regex_1(seq):
    x = 0
    matchObj = re.search("[ATGC]", str(seq))
    if matchObj:
        x += 1
    if x != 0:
        return False
    else:
        return True
    
def iteratie_2(seq):
    for item in seq:
            if item != "A" or item != "T" or item != "C" or item != "G":
                return False
    
def recursief_2(seq, n):
    if seq[n] == "A" or "G" or "T" or "C":
        n -= 1
        if n == 0:
            return True
        recursief_2(seq, n)
    else:
        return False

def recursief_1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def iteratie_1(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a)
    
main()
    
    
    
    
    
            
        