# Movies-AI-Recommender-System

An AI Content Based Recommender System recommends movies similar to the movie the user picks making some sentiment analysis on that movie and fetches the top similar group of movies **of at least 10**.

The details of the movies(`title`, `genre`, `cast`, `crew`, `runtime`, `release_data`, `rating`, `poster`, **etc..**) are fetched using an **API** by **`TMDB`**, https://www.themoviedb.org/documentation/api, and by using the IMDB id of the movie in the **API**, the movie posters are fetched and displayed along with each movie title.

## Featured by Streamlit Library
![11](https://user-images.githubusercontent.com/48348589/169676108-bf7df789-bb7f-421e-9d95-4bb7209a80c3.png)
:---------:

## Similarity Score
How does it decide which item is most similar to the item user likes? Here come the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

## Cosine Similarity
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

![3](https://user-images.githubusercontent.com/48348589/169433628-f7c025af-0319-44e9-8e91-4742dee9143e.png)

## How to get the API key!
Create an account in https://www.themoviedb.org/, click on the `API` link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give **"NA"** if you don't have one. You will see the API key in your `API` sidebar once your request is approved.

## Getting Started
1. Clone or download this repository to your local machine.
2. Install `numpy>=1.9.2`, `nltk==3.5`, `scikit-learn>=0.18`, `pandas>=0.19`, `requests==2.23.0`, `streamlit==1.2.0`.
3. Run the [Movies-AI-Content-Based-Recommender.ipynb](Movies-AI-Content-Based-Recommender.ipynb) first **to generate the 2 pkl files.**
4. Get your API key from https://www.themoviedb.org/. _(Refer the above section on how to get the API key)_
5. Replace YOUR_API_KEY in `interface.py`.
6. Open your terminal/command prompt from your project directory and type `streamlit run interface.py`.
7. The App will open in the default browser. If not Go to your browser and type `http://127.0.0.1:5000/` in the address bar.

***

### References
- [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- [Understanding the Math behind Cosine Similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/)
- [NLP Text Feature Extraction](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)
- [Streamlit Docs](https://docs.streamlit.io/)
- [List of 2020-2021 movies](https://en.wikipedia.org/wiki/List_of_American_films_of_2020)

### Copyrights
- KAN Org.
- University of Ain Shams, Egypt
