# def random(seed = None, a=0, b=10,  N=10**12, integer=True):
#
#     if seed:
#         print("Starting new sequence.")
#         global _rand_generator
#         if integer:
#             hash_plus = lambda j: int(a + (b-a)*(abs(hash(str(hash(str(seed) + str(j+1))))) % 10**13)/ 10**13)
#         else:
#             hash_plus = lambda j: a + (b-a)*(abs(hash(str(hash(str(seed) + str(j+1))))) % 10**13)/ 10**13
#         _rand_generator =  (hash_plus(j) for j in range(N))
#     try:
#         return next(_rand_generator)
#     except:
#         print("Random seed required.")

# import struct
# import time
# def lastbit(f):
#     return struct.pack('!f', f)[-1] & 1
#
# f = lastbit(5)
# def getrandbits(k):
#     "Return k random bits using a relative drift of two clocks."
#     # assume time.sleep() and time.clock() use different clocks
#     # though it might work even if they use the same clock
#     #XXX it does not produce "good" random bits, see below for details
#     result = 0
#     for _ in range(k):
#         time.sleep(0)
#         result <<= 1
#         result |= lastbit(time.clock())
#     return result
#
# k = lastbit(10)
# print(f)
# print(k)

# from time import time
#
# def time_random():
#  return time() - float(str(time()).split('.')[0])
#
# def gen_random_range(min, max):
#  return int(time_random() * (max - min) + min)
#
# if __name__ == '__main__':
#  for i in range(1):
#      print(gen_random_range(20,60))


