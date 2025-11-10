from flask_restx import fields

from api.core.namespaces import programs_ns


program_exercise_input_schema = programs_ns.model('ProgramExercise', {
    'name': fields.String(required=True, description='Exercise name', example='Bench Press'),
    'sets': fields.Integer(required=True, description='Number of sets', example=4),
    'reps': fields.Integer(required=True, description='Number of reps', example=8),
    'rpe': fields.Integer(description='Rate of perceived exertion (1–10)', example=7),
    'rest_seconds': fields.Integer(description='Rest time in seconds', example=90)
})

program_section_input_schema = programs_ns.model('ProgramSection', {
    'name': fields.String(required=True, description='Section name (e.g., Day 1 - Upper Body)', example='Day 1 - Upper Body'),
    'exercises': fields.List(fields.Nested(program_exercise_input_schema), required=True, description='List of exercises')
})

program_input_schema = programs_ns.model('Program', {
    'title': fields.String(required=True, description='Program title', example='6-Week Beginner Strength Program'),
    'description': fields.String(required=True, description='Program description', example='A 6-week plan focusing on full-body strength.'),
    'duration_weeks': fields.Integer(required=True, description='Duration in weeks', example=6),
    'sections': fields.List(fields.Nested(program_section_input_schema), required=True, description='Workout sections')
})
