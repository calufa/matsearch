import numpy as np

feature_vectors = np.load('feature_vectors.npy')

# Dictionary to keep track of vector strings and their indices
vector_dict = {}

# Detect duplicates
duplicates = []

for i, vec in enumerate(feature_vectors):
    print(i)
    # Convert the vector to a string
    vec_str = ','.join(map(str, vec))

    if vec_str in vector_dict:
        # If the string is already in the dictionary, we found a duplicate
        duplicates.append((vector_dict[vec_str], i))
    else:
        # Store the index of the vector using its string representation
        vector_dict[vec_str] = i

# Print duplicates
for dup in duplicates:
    print(f"Vector {dup[0]} is a duplicate of Vector {dup[1]}")
