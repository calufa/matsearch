import numpy as np
import deepchem as dc
from pymatgen.core import Composition
import pandas as pd
from joblib import Parallel, delayed
import time


start_time = time.time()

print("Load featurizer...")
featurizer = dc.feat.ElementPropertyFingerprint()

print("Reading materials...")
df = pd.read_csv('/data/stable_materials_summary.csv')


def featurize_composition(index, row):
    comp = row['Composition']
    composition = Composition(comp)
    vector = featurizer.featurize([composition])[0]
    print(index, vector)
    return vector


print("Featurizing compositions using parallel processing...")
features = Parallel(n_jobs=-1)(
    delayed(featurize_composition)(index, row) for index, row in df.iterrows()
)

print("Converting features to NumPy array...")
feature_vectors = np.array(features, dtype='float32')

print("Saving feature vectors to file...")
np.save('/data/feature_vectors.npy', feature_vectors)

total_time = time.time() - start_time
print(f"Total featurization time: {total_time} seconds")
