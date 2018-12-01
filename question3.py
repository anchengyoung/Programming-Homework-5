#A palindromic number reads the same both ways. The largest palindrome
#made from the product of two 2-digit numbers is 9009 = 91 * 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

pal = []

def Palindrome(n):
    og_num = list(str(n))
    rv_num = list(str(n))
    rv_num.reverse()
    return og_num == rv_num

for x in range(100, 1000):
    for y in range(100, 1000):
        product = x * y
        if Palindrome(product):
            pal.append(product)

print(max(pal))
