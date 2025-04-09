import numpy as np

arr = np.array([0, 1, np.nan, np.inf, -np.inf, 5])
print("Any nonzero:", np.any(arr))
print("All nonzero:", np.all(arr))
print("Check NaN:", np.isnan(arr))
print("Check Inf:", np.isinf(arr))
print("Check Finite:", np.isfinite(arr))
print("Check Real:", np.isreal(arr))
print("Check Complex:", np.iscomplex(arr))
print("Check Scalar:", np.isscalar(arr))

arr2 = np.array([1, 2, 3, 4, 5])
print("Less than 3:", np.less(arr2, 3))
print("Greater than 3:", np.greater(arr2, 3))
print("Less or equal to 3:", np.less_equal(arr2, 3))
print("Greater or equal to 3:", np.greater_equal(arr2, 3))

print("Zeros array:", np.zeros((2, 3)))

vector = np.arange(1, 10)
print("Arange:", vector)
print("Reshape:", vector.reshape(3, 3))
print("Linspace:", np.linspace(0, 10, 5))
print("Random Integers:", np.random.randint(1, 100, 5))

vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
print("Dot Product:", np.dot(vec1, vec2))
