import os
import json
import pickle
import sqlite3
from pathlib import Path
from datetime import datetime

MEMORY_DIR = Path("agent_memories")
LOG_PATH = Path("logs")
DB_FILE = LOG_PATH / "agent_performance.db"
LOG_FILE = LOG_PATH / "agent_run_log.jsonl"
ELITE_LOG = LOG_PATH / "elite_history.json"
MEMORY_DIR.mkdir(exist_ok=True)
LOG_PATH.mkdir(exist_ok=True)

# Ensure DB exists
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS decisions (timestamp TEXT, agent TEXT, vote TEXT, pnl REAL)''')
conn.commit()
conn.close()

class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.memory = []
        self.performance = []
        self.suppressed = False
        self.elite = False
        self.weight = 1.0
        self.memory_file = MEMORY_DIR / f"{self.name}.pkl"
        self.load_memory()

    def propose(self, market_state):
        raise NotImplementedError

    def remember(self, outcome):
        self.memory.append(outcome)
        self.performance.append(outcome)
        self.save_memory()

    def save_memory(self):
        with open(self.memory_file, 'wb') as f:
            pickle.dump({'memory': self.memory, 'performance': self.performance}, f)

    def load_memory(self):
        if self.memory_file.exists():
            with open(self.memory_file, 'rb') as f:
                data = pickle.load(f)
                self.memory = data.get('memory', [])
                self.performance = data.get('performance', [])

class StrategyAgent(BaseAgent):
    def propose(self, market_state):
        return {'agent': self.name, 'proposal': 'buy' if market_state.get('momentum', 0) > 0 else 'sell'}

class MacroAgent(BaseAgent):
    def propose(self, market_state):
        return {'agent': self.name, 'proposal': 'bullish' if market_state.get('gdp_growth', 0) > 2 else 'cautious'}

class SentimentAgent(BaseAgent):
    def propose(self, market_state):
        return {'agent': self.name, 'proposal': 'positive' if market_state.get('sentiment', 0) > 0.5 else 'negative'}

class RiskAgent(BaseAgent):
    def propose(self, market_state):
        return {'agent': self.name, 'proposal': 'reduce' if market_state.get('volatility', 0) > 30 else 'normal'}

class MultiAgentOrchestrator:
    def __init__(self, agents):
        self.agents = agents
        self.memory = []
        self.clones = []

    def run(self, state):
        decisions = [a.propose(state) for a in self.agents if not a.suppressed]
        for d in decisions:
            self.log_vote(state, d)
        decision = self.vote(decisions)
        self.execute_trade(decision)
        return decision, decisions

    def vote(self, decisions):
        weights = {}
        for d in decisions:
            a = d['agent']
            v = d['proposal']
            agent = next((x for x in self.agents if x.name == a), None)
            if agent:
                w = getattr(agent, 'weight', 1.0)
                if agent.elite: w *= 1.5
                weights[v] = weights.get(v, 0) + w
        return max(weights, key=weights.get) if weights else 'hold'

    def execute_trade(self, signal):
        print(f"[TRADE]: {signal.upper()}")

    def log_vote(self, state, vote):
        ts = datetime.utcnow().isoformat()
        with open(LOG_FILE, 'a') as f:
            f.write(json.dumps({'timestamp': ts, 'agent_votes': vote, 'market_state': state}) + '\n')
        conn = sqlite3.connect(DB_FILE)
        pnl = 1.0 if vote['proposal'] == 'buy' else -1.0 if vote['proposal'] == 'sell' else 0
        conn.execute("INSERT INTO decisions VALUES (?, ?, ?, ?)", (ts, vote['agent'], vote['proposal'], pnl))
        conn.commit()
        conn.close()

    def replay_and_train(self):
        print("Replaying logs and evolving memory...")
        self.adjust_weights_by_accuracy()
        self.suppress_underperforming_agents()
        self.reinstate_agents_by_recovery()
        self.reward_high_performers()
        self.generate_new_agent_templates()
        self.breed_elite_clones()
        self.test_clones_in_parallel()

    def adjust_weights_by_accuracy(self, decay=0.95):
        conn = sqlite3.connect(DB_FILE)
        scores, total = {}, 0
        for a in self.agents:
            recs = conn.execute("SELECT vote,pnl FROM decisions WHERE agent=? ORDER BY timestamp DESC", (a.name,)).fetchall()
            acc, denom = 0, 0
            for i, (v, p) in enumerate(recs):
                w = decay ** i
                denom += w
                if (v == 'buy' and p > 0) or (v == 'sell' and p < 0):
                    acc += w
            a.weight = round(acc / denom, 3) if denom > 0 else 0.0
            total += a.weight
        for a in self.agents:
            if total > 0: a.weight = round(a.weight / total, 3)
        conn.close()

    def suppress_underperforming_agents(self, threshold=0.05):
        for a in self.agents:
            a.suppressed = a.weight < threshold

    def reinstate_agents_by_recovery(self, threshold=0.07):
        conn = sqlite3.connect(DB_FILE)
        for a in self.agents:
            recs = conn.execute("SELECT vote, pnl FROM decisions WHERE agent=? ORDER BY timestamp DESC", (a.name,)).fetchall()
            recent = recs[:10]
            acc = sum(1 for v, p in recent if (v == 'buy' and p > 0) or (v == 'sell' and p < 0)) / len(recent) if recent else 0
            if acc >= threshold: a.suppressed = False
        conn.close()

    def reward_high_performers(self, threshold=0.85):
        for a in self.agents:
            a.elite = a.weight >= threshold

    def generate_new_agent_templates(self):
        if not ELITE_LOG.exists(): return
        with open(ELITE_LOG, 'r') as f: history = json.load(f)
        elite_counts = {}
        for snap in history.values():
            for k, v in snap.items():
                if v: elite_counts[k] = elite_counts.get(k, 0) + 1
        self.top_elite = sorted(elite_counts.items(), key=lambda x: x[1], reverse=True)[:3]

    def breed_elite_clones(self):
        self.clones.clear()
        for name, _ in getattr(self, 'top_elite', []):
            base = next((a for a in self.agents if a.name == name), None)
            if base:
                class Clone(type(base)):
                    def propose(self_inner, state):
                        base_decision = base.propose(state)['proposal']
                        flipped = 'sell' if base_decision == 'buy' else 'buy'
                        return {'agent': f"Clone_{base.name}", 'proposal': flipped}
                self.clones.append(Clone(f"Clone_{base.name}"))

    def test_clones_in_parallel(self):
        for c in self.clones:
            state = {'momentum': 1, 'volatility': 15, 'gdp_growth': 2.5, 'sentiment': 0.7}
            decision = c.propose(state)
            print(f"Clone {c.name}: {decision['proposal']}")
