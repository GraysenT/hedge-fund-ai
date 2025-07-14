from fastapi import FastAPI
from pydantic import BaseModel
from economy.business_seed import BusinessSeed
from worldbuilder.economy_sim import EconomySim

app = FastAPI()
sim = EconomySim()

class Submission(BaseModel):
    vision: str

@app.post("/submit")
def submit_seed(submission: Submission):
    seed = BusinessSeed(submission.vision)
    sim.seeds.append(seed)
    return {"status": "added", "id": seed.id}

def submit_seed(submission: Submission):
    seed = sim.add_venture(submission.vision)
    return {"status": "added", "id": seed.id}

@app.get("/top")
def get_top_seeds():
    top = sim.top(5)
    return [{"vision": s.vision, "capital": s.capital} for s in top]