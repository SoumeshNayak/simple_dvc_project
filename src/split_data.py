#split the raw data and save in data/prosessed folder

import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split

from get_data import read_params

def split_and_savedata(config_path):
    conig=read_params(config_path=config_path)
    train_data_path=conig["split_data"]["train_path"]
    test_data_path=conig["split_data"]["test_path"]
    raw_data_path=conig["load_data"]["raw_dataset_csv"]
    split_ratio=conig["split_data"]["test_size"]
    random_state=conig["base"]["random_state"]
    
    df=pd.read_csv(raw_data_path,sep=",")
    train,test=train_test_split(df,test_size=split_ratio,random_state=random_state)
    train.to_csv(train_data_path,sep=",",index=False,encoding="utf-8")
    test.to_csv(test_data_path,sep=",",index=False,encoding="utf-8")
if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default='params.yaml')
    parsed_args=args.parse_args()
    split_and_savedata(config_path=parsed_args.config)    