Here's a Python script using the `ray` library and `ray.tune` for hyperparameter tuning, which can automatically adjust runtime parameters such as update frequency, agent rollout, and decay curves. This example assumes you are working with a reinforcement learning environment, but the concept can be adapted to other applications.

First, ensure you have the necessary libraries installed. You can install them using pip:

```bash
pip install ray[tune] gym
```

Here's the Python script:

```python
import gym
import ray
from ray import tune
from ray.rllib.agents.ppo import PPOTrainer
from ray.tune.schedulers import PopulationBasedTraining
from ray.tune.registry import register_env

def env_creator(env_config):
    return gym.make("CartPole-v0")

register_env("my_env", env_creator)

def on_train_result(info):
    result = info["result"]
    trainer = info["trainer"]
    base_lr = trainer.config["lr"]
    vf_loss_coeff = trainer.config["vf_loss_coeff"]
    
    # Example of adjusting learning rate and vf_loss_coeff based on training progress
    if result["episode_reward_mean"] > 200:
        trainer.config["lr"] = base_lr * 0.9
        trainer.config["vf_loss_coeff"] = vf_loss_coeff * 1.1

if __name__ == "__main__":
    ray.init()

    pbt = PopulationBasedTraining(
        time_attr="training_iteration",
        metric="episode_reward_mean",
        mode="max",
        perturbation_interval=10,
        hyperparam_mutations={
            "lr": lambda: tune.uniform(0.0001, 0.01).func(None),
            "vf_loss_coeff": lambda: tune.uniform(0.5, 1.0).func(None),
            "train_batch_size": [200, 400, 800],
        })

    analysis = tune.run(
        PPOTrainer,
        name="PPO_CartPole",
        scheduler=pbt,
        stop={
            "training_iteration": 100,
        },
        config={
            "env": "my_env",
            "num_workers": 1,
            "lr": 0.01,
            "vf_loss_coeff": 0.5,
            "train_batch_size": 400,
            "callbacks": {
                "on_train_result": on_train_result,
            },
        },
        num_samples=10,
    )

    print("Best config: ", analysis.get_best_config(metric="episode_reward_mean", mode="max"))

    ray.shutdown()
```

This script sets up a reinforcement learning environment using Ray's RLlib and Ray Tune for hyperparameter tuning. It uses Population-Based Training (PBT) to adjust learning rates, value function loss coefficients, and training batch sizes dynamically during training. The `on_train_result` callback function allows for further custom adjustments based on training results. Adjust the environment and parameters as needed for your specific use case.