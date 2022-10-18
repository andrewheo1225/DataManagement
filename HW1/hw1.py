import math
from collections import defaultdict
from collections import Counter
#Awad Shawl ams934 
#cc1871 cynthia chen
#Andrew Heo ayh35
#Peter Zihe Zhang zz475
# --- TASK 1: READING DATA ---

# 1.1


def read_ratings_data(f):
    file1 = open(f, 'r')
    ans = {}
    for line in file1:
        words = line.split('|')
        nameMovie = words[0].strip()
        rating = float(words[1])
        if nameMovie in ans.keys():
            ans[nameMovie].append(rating)
        else:
            ans[nameMovie] = [rating]
            
    file1.close()
    return ans
    # check the last line too edge case
    
# 1.2
def read_movie_genre(f):
    file1 = open(f, 'r')
    ans = {}
    for line in file1:
        words = line.split('|')
        nameMovie = words[2].strip()
        genre = words[0].strip()
        ans[nameMovie] = genre
    file1.close()
    return ans

# --- TASK 2: PROCESSING DATA ---

# 2.1


def create_genre_dict(d):
    #genre-movie
   ans = {}
   for(movie,genre) in d.items():
       if genre in ans.keys():
           ans[genre].append(movie)
       else:
           ans[genre] = [movie]
            
   return ans

# 2.2
def calculate_average_rating(d):
    ans = {}
    for(name,ratingList) in d.items():
        sum = 0
        count = 0
        for rating in ratingList:
            sum+=float(rating)
            count+=1
        average = float("{:.1f}".format(sum/count))
        ans[name] = average

    return ans
    pass

# --- TASK 3: RECOMMENDATION ---

# 3.1


def get_popular_movies(d, n=10):
    sortDictList = dict(sorted(d.items(), key = lambda kv: kv[1], reverse = True))
  
    ans = {}
    for idx, (k, v) in enumerate(sortDictList.items()):
        if idx == n:
            break
        ans[k] = v
    #print((ans))
    return ans
    pass

# 3.2


def filter_movies(d, thres_rating=3):
    ans = {}
    for (k, v) in (d.items()):
        if v >= thres_rating:
            ans[k] = v
        else:
            continue
    #print((ans))
    return ans
    pass

# 3.3


def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    listOfMovieOfGenre = []
    
    for (k, v) in (genre_to_movies.items()):
        if(k == genre):
            listOfMovieOfGenre = v
    #print("\nGenre Type: " + genre, end = "\n\n")
    #print(listOfMovieOfGenre,end = "\n\n")
    
    listOfMovieOfGenreToAvgRating = {}
    for(k,v) in movie_to_average_rating.items():
        if k in listOfMovieOfGenre:
            listOfMovieOfGenreToAvgRating[k] = v
    
    #print("MovieofGenretoRating Unsorted: ",end = "\n\n")
    #print(listOfMovieOfGenreToAvgRating, end = "\n\n")
    
    movieoFGenreSorted = dict(sorted(listOfMovieOfGenreToAvgRating.items(), key = lambda kv: kv[1], reverse = True))
    
    #print("MovieofGenretoRating Sorted: ",end = "\n\n")
    #print(movieoFGenreSorted, end = "\n\n")
    
    ans = {}
    for idx, (k, v) in enumerate(movieoFGenreSorted.items()):
        if idx == n:
            break
        ans[k] = v
    
    #print(ans)
    return ans
    
        
    
    
    pass

# 3.4


def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    listOfMovieOfGenre = []
    
    for (k, v) in (genre_to_movies.items()):
        if(k == genre):
            listOfMovieOfGenre = v
    # print("\nGenre Type: " + genre, end = "\n\n")
    # print(listOfMovieOfGenre,end = "\n\n")
    
    listOfMovieOfGenreToAvgRating = {}
    for(k,v) in movie_to_average_rating.items():
        if k in listOfMovieOfGenre:
            listOfMovieOfGenreToAvgRating[k] = v
    
    # print("MovieofGenretoRating Unsorted: ",end = "\n\n")
    # print(listOfMovieOfGenreToAvgRating, end = "\n\n")
    
    sum = 0
    count = 0
    for (movieName,rating) in listOfMovieOfGenreToAvgRating.items():
        # print(movieName,rating)
        sum = sum + rating
        count = count + 1

    return float("{:.1f}".format(sum/len(listOfMovieOfGenreToAvgRating)))
    # pass

# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    genreAvgRating = {}
    for (genre,movies) in genre_to_movies.items():
        genreAvgRating[genre] = get_genre_rating(genre,genre_to_movies,movie_to_average_rating)           
    #print(genreAvgRating)
    
    ansSorted = dict(sorted(genreAvgRating.items(), key = lambda kv: kv[1], reverse = True))
    
    #print("sorted:")
    #print(ansSorted)
    
    finalAns = {}
    for idx, (k, v) in enumerate(ansSorted.items()):
        if idx == n:
            break
        finalAns[k] = v
        
    return finalAns
    pass

# --- TASK 4: USER FOCUSED ---

# 4.1


def read_user_ratings(f):
    file1 = open(f, 'r')
    dict = {}
    for line in file1:
        words = line.split('|')
        nameMovie = words[0]
        rating = float(words[1])
        id = int(words[2])
        newTuple = (nameMovie, rating)
        if id in dict.keys():
            dict[id].append(newTuple)
        else:
            dict[id]=[]
            dict[id].append(newTuple)
        # print(id)
    # print(dict)
    file1.close()
    return dict

# 4.2


def get_user_genre(user_id, user_to_movies, movie_to_genre):
    finalGenre = ""
    
    # for user, movieRate in user_to_movies.items():
    #     print(user, movieRate)
    
    # for movie, genre in movie_to_genre.items():
    #     print(movie, genre)
        
    # find all the movie that user rated 
    user_rated_movie = user_to_movies[user_id]
    # print( " user " + str(user_id) + ": ")
    # print(user_rated_movie)
    
    # sort movies in list in same the same genre
    sortedGenre = {}
    for tuples in user_rated_movie:
        movie = tuples[0]
        rating = tuples[1]
        # print(movie, rating)
        # if genre is not in dict, attach it
        # if genre is already in dict, append 
        # print(movie_to_genre[movie])
        if movie_to_genre[movie] in sortedGenre.keys():
            sortedGenre[movie_to_genre[movie]].append(tuples)
        else:
            sortedGenre[movie_to_genre[movie]] = []
            sortedGenre[movie_to_genre[movie]].append(tuples)
    # print(sortedGenre)
    
    # find the average of all the movie in the same genre that user rated
    rating_for_each_genre = {}
    for genre, tuples in sortedGenre.items():
        ave = 0
        sum = 0
        count = 0
        for items in tuples:
            sum = sum + items[1]
            count = count + 1
            # print(items)
            ave = sum / count
        rating_for_each_genre[genre] = ave
        
    # print(rating_for_each_genre)
    
    finalSorted = dict(sorted(rating_for_each_genre.items(), key = lambda kv: kv[1], reverse = True))
    
    # print(finalSorted)
    n = 0
    for genre, rating in finalSorted.items():
        if(n == 1):
            break
        finalGenre = genre
        n = n + 1
    
    # print(finalGenre)
    #return the highest rated genre
    return finalGenre

# 4.3


def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    
    ans = {}
    # find top 3 highest rated movie in 
    favGenre = get_user_genre(user_id, user_to_movies, movie_to_genre)
    # print(favGenre)
    # find all movies in user's fav cataogry 
    possibleMovies = []
    for movie, genre in movie_to_genre.items():
        if genre == favGenre:
            possibleMovies.append(movie)
    
    # print("all movies in user's top genre")
    # print(possibleMovies, end="\n\n")
    
    # now delete those movies that users has rated
    rated = user_to_movies[user_id]
    # print("all movies user has rated: ")
    # print(rated, end="\n\n")
    for tuples in rated:
        if tuples[0] in possibleMovies:
            possibleMovies.remove(tuples[0])
    
    # print("after getting rid of all user rated movies: ")
    # print(possibleMovies)
    
    tempToKeepRate = {}
    # find the rating of those movies and sort them
    for movie in possibleMovies:
        tempToKeepRate[movie] = movie_to_average_rating[movie]
    # print(tempToKeepRate)
    
    # sort it
    sortedMovies = dict(sorted(tempToKeepRate.items(), key = lambda kv: kv[1], reverse = True))
    # print(sortedMovies)
    
    count = 0
    for movie, rate in sortedMovies.items():
        if count == 3:
            break
        ans[movie] = rate
        count = count + 1
        
    # print(ans)
    return ans

# --- main function for your testing ---


def main():
    #1.1
    read_ratings = read_ratings_data("movieRatingSample.txt")
    #print("1.1", end = "\n")
    #print(read_ratings, end = "\n\n")
    
    #1.2
    #print("1.2", end = "\n")
    read_movie = read_movie_genre("genreMovieSample.txt")
    #print(read_movie, end = "\n\n")
    
    # #2.1
    #print("2.1", end = "\n")
    genre_dict = create_genre_dict(read_movie_genre("genreMovieSample.txt") )
    #print(genre_dict, end = "\n\n")
    
    #2.2
    #print("Q2.2", end = "\n")
    calc_average = calculate_average_rating(read_ratings)
    #print(calc_average , end = "\n\n")
    
    # # #3.1
   #print("Q3.1", end = "\n")
    n = 10
    get_popular  = get_popular_movies(calc_average,n)
    #print(get_popular, end = "\n\n")
    
    # # #3.2
    #print("Q3.2", end = "\n")
    d = 3.5
    filterMovies = filter_movies(get_popular,d)
   # print(filterMovies, end = "\n\n")
    
    # # #3.3
   # print("Q3.3", end = "\n")
    f = 5
    genre = "Adventure"
   # print(genre, end = "\n\n")
   # print("genre_dict: ", end = "\n\n")
   # print(genre_dict)
   # print("\ncalc_average: ", end = "\n\n")
   # print(calc_average,end = "\n\n")
    popular_in_genre = get_popular_in_genre(genre, genre_dict,calc_average,f)
   # print("answer for 3.3: ")
   # print(popular_in_genre, end = "\n\n")
    
    #3.4
   # print("Q3.4", end = "\n")
   # print(genre, end = "\n")
   # print("this avg is based on MovieofGenreToRatingSorted. Not based on the answer of 3.3")
    genre_rating = get_genre_rating(genre, genre_dict, calc_average)
   # print("answer: ", end = "\n")
   # print(genre_rating, end = "\n\n")
    
    #3.5
    #print("Q3.5", end = "\n")
    z=5
    genre_pop = genre_popularity(genre_dict, calc_average,z)
   # print("answer: ", end = "\n")
   # print(genre_pop, end = "\n\n")
    
    #4.1
   # print("Q4.1", end = "\n")
    user_rating = read_user_ratings("movieRatingSample.txt")
  #  print(user_rating, end = "\n\n")
    
    #4.2
   # print("Q4.2", end = "\n")
    userId = 8
    # used user_rating from 4.1
    # below equation from 1.2
    movie_to_genre = read_movie_genre("genreMovieSample.txt")
    user_genre = get_user_genre(userId, user_rating, movie_to_genre)
   # print(user_genre, end = "\n\n")
    
    #4.3
   # print("Q4.3")
    userIdFor4point3 = 8
    # the second parameter is from 4.1
    # third parameter from 1.2 movie to genre
    # last parameter from 2.2 
    recommendMovies = recommend_movies(userIdFor4point3, user_rating, movie_to_genre, calc_average)
   # print(recommendMovies)
    pass


main()