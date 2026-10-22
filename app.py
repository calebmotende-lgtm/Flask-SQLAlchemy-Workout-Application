from flask import Flask, request, jsonify
from flask_migrate import Migrate  
from schemas import WorkoutSchema


from models import db, Workout, Exercise, WorkoutExercise
from schemas import WorkoutSchema, ExerciseSchema, WorkoutExerciseSchema
from marshmallow import ValidationError

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)



app = Flask(__name__)

# Configuring SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def home():
    return {"message": "Welcome to the Workout API!"}

# GET: List all workouts
@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify(workouts_schema.dump(workouts)), 200

# GET: Single workout by ID
@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get_or_404(id)
    return jsonify(workout_schema.dump(workout)), 200

# POST: Create a workout
@app.route('/workouts', methods=['POST'])
def create_workout():
    json_data = request.get_json()
    try:
        data = workout_schema.load(json_data)
        new_workout = Workout(**data)
        db.session.add(new_workout)
        db.session.commit()
        return jsonify(workout_schema.dump(new_workout)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# DELETE: Delete a workout
@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    return '', 204

# POST: Add an exercise to a workout (Association endpoint)
@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    Workout.query.get_or_404(workout_id)
    Exercise.query.get_or_404(exercise_id)
    
    json_data = request.get_json()
    json_data['workout_id'] = workout_id
    json_data['exercise_id'] = exercise_id
    
    we_schema = WorkoutExerciseSchema()
    try:
        data = we_schema.load(json_data)
        new_we = WorkoutExercise(**data)
        db.session.add(new_we)
        db.session.commit()
        return jsonify(we_schema.dump(new_we)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)

