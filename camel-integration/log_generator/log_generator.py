import logging
import random
import time
import sys

# Create and configure the logger
logging.basicConfig(filename='app_logs.log', level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# List of users and movie categories for simulation
users = ["cinephile22", "cinemaaddict99", "movielover23", "filmjunkie45", "cinemania88",
         "moviebuff55", "filmenthusiast72", "filmgeek123", "cinefile18", "cinemalover101",
         "movieenthusiast77", "filmfanatic54", "cinemafreak92", "movieaddiction67", "filmbuff2000",
         "cinemalover365", "moviemaniac12", "filmaddict81", "cinemaenthusiast33", "moviegeekster",
         "cinephilia365", "filmlover29", "cinemalover87", "moviehound55"]

movies = ["The Godfather Part II", "The Shawshank Redemption", "The Lord of the Rings: The Fellowship of the Ring",
          "The Dark Knight Rises", "Inglourious Basterds", "The Departed", "The Green Mile", "The Prestige",
          "The Avengers: Endgame", "The Revenant", "Gone with the Wind", "The Sound of Music", "The Wizard of Oz",
          "Casablanca", "Citizen Kane", "Seven Samurai", "The Good, the Bad and the Ugly", "The Empire Strikes Back",
          "The Godfather Part III", "The Lord of the Rings: The Two Towers", "The Godfather Part I", "Fight Club",
          "The Matrix Reloaded", "The Matrix Revolutions", "Avatar", "Jurassic World", "Forrest Gump", "Gladiator",
          "Black Panther", "The Lion King (2019)", "Beauty and the Beast (2017)", "Frozen", "Finding Nemo", "The Dark Knight",
          "The Shawshank Redemption", "Inception", "Interstellar", "Forrest Gump", "Pulp Fiction", "Schindler's List"]

categories = ["Action Movies", "Comedy Movies", "Drama Movies", "Horror Movies",
              "Science Fiction", "Thriller Movies", "Crime Movies", "Adventure Movies", "Family Movies"]

# Simulate log generation
def generate_logs(num_logs):
    info_probability = 0.8  # Probability of generating INFO log (adjust this as per your preference)

    for _ in range(num_logs):
        if random.random() <= info_probability:
            # Generate INFO log
            user = random.choice(users)
            movie = random.choice(movies)
            category = random.choice(categories)
            action = random.choice(["logged in successfully.", "searched for", "visited the", "started watching",
                                    "paused watching", "resumed watching", "rated the"])
            if "watching" in action:
                log_message = f'User "{user}" {action} "{movie}"'
            elif "logged" in action:
                log_message = f'User "{user}" {action}'
            elif "searched" in action:
                log_message = f'User "{user}" {action} "{category}"'
            elif "rated" in action:
                log_message = f'User "{user}" {action} "{movie}"'
            logging.info(log_message)
        else:
            # Generate ERROR log
            user = random.choice(users)
            category = random.choice(categories)
            error_codes = [404, 500, 502, 503]
            error_code = random.choice(error_codes)
            log_message = f'An unexpected error occurred while processing the user request. Error code: {error_code}.'
            logging.error(log_message)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_generator.py <num_logs>")
        sys.exit(1)

    num_logs = int(sys.argv[1])
    generate_logs(num_logs)
