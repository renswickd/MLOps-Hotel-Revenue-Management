import os
import pandas as pd
import numpy as np
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml,load_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE

logger = get_logger(__name__)
config_path = os.path.join("config", "config.yaml") # need to update in paths_config
config = read_yaml(config_path)

def preprocess_data(df):
    try:
        logger.info("Starting our Data Processing step")

        logger.info("Dropping the columns")
        df.drop(columns=['Unnamed: 0', 'Booking_ID'] , inplace=True)
        df.drop_duplicates(inplace=True)

        cat_cols = config["data_processing"]["categorical_columns"]
        num_cols = config["data_processing"]["numerical_columns"]

        logger.info("Applying Label Encoding")

        label_encoder = LabelEncoder()
        mappings={}

        for col in cat_cols:
            df[col] = label_encoder.fit_transform(df[col])
            mappings[col] = {label:code for label,code in zip(label_encoder.classes_ , label_encoder.transform(label_encoder.classes_))}

        logger.info("Label Mappings are : ")
        for col,mapping in mappings.items():
            logger.info(f"{col} : {mapping}")

        logger.info("Doing Skewness HAndling")

        skew_threshold = config["data_processing"]["skewness_threshold"]
        skewness = df[num_cols].apply(lambda x:x.skew())

        for column in skewness[skewness>skew_threshold].index:
            df[column] = np.log1p(df[column])

        return df
    
    except Exception as e:
        logger.error(f"Error during preprocess step {e}")
        raise CustomException("Error while preprocess data", e)


def select_features(df):
    try:
        logger.info("Starting our Feature selection step")

        X = df.drop(columns='booking_status')
        y = df["booking_status"]

        model =  RandomForestClassifier(random_state=42)
        model.fit(X,y)

        feature_importance = model.feature_importances_

        feature_importance_df = pd.DataFrame({
                    'feature':X.columns,
                    'importance':feature_importance
                        })
        top_features_importance_df = feature_importance_df.sort_values(by="importance" , ascending=False)

        num_features_to_select = config["data_processing"]["no_of_features"]

        top_10_features = top_features_importance_df["feature"].head(num_features_to_select).values

        logger.info(f"Features selected : {top_10_features}")

        top_10_df = df[top_10_features.tolist() + ["booking_status"]]

        logger.info("Feature slection completed sucesfully")

        return top_10_df
    
    except Exception as e:
        logger.error(f"Error during feature selection step {e}")
        raise CustomException("Error while feature selection", e)