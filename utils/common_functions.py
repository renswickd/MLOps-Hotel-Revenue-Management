import os
import pandas
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml
import pandas as pd

logger = get_logger(__name__)

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No file found at {file_path}")
        
        with open(file_path,"r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("YAML file read successfully")
            return config
    
    except Exception as e:
        # logger.error("Error reading the YAML file")
        raise CustomException("Failed to read YAML file" , e)
    
def load_data(path):
    try:
        logger.info("Starting to load the data")
        if not os.path.exists(path):
            raise FileNotFoundError(f"No file found at {path}")
        return pd.read_csv(path)
    
    except Exception as e:
        logger.error(f"Error loading the data {e}")
        raise CustomException("Failed to load data" , e)
    