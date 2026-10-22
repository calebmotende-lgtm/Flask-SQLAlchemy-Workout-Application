# Flask SQLAlchemy Workout Application Backend

## Project Description
A backend API built with Flask and SQLAlchemy for tracking workouts, exercises, and performance metrics.

## Installation Instructions
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Initializing anf migrating the database
    python -m flask db init
    python -m flask db migrate -m "Initial migration"
    python -m flask db upgrade
4. Seed the database
    python seed.py

## API Endpoints
GET /workouts - List all workouts

GET /workouts/ - Show a single workout with its exercises

POST /workouts - Create a new workout

DELETE /workouts/ - Delete a workout

GET /exercises - List all exercises

GET /exercises/ - Show an exercise and associated workouts

POST /exercises - Create a new exercise

DELETE /exercises/ - Delete an exercise

POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises - Add an exercise to a workout with sets, reps, and duration

### Final Git Commit and Push
Stage all your changes, make your final commit, and push everything up to GitHub on your `main` branch[cite: 1, 3]:
```bash
git add .
git commit -m "Complete workout tracking API lab with models, validations, and endpoints"
git push origin main