# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This version of the project builds a transparent, content-based music recommender that scores each song against a user taste profile and returns the top matches. The model prioritizes exact matches on genre and mood, then refines ranking with numeric feature closeness (especially energy) so recommendations reflect both musical category and listening vibe.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

Answers:

- What features does each `Song` use in your system
  - Each song uses `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`, plus identity fields like `title` and `artist`.
- What information does your `UserProfile` store
  - The user profile stores `favorite_genre`, `favorite_mood`, a numeric `target_energy`, and `likes_acoustic` (a boolean preference).

  This is because Copilot suggested the acoustic feature, which I think can help understand if the user likes more stripped-back songs, and that preference oculd be important for recommending more songs. 

- How does your `Recommender` compute a score for each song
  - The scores are weighted. Genre and mood are the highest, but genre is a little higher because mood could change accross days or even listening sessions. Genres and mood can be matched, but the numeric features like energy will be based on how close they are to the user's preference. The second step scoring would be a weighted sum of the features, and then a ranking from highest to lowest for the recommendation system.  
  
- How do you choose which songs to recommend?You can include a simple diagram or bullet list if helpful.
  - The system scores every song, sorts songs by score from highest to lowest, and returns the top songs as recommendations. I think this could depend on how many songs we want. 



---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

Yes, a few likely biases are expected with this scoring setup:

1. Genre lock-in bias  
Genre gets a strong fixed bonus, so songs outside the user’s usual genre may rarely surface even if they match mood/energy well.

2. Exact-match categorical bias  
Mood and genre use exact matching, which can punish near-equivalent labels (for example relaxed vs chill).

3. Target-proximity bias on numeric features  
Songs close to target energy/tempo/valence win consistently, which can reduce variety and discovery.

4. Scale-range bias  
If numeric features are not normalized consistently, one feature may dominate scoring unintentionally.

5. Dataset representation bias  
If the CSV has more songs from certain genres/moods, those groups are more likely to appear in Top K.

6. Popularity/recency tie-breaker bias  
If used, these can favor already popular or recently played tracks and suppress long-tail songs.

7. Cold-start bias  
New users with sparse preferences or new songs with limited metadata can be scored unfairly low.

Simple mitigations:
1. Add a small exploration boost for diverse genres or underrepresented items.
2. Use soft categorical similarity instead of strict exact match.
3. Cap dominance of any one feature and periodically tune weights.
4. Audit Top K distribution by genre/mood to detect skew.
5. Add a diversity reranking step after scoring.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:

- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:

- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:

- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"
```
