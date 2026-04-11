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

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "="*55)
    print(f"{'🎵 YOUR TOP RECOMMENDATIONS':^55}")
    print("="*55)

    for i, (song, score, explanation) in enumerate(recommendations, 1):
        print(f"{i}. {song['title']} — {song.get('artist', 'Unknown Artist')}")
        print(f"   Match Score: {score:.2f}/4.0")
        print(f"   Why we picked this:")
        for reason in explanation.split("; "):
            print(f"     • {reason}")
        print("-" * 55)


if __name__ == "__main__":
    main()
