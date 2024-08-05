
from src.utils import *
from src.settings import Settings, Paths
from src.data import SnapDataLoader, EDA, DataProcessor



settings = Settings()
settings.load_settings()

paths = Paths(settings=settings)
paths.load_device_paths()


data_loader = SnapDataLoader(settings, paths)
data_loader.load_data()

# Preprocess data
data_processor = DataProcessor()
df_train = data_loader.get_train_data()
target_column = 'ride (target)'  # Replace with your target column name

X_train, X_val, y_train, y_val = data_processor.preprocess(df_train, target_column)

