# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

--- ThemeFinder 2.0

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

--- My recommender is designed to suggest the top 5 songs from a small profile based on the user's preferred genre, mood, and energy level. It is only intended for classroom exploration.

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

--- In the WEIGHTS dictionary, I defined the original weights as the weight of genre as 2.0 point, the weight of mood as 1.0 point, and the weight of energy as 1.0 points. The user's preferred genre, mood, and energy level are considered in the scoring logic. If the user's preferred genre matches the song's genre, then that song scores 1.0 point. If the user's preferred mood matches the song's mood, then that song scores additional 1.0 point. For the energy level, I used the Gaussian decay to calculate its score. First, it ensure the user's input is between 0.0 and 1.0. Then, it finds the raw distance. After that, it uses the following formula for the Gaussian Proximity function: energy_score = Weight * e^(-(difference^2) / width). The width is originally set to 0.1 as a tuning parameter. The songs that are very close to the user's preferred energy level will receive nearly full points, while points drop off rapidly as the raw distance increases. For example, if the raw distance is 0.05, that song scores nearly to 2.0 points. If the raw distance is 0.5, then that song will have lower score on energy. From the starter logic, I changed the weight of genre to 1.0 point and the weight of energy to 2.0 points, and added the normalization logic to ensure the user's input is between 0.0 and 1.0, which adjusted the energy score for "Boundary Pusher" profiles. I also changed the width to 0.2 to have better handling sparse data and preventing ignoring users with mid-range energy preferences.

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

--- There are originally 10 songs in the catalog. I added additional 10 songs before implementing the logic. The genres are pop, lofi, rock, ambient, jazz, synthwave, indie pop, classical, hip-hop, r&b, metal, country, electronic, folk, blues, reggae, and gospel. The moods are happy, chill, intense, relaxed, moody, focused, melancholic, confident, romantic, angry, nostalgic, euphoric, peaceful, sad, carefree, and uplifting. There are no parts of musical taste missing in the dataset.

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

--- The system works well for the users who prefer very high-intensity music such as Deep Intense Rock profile or very low-intensity music such as Chill Lofi profile. By weighting energy higher than genre, it correctly identifies that a song with a different genre but matching energy will have a higher score than a song with the same genre but different energy. Additionally, changing the width of the Gaussian decay function to 0.2 correctly identifies that a song with 0.8 energy is a great match for a 0.9 target. Also, I used the "Genre Ghost" profile as a test case to see that the system can work, even though the genre isn't found. It means that this profile doesn't match any of the genres in the catalog, but it still calculates the scores for energy and mood to provide relevant recommendations.

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

--- The system does not consider tempo, valence, danceability, and acousticness. Additionally, many genres like Metal, Blues, and Country are underrepresented with only one song each, meaning the system cannot provide diverse choices for those users. The current 2.0 weight on Energy also creates a bias where "vibe" overrides "emotion"—in the "Sad Party" test case, the system favors high-energy Happy songs over lower-energy Sad songs because the energy score is worth twice as much as the mood score. Finally, the catalog is "bimodal" (mostly high or low energy), which unintentionally favors users with extreme tastes while providing fewer relevant results for users who prefer moderate (0.5-0.7) energy levels.

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

--- I tested six profiles: three standard music archetypes (High-Energy Pop, Chill Lofi, and Deep Intense Rock) and three adversarial edge cases - "Sad Party" (mood/energy conflict), "Genre Ghost" (unknown genre), and "Boundary Pusher" (extreme out-of-bounds input). I looked for how the system calculated the energy score based on the 2.0 energy weight when labels conflicted. I also checked that the "Genre Ghost" profile still received relevant suggestions based on mood and energy score without a genre match. I was surprised thaat the result of the "Sad Party" profile prioritized high-intensity happy songs over low-intensity sad ones. It shows that numerical weights can easily override semantic labels. I also ran comparisons between a 0.1 and 0.2 Gaussian width. The 0.2 width was significantly more successful at providing relevant options for the "Chill Lofi" profile, while the original 0.1 width generates near-matches too harshly.

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

--- I would improve the model next by adding the scoring logic of other features such as tempo and valence, and adding other features in the catalog such as instrumentalness, liveness, and release year. I would also increase the maximum of the total score to 10.0 points, so that other songs could have more points based on the existing and additional features. I would improve explaining recommendations by transitioning from technical point tallies to natural language templates that compare the song's energy and genre directly to the user's profile. To improve diversity, I would implement an "Artist Penalty" in the selection loop, which ensures that the top 5 results represent a variety of artists rather than flooding the user with multiple tracks from the same creator.

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

--- I learned about recommender systems that it helps filtering tools for the users' preferred items. I got interested that the recommender systems use the scoring rule to calculate the score based on the provided features of the specific item. For example, I used the Gaussian decay to calculate the energy score of each song. This changed the way I think about music recommendation apps by ranking the songs easily using the scoring logic to calculate the score of each feature for each song, and sorting the songs from higher scores to lower scores.