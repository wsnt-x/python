# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 f = (y<=(x or z)) and (z<=y)
#                 if not f:
#                     print(x,y,z,w)

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
#     return (w or y) and (x<=(not z)) and (not w)
# for a,b,c,d,e in product([0,1],repeat=5):
#     table=((a,0,b,0,1),
#            (1,c,d,e,1),
#            (1,1,0,0,1))
#     if len(table)==len(set(table)):
#         for p in permutations("xyzw",r=4):
#             if all(f(**dict(zip(p,line)))==line[-1] for line in table):
#                 print(*p)


# from itertools import *
# def f(x,y,z,w):
#     return not((((not w)<=(not y))<=(not z))<=x)
# for a,b,c,d,e in product([0,1],repeat=5):
#     table=((a,b,1,0,1),
#            (c,1,d,1,1),
#            (0,1,e,0,0))
#     if len(table)==len(set(table)):
#         for p in permutations("xyzw",r=4):
#             if all(f(**dict(zip(p,line)))==line[-1] for line in table):
#                 print(*p)


# from itertools import *
# def f(x,y,w,z):
#     return (z<=(not(y<=x))) or w
# for a1,a2,a3,a4 in product([0,1], repeat=4):
#     table = [(1,a1,1,a2),
#              (0,1,a3,0),
#              (a4,1,1,0)]
#     if len(set(table))==len(table):
#         for p in permutations('xywz'):
#             if [f(**dict(zip(p,r))) for r in table]==[1,1,1]:
#                 print(*p)
