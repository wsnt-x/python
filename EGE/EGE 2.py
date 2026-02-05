# print("a b c d")
# for a in range(2):
#     for b in range(2):
#         for c in range(2):
#             for d in range(2):
#                 f = ((a and b)==(not c)) and (b<=d)
#                 if f:
#                     print(a, b, c, d)

# from itertools import *
# def f(x,y,z,w):
#     return not(((x<=(y and w)) and (z<=(x or y)))==w)
# for a,b,c,d in product([0,1],repeat=4):
#     table=((a,1,b,0,1),
#            (c,1,1,1,1),
#            (1,d,1,0,1))
#     if len(table)==len(set(table)):
#         for p in permutations("xyzw",r=4):
#             if all(f(**dict(zip(p,line)))==line[-1] for line in table):
#                 print(*p)

# from itertools import *
# def f1(x,y, z ,w):
#     return (x <= y) or ((not w) == z)
# def f2(x, y, z, w) :
#     return (x <= y) == (w and not z)
# for a, b, c, d, e, f in product ([0, 1], repeat=6) :
#     table = [(a, b, c, 0),
#              (d, e, 0, 0),
#              (f, 0, 0, 0)]
#     if len (table) != len (set (table)) :
#         continue
# for p in permutations ('xywz') :
#     if [f1 (**dict (zip(p, r))) for r in table] \
#     == [f2 (**dict (zip(p, r))) for r in table]:
#         print (*p)

# from itertools import *
# def f(x,y,z,w):
#     return w and ((y<=x)<=z)
# for a,b,c,d,e in product([0,1],repeat=5):
#     table=((a,b,0,1,1),
#            (0,c,d,0,1),
#            (0,1,e,1,0))
#     if len(table)==len(set(table)):
#         for p in permutations("xyzw",r=4):
#             if all(f(**dict(zip(p, line))) == line[-1] for line in table):
#                 print(*p)

# from itertools import *
# def f(x,y,z,w):
#     return (z<=w) and y and (not x)
# for a,b,c,d,e in product([0,1],repeat=5):
#     table=((0,1,a,0,1),
#            (b,0,c,d,1),
#            (0,1,1,e,0))
#     if len(table)==len(set(table)):
#         for p in permutations("xyzw",r=4):
#             if all(f(**dict(zip(p,line)))==line[-1] for line in table):
#                 print(*p)