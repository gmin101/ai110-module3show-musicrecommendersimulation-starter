import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file into a list of dictionaries.

    Numeric columns are converted from strings so they can be used in
    scoring math later: `id` and `tempo_bpm` become ints, and the audio
    features (energy, valence, danceability, acousticness) become floats.
    Text columns (title, artist, genre, mood) are left as strings.

    Required by src/main.py
    """
    int_fields = {"id", "tempo_bpm"}
    float_fields = {"energy", "valence", "danceability", "acousticness"}

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song: Dict = {}
            for key, value in row.items():
                if key in int_fields:
                    song[key] = int(value)
                elif key in float_fields:
                    song[key] = float(value)
                else:
                    song[key] = value
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.

    Uses the finalized additive recipe (max 5.0 points):
      - genre match:      +2.0
      - mood match:       +1.0
      - energy similarity: +1.5 * (1 - |song energy - target energy|)
      - acoustic match:   +0.5  (if the user likes acoustic and the song is)

    Returns the numeric score plus a list of human-readable reasons so the
    recommendation can be explained.

    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons: List[str] = []

    # Genre match: +2.0 (strongest taste signal)
    if user_prefs.get("genre") and song.get("genre") == user_prefs["genre"]:
        score += 2.0
        reasons.append(f"genre match: {song['genre']} (+2.0)")

    # Mood match: +1.0
    if user_prefs.get("mood") and song.get("mood") == user_prefs["mood"]:
        score += 1.0
        reasons.append(f"mood match: {song['mood']} (+1.0)")

    # Energy similarity: graded reward for being close to the target energy.
    target_energy = user_prefs.get("energy")
    if target_energy is not None:
        energy_points = 1.5 * (1.0 - abs(song["energy"] - target_energy))
        score += energy_points
        reasons.append(
            f"energy {song['energy']:.2f} vs target {target_energy:.2f} "
            f"(+{energy_points:.2f})"
        )

    # Acoustic preference: +0.5, only rewards (never penalizes).
    if user_prefs.get("likes_acoustic") and song.get("acousticness", 0.0) >= 0.6:
        score += 0.5
        reasons.append(f"acoustic match: acousticness {song['acousticness']:.2f} (+0.5)")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Ranks the whole catalog against the user's preferences and returns the
    top k recommendations.

    Steps:
      1. Judge every song with score_song() to get (score, reasons).
      2. Sort all songs by score, highest first (ties broken by title so the
         ordering is deterministic and reproducible in tests).
      3. Join each song's reasons into a single explanation string.
      4. Return the top k as (song, score, explanation) tuples.

    Required by src/main.py
    """
    scored: List[Tuple[Dict, float, str]] = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "no matching preferences"
        scored.append((song, score, explanation))

    # Highest score first; break ties by title for stable, reproducible output.
    scored.sort(key=lambda item: (-item[1], item[0]["title"]))

    return scored[:k]
