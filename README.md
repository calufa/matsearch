## matsearch

## Overview
`matsearch` provides an API for searching materials based on their composition using deep learning and material science techniques. It leverages a FAISS (Facebook AI Similarity Search) index for efficient similarity searching and DeepChem for feature extraction of material compositions. This system is designed to aid in the discovery and analysis of new material compositions, drawing inspiration from recent advances in AI-driven material science research.

## Convenience Note
The `faiss.index` and `feature_vectors.npy` files were pre-generated from a dataset of [380,000 materials by DeepMind (GNoME Project)](https://deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning/), enabling direct `api` use without needing to run `vectorize` and `create_index`.

## Components

The project consists of several key services: `api`, `vectorize` and `create_index`.

## `api`
### Running the API
To run the `api`, execute the following command:
```bash
./start.sh api
```
This will build a Docker container and start the API service, accessible on port 8080.

### Usage
To search for materials similar to a given composition, send a POST request to the `/search` endpoint with the composition data:

```bash
curl -X POST http://localhost:8080/search -H "Content-Type: application/json" -d '{"composition": "KCl"}'
```

#### Response Structure
The response includes two key pieces of information:
- `distances`: A list of distances from the query composition to the similar materials found. Lower values indicate closer similarity to the queried composition.
- `similar`: A list of similar material compositions.

```json
{
    "distances": [
        0.0023
    ],
    "similar": [
        "NaCl"
    ]
}
```

## `vectorize`
The `vectorize` service is responsible for processing the material compositions and converting them into feature vectors. This is done using the `ElementPropertyFingerprint` from DeepChem, which creates a fingerprint based on elemental stoichiometry.

### Running the Service
Execute:
```bash
./start.sh vectorize
```
This will read material compositions from a CSV file, featurize each composition, and save the resulting feature vectors as a NumPy array.

## `create_index`
The `create_index` service creates a FAISS index from the feature vectors generated by `vectorize`. This index is used for efficient similarity searches in the `api`.

### Running the Service
Execute:
```bash
./start.sh create_index
```

This will load the feature vectors, create a FAISS index, and save it for use by the `api`.

## Technologies
- **[DeepChem](https://deepchem.io/)**: Used for featurizing material compositions.
- **[FAISS](https://github.com/facebookresearch/faiss)**: Provides efficient similarity search for high dimensional vectors.
- **[Flask](https://github.com/pallets/flask)**: Serves the API for searching material compositions.
- **[Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/)**: For data manipulation and array operations.
- **[Docker](https://www.docker.com/)**: For containerizing and orchestrating the services.

---

Contact us for clarifications or contributions.
