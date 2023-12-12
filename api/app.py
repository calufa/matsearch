from flask import Flask, request, jsonify
import faiss
import numpy as np
from pymatgen.core import Composition
import pandas as pd
import deepchem as dc


app = Flask(__name__)


# Load the FAISS index
index = faiss.read_index('/data/faiss.index')

# Load the list of material compositions
materials = pd.read_csv('/data/stable_materials_summary.csv')
compositions = materials['Composition'].tolist()

# Initialize the featurizer
featurizer = dc.feat.ElementPropertyFingerprint()


def featurize_composition(comp):
    composition = Composition(comp)
    vector = featurizer.featurize([composition])[0]
    print("vector:", vector)
    return vector


@app.route('/search', methods=['POST'])
def search():
    composition = request.json['composition']
    print("composition:", composition)
    query = featurize_composition(composition)

    # Convert the query vector to FAISS format
    query = np.array(query, dtype='float32').reshape(1, -1)

    # Search the index
    distances, indexes = index.search(query, 10)  # Top 10 results
    indexes = indexes[0]

    # Map indices to material compositions
    similar = [compositions[i] for i in indexes]

    return jsonify({
        'distances': distances.tolist(),
        'similar': similar
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
