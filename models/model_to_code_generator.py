import numpy as np
import random

def simulate_model_output():
    # Simulated model logits translated to signal logic
    logic_options = [
        "if price[-1] > np.mean(price[-5:]): print('BUY')",
        "if price[-1] < np.mean(price[-20:]): print('SELL')",
        "if price[-1] > price[-2] > price[-3]: print('MOMENTUM BUY')"
    ]
    return random.choice(logic_options)

def generate_strategy_code():
    logic = simulate_model_output()
    code = f"""
def run():
    import numpy as np
    import pandas as pd
    price = pd.read_csv('data/price_history/TSLA.csv')['close'].values
    {logic}
"""
    return code

def save_and_run():
    name = "model_synth_" + str(random.randint(1000,9999))
    code = generate_strategy_code()

    from nlp.strategy_compiler import save_strategy, run_in_sandbox
    save_strategy(code, name)
    run_in_sandbox(name)

if __name__ == "__main__":
    save_and_run()
