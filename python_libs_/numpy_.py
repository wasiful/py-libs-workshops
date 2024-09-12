import numpy as np

# 1. Array Creation
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr_zeros = np.zeros((3, 3))
arr_ones = np.ones((3, 3))
arr_empty = np.empty((2, 2))
arr_identity = np.eye(3)
arr_arange = np.arange(0, 10, 2)
arr_linspace = np.linspace(0, 1, 5)
arr_random = np.random.random((2, 2))
arr_normal = np.random.randn(3, 3)

# 2. Array Attributes
print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Data Type:", arr2.dtype)
print("Dimensions:", arr2.ndim)

# 3. Indexing and Slicing
print("Element [0,1]:", arr2[0, 1])
print("Column 1:", arr2[:, 1])
print("Row 0:", arr2[0, :])
print("Rows 1 to 2:", arr2[1:, :])

# Boolean Indexing
print("Elements greater than 3:", arr2[arr2 > 3])

# 4. Array Operations
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([[10, 20, 30], [40, 50, 60]])
print("Addition:\n", arr3 + arr4)
print("Matrix Multiplication:\n", np.dot(arr3, arr4.T))

# Aggregation Operations
print("Sum:", arr2.sum())
print("Mean:", arr2.mean())
print("Max:", arr2.max())
print("Min:", arr2.min())
print("Std Dev:", arr2.std())
print("Variance:", arr2.var())

# 5. Reshaping and Resizing
reshaped_arr = arr2.reshape((3, 2))
print("Reshaped Array:\n", reshaped_arr)
resized_arr = np.resize(arr2, (3, 3))
print("Resized Array:\n", resized_arr)
flattened_arr = arr2.flatten()
print("Flattened Array:", flattened_arr)
transposed_arr = arr2.T
print("Transposed Array:\n", transposed_arr)

# 6. Broadcasting
vec = np.array([1, 2, 3])
broadcasted_arr = arr2 + vec
print("Broadcasted Addition:\n", broadcasted_arr)

# 7. Linear Algebra
matrix = np.array([[1, 2], [3, 4]])
determinant = np.linalg.det(matrix)
inverse = np.linalg.inv(matrix)
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Determinant:", determinant)
print("Inverse:\n", inverse)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# 8. Statistics
print("Median:", np.median(arr2))
print("Correlation Coefficient:\n", np.corrcoef(arr2))
print("50th Percentile:", np.percentile(arr2, 50))

# 9. Random Number Generation
uniform_random = np.random.uniform(low=0, high=10, size=10)
normal_random = np.random.normal(loc=0, scale=1, size=10)
integers_random = np.random.randint(low=0, high=10, size=5)
sampled_random = np.random.choice(arr1, size=3)
print("Uniform Random:", uniform_random)
print("Normal Random:", normal_random)
print("Random Integers:", integers_random)
print("Random Sampled:", sampled_random)

# 10. Handling Missing Values
arr_with_nan = np.array([1, 2, np.nan, 4, np.nan])
print("NaN Check:", np.isnan(arr_with_nan))
arr_no_nan = np.nan_to_num(arr_with_nan, nan=-1)
print("NaN Replaced:", arr_no_nan)

# 11. Data Type Conversion
arr_float = arr1.astype('float32')
print("Converted to Float32:", arr_float)

# 12. File I/O
np.save('array.npy', arr1)
loaded_arr = np.load('array.npy')
print("Loaded Array from file:", loaded_arr)
np.savetxt('array.txt', arr1)
loaded_txt_arr = np.loadtxt('array.txt')
print("Loaded Array from text file:", loaded_txt_arr)

# 13. Advanced Indexing
indexing_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Integer Array Indexing:", indexing_arr[[0, 2], [1, 2]])
print("Fancy Indexing:", indexing_arr[[0, 1], [2, 1]])

# 14. Vectorization
vec = np.array([1, 2, 3])
squared_vec = np.sqrt(vec)
print("Vectorized Square Root:", squared_vec)

# 15. Memory Management
arr_copy = arr1.copy()
arr_copy += 1
print("Original Array:", arr1)
print("Modified Copy:", arr_copy)

# 16. Advanced Functions
x = np.arange(-5, 5, 1)
y = np.arange(-5, 5, 1)
xv, yv = np.meshgrid(x, y)
print("Meshgrid X:\n", xv)
print("Meshgrid Y:\n", yv)
print("Unique Elements:", np.unique(arr2))
arr_expanded = arr1[:, np.newaxis]
print("Expanded Array:\n", arr_expanded)

# 17. Conditional Operations
conditions = np.where(arr2 > 3, 'High', 'Low')
print("Conditional Operations:\n", conditions)

# 18. Mathematical Functions
angles = np.array([0, np.pi/4, np.pi/2])
print("Sine:", np.sin(angles))
print("Cosine:", np.cos(angles))
print("Tangent:", np.tan(angles))
print("Logarithm:", np.log(arr1[arr1 > 0]))
print("Exponential:", np.exp(arr1))

# 19. Copying and Broadcasting Rules
arr_broadcast = arr2 + 5
print("Broadcasted Addition:\n", arr_broadcast)

# 20. Array Splitting and Combining
arr5 = np.array([[1, 2, 3], [4, 5, 6]])
arr6 = np.array([[7, 8, 9], [10, 11, 12]])
hstacked_arr = np.hstack((arr5, arr6))
vstacked_arr = np.vstack((arr5, arr6))
print("Horizontally Stacked:\n", hstacked_arr)
print("Vertically Stacked:\n", vstacked_arr)
split_arr = np.split(arr2, 2)
print("Split Array:", split_arr)

# 21. Basic Iteration
print("Array Iteration:")
for x in np.nditer(arr2):
    print(x, end=' ')
print()

