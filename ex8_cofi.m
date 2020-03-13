%% Match with Movies using Collaborative Filtering Recommender System

%  Y is a 1682x943 matrix, containing ratings (1-5) of 1682 movies on 
%  943 users

%  R is a 1682x943 matrix, where R(i,j) = 1 if and only if user j gave a
%  rating to movie i
%% ============== Load User's Movies Ratings ===============
%  Loads the User's movies ratings
%
movieList = loadMovieList(); % Returns a cell array of the movies in movieList

% Initialize my(User's) ratings
my_ratings = zeros(1682, 1);

% Reads the .csv file which is the contains Movie IDs and it's rating as done by the User in 'gui.py' 
X=readtable('/Users/adarshkumar/Desktop/ML:DL Projects/Machine Learning Coursera GitHub/machine-learning-ex8/ex8/outputgui.csv');
indices=X.(1);
ratings=X.(2);
for j=1:size(X,1)
    my_ratings(indices(j))=ratings(j);
end
%% ================== Learning Movie Ratings ====================
%  Now, I'll train the collaborative filtering model on a movie rating 
%  dataset of 1682 movies and 943 users
%

fprintf('\nTraining collaborative filtering...\n');

%  Loads data
load('ex8_movies.mat');

%  Y is a 1682x943 matrix, containing ratings (1-5) of 1682 movies by 
%  943 users
%
%  R is a 1682x943 matrix, where R(i,j) = 1 if and only if user j gave a
%  rating to movie i

%  Add User's ratings to the data matrix
Y = [my_ratings Y];
R = [(my_ratings ~= 0) R];

%  Normalize Ratings
[Ynorm, Ymean] = normalizeRatings(Y, R);

%  Useful Values
num_users = size(Y, 2);
num_movies = size(Y, 1);
num_features = 10;

% Randomly Initialising Parameters (Theta, X)
X = randn(num_movies, num_features);
Theta = randn(num_users, num_features);

initial_parameters = [X(:); Theta(:)];

% Set options for fmincg
options = optimset('GradObj', 'on', 'MaxIter', 100);

lambda = 10; % Set Regularization, can play around with this
theta = fmincg (@(t)(cofiCostFunc(t, Y, R, num_users, num_movies, ...
                                num_features, lambda)), ...
                initial_parameters, options);

% Unfold the returned theta back into X and Theta
X = reshape(theta(1:num_movies*num_features), num_movies, num_features);
Theta = reshape(theta(num_movies*num_features+1:end), ...
                num_users, num_features);

fprintf('Recommender system learning completed.\n');


%% ================== Recommendation for the User! ====================
%  After training the model, we can now make recommendations by computing
%  the predictions matrix.
%

p = X * Theta'; % Predictions matrix
my_predictions = p(:,1) + Ymean;

movieList = loadMovieList();
my_movies=string.empty; % Initialise array to store Recommended movies for User
count=0; 
[r, ix] = sort(my_predictions, 'descend');
for i=1:50
    if count==11 % Pick only the top 10 recommendations
        break
    end
    j = ix(i);
    if R(j,1)==0
        count=count+1;
        my_movies(count)=movieList{j};
    end
end
%% ================== Cosine Similarity between Predicted Vectors ====================
%  Computes the Cosine Similarity between User's prediction vector, p(:,1)
%  and others prediction vectors. The prediction matrix captures a User's
%  movies taste!
%

n_col = size(p,2); % Number of other Users
norm_c=vecnorm(p);
%norm_r = sqrt(sum(abs(p).^2,2)); % same as norm(S1,2,'rows')
max_sim = zeros(1,n_col); % Cosine Similarity between User's predictions 
for i = 2:n_col           % and other's prediction vectors
    max_sim(1,i) = dot(p(:,1), p(:,i)) / (norm_c(1) * norm_c(i));
end
[B,I]=maxk(max_sim,3); % Pick only the 3 users which have the most similar movie preferences as our User!
%fprintf('\nUser1:%.1f & %.1f User2:%.1f & %.1f User3:%.1f & %.1f\n', B(1,1),...
%I(1,1),B(1,2),I(1,2),B(1,3),I(1,3));

%% ================== Common Movie Recommendation & Top Recommended Movies for User ====================
%  Writes to a file common predicted movies for top 3 users who have similar movie
%  taste as our User. Also writes to another file top 10 Recommended movies
%  based on his/her provided movie ratings
%

movies_1=string.empty; % To store top movie Recommendations for User 1
movies_2=string.empty;
movies_3=string.empty;
for l=1:3
    user = p(:,I(1,l)) + Ymean;
    count=0;
    [r, ix] = sort(user, 'descend');
    %fprintf('\nTop recommendations for User%.1f:\n',l);
    for i=1:10
        j = ix(i);
        count=count+1;
        if l==1
            movies_1(count)=movieList{j};
        elseif l==2
            movies_2(count)=movieList{j};
        else
            movies_3(count)=movieList{j};
        end
        %fprintf('Predicting rating %.1f for movie %s\n', user(j), ...
                %movieList{j});
    end
end

% To compute the common Recommendations for all 4 Users
final_movies=intersect(my_movies, movies_1);
final_movies=intersect(final_movies, movies_2);
final_movies=intersect(final_movies, movies_3);
%{
fprintf('\nCommon movies-\n');
for i=1:min(size(final_movies,2),3)
    fprintf('%s\n', final_movies(i));
end
%}

% Write the Common Recommendations in file named 'output.txt'
fid = fopen('/Users/adarshkumar/Desktop/ML:DL Projects/Machine Learning Coursera GitHub/machine-learning-ex8/ex8/output.txt','wt');
fprintf(fid, '%d\n%d\n%d\n', I(1,1), I(1,2), I(1,3));
for i=1:min(3,size(final_movies,2))
    fprintf(fid, '%s\n', final_movies(i));
end
fclose(fid);

% Write the Top 10 Recommendations for main User in file named 'my_recom.txt'
fid1 = fopen('/Users/adarshkumar/Desktop/ML:DL Projects/Machine Learning Coursera GitHub/machine-learning-ex8/ex8/my_recom.txt','wt');
for i=1:10
    fprintf(fid1,'%s\n',  ...
            my_movies(i));
end
fclose(fid);