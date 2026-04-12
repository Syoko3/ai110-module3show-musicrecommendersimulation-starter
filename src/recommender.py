import csv
import os
import math
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
    """Loads songs from a CSV file into a list of dictionaries."""
    songs = []
    # Resolve the path relative to the project root if not found
    if not os.path.exists(csv_path):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(project_root, csv_path)

    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['tempo_bpm'] = int(row['tempo_bpm'])
            row['energy'] = float(row['energy'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculates a compatibility score and reason list for a song based on user preferences."""
    # Define weights for easy tuning
    WEIGHTS = {
        "genre": 1.0,
        "mood": 1.0,
        "energy": 2.0
    }
    
    score = 0.0
    reasons = []

    # 1. Genre match (Case-insensitive)
    target_genre = user_prefs.get('genre', "").lower()
    song_genre = song.get('genre', "").lower()
    
    if target_genre and song_genre == target_genre:
        score += WEIGHTS["genre"]
        reasons.append(f"Exact genre match (+{WEIGHTS['genre']})")

    # 2. Mood match (Case-insensitive)
    target_mood = user_prefs.get('mood', "").lower()
    song_mood = song.get('mood', "").lower()
    
    if target_mood and song_mood == target_mood:
        score += WEIGHTS["mood"]
        reasons.append(f"Exact mood match (+{WEIGHTS['mood']})")

    # 3. Energy match using Gaussian decay
    raw_target_energy = user_prefs.get('energy', 0.5)
    
    # Fix for 'Boundary Pusher': Clamp energy between 0.0 and 1.0
    target_energy = max(0.0, min(1.0, raw_target_energy))
        
    energy_diff = song.get('energy', 0.0) - target_energy
    
    # Gaussian decay: Increased width to 0.2 to better handle sparse data
    # and prevent 'ignoring' users with mid-range energy preferences.
    energy_score = WEIGHTS["energy"] * math.exp(-(energy_diff ** 2) / 0.2)
    
    score += energy_score
    
    if energy_score > 0.1: # Only mention if it's a significant match
        reasons.append(f"Energy match (+{energy_score:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Returns the top k songs sorted by compatibility score and energy proximity."""
    target_energy = user_prefs.get('energy', 0.5)

    scored_songs = [
        (song, score, "; ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    return sorted(
        scored_songs,
        key=lambda item: (
            item[1],
            -abs(item[0].get('energy', 0.0) - target_energy)
        ),
        reverse=True
    )[:k]
