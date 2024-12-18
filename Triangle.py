def equilateral(sides):
    a, b, c = sides
    if a > 0 and b > 0 and c > 0:
        if a + b >= c and b + c >= a and c + a >= b:
            return a == b == c
        return False
    return False
     
def isosceles(sides):
    a, b, c = sides 
    if a > 0 and b > 0 and c > 0:
        if a + b >= c and b + c >= a and c + a >= b:
            return a == b or b == c or c == a
        return False
    return False

def scalene(sides):
    a, b, c = sides
    if a > 0 and b > 0 and c > 0:
        if a + b >= c and b + c >= a and c + a >= b:
            return a != b and b != c and a != c
        return False
    return False
