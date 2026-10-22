from datetime import date
from app import app
from models import db, Exercise, Workout, WorkoutExercise

with app.app_context():
    print("Clearing database...")
    WorkoutExercise.query.delete()
    Exercise.query.delete()
    Workout.query.delete()

    print("Creating exercises...")
    ex1 = Exercise(name="Push-up", category="Strength", equipment_needed=False)
    ex2 = Exercise(name="Running", category="Cardio", equipment_needed=True)
    
    db.session.add_all([ex1, ex2])
    db.session.commit()

    print("Creating workouts...")
    w1 = Workout(date=date(2026, 6, 1), duration_minutes=30, notes="Morning routine")
    db.session.add(w1)
    db.session.commit()

    print("Linking workout and exercise...")
    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=ex1.id, reps=15, sets=3, duration_seconds=60)
    db.session.add(we1)
    db.session.commit()

    print("Seeding complete!")