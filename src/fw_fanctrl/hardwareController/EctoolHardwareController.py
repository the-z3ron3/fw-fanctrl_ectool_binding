import ctypes
import pathlib
from abc import ABC

from fw_fanctrl.hardwareController.HardwareController import HardwareController


class EctoolHardwareController(HardwareController, ABC):
    noBatterySensorMode = False
    nonBatterySensors = None

    def __init__(self, no_battery_sensor_mode=False):
        # Load the shared library into ctypes
        self.libname = pathlib.Path().absolute() / "libectool.so"
        self.ectool_lib = ctypes.CDLL(self.libname)

        if no_battery_sensor_mode:
            self.noBatterySensorMode = True
            self.populate_non_battery_sensors()

    def populate_non_battery_sensors(self):
        self.nonBatterySensors = []

        # Tell ctypes the format of `BatteryInfo` struct
        class BatteryInfo(ctypes.Structure):
            _fields_ = [
                ("capacity", ctypes.c_int),
                ("kilowatts", ctypes.c_float)
            ]

        # Set return type of get_battery_info() function
        self.ectool_lib.get_battery_info.restype = BatteryInfo
        
        # Call get_temperature() function to get battery information
        battery_info = self.ectool_lib.get_battery_info()

        # Append each member into list
        for info in battery_info:
            self.nonBatterySensors.append(info)

    def get_temperature(self):
        # Set return type of get_temperature() function
        self.ectool_lib.get_temperature.restype = ctypes.c_int
        
        # Call get_temperature() function to get temperature
        temps = self.ectool_lib.get_temperature()
        
        return temps
        
    def set_speed(self, speed):
        # Call set_speed() function to set fan speed
        self.ectool_lib.set_speed(speed)

    def is_on_ac(self):
        # Set return type of is_on_ac() function
        self.ectool_lib.is_on_ac.restype = ctypes.c_bool
        
        # Call is_on_ac() function to check if laptop is on AC or DC power
        on_ac = self.ectool_lib.is_on_ac()
        
        return on_ac

    def pause(self):
        # Call pause() function to pause fan
        self.ectool_lib.pause()

    def resume(self):
        # Empty for ectool, as setting an arbitrary speed disables the automatic fan control
        pass
