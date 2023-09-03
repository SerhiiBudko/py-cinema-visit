from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            costumers: list[Customer],
            cleaning_staff: Cleaner
    ) -> None:

        print(f"{movie_name} start in hall number{self.number}")

        for costumer in costumers:
            costumer.watch_movie(movie_name)

        print(f"{movie_name} end")

        cleaning_staff.clean_hall(self.number)
