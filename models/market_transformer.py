import torch
import torch.nn as nn

class MarketTransformer(nn.Module):
    def __init__(self, input_dim=32, hidden_dim=64, num_layers=2):
        super().__init__()
        self.transformer = nn.Transformer(d_model=hidden_dim, num_encoder_layers=num_layers)
        self.fc = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        x = self.transformer(x, x)
        return self.fc(x[-1])