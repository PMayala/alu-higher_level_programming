#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dict = sorted(a_dictionary)
    for k in sort_dict:
        print(f"{k}: {a_dictionary[k]}")
