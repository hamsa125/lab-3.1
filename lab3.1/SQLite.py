from sqlDatabase import  CJRecord
from Menu import Manager

def blue():
    print("Chainsaw Juggling Records.")
    #create data base
    # create tables
    db = CJRecord()
    db.create()
    data = None

    # loop
    while True:

        # display menu
        Manager.display_menu(Manager.Main_menu)

        # get user input
        selection = Manager.menu_input(Manager.Main_menu)

        #input a data in to table
        if selection == 1:
            # get  name, country, number of catches
            data = Manager.add_data()
            #put it in the database
            db.insert(data)


        # delete a record
        if selection == 2:
            data = db.get_table()

            Manager.display_table(data)

            id = Manager.pick_delete()
            db.delete_query(id)

            data = db.get_table()

            Manager.display_table(data)

        #Update
        if selection == 3:

            data = db.get_table()
            print(data)
            Manager.display_table(data)

            new_data = Manager.show_update()

            db.update_prepare(new_data)



        #Search
        if selection == 4:
            Manager.display_menu(Manager.Search_menu)
            # get user input on what there search for
            selection = Manager.menu_input(Manager.Search_menu)
            # Search by name
            if selection == 1:

                name =  Manager.get_string_input('Enter name\n')
                data = db.find(name,'RecordHolder' )

            # Search by  country
            elif selection == 2:

                country =  Manager.get_string_input('Enter country\n')
                data = db.find(country,'Country ')

            # Search by catches
            elif selection == 3:

                catches = Manager.get_int_input('Enter number of catches\n')
                data = db.find(catches,'NumofCatches')

            else:
                data = db.get_table()
            #print results
            print('\n')
            Manager.search_display_table(data)
            print('\n')




        # exit program
        if selection == 5:
            db.close_connection()
            print("Goodbye!")
            exit()





def red (): print("lalalala bamba")

if __name__ == '__main__':
    blue()


