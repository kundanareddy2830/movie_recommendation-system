🎬 Movie Recommender System
📌 About the App

The Movie Recommender System is a web application that suggests movies based on a selected movie. The app uses machine learning techniques to recommend movies with similar characteristics, providing both movie titles and posters to enhance the user experience.

💡 How It Works:
Data Preparation:
A dataset of movies and their similarity scores is preprocessed.
The similarity matrix is split into multiple chunks and stored as .pkl files to optimize memory usage.
Recommendation Engine:
When a user selects a movie, the app loads the appropriate similarity chunk.
The app finds the most similar movies using cosine similarity.
It fetches movie posters using the TMDB API.
Frontend with Streamlit:
The app features a clean UI with a dropdown to select a movie.
Displays five recommended movies along with their posters.
Error handling ensures a smooth user experience.

🌐 Live Demo

Click here to view the live app

🚀 Features
🎥 Select a movie from a dropdown list of popular movies.
🤖 Get five similar movie recommendations instantly.
🖼️ Display movie posters along with titles.
💨 Fast and easy-to-use interface with Streamlit.



🚀 Technologies Used:
Python: Backend logic and data processing.
Streamlit: Web app framework.
Pandas: Data manipulation.
Pickle: Serialization of similarity matrices.
Requests: Fetching movie posters via the TMDB API.
 
 
🚧 How to Run Locally
Clone the repository:
git clone https://github.com/yourusername/movie-recommender-system.git
cd movie-recommender-system
Install dependencies:
pip install -r requirements.txt
Run the app:
streamlit run app/app.py


🛠️ Requirements
Python 3.x
streamlit
pandas
requests
pickle

🌐 Deployment:
The app is deployed using Streamlit Cloud, generating a live link that can be shared and accessed by anyone. This link is also included in the project's GitHub repository.

💡 Future Enhancements
Add user login for personalized recommendations.
Expand the movie database.
Enhance the UI/UX.



