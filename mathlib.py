import math

x = 0.5
y = 2
n = 5

# Trigonometric
print("acos:", math.acos(x))
print("asin:", math.asin(x))
print("atan:", math.atan(x))
print("atan2:", math.atan2(1, 2))
print("cos:", math.cos(x))
print("sin:", math.sin(x))
print("tan:", math.tan(x))

# Hyperbolic
print("acosh:", math.acosh(2))
print("asinh:", math.asinh(2))
print("atanh:", math.atanh(0.3))
print("cosh:", math.cosh(x))
print("sinh:", math.sinh(x))
print("tanh:", math.tanh(x))

# Rounding
print("ceil:", math.ceil(3.4))
print("floor:", math.floor(3.7))
print("trunc:", math.trunc(3.9))

# Power & logarithmic
print("pow:", math.pow(2, 3))
print("sqrt:", math.sqrt(25))
print("log:", math.log(10))
print("log10:", math.log10(10))
print("log2:", math.log2(8))
print("log1p:", math.log1p(2))
print("exp:", math.exp(2))
print("expm1:", math.expm1(2))

# Absolute & remainder
print("fabs:", math.fabs(-5))
print("fmod:", math.fmod(7, 3))
print("remainder:", math.remainder(7, 3))

# Combinatorics
print("factorial:", math.factorial(n))
print("comb:", math.comb(5, 2))
print("perm:", math.perm(5, 2))
print("gcd:", math.gcd(12, 18))

# Distance & norm
print("dist:", math.dist((1, 2), (4, 6)))
print("hypot:", math.hypot(3, 4))

# Floating utilities
print("copysign:", math.copysign(3, -1))
print("frexp:", math.frexp(8))
print("ldexp:", math.ldexp(0.5, 4))
print("fsum:", math.fsum([1.1, 2.2, 3.3]))
print("prod:", math.prod([1, 2, 3, 4]))

# Special functions
print("gamma:", math.gamma(5))
print("lgamma:", math.lgamma(5))
print("erf:", math.erf(1))
print("erfc:", math.erfc(1))

# Angle conversion
print("degrees:", math.degrees(math.pi))
print("radians:", math.radians(180))

# Checks
print("isclose:", math.isclose(0.1 + 0.2, 0.3))
print("isfinite:", math.isfinite(10))
print("isinf:", math.isinf(math.inf))
print("isnan:", math.isnan(math.nan))
print("isqrt:", math.isqrt(17))

# Constants
print("PI:", math.pi)
print("E:", math.e)
print("TAU:", math.tau)
print("INF:", math.inf)
print("NAN:", math.nan)
