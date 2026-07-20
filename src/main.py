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
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # --- Formatted output -------------------------------------------------
    profile = f"genre={user_prefs['genre']}, mood={user_prefs['mood']}, energy={user_prefs['energy']}"

    print()
    print("=" * 60)
    print(f"  TOP {len(recommendations)} RECOMMENDATIONS")
    print(f"  For profile: {profile}")
    print("=" * 60)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n  {rank}. {song['title']} — {song['artist']}")
        print(f"     Score: {score:.2f}")
        print(f"     Why:")
        # explanation is a "; "-joined string of individual reasons
        for reason in explanation.split("; "):
            print(f"       • {reason}")

    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
