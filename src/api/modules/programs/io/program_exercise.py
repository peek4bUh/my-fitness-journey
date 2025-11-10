class ProgramExerciseDto:
    """Data Transfer Object for Program Exercise data."""

    def __init__(
            self,
            name: str,
            sets: int,
            reps: int,
            rpe: int,
            rest_seconds: int):
        self.name = name
        self.sets = sets
        self.reps = reps
        self.rpe = rpe
        self.rest_seconds = rest_seconds
