function movieList = loadMovieList()
%   movieList = GETMOVIELIST() reads the movie list in movie.txt 
%   and returns a cell array of the movies in movieList.


%% Read the movie list
fid = fopen('movie_ids.txt');

% Store all movies in cell array movie{}
n = 1682;  % Total number of movies 

movieList = cell(n, 1);
for i = 1:n
    line = fgets(fid);
    % Word Index (can ignore since it will be = i)
    [idx, movieName] = strtok(line, ' ');
    movieList{i} = strtrim(movieName); % Actual movie
end
fclose(fid);

end
