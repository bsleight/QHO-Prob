####Trapezoid Rule Integration of a function f, from x=a to x=b, with N steps
def trap_int(f,a ,b, N):
    dx = float(b - a) / N
    ans = 0.0
    ans += f(a)/2.0
    for i in range(1, N):
        ans += f(a + i*dx)
    ans += f(b)/2.0
    ans = ans * dx
    return ans
