# -*- coding: utf-8 -*-
"""DataOperationsHw1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d6diVV103eY2hAT9jspUhxo_dy1i2cac
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Union
class DataOperations:
    """ The aim of this class is having a dinamic structure to 
    get informations about our data that came from any kind of 
    data file type.
    By the first function, dataset is taken from the user and converting 
    pandas dataframe
    """
    
    def __init__(self, user_input: Union[str, np.ndarray, pd.DataFrame]):
        if isinstance(user_input, np.ndarray):
            user_input = pd.DataFrame(user_input)
        elif isinstance(user_input, str):
          path = user_input.split(sep = ".")
          filetype = path[-1]
          if filetype == "csv":
                self.df = pd.read_csv(user_input)
                return self.df
          elif filetype == "json":
                self.df = pd.read_json(user_input)
                return self.df
          else:
                raise Exception("Please provide a proper variable.")
        elif isinstance(user_input, pd.DataFrame):
          return self.pd
        
    def get_statistics(self):
        """Return statistics of the given data"""
        data = self.user_input
        print(self.data.describe())
        print(self.data.info())
        # ya da direk olarak return self.data.describe() da kullanabilirsin.
        
    def visualize(self):
        """Visualize the given data"""
        data = self.user_input
        plt.plot(self.data)