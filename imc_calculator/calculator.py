from numpy import arange

class IMCCalculator():
    def __init__(self, weight: float, height: float) -> None:
        self.weight = weight
        self.height = height
    
    @property
    def _classification(self) -> dict:
        imc = round(self.weight / (self.height ** 2), 1)
        if imc < 18.5:
            return {"imc": imc, "classification": "Under weight"}
        if imc in [round(x, 2) for x in arange(18.5, 25.0, 0.1)]:
            return {"imc": imc, "classification": "Normal weight"}
        if imc in [round(x, 2) for x in arange(25.0, 30.0, 0.1)]:
            return {"imc": imc, "classification": "Overweight"}
        if imc in [round(x, 2) for x in arange(30.0, 35.0, 0.1)]:
            return {"imc": imc, "classification": "Obesity I"}
        if imc in [round(x, 2) for x in arange(35.0, 40.0, 0.1)]:
            return {"imc": imc, "classification": "Obesity II"}
        if imc > 40.0:
            return {"imc": imc, "classification": "Obesity III"}

