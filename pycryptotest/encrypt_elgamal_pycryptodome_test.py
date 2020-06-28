from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD

import sys

aaaa = 168617719568086000159379507213123216781479591206114660313130075522479671513128012959917339946222571063638657762211600982027201825188878395574962302536024800949820510786742568267994225495998118224541045617314788223214848572116763699788553459675049341138040138216528073569775323527808034877503825629537500311446
k = random.StrongRandom().randint(1, aaaa)
print(k)

print(sys.maxsize)

message = b"Hello!"

# aa = (message*pow(128961657010348571539265495281510611621030065721820355491190421605405544437433130481049658566752265633130354715167110119485118509331178101689361185825166600716400610975360143557437793065708275582617616343374673956890180713999236698414347229956544627212945402924913719723828450839690196585079832049020428092003, 100836833719315657077023107479670893219306619587385791183428512322716000054463000712589450566400258323954839255665067167413132626204226017737707529496496604187538494389598953413376534325516899506339052246787759872358963372271624730951059847207370838267787380349403680212682337263466438700552662530255861840223, 156696798063143980128248220760731616306011396815387108010879180107303754570032199729842206751431483722564550981418926601557567245339693512120831686544962553412142347854914615341395646370379720690971229405336679215073246593456756050173747781771633286883631390370536577208962362745028983872798497238467792989723)) % 156696798063143980128248220760731616306011396815387108010879180107303754570032199729842206751431483722564550981418926601557567245339693512120831686544962553412142347854914615341395646370379720690971229405336679215073246593456756050173747781771633286883631390370536577208962362745028983872798497238467792989723
# print(aa)
key = ElGamal.generate(1024, Random.new().read)

print(key.p)
print("random")
# aaaa = 167155735397405018723078157556495927453709012364626691549838238147045365236530613339513007618249987435460333212970077400460903026268887215164847534839939550280660035812961873757691890200201571322018512938229181070357877873385827246619469829463017224710738959275832916298788108230004269866393261848792356796862
# print(random.StrongRandom().randint(1, aaaa))

aaaa = key.p - 1
print(aaaa)
k = random.StrongRandom().randint(1, int(aaaa))
# print(k)
# while 1:
#     k = random.StrongRandom().randint(1, int(aaaa))
#     print("k")
#     print(k)
#     print("key.p")
#     print(key.p)
#     gcd = GCD(k, int(aaaa))
#     print(gcd)
#     if gcd == 1:
#         break

h = key.encrypt(message, k)
d = key.decrypt(h)
print(h)
print(d)