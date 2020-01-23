"""
The 'esp32' module contains functions and classes specifically aimed at controlling ESP32 modules.

synced with micropython release 1.12
"""

from typing import overload, Optional, List, Union
from machine import Pin


WAKEUP_ALL_LOW: bool = False
WAKEUP_ANY_HIGH: bool = True


def hall_sensor() -> int:
    """
    Read the raw value of the internal Hall sensor, returning an integer.
    """
    ...


def raw_temperature() -> int:
    """
    Read the raw value of the internal temperature sensor, returning an integer.
    """
    ...


def wake_on_touch(wake: bool) -> None:
    """
    Configure whether or not a touch will wake the device from sleep. wake should be a boolean value.
    """
    ...


def wake_on_ext0(pin: Optional[Pin], level: bool) -> None:
    """
    Configure how EXT0 wakes the device from sleep. pin can be 'None' or a valid Pin object. level should be
    'esp32.WAKEUP_ALL_LOW' or 'esp32.WAKEUP_ANY_HIGH'.
    """
    ...


def wake_on_ext1(pins: Optional[List[Pin]], level: bool) -> None:
    """
    Configure how EXT1 wakes the device from sleep. pins can be 'None' or a tuple/list of valid Pin objects. level
    should be 'esp32.WAKEUP_ALL_LOW' or 'esp32.WAKEUP_ANY_HIGH'.
    """
    ...


class Partition(id: Union[str, int]):
    """
    Create an object representing a partition. id can be a string which is the label of the partition to retrieve, or
    one of the constants: 'BOOT' or 'RUNNING'.
    """
    # Used in the Partition constructor to fetch various partitions.
    BOOT: int
    RUNNING: int
    TYPE_APP
    # Used in 'Partition.find' to specify the partition type.
    TYPE_DATA

    @classmethod
    def find(cls, type=TYPE_APP, subtype=0xff, Optional[label=None]):
        """
        Find a partition specified by type, subtype and label. Returns a (possibly empty) list of Partition objects.
        """
        ...

    def info(self):
        """
        Returns a 6-tuple '(type, subtype, addr, size, label, encrypted)'.
        """
        ...

    @overload
    def readblocks(self, block_num, buf):
        """
        """
        ...

    @overload
    def readblocks(self, block_num, buf, offset):
        """
        """
        ...

    @overload
    def writeblocks(self, block_num, buf):
        """
        """
        ...

    @overload
    def writeblocks(self, block_num, buf, offset):
        """
        """
        ...

    def ioctl(self, cmd, arg):
        """
        These methods implement the simple and extended block protocol defined by 'uos.AbstractBlockDev'.
        """
        ...

    def set_boot(self):
        """
        Sets the partition as the boot partition.
        """
        ...

    def get_next_update(self):
        """
        Gets the next update partition after this one, and returns a new Partition object.
        """
        ...


class RMT(channel, *, pin=None, clock_div: int = 8):
    """
    This class provides access to one of the eight RMT channels. channel is required and identifies which RMT channel
    (0-7) will be configured. pin, also required, configures which Pin is bound to the RMT channel. clock_div is an
    8-bit clock divider that divides the source clock (80MHz) to the RMT channel allowing the resolution to be
    specified.
    """
    def source_freq(self):
        """
        Returns the source clock frequency. Currently the source clock is not configurable so this will always return
        80MHz.
        """
        ...

    def clock_div(self):
        """
        Return the clock divider. Note that the channel resolution is '1 / (source_freq / clock_div)'.
        """
        ...

    def wait_done(self, timeout=0):
        """
        Returns True if 'RMT.write_pulses' has completed.

        If timeout (defined in ticks of 'source_freq / clock_div') is specified the method will wait for timeout or
        until 'RMT.write_pulses' is complete, returning 'False' if the channel continues to transmit.

        Warning: Avoid using 'wait_done()' if looping is enabled.
        """
        ...

    def loop(self, enable_loop):
        """
        Configure looping on the channel, allowing a stream of pulses to be indefinitely repeated. enable_loop is bool,
        set to True to enable looping.
        """
        ...

    def write_pulses(self, pulses, start):
        """
        Begin sending pulses, a list or tuple defining the stream of pulses. The length of each pulse is defined by a
        number to be multiplied by the channel resolution '(1 / (source_freq / clock_div))'. start defines whether the
        stream starts at 0 or 1.
        """
        ...


class ULP():
    """
    This class provides access to the Ultra-Low-Power co-processor.
    """
    # Selects the wake level for pins.
    WAKEUP_ALL_LOW
    WAKEUP_ANY_HIGH

    def set_wakeup_period(self, period_index, period_us):
        """
        Set the wake-up period.
        """
        ...

    def load_binary(self, load_addr, program_binary):
        """
        Load a program_binary into the ULP at the given load_addr.
        """
        ...

    def run(self, entry_point):
        """
        Start the ULP running at the given entry_point.
        """
        ...

