movies = {}
run = True
MENU_PROMPT = """
    Press (a) to add a movie
    Press (f) to find a movie
    Press (l) to list your movie(s)
    Press (q) to quit
    """


def add_movie():
    title = input('Enter the title of the movie: ')
    director = input('Enter the director of the movie: ')
    year = input('Enter the release year of the movie: ')
    movies['title'] = title
    movies['director'] = director
    movies['year'] = year


def find_movie():
    movie = input('Enter a movie title: ')
    for m in movies:
        if movies['title'] == m:
            return m


def list_movie():
    for m in movies:
        return m


print("Welcome to the Movie Tracker!")


while run:

    option = input(MENU_PROMPT)

    if option.lower() == 'a':
        add_movie()
        print('Done!!!')
        run = False

    elif option.lower() == 'l':
        list_movie()
        print('Done!!!')
        run = False

    elif option.lower() == 'f':
        find_movie()
        print('Done!!!')
        run = False

    elif option.lower() == 'q':
        print('Okay!!!')
        run = False

    else:
        print('INVALID OPTION!!!')
        run = False
