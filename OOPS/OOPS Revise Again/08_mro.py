# mro-method_resolution_order
class A:
    label = "A: Base class"

class B(A):
    label = "B : Masala blend"

class C(A):
    label = "C: Herbal blend"

class D(B,C):
    pass

cup = D()

print(cup.label) # B : Masala blend
# why because which ever the class of D inherited first  e.g (B) will call it first.
# the order of inheritence matters alot.

print(D.__mro__) 
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
