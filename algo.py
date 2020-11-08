import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from wallstreet import Stock, Call, Put

s = Stock('AAPL')

print(s.price)

