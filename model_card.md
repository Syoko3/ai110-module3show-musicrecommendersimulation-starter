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

--- 

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

--- 

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

--- 

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

--- 

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

--- 