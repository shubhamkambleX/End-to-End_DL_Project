from CnnClassifier import logger
from CnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CnnClassifier.pipeline.stage_02_prepare_base_model import  PrepareBaseModelTrainingPipeline
from CnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline


STAGE_NAME =  "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n x====================================x")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME =  "Prepare Base Model"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n x====================================x")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME =  "Model Trainer"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n x====================================x")
except Exception as e:
    logger.exception(e)
    raise e 

