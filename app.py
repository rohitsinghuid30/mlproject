from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestion




if __name__ == "__main__":
    logging.info("The execution has started.")

    try:
        # a=1/0
        data_injestion=DataIngestion()
        data_injestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)