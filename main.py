from fastapi import FastAPI
from collections import Counter
import json

app = FastAPI()

# Load the student data
with open('./data.json') as f:
    data = json.load(f)

@app.get('/')
async def hello_world():
    return 'Hello, World!'

# --- STUDENT DATA ROUTES ---

@app.get('/students')
async def get_students(pref=None):
    if pref:
        return [s for s in data if s['pref'] == pref]
    return data

@app.get('/students/{id}')
async def get_student(id: str): # Matches "STD0001"
    for student in data: 
        if student['id'] == id:
            return student
    return {"error": "Student not found"}

# --- EXERCISE 1: STATS ROUTE ---

@app.get('/stats')
async def get_stats():
    # Use list comprehensions to grab all preferences and programmes
    all_prefs = [student.get('pref') for student in data]
    all_progs = [student.get('programme') for student in data]
    
    # Counter returns a dictionary-like object with counts
    return {
        "meal_preferences": Counter(all_prefs),
        "programmes": Counter(all_progs)
    }

# --- EXERCISE 2: CALCULATOR ROUTES ---

@app.get('/add/{a}/{b}')
async def add(a: float, b: float):
    return {"result": a + b}

@app.get('/subtract/{a}/{b}')
async def subtract(a: float, b: float):
    return {"result": a - b}

@app.get('/multiply/{a}/{b}')
async def multiply(a: float, b: float):
    return {"result": a * b}

@app.get('/divide/{a}/{b}')
async def divide(a: float, b: float):
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"result": a / b}
