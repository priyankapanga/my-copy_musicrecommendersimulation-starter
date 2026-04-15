"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded {len(songs)} songs from data/songs.csv")

    # Starter example profile
    #user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    # Phase 4: stress test. Three distinct user preferences
    user_prefs_1 = {"genre": "pop", "mood": "exciting", "energy": 0.9}
    user_prefs_2 = {"genre": "lofi", "mood": "chill", "energy": 0.51}
    user_prefs_3 = {"genre": "rock", "mood": "intense", "energy": 0.95}
    # Adversarial: conflicting vibe (high energy + sad mood)
    user_prefs_4 = {"genre": "pop", "mood": "sad", "energy": 0.98}
    # Adversarial: out-of-range numeric values
    user_prefs_5 = {"genre": "pop", "mood": "happy", "energy": 2.5, "targetValence": -0.4}

    # Test all user preferences
    for i, prefs in enumerate([user_prefs_1, user_prefs_2, user_prefs_3, user_prefs_4, user_prefs_5], start=1):
        print(f"\nUser Profile {i}:")
        recommendations = recommend_songs(prefs, songs, k=5)
        print("\nTop recommendations:")
        print("-" * 60)
        for index, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            print(f"{index}. {song['title']}")
            print(f"   Score : {score:.2f}")
            print(f"   Reasons: {explanation}")
        print("-" * 60)


if __name__ == "__main__":
    main()
