from math import *

n = int(input())
arr = list(map(int, input().split()))
offset = -min(min(arr), 0)


def fft(v, inv=False):
    n = len(v)
    if n == 1: return v
    ye, yo = fft(v[::2], inv), fft(v[1::2], inv) 
    y, a, wj = [0]*n, (2-4*inv)*pi/n, 1
    w = complex(cos(a), sin(a))
    for i in range(n//2):
        y[i] = ye[i] + wj * yo[i]
        y[i + n//2] = ye[i] - wj * yo[i]
        wj *= w
    return y


def mult(p1, p2):
    n = 2**(len(bin(len(p1) + len(p2) - 1)) - 2)
    p1 = p1 + [0]*(n - len(p1))
    p2 = p2 + [0]*(n - len(p2))
    fft1, fft2 = fft(p1), fft(p2)
    return [round(t.real/n) for t in fft([fft1[i]*fft2[i] for i in range(n)], inv=True)]


p = [0]*(max(arr)+offset+1)
for i in arr: p[i+offset] += 1
z, ans = p[offset], 0 # z for number of 0's


prod = mult(p, p)
for i in range(len(p)): prod[2*i] -= p[i]
ans -= 2*z*(n-1)


for i in range(len(p)): ans += prod[i+offset]*p[i]
print(ans)
