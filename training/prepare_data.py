# Load necessary libraries
import sys
from pathlib import Path
import json
import numpy as np

from moftransformer.utils import prepare_data

# ======== RUN ========

ROOT_PATH = sys.argv[1]
DOWNSTREAM = sys.argv[2]
SAVE_PATH = sys.argv[3]

# load target property from json file
with open(f'{ROOT_PATH}/raw_{DOWNSTREAM}.json', 'rb') as json_file:
    d = json.load(json_file)

# Prepare energy grid and graph from cif files.
# Increase max length to 1000.
train_fraction = 1.0  # default value
test_fraction = 0.0   # default value
max_length=1000

prepare_data(ROOT_PATH, SAVE_PATH, downstream=DOWNSTREAM, seed=42,
            train_fraction=train_fraction, test_fraction=test_fraction, max_length=max_length) 