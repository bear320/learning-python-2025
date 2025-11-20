class E:
    pass


class F:
    def do_something(self):
        print("Doing something in F")


class G:
    def do_something(self):
        print("Doing something in G")


class B(E, F):
    pass


class C:
    def do_something(self):
        print("Doing something in C")


class D(G):
    pass


class A(B, C, D):
    pass


a = A()
a.do_something()
print(A.mro())  # Method Resolution Order as a list
print(A.__mro__)  # Method Resolution Order as a tuple
