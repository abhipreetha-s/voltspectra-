from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class CircuitData(BaseModel):
    voltage: float
    expected_voltage: float
    current: float
    temperature: float
    ripple: float


def check_anomaly(data: CircuitData):
    issues = []

    if abs(data.voltage - data.expected_voltage) > 0.5:
        issues.append("Voltage deviation")

    if data.temperature > 80:
        issues.append("Overheating")

    if data.ripple > 10:
        issues.append("High ripple")

    return issues


@app.get("/")
def root():
    return {"message": "CHRTD Mini running with AI"}


@app.post("/analyze-circuit")
def analyze_circuit(data: CircuitData):

    issues = check_anomaly(data)

    if not issues:
        return {
            "status": "Healthy",
            "message": "No major anomaly detected."
        }

    prompt = f"""
    Circuit readings:
    Voltage: {data.voltage}
    Expected Voltage: {data.expected_voltage}
    Current: {data.current}
    Temperature: {data.temperature}
    Ripple: {data.ripple}

    Detected issues: {issues}

    Return output strictly in this format:

    Fault: <short fault name>
    Severity: <Low/Medium/High>
    Recommendation: <short corrective action>
    """

    try:
        response = requests.post(
            "http://127.0.0.1:8000/v1/chat/completions",
            json={
                "model":"Gemma-3-4b-it-GGUF",

                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3
            },
            timeout=20
        )

        result = response.json()
        return {
             "debug_full_response": result
        }
        return {
            "status": "Anomaly Detected",
            "analysis": message_content
        }

    except Exception as e:
        return {
            "status": "Error",
            "message": str(e)
        }