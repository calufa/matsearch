import numpy as np
import faiss

feature_vectors = np.load('/data/feature_vectors.npy')

# Number of dimensions for each vector
d = feature_vectors.shape[1]

# Create a FAISS index
index = faiss.IndexFlatL2(d)

# Add vectors to the index
index.add(feature_vectors)

# Save the index
faiss.write_index(index, "/data/faiss.index")
