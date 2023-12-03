from dvd import DVD
from linklist import LinkedList
import sqlqueries as qs
import prettytable


class DVListType:

    def __init__(self):
        self.dvd_data = LinkedList()

    def load_dvd_data(self):
        record = qs.get_db_dvd()

        for mov in record:
            # db order: movie name, stars, producer, director, company, copies, dvd id
            record = DVD(mov[0], mov[1], mov[2], mov[3], mov[4], mov[5], mov[6],
                         qs.get_rented_copies(mov[6]), qs.get_all_dvdid(mov[6]))
            self.dvd_data.insert(record.get_movie_id(), record)


    def print_all_dvddata(self):
        dvd_list = self.dvd_data.get_linked_data()
        table = [["Movie ID",  "DVD IDs", "Movie", "TTL. Amt", "In-store", "Starring",
                  "Producer", "Director", "Production company"]]

        table.extend([item.get_movie_list() for item in dvd_list if item is not None])
        prettytable.create_table(table)

    def insert_dvd_ll(self, movie_id, mov, ids):
        # db order: movie_name0, list_stars_names1, producer2, director3, production_compnay4, total_copies5, movie_id6, rented_copies7, dvd_copies_id8
        record = DVD(mov[0], mov[1], mov[2], mov[3], mov[4], mov[5],movie_id, 0, ids)
        self.dvd_data.insert(movie_id, record)

    def search_dvd_id(self, dvd_id):
        current_node = self.dvd_data.head
        while current_node.next is not None:
            if int(dvd_id) in current_node.next.data.get_dvd_ids():
                return current_node.next.data
            current_node = current_node.next
        return False

    def search_dvd_name(self, dvd_name):
        current_node = self.dvd_data.head
        while current_node.next is not None:
            if dvd_name == current_node.next.data.get_movie_name():
                return current_node.next.data
            current_node = current_node.next
        return False

    def search_movie_id(self, movie_id):
        current_node = self.dvd_data.head
        while current_node is not None:
            if current_node.value == int(movie_id):
                return current_node.data
            current_node = current_node.next

# x = DVListType()
# x.load_dvd_data()


# #
# print(x.search_dvd_name("WALL-E"))
# # print(x.search_movie_id(3).get_movie_name())
