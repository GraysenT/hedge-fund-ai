# strategies/overnight_rotator.py

from typing import List
from .signalizer import Signalizer
from .fed_day import FedDay

class OvernightRotator:
    def __init__(self, signalizer: Signalizer, fed_day: FedDay):
        self.signalizer = signalizer
        self.fed_day = fed_day

    def blend_signals(self, signals: List[int]) -> List[int]:
        """
        Blends fed_day signals with signalizer behavior.
        """
        fed_day_signals = self.fed_day.get_signals()
        signalizer_signals = self.signalizer.get_signals(signals)

        blended_signals = []
        for fd_signal, s_signal in zip(fed_day_signals, signalizer_signals):
            blended_signal = self.blend(fd_signal, s_signal)
            blended_signals.append(blended_signal)

        return blended_signals

    @staticmethod
    def blend(fd_signal: int, s_signal: int) -> int:
        """
        Blends two signals. The blending strategy is defined here.
        """
        # This is a placeholder. Actual blending strategy should be defined here.
        return (fd_signal + s_signal) // 2