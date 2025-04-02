import statistics


class Series:
    def __init__(self, name: str, no_seasons: int, genre: list) -> None:
        self.title = name
        self.no_seasons = no_seasons
        self.genre = genre
        self.ratings = []

    def get_average_rating(self) -> float:
        return statistics.fmean(self.ratings)

    def __str__(self) -> str:
        if len(self.ratings) == 0:
            ratings_str = "no ratings"
        else:
            ratings_str = f"{len(self.ratings)} ratings, average {'{:.1f}'.format(statistics.fmean(self.ratings))} points"
        genres = ", ".join(self.genre)
        return (
            f"{self.title} ({self.no_seasons} seasons)\ngenres: {genres}\n{ratings_str}"
        )

    def rate(self, rating: int) -> None:
        if rating in range(0, 6):
            self.ratings.append(rating)


def minimum_grade(rating: float, series_list: list) -> list:
    return_list = []
    for series in series_list:
        if series.get_average_rating() > rating:
            return_list.append(series)
    return return_list


def includes_genre(genre: str, series_list: list) -> list:
    return_list = []
    for series in series_list:
        if genre in series.genre:
            return_list.append(series)
    return return_list
