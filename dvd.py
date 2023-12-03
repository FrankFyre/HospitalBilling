
class DVD:
    def __init__(self, movie_name, list_stars_names, producer, director, production_company,
                 total_copies, movie_id, rented_copies, dvd_copies_id):
        self.movie_name = movie_name
        self.stars = list_stars_names
        self.producer = producer
        self.director = director
        self.production_company = production_company
        self.total_copies = total_copies
        self.rented_copies = rented_copies
        self.in_store = self.total_copies - self.rented_copies
        self.movie_id = int(movie_id)
        self.dvd_copies_id = dvd_copies_id # takes a list of dvd ids

    def get_movie_list(self):
        return [self.movie_id, f'{",".join(str(x) for x in self.dvd_copies_id)}',
                self.movie_name, self.total_copies, self.in_store, self.stars,
                self.producer, self.director, self.production_company
                ]

    def get_movie_name(self):
        return self.movie_name

    def get_stars(self):
        return self.stars

    def get_producer(self):
        return self.producer

    def get_director(self):
        return self.director

    def get_production(self):
        return self.production_company

    def get_copies(self):
        return self.total_copies

    def get_movie_id(self):
        return self.movie_id

    def get_dvd_ids(self):
        return self.dvd_copies_id

    # setters
    def set_movie_name(self, name):
        self.movie_name = name

    def set_stars(self, stars):
        self.stars = stars

    def set_producer(self, producer):
        self.producer = producer

    def set_director(self, director):
        self.director = director

    def set_production(self, production_company):
        self.production_company = production_company

    def set_copies(self, copy):
        self.total_copies = copy

    def set_movie_id(self, new):
        self.movie_id = new

    def set_dvd_ids(self, new):
        self.dvd_copies_id = new

    def __str__(self):
        return (f' Title: {self.movie_name}\n'
                f' Starring: {self.stars}\n'
                f' Producer: {self.producer}\n'
                f' Director: {self.director}\n'
                f' Production company: {self.production_company}\n'
                f' Total copies: {self.total_copies}\n'
                f' Available in-store: {self.in_store}\n'
                f' DVD IDs: {",".join(str(x) for x in self.dvd_copies_id)}\n'
                )

# if __name__ == '__main__':
#     dvd =DVD("Cloud Atlas", "Halle Berry"," Grant Hill", "Lana Wachowski", "FoxSearchlight Pictures", 3, 1, 0, [1, 2])
#     print(dvd)
#     dvd.set_movie_name("Cloud Atlas 2")
#     print (f'{dvd.get_movie_name()}, {dvd.get_production()}')