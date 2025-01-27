from src.Datascienceproject.config.configuration import ConfigurationManager
from src.Datascienceproject.components.data_transformation import DataTransformation
from src.Datascienceproject import logger
from pathlib import Path

STAGE_NAME="Data Trnsformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        
        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status=f.read().split(" ")[-1]
            if status=="True":
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("You data schema is not valid")
        except Exception as e:
            print(e)