import os 
import sys 
import json 
from dotenv import load_dotenv 
load_dotenv() 

MONGO_DB_URL = os.getenv("MONGO_DB_URL") 


import certifi 
ca=certifi.where() 

import pandas as pd
import numpy as np
import pymongo 
from networksecurity.logging.logger import logging 
from networksecurity.exception.exception import NetworkSecurityException 

class NetworkDataExtract(): 
    """responsible For ETL Pipeline"""  

    def __init__(self):
        try:
            pass 
        except Exception as e: 
            raise NetworkSecurityException(e,sys) 


    def csv_to_json_converter(self,file_path):
        """responsibles for converting csv into list of json"""   
        try:
            data = pd.read_csv(file_path) 
            data.reset_index(drop=True,inplace=True)   ##removing the default index otherwise there can be a two index 
            records = list(json.loads(data.T.to_json()).values()) 
            return records
        except Exception as e: 
            raise NetworkSecurityException(e,sys)  


    def insert_data_mongodb(self,records,collection,database): 
        try:
            self.database = database 
            self.records = records
            self.collection = collection 


            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL) 
            self.database = self.mongo_client[self.database] 

            self.collection = self.database[self.collection] 
            self.collection.insert_many(self.records) 
            return (len(self.records))
        except Exception as e: 
            raise NetworkSecurityException(e,sys)