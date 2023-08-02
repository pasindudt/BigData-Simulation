
class UserIdGenerator:
    def __init__(self):
        self.counter = 0

    def get_next_user_id(self):
        self.counter += 1
        return f"user_{self.counter:04d}"


class MovieIdGenerator:
    def __init__(self):
        self.counter = 0

    def get_next_movie_id(self):
        self.counter += 1
        return f"movie_{self.counter:04d}"