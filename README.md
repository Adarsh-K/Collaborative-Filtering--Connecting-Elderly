# Match with Movies AI APP

### Used Recommender System based on an AI algorithm "Collaborative Filtering" to recommend movies to User. Use those predictions to match people with similar movie taste all with a novel GUI. The code is in Matlab and Python. See demo video [here](https://drive.google.com/file/d/1pLGgUXz391QgXHuL9LnJlWgVuM-YUInb/view?usp=sharing)

#### This is an AI app specially for elderly people. It's meant to overcome their loneliness by getting in touch with other elderlies living nearby with similar movie taste. And allows them to invite other elderlies around to watch a movie which all of them would like.

**Note:** All the files are well documented and commented wherever I felt necessary

Run the file named gui.py which does the following:
1. Creates a starting window on which the User rates movies.

<img src="img/Screen Shot 2020-03-13 at 5.42.13 PM.png">

2. After selecting the *Done* button the User gets to see his/her recommended movies. 

<img src="img/Screen Shot 2020-03-13 at 5.42.34 PM.png">

  **Note:** This Recommendation is done using a MATLAB script 'ex8_cofi.m'. This ***Recommender System uses a Machine Learning Algorithm "Collaborative Filtering"*** which predicts if one's gonna like or dislike a particular movie based on the user's rating on other movies and similar users rating on that movie.
  
3. The script 'ex8_cofi.m' also finds other users with **similar** movie taste as our User. This is done by computing most similar prediction vectors using cosine similarity(for detailed explaination see 'ex8_cofi.m').

<img src="img/Screen Shot 2020-03-13 at 5.42.53 PM.png">

4. The User gets to send an invitation to other users for a movie that is recommended to all of them by our model.

<img src="img/Screen Shot 2020-03-13 at 5.43.12 PM.png">
