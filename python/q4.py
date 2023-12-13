# 04/15/2022

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# a = 999
# b = 999
# while str(a*b) not in str(a*b)[::-1]:
#     while str(a*b) not in str(a*b)[::-1]:
#         b -= 1
#         if b == 999:
#             b = 999
#             break
#     a -=1 

# x = tuple()         
n = list()
for a in range(100,1000):
    b = 100
    while b != 999:
        if str(a*b) in str(a*b)[::-1]:
            n.append(a*b)
            # x = (a,b)
            break
        else:
            b += 1
print(max(n))
# print(x)

# solution is 906609