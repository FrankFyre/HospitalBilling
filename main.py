from databaseloaders.customerinfoloader import customerBTreeType
from databaseloaders.dvdinfoloader import DVListType
import sqlqueries as qs
import prettytable


def select_options(option_range):
    print("")

    while True:
        try:
            selected_option = int(input("Select an option: "))
            print("_____________________________________")
        except ValueError:
            print("Invalid input. Please enter an number (E.g 1).")
        else:
            if 1 <= selected_option <= option_range:  # this is faster
                break
            else:
                print("Invalid option. Please enter an a number from the available options above.")
    print("")
    return selected_option


def yes_no(question):
    reply = str(input(question + ' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    elif reply[0] == 'n':
        return False
    else:
        return yes_no("Please Enter (y/n) ")


def rent_dvd(customer_link, dvd_link):
    print(f'|-----    Rent DVD    ------|\n')
    dvd_id = int(input(f'\nEnter the dvd id: '))
    account = int(input(f'Enter the customer account number: '))
    # get movie name
    dvd_name = dvd_link.search_dvd_id(dvd_id).get_movie_name()
    print(f'\n---Entered details---\n '
          f'DVD {dvd_name} \n '
          f'DVD ID selected: {dvd_id} \n '
          f'Account number selected: {account} \n')
    selected = yes_no(f'Confirm checkout out DVD ?')

    if selected is False:
        return False

    check = qs.sql_checkout(account, dvd_id)
    print (check)
    if not check:
        print(f'\n**** DVD selected is already checkout! ****')
        return

    # Get customer variable from bst
    customer = customer_link.bsearch_customer(account)

    # saves to rented movie to customer bst
    customer.add_rented(dvd_name)



    rec = customer.get_customer_all()
    customer_table = [["Account No.", "First name", "Last name", "Rented Dvds"],
                      rec]
    prettytable.create_table(customer_table)

    # Print transaction
    rentals = qs.sql_active_rentals_customer(account)
    rental_table = [["Movie name", "DVD ID", "Rental number", "Account number", "Checkout date"]]
    rental_table.extend([[rec[4], rec[2], rec[0], rec[1], rec[3]] for rec in rentals])

    prettytable.create_table(rental_table)


def return_dvd(link):
    print(f'|---------DVD Return ---------|\n')
    confirm = False


    dvd_id = input(f'Enter the dvd id to return: ')
    dvd = link.search_dvd_id(dvd_id)

    if not dvd:
        print(f'No dvd found')
        return
    print(f'\n Name: {dvd.get_movie_name()}\n '
          f'DVD ID: {dvd_id}\n')
    selection = yes_no(f'Confirm return ?')

    if not selection:
        return


    # edits database
    check = qs.sql_checkin(dvd_id)
    if check:
        print(f'\n {dvd.get_movie_name()} has been returned')

    elif not check:
        print("\n ****DVD is not checked out and cannot be return!****")


def all_rented_dvd():
    table = [["Movie name", "DVD ID","First Name", "Last Name","Account Number"]]
    record = qs.each_dvd_rented()
    table.extend([rec for rec in record])
    prettytable.create_table(table)

def search_dvd_menu(link):
    print(
        f"\n ---Find DVD/Movie--- \n "
        f"\n 1. Search by DVD ID\n "
        f"2. Search by Name\n "
        f"3. Search by Movie ID\n "
    )
    select_sub = select_options(3)
    movie_info = None
    get_id = True
    while get_id:
        if select_sub == 1:
            dvd_id = input(f'Enter the DVD ID:')
            movie_info = link.search_dvd_id(dvd_id)

        elif select_sub == 2:
            dvd_id = input(f'Enter the DVD name:')
            movie_info = link.search_dvd_name(dvd_id)

        elif select_sub == 3:
            movie_id = input(f'Enter the movie ID:')
            movie_info = link.search_movie_id(movie_id)

        if movie_info is False:
            print (f"DVD ID is not found !")
            return
        else:
            get_id = False

    table = [["Movie ID", "DVD IDs", "Movie", "TTL. Amt", "In-store", "Starring", "Producer", "Director",
              "Production company"], movie_info.get_movie_list()]

    prettytable.create_table(table)


def create_customer_db(link):
    print(f'|------New Customer Account------|')
    # Get Name
    first_name = input(f'Enter first name:')
    last_name = input(f'Enter last name:')

    print(f'Customer name: {first_name} {last_name}')
    selection = yes_no(f'Create account ?')
    if selection:
        customer = qs.add_new_customer(first_name, last_name)

        table = [["Account No.", "First name", "Last name"],
                 [customer[0], customer[1], customer[2]]]
        prettytable.create_table(table)

        #Adds to current lbinary tree
        link.insert_customer(customer[0], customer[0], customer[1], customer[2])


def create_new_dvd(link):
    print(f'\n|--------- New Movie DVD ---------|\n')
    movie_name = input(f'Enter movie name: ')
    list_stars_names = input(f'Enter celebrity name starring in movie: ')
    producer = input(f'Enter producer name: ')
    director = input(f'Enter director name: ')
    production_company = input(f'Enter production company name: ')
    total_copies = int(input(f'Enter how many copies of dvd for the movie: '))

    # passes to sql
    new_movie = qs.add_new_dvd(movie_name, list_stars_names, producer, director,
                               production_company, total_copies)

    # prints data
    table = [["Movie", "Starring", "Producer", "Director",
              "Production company", "Total copies", "Movie ID", "DVD ID"]]
    movie_info_table = [info for info in new_movie]
    dvd_ids = qs.add_dvd_table(total_copies, movie_info_table[6])
    movie_info_table.append(",".join(str(x) for x in dvd_ids))
    table.append(movie_info_table)
    prettytable.create_table(table)

    #Inserts into Link List
    link.insert_dvd_ll(movie_info_table[6], movie_info_table, dvd_ids)


def main():
    # Global variables for menus loops
    main_menu = True
    main_sub_menu = False
    # initializes Lists
    # Customer Link List
    customer_bst = customerBTreeType()
    customer_bst.load_customer_btree()
    # Dvd binary search tree
    dvd_list = DVListType()
    dvd_list.load_dvd_data()

    while main_menu:
        print(
            f"\n Welcome to Franks Films !\n "
            f"\n 1. Rent a DVD \n "
            f"2. Return DVD \n "
            f"3. Check DVDs information \n "
            f"4. Check Customers information \n "
            f"5. New customer entry \n "
            f"6. New DVD entry \n "
            f"7. Exit Program \n"
        )

        selected = select_options(7)

        # Rent DVD option
        if selected == 1:
            main_sub_menu = True
            while main_sub_menu:
                # call rent dvd function
                rent_dvd(customer_bst, dvd_list)
                # submenu
                print(
                    f"\n Options \n "
                    f"1. Check out another DVD \n "
                    f"2. Return to main menu \n ")

                return_menu = select_options(2)

                if return_menu == 1:
                    pass

                if return_menu == 2:
                    main_sub_menu = False

        # Return DVD option
        elif selected == 2:
            main_sub_menu = True
            while main_sub_menu:

                return_dvd(dvd_list)
                # submenu
                print(
                    f"\n Options \n "
                    f"1. Check in another DVD \n "
                    f"2. Return to main menu \n ")

                return_menu = select_options(2)

                if return_menu == 1:
                    pass

                if return_menu == 2:
                    main_sub_menu = False

        # Check DVD option
        elif selected == 3:
            main_sub_menu = True
            while main_sub_menu:
                print(
                    f"\n |------Check DVDs------| \n "
                    f"\n 1. Retrieve all dvds information.\n" 
                    f" 2. Retrieve individually rented DVD information\n "
                    f"3. Search for single dvd.\n "
                    f"4. Return to main menu \n ")


                select_sub = select_options(4)

                # Print All movies
                if select_sub == 1:
                    dvd_list.print_all_dvddata()

                    print(f'\n**--returned to previous menu--** \n')

                if select_sub == 2:
                    all_rented_dvd()

                    print(f'\n**--returned to previous menu--** \n')

                # Search by movie id
                elif select_sub == 3:
                    sub_menu = True

                    while sub_menu:
                        search_dvd_menu(dvd_list)

                        print(f"\nOptions: \n "
                              f"\n 1. Search for another DVD \n "
                              f"2. Return to previous menu  \n "
                              f"3. Return to main menu \n ")

                        return_menu = select_options(3)

                        if return_menu == 1:
                            pass

                        elif return_menu == 2:
                            sub_menu = False

                        elif return_menu == 3:
                            main_sub_menu= False
                            break

                        else:
                            print("error")

                elif select_sub == 4:
                    main_sub_menu = False

        # Check customer information
        elif selected == 4:
            main_sub_menu = True
            while main_sub_menu:
                print(
                    f"\n ---Check customer information--- \n "
                    f"\n 1. Retrieve all customer information  \n "
                    f"2. Get all rented DVD by each customer.\n "
                    f"3. Search for customer account.\n "
                    f"4. Return to main menu.\n "
                )
                customer_menu = select_options(4)

                if customer_menu == 1:
                    customer_bst.list_all_customer()

                elif customer_menu == 2:
                    customer_bst.list_only_rent()

                elif customer_menu == 3:
                    print(customer_bst.bsearch_customer(int(input(f'Enter customer account number: '))))

                elif customer_menu == 4:
                    main_sub_menu = False

        # Create new Customer Account
        elif selected == 5:
            main_sub_menu = True
            while main_sub_menu:
                create_customer_db(customer_bst)

                print(
                    f"\nOptions \n "
                    f"\n 1.  Create another new customer account \n"
                    f" 2. Return to Main menu\n "

                )
                customer_menu = select_options(2)

                if customer_menu == 1:
                    pass
                elif customer_menu == 2:
                    break

        # Create new movie
        elif selected == 6:
            main_sub_menu = True
            while main_sub_menu:
                create_new_dvd(dvd_list)
                print(
                    f"\nOptions \n "
                    f"\n 1.  Add another new DVD \n"
                    f" 2. Return to Main menu\n "
                )
                new_dvd_menu = select_options(2)

                if new_dvd_menu == 1:
                    pass
                elif new_dvd_menu == 2:
                    break

        # Exit program
        elif selected == 7:
            main_menu = False


if __name__ == '__main__':
    main()
