#-----------------------------------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with Classes and Objects, Constructors, Fields, Attributes and Methods
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Bill McGinty, 2022-Mar-20, Modified File to add functionality
#-----------------------------------------------------------------------#

import sys

# -- DATA -- #
strFileName = 'CDInventory.txt'
lstOfCDObjects = []


class DataProcessor:

    def myDeleteDataProcFunc(intIDDelReceived):
        """ Function to delete CD based on ID passed to function

        Args:
            intIDDelReceived (int): ID of CD to delete.

        Returns:
            None.

        """
        # search thru table and delete CD
        intRowNr = -1
        blnCDRemoved = False
        for row in lstOfCDObjects:
            intRowNr += 1
            if lstOfCDObjects[intRowNr].cd_id_a == intIDDelReceived:
                del lstOfCDObjects[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print("The CD was removed")
        else:
            print("Could not find this CD!")
        IO.disp_current_data_screen(lstOfCDObjects)  # display inventory
        return

    @staticmethod
    def myAddProcCode(myID, myTitle, myArtist):
        """ Function to process ID, Title and Artist
        
        Args:
            myID (string): ID of CD.
            myTitle (string): Title of CD.
            myArtist (string): Artist name.

        Returns:
            None.

        """
        # Add item to the table
        intID = int(myID)
        lstTbl = [intID, myTitle, myArtist]
        lstOfCDObjects.append(CD(lstTbl[0], lstTbl[1], lstTbl[2]))
        IO.disp_current_data_screen(lstOfCDObjects)


class CD(object):

    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """

    #fields#
    __numCans = 0
    #constructor#

    def __init__(self, cd_id, cd_title, cd_artist):
        #attributes#
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
        CD.__incrementCount()

    @property
    def cd_id_a(self):
        return self.__cd_id

    @property
    def cd_title_a(self):
        return self.__cd_title.title()

    @property
    def cd_artist_a(self):
        return self.__cd_artist.title()

    @staticmethod
    def __incrementCount():
        CD.__numCans += 1

    @cd_id_a.setter
    def cd_id_a(self, value):
        if str(value).isnumeric():
            raise Exception("This message can\'t be cryptic")
        else:
            self.__cd_id = value

    @cd_title_a.setter
    def cd_title_a(self, value):
        if str(value).isnumeric():
            raise Exception("This message can\'t be cryptic")
        else:
            self.__cd_title = value

    @cd_artist_a.setter
    def cd_artist_a(self, value):
        if str(value).isnumeric():
            raise Exception("This message can\'t be cryptic")
        else:
            self.__cd_artist = value

# -- PROCESSING -- #


class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        read_file(file_name, lst_Inventory): -> None
        write_file(file_name): -> (a list of CD objects)

    """

    @staticmethod
    def read_file(file_name, lstTbl):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dictionary): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        try:
            lstTbl.clear()  # this clears existing data and allows to load data from file
            lstOfCDObjects.clear()
            objFile = open(file_name, "r")
            for line in objFile:
                data = line.strip().split(",")
                lstTbl = [int(data[0]), data[1], data[2]]
                lstOfCDObjects.append(CD(lstTbl[0], lstTbl[1], lstTbl[2]))
               # startTbl = CD(line)
            objFile.close()
        except Exception as e:
            print("\nYou need to create a CDInventory.txt file first. \n")
            print(e)
            print("Exiting Program\n")
            sys.exit()

    @staticmethod
    def write_file(file_name, recTbl):  # save data
        """ Function to save table data to text file
        
        Args:
            file_name (string): name of the file used to write data to.
            recTbl (list of dictionary): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        # Save to text file
        billIntA = 0
        objFile = open(file_name, "w")
        for row in recTbl:  # Parse each row
            lstValues = [lstOfCDObjects[billIntA].cd_id_a,
                         lstOfCDObjects[billIntA].cd_title_a, lstOfCDObjects[billIntA].cd_artist_a]
            lstValues[0] = str(lstValues[0])
            objFile.write(",".join(lstValues) + "\n")
            billIntA += 1
        objFile.close()

# -- PRESENTATION (Input/Output) -- #


class IO(object):
    """Handling Input / Output"""

    @staticmethod
    def show_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print(
            "Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory")
        print("[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n")

    @staticmethod
    def capture_users_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = " "
        while choice not in ["l", "a", "i", "d", "s", "x"]:
            choice = input(
                "Which operation would you like to perform? [l, a, i, d, s or x]: ").lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def disp_current_data_screen(lstOfCDObjects):
        """Displays current inventory of table invTbl


        Args:
            invTbl (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print("======= The Current Inventory: =======")
        print("ID\tCD Title (by: Artist)\n")
        billIntA = 0
        for row in lstOfCDObjects:
            print("{}\t{} (by:{})".format(
                lstOfCDObjects[billIntA].cd_id_a, lstOfCDObjects[billIntA].cd_title_a, lstOfCDObjects[billIntA].cd_artist_a))
            billIntA += 1
        print("======================================")

    @staticmethod
    def get_CD_add_data_from_user():
        """ Function for input / ouput
            Ask the user CD ID, Title and Artist
    
        Returns:
            strID1 (string): User inputted CD ID.
            strTitle1 (string): User inputted CD Title.
            strArtist1 (string): User inputted CD Artist.
    
        """
        while True:
            strID1 = input("Enter ID: ").strip()
            try:
                intID = int(strID1)
            except ValueError as e:
                print("\n")
                print("That is not an Integer!")
                continue
            while True:
                strTitle1 = input("What is the CD\"s title? ").strip()
                try:  # if blank raise error and start over
                    if len(strTitle1) == 0:
                        raise ValueError("You must enter a Title!")
                except ValueError as e:
                    print("\n")
                    print(e)
                    continue
                while True:
                    strArtist1 = input("What is the Artist\"s name? ").strip()
                    try:  # if blank raise error and start over
                        if len(strArtist1) == 0:
                            raise ValueError("You must enter an Artist!")
                    except ValueError as e:
                        print("\n")
                        print(e)
                        continue
                    return strID1, strTitle1, strArtist1


# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start

FileIO.read_file(strFileName, lstOfCDObjects)

while True:
    # Display Menu to user and get choice
    IO.show_menu()
    strChoice = IO.capture_users_choice()
    # Process menu selection
    # Process exit first
    if strChoice == "x":
        break
    # Process load inventory
    if strChoice == "l":
        print(
            "WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.")
        strYesNo = input(
            "type \"yes\" to continue and reload from file. otherwise reload will be canceled: ")
        if strYesNo.lower() == "yes":
            print("reloading...")
            FileIO.read_file(strFileName, lstOfCDObjects)
            IO.disp_current_data_screen(lstOfCDObjects)
        else:
            input(
                "canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.")
            IO.disp_current_data_screen(lstOfCDObjects)
        continue  # start loop back at top.
    # Process add a CD
    elif strChoice == "a":
        # Ask user for new ID, CD Title and Artist
        strID, strTitle, strArtist = IO.get_CD_add_data_from_user()
        #IO.get_CD_add_data_from_user()
        DataProcessor.myAddProcCode(strID, strTitle, strArtist)
        continue  # start loop back at top.
    # Process display current inventory
    elif strChoice == "i":
        IO.disp_current_data_screen(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == "d":  # process delete a CD
        IO.disp_current_data_screen(lstOfCDObjects)  # display inventory
        # Get Userinput for which CD to delete
        try:
            intIDDelInput = int(
                input("Which ID would you like to delete? ").strip())
        except ValueError as e:
            print("\n")
            print("That is not an Integer!")
            continue
        DataProcessor.myDeleteDataProcFunc(intIDDelInput)
        continue  # start loop back at top.
    elif strChoice == "s":  # process save inventory to file
        # Display current inventory and ask user for confirmation to save
        IO.disp_current_data_screen(lstOfCDObjects)
        strYesNo = input(
            "Save this inventory to file? [y/n] ").strip().lower()
        # Process choice
        if strYesNo == "y":
            FileIO.write_file(strFileName, lstOfCDObjects)
        else:
            input(
                "The inventory was NOT saved to file. Press [ENTER] to return to the menu.")
        continue  # start loop back at top.
    # Catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print("General Error")
