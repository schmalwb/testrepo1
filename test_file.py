# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:06:20 2022

@author: DICE
"""

Lalilu

import os
os.chdir('C:\\Users\\DICE\\sciebo\\research\\DEAL_econ2\\orig2') #change directory as needed
from datetime import datetime
import pandas as pd
from pybliometrics.scopus import ScopusSearch

from pybliometrics.scopus.utils import config
print(config['Authentication']['APIKey'])  # Show keys


