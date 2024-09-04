# n3hub_project
## Description

This project focuses on EcoG Analysis

## Settings

In the GitHub repository, you will find `settings_sample.yaml` and `device_path_sample.yaml` in the `configs` folder. Copy these files into the `configs` folder and remove `_sample` from the copied file names. This is done because `settings.yaml` and `device_path.yaml` are included in `.gitignore` to prevent conflicts among team members.

### Device Path Configuration

Edit `device_path.yaml` to provide the correct paths to your dataset:

```yaml
raw_dataset_path: \"D:/path_to_dataset/dataset\"
preprocessed_dataset_path: \"D:/path_to_dataset/dataset_preprocessed/\"
model_path: \"D:/path_to_working_directory/saved_model/\"
```

The `raw_dataset_path` should contain folders for each subject containing multiple sessions:
- `sub-01`: Contains Session data `sub-01_ses-*_behavior+ecephys.nwb` .
- `sub-02`: Contains Session data `sub-02_ses-*_behavior+ecephys.nwb` .


### Settings Configuration

Edit `settings.yaml` to modify the training parameters:

```yaml
dataset: "AJILE12"

# Training LDGD
load_trained_model : False
batch_size : 100
num_epochs : 100
test_size: 0.2

# Enable or disable debug mode
debug_mode: true
```

## Running the Project

### Steps to Run the Code

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Install Dependencies**:
   Ensure you have Python and the necessary packages installed. You can install the required packages using:
   ```sh
   pip install -r requirements.txt
   ```

3. **Prepare Configuration Files**:
   Copy the sample configuration files and remove the `_sample` suffix:
   ```sh
   cp configs/settings_sample.yaml configs/settings.yaml
   cp configs/device_path_sample.yaml configs/device_path.yaml
   ```
   Edit `configs/device_path.yaml` and `configs/settings.yaml` with the appropriate paths and settings.


4. **Run the Main Script**:
   Execute the main script to start training:
   ```sh
   python main.py
   ```

## Experiments

To run experiments, open the Jupyter notebooks in the `experiments` folder.

## Project Structure

```
├── .gitignore
├── configs
│   ├── device_path.yaml
│   └── settings.yaml
├── main.py
├── README.md
├── results
├── saved_model
└── src
    ├── data
    │   ├── data_loader.py
    │   ├── data_preprocessor.py
    │   └── __init__.py
    ├── experiments
    │   ├── data_visualization.ipynb
    │   └── __init__.py
    ├── model
    │   └── __init__.py
    ├── settings
    │   ├── paths.py
    │   ├── settings.py
    │   └── __init__.py
    ├── utils
    │   ├── multitapper
    │   │   ├── example.py
    │   │   ├── multitaper_spectrogram_python.py
    │   │   ├── README.md
    │   │   └── __init__.py
    │   ├── utils.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── utils.cpython-312.pyc
    │       └── __init__.cpython-312.pyc
    ├── visualization
    │   ├── vizualize_utils.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── vizualize_utils.cpython-312.pyc
    │       └── __init__.cpython-312.pyc
    └── __init__.py
