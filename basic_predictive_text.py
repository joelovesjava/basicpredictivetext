# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 21:30:11 2023

@author: kearn
"""

# Predictive text

def top_two_values(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    top_two_keys = [key for key, value in sorted_items[:2]]
    return top_two_keys

print("Type some sentences using the verb \"be\",\nand in the form \"pronoun - verb - adjective\": ")
t = 1
qs = []

suggestions = {
    'pronoun': {},
    'verb': {},
    'adjective': {}
}

while t <= 10:
    q = input(f"Sentence {str(t)}: ")
    qs.append(q.split())
    t += 1

for a in qs:
    suggestions['pronoun'][a[0]] = suggestions['pronoun'].get(a[0], 0) + 1
    suggestions['verb'][a[1]] = suggestions['verb'].get(a[1], 0) + 1
    suggestions['adjective'][a[2]] = suggestions['adjective'].get(a[2], 0) + 1

print("Write a new sentence, paying attention to the suggestions")
newpron = input(f"Pronoun: \nSuggestions: {top_two_values(suggestions['pronoun'])}: ")
newverb = input(f"Verb: \nSuggestions: {top_two_values(suggestions['verb'])}: ")
newadj = input(f"Adjective: \nSuggestions: {top_two_values(suggestions['adjective'])}: ")

print(f"New sentence: {newpron} {newverb} {newadj}")