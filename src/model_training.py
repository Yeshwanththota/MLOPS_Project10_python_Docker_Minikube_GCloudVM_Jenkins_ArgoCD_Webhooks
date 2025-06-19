import os
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from src.logger import get_logger
from src.custom_exception import CustomException
from sklearn.metrics import accuracy_score, classification_report,precision_score,f1_score,recall_score

logger = get_logger(__name__)
class ModelTraining:
    def __init__(self,processed_data_path,model_output_path):
        self.processed_path = processed_data_path
        self.model_output_path = model_output_path
        self.clf = None
        self.model = None
        self.X_train, self.X_test, self.y_train, self.y_test = None, None, None, None

        os.makedirs(self.model_output_path, exist_ok=True)
        logger.info("Model Training initialized...")
    def load_data(self):
        try:
            self.X_train = joblib.load(os.path.join(self.processed_path, 'X_train.pkl'))
            self.X_test = joblib.load(os.path.join(self.processed_path, 'X_test.pkl'))
            self.y_train = joblib.load(os.path.join(self.processed_path, 'y_train.pkl'))
            self.y_test = joblib.load(os.path.join(self.processed_path, 'y_test.pkl'))
            logger.info("Data loaded successfully for model training...")
        except Exception as e:
            logger.error(f"Error while loading data for model training: {e}")
            raise CustomException("Failed to load data for model training", e)
    def train_model(self):
        try:
            self.clf = LogisticRegression(random_state=42,max_iter=1000)
            self.clf.fit(self.X_train, self.y_train)

            joblib.dump(self.clf, os.path.join(self.model_output_path, 'model.pkl'))
            logger.info("Model trained and saved successfully...")
        except Exception as e:
            logger.error(f"error while training model {e}")
            raise CustomException("failed to train model",e)
    def evaluate_model(self):
        try:
            y_pred = self.clf.predict(self.X_test)
            accuracy = accuracy_score(self.y_test,y_pred)
            precision = precision_score(self.y_test,y_pred,average="weighted")
            recall = recall_score(self.y_test,y_pred,average="weighted")
            f1 = f1_score(self.y_test,y_pred,average="weighted")

            logger.info(f"accuracy:{accuracy}")
            logger.info(f"Precision: {precision}")
            logger.info(f"recall: {recall}")
            logger.info(f"f1_score: {f1}")
            logger.info("Model Evalaution Done..")
        except Exception as e:
            logger.error(f"Error while evaluating model {e}")
            raise CustomException("failed to evaluate model",e)
    def run(self):
        self.load_data()
        self.train_model()
        self.evaluate_model()
if __name__ == "__main__":
    trainer = ModelTraining("artifacts/processed","artifacts/models")
    trainer.run()
