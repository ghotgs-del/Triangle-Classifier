import math

def is_valid_triangle(a, b, c):
    """Return True if the given sides can form a valid triangle."""
    if a <= 0 or b <= 0 or c <= 0:
        return False

    return(
        a + b > c 
        and a + c > b
        and b + c > a
    )

def classify_triangle(a, b, c):
    """Return the type of triangle, or "Invalid" if it cannot be built."""
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    x, y, z = sorted([a, b, c])

    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    if math.isclose(
        x * x + y * y,
        z * z,
        rel_tol=1e-9,
        abs_tol=1e-9,
    ):
        return "Right " + triangle_type

    return triangle_type