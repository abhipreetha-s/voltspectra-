# CircuitSense – AI Assisted Electronic Fault Insight

This project demonstrates a prototype system that analyzes circuit sensor data and predicts possible electronic faults using a local AI model.

Features:
- FastAPI backend
- Circuit anomaly detection
- AI-based fault interpretation
- Local model inference using Lemonade

Sensor Data → FastAPI Backend → Lemonade Local LLM → Fault Analysis Response


Run the Project

Install dependencies:

pip install -r requirements.txt

Run the server:

uvicorn main:app --reload --port 9000

@9000--swagger ui

@8000 --lemonade 

Open Swagger UI:

http://127.0.0.1:9000/docs