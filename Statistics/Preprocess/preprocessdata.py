import numpy as np
import pandas as pd
import sklearn
from  Statistics.stat_base import Stat_base



class Preprocess(Stat_base):


    def __init__(self,filename,filetype):
        self.filename = filename
        self.filetype = filetype


    def read_file(self):

        doc_df = pd.read_csv("/app/example_test.csv")
        print('-- Reading File --------'+self.filename)
        print('================================')
        print(doc_df.head())
        return doc_df

    