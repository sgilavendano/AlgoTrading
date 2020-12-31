import pandas as pd 
import numpy as np
import scipy
from bs4 import BeautifulSoup
import quandl

quandl.ApiConfig.api_key = 'z8yaUmivVu3o-3KngVCH'

mydata = quandl.get("EIA/PET_RWTC_D")


