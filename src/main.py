"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Define distinct user profiles for testing
    test_profiles = [
        {"name": "High-Energy Pop", "genre": "pop", "mood": "happy", "energy": 0.90},
        {"name": "Chill Lofi", "genre": "lofi", "mood": "chill", "energy": 0.35},
        {"name": "Deep Intense Rock", "genre": "rock", "mood": "intense", "energy": 0.95},
        {"name": "Sad Party", "genre": "pop", "mood": "sad", "energy": 0.95},
        {"name": "Genre Ghost", "genre": "underground-experimental-synthwave", "mood": "focused", "energy": 0.4},
        {"name": "Boundary Pusher", "genre": "rock", "mood": "angry", "energy": -5.0}
    ]
    
    for profile in test_profiles:
        print("\n" + "="*55)
        print(f"{f'🎵 RECOMMENDING FOR: {profile['name']}':^55}")
        print(f"{f'(Target: {profile['genre']}, {profile['mood']}, {profile['energy']} energy)':^55}")
        print("="*55)

        # Extract preferences for the recommender (excluding the custom 'name' key)
        user_prefs = {k: v for k, v in profile.items() if k != 'name'}
        recommendations = recommend_songs(user_prefs, songs, k=5)

        for i, (song, score, explanation) in enumerate(recommendations, 1):
            print(f"{i}. {song['title']} — {song.get('artist', 'Unknown Artist')}")
            print(f"   Match Score: {score:.2f}/4.0")
            print(f"   Why we picked this:")
            for reason in explanation.split("; "):
                print(f"     • {reason}")
            print("-" * 55)


if __name__ == "__main__":
    main()
