class Game:
    def __init__(self, title, producer):
        self.__title = title
        self.__producer = producer
        self._year = None

    # setter
    def set_year(self, year):
        self._year = year

    # getter
    def get_title_producer(self):
        print("Title:", self.__title, "/ Producer:", self.__producer)

    def get_year(self):
        print("Year:", self._year)


if __name__ == "__main__":
    mygame1 = Game("GTA San Andreas", "Rockstar Games")

    mygame1.get_title_producer()
    mygame1.set_year(2004)
    mygame1.get_year()

    mygame2 = Game("Need For Speed Underground 2", "EA Games")

    mygame2.get_title_producer()
    mygame2.set_year(2004)
    mygame2.get_year()
