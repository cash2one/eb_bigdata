# -*- coding:utf8 -*-
class A:
    def __init__(self, a):
        self.a = a


class B(A):
    def __init__(self, a, be):
        A.__init__(self,a)
        # self(a)
        # super(B, self).__init__(a)
        self.b = be


b = B("1", "2")
print b.a
# class Foo():
#     def __init__(self, frob, frotz)
#         self.frobnicate = frob
#         self.frotz = frotz
#
#
# class Bar(Foo):
#     def __init__(self, frob, frizzle)
#         super.__init__(frob, 34)
#         self.frazzle = frizzle
