FROM deepchemio/deepchem

RUN conda install -n deepchem -c conda-forge \
	flask \
	scikit-learn
RUN conda install -n deepchem -c pytorch \
	faiss-cpu

WORKDIR /app
