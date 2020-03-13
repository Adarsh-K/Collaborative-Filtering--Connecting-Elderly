# Match with Movies APP

### Used Recommender System based on "Collaborative Filtering" to recommend movies to User. Use those predictions to match people with similar movie taste all with a novel GUI. The code is in Matlab and Python.

**Note:** All the files are well documented and commented wherever I felt necessary

Run the file named gui.py which does the following:
1. Creates a starting window on which the User rates movies. 
2. After selecting the *Done* button the User gets to see his/her recommended movies. 
  
  **Note:** This Recommendation is done using a MATLAB script 'ex8_cofi.m'. This ***Recommender System uses a Machine Learning Algorithm "Collaborative Filtering"*** which predicts if one's gonna like or dislike a particular movie based on the user's rating on other movies and similar users rating on that movie.
  
3. The script 'ex8_cofi.m' also finds other users with **similar** movie taste as our User. This is done by computing most similar prediction vectors using cosine similarity(for detailed explaination see 'ex8_cofi.m').
4. The User gets to send an invitation to other users for a movie that is recommended to all of them by our model.
