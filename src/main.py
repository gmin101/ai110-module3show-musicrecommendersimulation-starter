"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from recommender import load_songs, recommend_songs
except ImportError:  # allows both `python src/main.py` and `python -m src.main`
    from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Starter example profile
    # user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.90}

    recommendations = recommend_songs(user_prefs, songs, k=5)
    profile = f"genre={user_prefs['genre']}, mood={user_prefs['mood']}, energy={user_prefs['energy']}"

    print()
    print(f"Top {len(recommendations)} Recommendations")
    print(f"For profile: {profile}")
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n{rank}. {song['title']} - {song['artist']}")
        print(f"Score: {score:.2f}")
        print(f"Why:")
        for reason in explanation.split("; "):
            print(f"- {reason}")

    print()


    """
    "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.90},
    "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.40, "likes_acoustic": True},
    "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.90},
    """


if __name__ == "__main__":
    main()
