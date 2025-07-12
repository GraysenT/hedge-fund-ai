# strategies/momentum_breakout_booster.py

import numpy as np
import pandas as pd
from scipy.signal import argrelextrema

def calculate_momentum(data, period):
    return data - data.shift(period)

def calculate_breakout(data, period):
    return data[(data > data.rolling(window=period).max())]

def find_extrema(data, comparator):
    return argrelextrema(data.values, comparator)

def momentum_breakout_booster(data, momentum_period, breakout_period):
    data['momentum'] = calculate_momentum(data['Close'], momentum_period)
    data['breakout'] = calculate_breakout(data['Close'], breakout_period)
    
    maxima = find_extrema(data['momentum'], np.greater)
    minima = find_extrema(data['momentum'], np.less)
    
    data['maxima'] = data.iloc[maxima]['momentum']
    data['minima'] = data.iloc[minima]['momentum']
    
    boosted_momentum_breakout = data[(data['maxima'].notna() | data['minima'].notna()) & data['breakout'].notna()]
    
    return boosted_momentum_breakout

def generate_signal():
    return 'skip'
