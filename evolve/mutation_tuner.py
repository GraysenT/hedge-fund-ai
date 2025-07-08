class MutationTuner:
    def __init__(self):
        self.performance_history = {}

    def tune(self, strategy_name, recent_return):
        history = self.performance_history.setdefault(strategy_name, [])
        history.append(recent_return)
        if len(history) > 10:
            history.pop(0)

        avg_return = sum(history) / len(history)
        mutation_rate = 0.05
        if avg_return < 0:
            mutation_rate = 0.2
        elif avg_return > 0.05:
            mutation_rate = 0.01

        print(f"[TUNER] {strategy_name} mutation rate tuned to {mutation_rate:.2f} based on avg return {avg_return:.3f}")
        return mutation_rate