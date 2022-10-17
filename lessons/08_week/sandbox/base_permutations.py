#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Monoid:
    def __init__(self, null, typeify, operator):
        # __init__ allows class variables to be definded 
        # when the class is initiated
        self.null = null
        self.typeify = typeify
        self.operator = operator

    def __call__(self, *args): 
        # __call__ method enables classes for which 
        # the instances behave like functions and 
        # can be called as such 
        result = self.null
        for arg in args:
            arg = self.typeify(arg)
            result = self.operator(result, arg)
        return result

def cartesian_prod(a_list,b_list):
    print(f"my a_list and my b_list : {a_list} && {b_list}")
    # input()
    c = []
    for a in a_list:
        for b in b_list:
            c.append(a+b)
    return c

cartesian_product_monoid  = Monoid([''],  lambda x: x, cartesian_prod) # define class

base_list = ['A','C','G','T']

print("Length 2 cartesian products")
permutations_list = cartesian_product_monoid(base_list, base_list)
print(f"\t [+] Length 2 Permutations_list = {permutations_list}")
print(f"\t [+] Number of permutations : {len(permutations_list)}")


print("Length 4 cartesian products")
permutations_list = cartesian_product_monoid(base_list, base_list, base_list, base_list)
print(f"\t [+] Length 4 Permutations_list = {permutations_list}")
print(f"\t [+] Number of permutations : {len(permutations_list)}")

print("Length 5 cartesian products")
permutations_list = cartesian_product_monoid(base_list, base_list, base_list, base_list, base_list)
print(f"\t [+] Length 5 Permutations_list = {permutations_list}")
print(f"\t [+] Number of permutations : {len(permutations_list)}")

