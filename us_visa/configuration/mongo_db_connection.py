import sys
from us_visa.exception import USvisaException
from us_visa.logger import logging
import os
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY, COLLECTION_NAME
import pymongo
import numpy as np
import pandas as pd 

class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
        
    # connect with mongodb
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            self.client = pymongo.MongoClient()
            self.database = self.client[database_name]
            self.collection = self.database[COLLECTION_NAME]  # Fixed the typo 'datbase' to 'database'
            self.database_name = database_name
            logging.info("MongoDB connection successful")
        except Exception as e:
            raise USvisaException(e, sys)

    def export_data_as_dataframe(self, collection_name=COLLECTION_NAME) -> pd.DataFrame:
        """
        Method Name :   export_data_as_dataframe
        Description :   This method exports the data from a MongoDB collection as a pandas DataFrame 
        
        Output      :   A pandas DataFrame containing the data from the MongoDB collection
        On Failure  :   raises an exception
        """
        try:
            logging.info(f"Exporting data from MongoDB collection: {collection_name}")
            collection = self.database[collection_name]
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na":np.nan},inplace=True)
            logging.info(f"Data export successful, retrieved {len(df)} records")
            return df
        except Exception as e:
            raise USvisaException(e, sys)
