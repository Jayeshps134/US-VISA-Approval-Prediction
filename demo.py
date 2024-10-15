from us_visa.logger import logging
import sys
from us_visa.exception import USvisaException
from us_visa.pipline.prediction_pipeline import USvisaData, USvisaClassifier

"""
logging.info("enter try-catch block")
try:
    a=2/0
    logging.info("divisible by 0")
except Exception as e:
    #raise USvisaException(e, sys)
    logging.error(USvisaException(e, sys))
"""

"""
from us_visa.pipline.training_pipeline import TrainPipeline

train_ppl = TrainPipeline()
train_ppl.run_pipeline()
"""

usvisadata = USvisaData(continent="Asia", education_of_employee="High School",has_job_experience= "Y",
                        requires_job_training="N", no_of_employees=18000, region_of_employment="West",
                        prevailing_wage=800,full_time_position="Y",company_age=50, unit_of_wage="Hour")

test_data = usvisadata.get_usvisa_input_data_frame()


usclf = USvisaClassifier()
print(usclf.makepredict(dataframe=test_data))