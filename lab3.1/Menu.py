class Manager:
#Globel Menu options
#Edit display
#todo make note at main on what are the menu if edit

    Main_menu = ['Add', 'Delete', 'Update','Find',  'Quit']
    Search_menu = ['find by name', 'find by country', 'find by catches']

    def __init__(self):
        pass
#display Menu
    def display_menu(menus):
        options_no = 1
        for value in menus:
            print(options_no , value)
            options_no += 1





    def search_display_table (data):
        try:
            if len(data) == 0 :
                print("There's nothing here")
            else:
                print(data)
        except: print("somthimg happened ")


    @staticmethod
    def display_table(data):

        if len(data) == 0:
            print('The database is empty.')
        else:
            spacing = [4,14,8,15]
            for x in data:
                if len(str(x[0]))> spacing[0]:  spacing[0] = len(str(x[0]))
                if len(str(x[1]))> spacing[1]:  spacing[1] = len(str(x[1]))
                if len(str(x[2]))> spacing[2]:  spacing[2] = len(str(x[2]))
                if len(str(x[3])) > spacing[3]:  spacing[3] = len(str(x[3]))


            print('ID |RecordHolder |Country |No of Catches ')
            for d in data:
                print( '{0}{1}{2}{3}'.format(str(d[0]).ljust(spacing[0]), str(d[1]).ljust(spacing[1]), str(d[2]).ljust(spacing[2]), str(d[3]).ljust(spacing[3])))

            print("\n")




        #---------------------------------------------------------------------------------------------------------

# ask usre to add info to table
    @staticmethod
    def add_data():

        name = input('Enter name:\n')
        country = input('Enter country:\n')
        num_catches = Manager.get_int_input('Enter number of catches:\n')

        return name, country, num_catches

    def show_update():

       id = Manager.get_int_input('Enter record ID\n')
       name = Manager.get_string_input("Enter name\n")
       country = Manager.get_string_input("Enter country\n")
       catches = Manager.get_int_input("Enter number of catches\n")

       return id, name, country, catches

    def pick_delete():
                id = Manager.get_int_input('Enter record ID to delete\n')
                return id

            #----------------------Input Velidation-----------------------------------

#Menu Validation range and exit
    def menu_input(menu):
        while True:
            try:
                selection = int(input('\n'))
                if selection not in range(len(menu) + 1):
                    print("\nWas that a valid menu option?")
                    pass
                else:
                    return selection

            except ValueError as e:
                print("Please use digit when entering value")
                #print(e)



#int Validatio
    def get_int_input(param):
        while True:
            try:
                number_input = int(input(param))
                return number_input

            except ValueError as e:
                print("Please use digit when entering value")
                #print(e)

#string Validation
    def get_string_input(param):
        while True:
            try:
                search_string = input(param)
                return search_string
            except ValueError as e:
                print('Find by name error')
                #print(e)
