import sys 
import os 
from networksecurity.exception.exception import NetworkSecurityException 
from networksecurity.logging.logger import logging 
  

from pushmongodb.push_data import NetworkDataExtract

if __name__ == "__main__":

    FILE_PATH = "Network_Data\phisingData.csv"

    DATABASE = "NetworkSecurity"
    COLLECTION = "NetworkData"

    network_obj = NetworkDataExtract()

    records = network_obj.csv_to_json_converter(FILE_PATH)

    print("Total records:", len(records))

    no_of_records = network_obj.insert_data_mongodb(
        records,
        COLLECTION,
        DATABASE
    )

    
    print("Successfully inserted:", no_of_records)  

if __name__ == '__main__':
    try:
        logging.info("Testing started")

        result = 10 / 0
        print("the result will not printed",result)

    except Exception as e:
        logging.error("An error occurred")
        raise NetworkSecurityException(e, sys)