import matplotlib.pyplot as plt
from pynwb import NWBHDF5IO


class NWBVisualizer:
    def __init__(self, nwbfile):
        """
        Initializes the visualizer with an NWB file.
        :param nwbfile: Loaded NWB file object.
        """
        self.nwbfile = nwbfile

    def plot_time_series(self, series_name):
        """
        Plots a specified TimeSeries object from the acquisition.
        :param series_name: Name of the TimeSeries to plot.
        """
        time_series = self.nwbfile.acquisition[series_name]
        data, timestamps = time_series.data[:], time_series.timestamps[:]

        plt.figure(figsize=(10, 4))
        plt.plot(timestamps, data)
        plt.title(f'{series_name} Data Plot')
        plt.xlabel('Time (s)')
        plt.ylabel(time_series.unit)
        plt.grid(True)
        plt.show()

    def list_devices(self):
        """
        Lists all devices registered in the NWB file.
        """
        print("Devices in the NWB File:")
        for device_name, device in self.nwbfile.devices.items():
            print(f"{device_name}: {device}")

    def list_electrode_groups(self):
        """
        Lists all electrode groups in the NWB file.
        """
        print("Electrode Groups:")
        for group_name, group in self.nwbfile.electrode_groups.items():
            print(f"{group_name}: {group.description}")