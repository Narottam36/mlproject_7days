

import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path :str = os.path.join('artifacts', "train.csv")
    test_data_path :str = os.path.join('artifacts', "test.csv")
    raw_data_path :str = os.path.join('artifacts', "data.csv")


class DataIngestion:
    def __init__(self):
        self.train_data_path = os.path.join('artifacts', "train.csv")
        self.test_data_path = os.path.join('artifacts', "test.csv")
        self.raw_data_path = os.path.join('artifacts', "data.csv")

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("File read from the source location")
            os.makedirs(os.path.dirname(self.raw_data_path), exist_ok = True)
            print("os.path.dirname(self.raw_data_path) : ", os.path.dirname(self.raw_data_path))
            df.to_csv(self.raw_data_path, index= False, header = True)
            logging.info("Train test split initiated")

            train_set, test_set = train_test_split(df, test_size = 0.2, random_state=42)

            train_set.to_csv(self.train_data_path, index=False, header = True)
            test_set.to_csv(self.test_data_path, index=False, header = True)

            logging.info("Ingestion of the data is completed")

            return(
                self.train_data_path,
                self.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data, test_data)

    modeltrainer = ModelTrainer()
    r2_square = modeltrainer.initiate_model_trainer(train_arr,test_arr)
    print("Best selected modell r2_square : ", r2_square)



### Implementation without @dataclass 
# @dataclass
# class DataIngestionConfig:
#     train_data_path :str = os.path.join('artifacts', "train.csv")
#     test_data_path :str = os.path.join('artifacts', "test.csv")
#     raw_data_path :str = os.path.join('artifacts', "data.csv")


# class DataIngestion:
#     def __init__(self):
#         self.train_data_path = os.path.join('artifacts', "train.csv")
# 		self.test_data_path = os.path.join('artifacts', "test.csv")
# 		self.raw_data_path = os.path.join('artifacts', "data.csv")

#     def initiate_data_ingestion(self):
#         logging.info("Entered the data ingestion method or component")
#         try:
#             df = pd.read_csv("notebook\data\stud.csv")
#             logging.info("File read from the source location")
#             os.makedirs(os.path.dirname(self.raw_data_path), exist_ok = True)
#             print("os.path.dirname(self.raw_data_path) : ", os.path.dirname(self.raw_data_path))
#             df.to_csv(self.raw_data_path, index= False, header = True)
#             logging.info("Train test split initiated")

#             train_set, test_set = train_test_split(df, test_size = 0.2, random_state=42)

#             train_set.to_csv(self.train_data_path, index=False, header = True)
#             test_set.to_csv(self.test_data_path, index=False, header = True)

#             logging.info("Ingestion of the data is completed")

#             return(
#                 self.train_data_path,
#                 self.test_data_path
#             )

#         except Exception as e:
#             raise CustomException(e, sys)


# if __name__ == "__main__":
#     obj = DataIngestion()
#     train_data,test_data = obj.initiate_data_ingestion()

