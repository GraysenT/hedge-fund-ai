import pandas as pd
import numpy as np

class LowLatencyRouter:
    def __init__(self, min_trades=10, delay_penalty_weight=1.0, slippage_penalty_weight=0.5):
        self.min_trades = min_trades
        self.delay_penalty_weight = delay_penalty_weight
        self.slippage_penalty_weight = slippage_penalty_weight

    def compute_strategy_weights(self, execution_log: pd.DataFrame):
        """
        Given execution logs, return latency-optimized strategy weights.
        Args:
            execution_log: DataFrame with columns ['strategy', 'delay_sec', 'slippage', 'execution_price', 'confidence']
        Returns:
            dict: {strategy_name: weight}
        """
        if execution_log.empty:
            return {}

        # Filter out low-frequency strategies
        strat_counts = execution_log['strategy'].value_counts()
        valid_strategies = strat_counts[strat_counts >= self.min_trades].index
        filtered = execution_log[execution_log['strategy'].isin(valid_strategies)]

        if filtered.empty:
            return {}

        # Compute penalty scores
        grouped = filtered.groupby('strategy').agg({
            'delay_sec': 'mean',
            'slippage': 'mean',
            'confidence': 'mean'
        }).reset_index()

        # Lower delay and slippage = higher score
        grouped['score'] = (
            grouped['confidence'] -
            self.delay_penalty_weight * grouped['delay_sec'] -
            self.slippage_penalty_weight * grouped['slippage']
        )

        # Normalize to weights
        grouped['score'] = grouped['score'].clip(lower=0)
        total_score = grouped['score'].sum()
        if total_score == 0:
            weights = {row['strategy']: 0 for _, row in grouped.iterrows()}
        else:
            grouped['weight'] = grouped['score'] / total_score
            weights = dict(zip(grouped['strategy'], grouped['weight']))

        return weights
