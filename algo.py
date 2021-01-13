import pandas as pd
import matplotlib as plt
import numpy as np
import statistics
import math
import quandl
quandl.ApiConfig.api_key = 'z8yaUmivVu3o-3KngVCH'


mydata = quandl.get("EIA/PET_RWTC_D")
print(mydata)

