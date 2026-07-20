# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

In my system, each song is described by a genre and mood (category labels) as well as numeric audio measurements like energy, tempo, valence, danceability, and acousticness. The UserProfile doesn't store a favorite song but the qualities a user wants: their favorite genre, favorite mood, a target energy level (0-1), and whether they like acoustic music. To score a song, the Recommender measures how closely it matches those preferences: for energy it rewards songs near the target using 1 - |song energy - target energy|, and for genre, mood, and acoustic-ness it awards points for a match. Each part is multiplied by a weight that reflects its importance - energy 0.40, genre 0.30, acoustic 0.20, and mood 0.10 (genre outranks mood because it's a stronger taste signal and mood is already partly reflected in energy) - and the weighted parts add up to a single score from 0 to 1. Finally, to choose recommendations, I score every song, sort them from highest to lowest, and return the top k (default is 5).

In regards to some potential biases, genres that appear only once in the catalog (classical, metal, funk) give niche tastes fewer good matches than mainstream ones. Additionally, the acoustic preference only adds points, never subtracts, so disliking acoustic music has no effect.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

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

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

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

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



