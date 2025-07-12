```python
import numpy as np
import pandas as pd

def apply_decay(signal_data, regime_data, sector_data, volume_data, decay_factors):
    """
    Applies decay to older signal data based on regime, sector, and volume shifts.

    Parameters:
        signal_data (pd.DataFrame): DataFrame containing the signal values with columns ['date', 'signal_value'].
        regime_data (pd.DataFrame): DataFrame containing regime information with columns ['date', 'regime'].
        sector_data (pd.DataFrame): DataFrame containing sector information with columns ['date', 'sector'].
        volume_data (pd.DataFrame): DataFrame containing volume information with columns ['date', 'volume'].
        decay_factors (dict): Dictionary containing decay factors for different regimes, sectors, and volume shifts.

    Returns:
        pd.DataFrame: DataFrame with decayed signal values.
    """
    # Ensure data is sorted by date
    signal_data = signal_data.sort_values('date')
    regime_data = regime_data.sort_values('date')
    sector_data = sector_data.sort_values('date')
    volume_data = volume_data.sort_values('date')

    # Merge all data on the 'date' column
    merged_data = pd.merge_asof(signal_data, regime_data, on='date')
    merged_data = pd.merge_asof(merged_data, sector_data, on='date')
    merged_data = pd.merge_asof(merged_data, volume_data, on='date')

    # Calculate volume shift
    merged_data['volume_shift'] = merged_data['volume'].pct_change().fillna(0)

    # Apply decay factors
    def decay_signal(row):
        regime_factor = decay_factors.get('regime', {}).get(row['regime'], 1)
        sector_factor = decay_factors.get('sector', {}).get(row['sector'], 1)
        volume_factor = decay_factors.get('volume_shift', {}).get(
            'high' if row['volume_shift'] > 0.1 else 'low', 1)
        return row['signal_value'] * regime_factor * sector_factor * volume_factor

    merged_data['decayed_signal'] = merged_data.apply(decay_signal, axis=1)

    return merged_data[['date', 'decayed_signal']]

# Example usage
signal_data = pd.DataFrame({
    'date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
    'signal_value': [100, 150, 120]
})
regime_data = pd.DataFrame({
    'date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
    'regime': ['bull', 'bear', 'bull']
})
sector_data = pd.DataFrame({
    'date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
    'sector': ['tech', 'finance', 'tech']
})
volume_data = pd.DataFrame({
    'date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
    'volume': [1000, 1100, 1050]
})
decay_factors = {
    'regime': {'bull': 0.95, 'bear': 0.90},
    'sector': {'tech': 0.98, 'finance': 0.97},
    'volume_shift': {'high': 0.99, 'low': 1.01}
}

decayed_signals = apply_decay(signal_data, regime_data, sector_data, volume_data, decay_factors)
print(decayed_signals)
```