from fastapi import APIRouter, Path
from schemas.plan import Plan

plan = APIRouter(
    tags=["plan"],
    
)

plans = []

@plan.get("/plans", response_model=Plan)
async def getPlans():
    return plans

@plan.post("/plans")
async def create_plan(plan: Plan):
    plans.append(plan)
    return {"Message": "Usuario agregado"}

@plan.get("plans/{id}")
async def get_plan(id: int = Path(..., description="Id del usuario a retornar")):
    return plan[id]