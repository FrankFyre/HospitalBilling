from avltree import AvlBst
from customer import Customer
import sqlqueries as qs
import prettytable


class customerBTreeType:
    def __init__(self):
        self.customer = AvlBst()
        self.root = None

    def load_customer_btree(self):
        records = qs.get_db_customer()

        for col in records:
            # passes the customer account number to query movies rented if any
            movie = qs.db_custo_movie(col[0])
            # Store rented dvd names into list as per assignment
            movie_list = []
            for name in movie:
                movie_list.append(name[0])

            # db order: 0 account number, 1 first name,2 last name, 3 list movies
            # Python Class: First, last, acc. no. , list
            record = Customer(col[1], col[2], col[0], movie_list)

            self.root = self.customer.insert(self.root, record)


    def list_all_customer(self):
        customer = self.customer.inorder(self.root)
        table = [["Account No.", "First name", "Last name", "Rented movie"]]
        table.extend([cust.get_customer_all() for cust in customer])
        prettytable.create_table(table)

    def list_only_rent(self):
        customers = self.customer.inorder(self.root)
        table = [["Account No.", "First name", "Last name", "Rented movie"]]
        table.extend([x.get_customer_all() for x in customers if x.get_rented()])

        prettytable.create_table(table)

    def insert_customer(self, value, c1, c2, c3):
        new_cus = Customer(c1, c2, c3)
        self.root = self.customer.insert(self.root, value)

    def bsearch_customer(self,  customer_id, root=None,):
        if root is None:
            root = self.root

        if not root.value.get_account() or root.value.get_account() == customer_id:
            return root.value

        if root.value.get_account() < customer_id:
            return self.bsearch_customer(customer_id, root.right)

        return self.bsearch_customer(customer_id, root.left)

