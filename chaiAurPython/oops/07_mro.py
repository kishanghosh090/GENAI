class A:
    label = "A: Base Class"

class B(A):
    label = "B: Masala Blend"

class C(A):
    label = "C: Elychi tea"

class D(C,B):
    pass

cup = D()
print(cup.label)

print(D.__mro__)