def sort_by_year(movies):
    sorted_movies = sorted(movies, key=lambda x: (x['year'], x['title']), reverse=True)
    return [movie['title'] for movie in sorted_movies]


def sort_by_title(movies):
    def trim_movie(title):
        for no_no in ["The ", "A ", "An "]:
            if title.startswith(no_no):
                return title.replace(no_no, "", 1)
        return title
    sorted_movies = sorted(movies, key=lambda x: trim_movie(x['title']))
    return [movie['title'] for movie in sorted_movies]

