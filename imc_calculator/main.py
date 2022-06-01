from imc_calculator.calculator import IMCCalculator
from pydantic import BaseModel
from fastapi import FastAPI, Header
from fastapi import HTTPException
from typing import Union

app = FastAPI(
    title="IMC Calculator",
    description="An IMC calculator",
    openapi_url= "/imc-calculator",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
    )

class IMCIn(BaseModel):
    weight: float
    height: float

class IMCOut(BaseModel):
    imc: float
    classification: str

@app.get("/",)
def teste(user_agent: Union[str, None] = Header(default= None)):
    return {
        "User-agent": user_agent
    }

@app.post("/calc/", response_model=IMCOut)
def calculator(
    imc: IMCIn, user_agent: Union[str, None] = Header(default= None)
    ):
    if not "Linux" in user_agent:
        raise HTTPException(
            404, detail={"message": "useragent mismatch", "status":"fail"})
    return IMCCalculator(imc.weight, imc.height)._classification