# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Model Name: Tune2Tune

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

My recommender is designed to recommend songs (given a dictionary of songs) based on the profile of the user. A profile includes the user's favorite genre, mood, and energy level. These factors are used to generate song recommendations for the particular user. This recommender is meant for classroom exploration rather than for real users.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

As mentioned earlier, factors such as genre, energy, and mood are taken into account in regards to recommending a user to a song. User preferences such as whether they enjoy acoustic is also taken into account when generating scores for the song recommendations. The overall scoring approach that I took is the following: 2 points if the genre of the song matches the profile's genre, 1 point if the mood of the song matches the profile's mood, 1.5 points x difference between song energy and user's energy, and .5 points if the user also likes acoustics.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

There are currently 18 songs in the catalog and the most popular genres and moods represented are pop, lofi, and chill. The catalog began with 10 songs and I added 8 more. No data was removed in the process. There are some musical taste missing in the dataset, such as punk and folk.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

My system seems to work well for profiles of users who are into pop and lofi music. Some patterns I think my scoring captures correctly are balancing the scoring between genre and mood vs scoring majority on the energy and less on genre.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

One major limitation within the system is that the energy gap is what essentially decides the overall ranking and is the main filter bubble. For example, if a profile of someone who enjoys metal music and a fan who enjoys pop tries to get song recommendations, their lists would be nearly identical because their genre preference is lower in priority in comparison to the energy level. The energy gap ignores users whose genre taste doesn't correlate with their energy target.
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

In my experiment, I have tested three profiles: High energy pop, chill lofi, and deep intense rock. All three profiles had the same exact song recommendations as well as the same order of the songs. The only difference between the original output with the experimental output is the scoring difference. Surprisingly, the scores of the experimental output came out to be much higher than the original output scores, typically ranging 1-2 points higher than the original score. For the high energy pop user, they prefer energetic happy songs. For the chill lofi user, they preferred chill acoustic songs. For the deep intense rock user, they preferred high energy songs.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

For future models, I would try to include more songs in the dataset in order to actually see a difference in the songs recommended when changing the point weighing system. This would help improve the diversity of songs in the top results as well. 

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Through this experience, I was able to learn about the complexities of the math driven decision making that these song recommenders must process in order to compute mathematical reasoning behind song recommendations. After having a taste of what music recommendation is like on the backend, I can understand why it can be so difficult recommending a song that a user will like purely based off of numbers alone.