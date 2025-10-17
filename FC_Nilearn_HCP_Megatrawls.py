from nilearn import datasets
import numpy as np

# Download the HCP Megatrawls connectivity matrices
megatrawls = datasets.fetch_megatrawls_netmats()

# Attributes
print("Available attributes:")

for att in megatrawls.keys():
    print(att)


# Accessing the FC matrices
print(megatrawls['correlation_matrices'])


