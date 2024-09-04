from src.data.eda import EDA
from src.utils import *
from src.settings import Settings, Paths
from src.data import NWBDataLoader


# Initialize a Settings object to load and manage settings configurations
settings = Settings()
settings.load_settings()

# Initialize a Paths object using the loaded settings to manage file and directory paths
paths = Paths(settings=settings)
paths.load_device_paths()

# Initialize the NWBDataLoader with the settings and paths to handle NWB data loading
data_loader = NWBDataLoader(settings, paths)
data = data_loader.load_data()


eda = EDA(data)
eda.plot_electrode_positions('sub-01')  # Replace 'P01' with actual subject ID
eda.plot_electrode_quality('sub-01')
eda.plot_power_spectral_density('sub-01', session_id=4, channel_idx=34)
eda.plot_behavioral_labels_distribution('sub-01')
eda.analyze_movement_events('sub-01')
eda.plot_pose_trajectories('sub-01', 'L_Wrist')
eda.plot_coarse_behavior_labels('sub-01')

