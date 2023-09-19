import math

def mysqrt(a):
    x = a
    while True:
        # print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
        return x
    
result = mysqrt(16)
print("Estimated square root:", result)


def test_square_root():
    print("a\tmysqrt(a)\tmath.sqrt(a)\tdiff")
    print("-" * 35)
    
    for a in range(1, 10):
        my_sqrt_result = mysqrt(a)
        math_sqrt_result = math.sqrt(a)
        diff = abs(my_sqrt_result - math_sqrt_result)
        
        print(f"{a:.1f}\t{my_sqrt_result:.11f}\t{math_sqrt_result:.11f}\t{diff:.11f}")

test_square_root()