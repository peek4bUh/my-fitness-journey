class ProgramExerciseOutput:
    """Output Object for Program Exercise data."""

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

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_sets(self):
        return self.sets

    def set_sets(self, sets):
        self.sets = sets

    def get_reps(self):
        return self.reps

    def set_reps(self, reps):
        self.reps = reps

    def get_rpe(self):
        return self.rpe

    def set_rpe(self, rpe):
        self.rpe = rpe

    def get_rest_seconds(self):
        return self.rest_seconds

    def set_rest_seconds(self, rest_seconds):
        self.rest_seconds = rest_seconds
