# -*- coding: utf-8 -*-    
from collections import Counter

def check_anagram(string1, string2):
    return Counter(string1) == Counter(string2)


if __name__ == '__main__':
    string1 = input("Enter First String: ")
    string2 = input("Enter Second String: ")
    if check_anagram(string1, string2):
        print("Strings are Anagram!")
    else:
        print("Strings are not Anagram!")
 
