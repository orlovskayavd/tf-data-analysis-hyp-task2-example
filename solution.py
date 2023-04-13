import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 776430833 # Your chat ID, do not change the name of the variable

def solution(x: np.array, y: np.array) -> bool:
    # perform KS test on x and y
    ks_stat, p_value = ks_2samp(x, y)
    # compare p-value with significance level
    significance_level = 0.1
    if p_value > significance_level:
        return True # cannot reject the hypothesis of sample homogeneity
    else:
        return False # reject the hypothesis of sample homogeneity

# Load the data
historical_data = pd.read_csv("historical_data.csv")["F"].values
modified_data_type_1 = pd.read_csv("modified_data_of_type_1.csv")["F"].values
modified_data_type_2 = pd.read_csv("modified_data_of_type_2.csv")["F"].values
modified_data_type_3 = pd.read_csv("modified_data_of_type_3.csv")["F"].values

# Test the function on different samples
print(solution(historical_data[:300], historical_data[:300])) # should return True
print(solution(historical_data[:300], modified_data_type_1[:300])) # should return True
print(solution(historical_data[:300], modified_data_type_2[:300])) # should return False
print(solution(historical_data[:300], modified_data_type_3[:300])) # should return False
