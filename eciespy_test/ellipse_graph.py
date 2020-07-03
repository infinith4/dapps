import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(0, 100, 101)
# y = np.random.randn(101)
# #Y^2 = X^3 + X + 1

# plt.plot(x, y, color=(0,0,1))

# plt.show()

# x = np.linspace(-10,10,100)
# y = x*x
# plt.plot(x,y) 
# plt.show()

# a = 1
# b = 1 

# y, x = np.ogrid[-5:5:100j, -5:5:100j] 
# plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x - b, [0]) 
# plt.grid() 
# plt.show() 

# import sympy as sym
# sym.init_printing()
# Pi = sym.S.Pi # 円周率
# E = sym.S.Exp1 # 自然対数の底

# # 使用する変数の定義(小文字1文字は全てシンボルとする)
# (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) = sym.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')

# def generator_p(start): # 引数が指定されればその色をそうでないときは順番に色を生成するためのジェネレーター
#     prime = 37 # リストの数 (素数なのでprimitiveに何を指定しても必ず最大周期になる)
#     primitive = 8 # 生成元 (1ステップ当たり色相がprimitive * 37/360度進む)
#     g0 = start # 開始元 (実際に返されるのは g0 * primitive)
#     while True:
#         val = yield g0
#         if val: # ジェネレーターに引数が渡されるとそれを開始元としてリセットする
#             g0 = val
#         g0 += primitive
#         if g0 >= prime: # 剰余を取る
#             g0 -= prime
# gen_hexnum = generator_p(0) # 引数に初期色を入れる
# gen_hexnum.__next__() # ジェネレーターの初期化

# def hexNum(num, type): # 色のリスト
#     # 基本色(白背景で汎用的に使える落ち着いた色)
#     color_basic = ['#9c1954', '#9e1a46', '#9d1e38', '#9a252a', '#962d1c', '#8f350d', '#873c00',
#                    '#7d4300', '#734900', '#674f00', '#5b5300', '#4d5700', '#3e5b00', '#2b5d00',
#                    '#0f6009', '#00611c', '#00632b', '#00643a', '#006449', '#006558', '#006567',
#                    '#006575', '#006482', '#00648e', '#006298', '#0060a0', '#005ea6', '#005baa',
#                    '#0056aa', '#0051a9', '#2f4ca4', '#50459d', '#673d94', '#78358a', '#862d7d', '#902470', '#981e62']
#     # 彩度の高い色(目立つが多用はしないほうがよい。)
#     color_vivid = ['#ffadc7', '#ffadbc', '#ffaeb2', '#ffb0a8', '#ffb29e', '#ffb596', '#f9b88f',
#                    '#f1bc8a', '#e9bf86', '#dfc385', '#d5c685', '#caca87', '#becd8b', '#b2cf90',
#                    '#a6d298', '#99d4a0', '#8dd5aa', '#80d7b4', '#74d7bf', '#6ad8ca', '#61d8d5',
#                    '#5bd7e0', '#59d6e9', '#5dd5f2', '#65d3f9', '#71d1ff', '#7fceff', '#8ecbff',
#                    '#9ec8ff', '#afc4ff', '#bec1ff', '#cdbdfd', '#dab9f7', '#e6b6ef', '#f0b3e6', '#f9b0dc', '#ffaed2']
#     # 薄い色(白背景では使わない。黒背景で使うことを想定。)
#     color_thin = ['#ffc3d5', '#ffc3cd', '#ffc3c5', '#ffc4be', '#ffc6b7', '#ffc8b1', '#fbcaac',
#                   '#f5cca9', '#efcfa6', '#e8d2a5', '#e0d4a5', '#d8d7a6', '#cfd9a9', '#c6dbad',
#                   '#bdddb3', '#b5deb9', '#ace0c0', '#a5e0c7', '#9ee1cf', '#98e1d7', '#94e1df',
#                   '#92e1e6', '#92e0ed', '#94dff4', '#99def9', '#9fdcfd', '#a7daff', '#b1d8ff',
#                   '#bbd5ff', '#c5d3ff', '#cfd0ff', '#dacdfc', '#e3cbf7', '#ecc8f2', '#f3c6eb', '#f9c5e4', '#fec4dc']

#     if (type == 'thin'):
#         hex_list = color_thin
#     elif (type == 'vivid'):
#         hex_list = color_vivid
#     else:
#         hex_list = color_basic
#     if num is not None:
#         gen_hexnum.send(num)
#     return hex_list[gen_hexnum.__next__()]

# F = y**2 - x**3 - x -1
# sym.plot_implicit(F, (x, -2, 2), (y, -2, 2), line_color=hexNum(2, 'thin'))
# y, x = np.ogrid[-5:5:100j, -5:5:100j] 
# plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0]) 
# plt.grid() 
# #plt.show() 

# # https://tex2e.github.io/blog/crypto/point-of-elliptic-curve-over-GF

# # def quadratic_residue(a, p):
# #     return pow(a, (p - 1) // 2, p) == 1

# # def f(x, p):
# #     return (x**3 + x + 6) % p

# # def calc_y(z, p):
# #     res = z**3 % p
# #     return res % p, -res % p

# # p = 11
# # points = []
# # for x in range(p):
# #     z = f(x, p)
# #     if quadratic_residue(z, p):
# #         y1, y2 = calc_y(z, p)
# #         print('x = %2d, z = %d, QR(%2d, 11)? = True, y = %d, %d' % (x, z, x, y1, y2))
# #         points.append((x, y1))
# #         points.append((x, y2))
# #     else:
# #         print('x = %2d, z = %d, QR(%2d, 11)? = False' % (x, z, x))

# # print("points:")
# # print(sorted(points))

# # E(F_11)={(2,4),(2,7),(3,5),(3,6),(5,2),(5,9),(7,2),(7,9),(8,3),(8,8),(10,2),(10,9),∞}

# # def quadratic_residue(a, p):
# #     return pow(a, (p - 1) // 2, p) == 1

# # def f(x, p):
# #     return (x**3 + x + 1) % p

# # def calc_y(z, p):
# #     res = z**3 % p
# #     return res % p, -res % p

# # p = 5
# # points = []
# # for x in range(p):
# #     z = f(x, p)
# #     if quadratic_residue(z, p):
# #         y1, y2 = calc_y(z, p)
# #         print('x = %2d, z = %d, quadratic_residue(%2d, %d)? = True, y = %d, %d' % (x, z, x, p, y1, y2))
# #         points.append((x, y1))
# #         points.append((x, y2))
# #     else:
# #         print('x = %2d, z = %d, quadratic_residue(%2d, %d)? = False' % (x, z, x, p))

# # print("points:")
# # print(sorted(points))

# # x =  0, z = 1, quadratic_residue( 0, 5)? = True, y = 1, 4
# # x =  1, z = 3, quadratic_residue( 1, 5)? = False
# # x =  2, z = 1, quadratic_residue( 2, 5)? = True, y = 1, 4
# # x =  3, z = 1, quadratic_residue( 3, 5)? = True, y = 1, 4
# # x =  4, z = 4, quadratic_residue( 4, 5)? = True, y = 4, 1

# # E(F_5)={(0, 1), (0, 4), (2, 1), (2, 4), (3, 1), (3, 4), (4, 1), (4, 4),∞}



# def quadratic_residue(a, p):
#     return pow(a, (p - 1) // 2, p) == 1

# def f(x, p):
#     return (x**3 + 2*x + 17) % p

# def calc_y(z, p):
#     res = z**3 % p
#     return res % p, -res % p

# p = 31
# points = []
# for x in range(p):
#     z = f(x, p)
#     if quadratic_residue(z, p):
#         y1, y2 = calc_y(z, p)
#         print('x = %2d, z = %d, quadratic_residue(%2d, %d)? = True, y = %d, %d' % (x, z, x, p, y1, y2))
#         points.append((x, y1))
#         points.append((x, y2))
#     else:
#         print('x = %2d, z = %d, quadratic_residue(%2d, %d)? = False' % (x, z, x, p))

# print("points:")
# print(sorted(points))
# print(len(points))



def plot_ec(a, b, p):
    xlist = []
    ylist = []
    for x in range(p):
        for y in range(p):
            if((x**3 + a * x + b - y**2) % p == 0):
                # 方程式を満たす x,y の組をリストに格納
                xlist.append(x)
                ylist.append(y)
                #以下は表示のため
                plt.figure(figsize=(10,10))
                plt.axis([0,p,0,p])
            if(p < 55):
                point_style = 'o'
                plt.grid(which='major',linestyle=':'
                , color="black")
                plt.yticks( [i for i in range(p)] )
                plt.xticks( [i for i in range(p)] )
        else:
            point_style = '.'
    plt.plot(xlist, ylist, point_style , color="black")
    plt.show()
#plot_ec(1, 1, 17)
#plot_ec(2, 17, 31)

# F_p 上の y^2=x^3+ax+b での p, a, b
p, a, b = 23, 1, 1
G=(0,1)
def inv(n, p):
    return pow(n, p-2, p)

def ec_double(A):
    l = (((3 * A[0] **2) + a) * inv(2*A[1], p)) % p
    x = (l ** 2 - A[0] - A[0]) % p
    y = (l * (A[0] - x) - A[1]) % p
    return x, y

G2=ec_double(G)
print(G2) # (6, 19)

def ec_add(A, B):
    l = ((B[1] - A[1]) * inv(B[0] - A[0], p)) % p
    x = (l ** 2 - B[0] - A[0]) % p
    y = (l * (A[0] - x) - A[1]) % p
    return x, y
G3 = ec_add(G2, G)
print(G3) # (3, 13)

from ecdsa.ellipticcurve import CurveFp, Point

# F_p 上の y^2=x^3+ax+b の意味での p, a, b
p, a, b = 23, 1, 1
c = CurveFp(p,a,b)
# G を c 上の点(0,1)とする
G = Point(c, 0, 1)
current = G
for i in range(1,28):
    print("{}G:¥t{}".format(i,current))
    current = current + G

# F_p 上の y^2=x^3+ax+b の意味での p, a, b
p, a, b = 31, 2, 17
c = CurveFp(p,a,b)
# G を c 上の点(10,13)とする
G = Point(c, 10, 13)
current = G
for i in range(1,91):
    print("{}G:¥t{}".format(i,current))
    current = current + G
