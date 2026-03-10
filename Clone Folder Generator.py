# System Imports 
import os
import time

# Library Imports
from termcolor import colored

# Change Log File Contents Import
from ChangeLogContents import ChangeLogFileContents

# ===================================================================

# Prints Title in the CMD Console.
print(colored("*** A3 Clone Folder Creation Tool ***", "light_red"))
print(colored("========================================================================", "light_blue"))

# Asks User for the Name of Their Model of Device.
print(colored("*** Model Name ***", "light_red"))
ParentFolder = input("What is the name of the Series of A3 Machine? (e.g. IM Cxx10) ")
print(colored("========================================================================", "light_blue"))

# Asks User for the Model Name of the Finishing Options for the Specified Model.
print(colored("*** Finisher Model Names ***", "light_red"))
BookletFinisherBig = input("What is the Model Name of the Big Booklet Finsiher? (e.g. SR 3350) ")
BookletFinisherSmall = input("What is the Model Name of the Small Booklet Finisher? (e.g. SR 3330) ")
HybridFinisher = input("What is the Model Name of the Hybrid Finisher? (e.g. SR 3320) ")
InternalFinisher = input("What is the Model Name of the Internal Finisher? (e.g. SR 3310) ")
print(colored("========================================================================", "light_blue"))

# Prints in the CMD Console After the User has input the data. 
print(colored("*** Creating Clone Folder ***", "light_red"))
print(colored("========================================================================", "light_blue"))

# ===================================================================

# Sub Folders List
SubFolderNames = [
    f"2 Drawer - Hybrid ({HybridFinisher}) - Multifold - LCIT RT",
    f"2 Drawer - Booklet ({BookletFinisherSmall} & {BookletFinisherBig}) - Multifold - LCIT RT",
    f"2 Drawer - Hybrid ({HybridFinisher}) - Multifold",
    f"2 Drawer - Booklet ({BookletFinisherSmall} & {BookletFinisherBig}) - Multifold",
    f"2 Drawer - Booklet ({BookletFinisherSmall} & {BookletFinisherBig})",
    f"2 Drawer - Booklet ({BookletFinisherSmall} & {BookletFinisherBig}) - LCIT RT",
    f"2 Drawer - Hybrid ({HybridFinisher})",
    f"2 Drawer - Hybrid ({HybridFinisher}) - LCIT RT",
    f"2 Drawer or Console - Internal Finisher ({InternalFinisher})",
    "2 Drawer or Console",
    "LCIT PB",
    f"LCIT PB - Booklet ({BookletFinisherSmall} & {BookletFinisherBig})",
    f"LCIT PB - Hybrid ({HybridFinisher})",
]

# Miscelllaneous Folders List
Miscellaneous_Folders = [
    "Education",
    "Linktech",
    "Papercut",
    "Tasprint",
]

# ===============================================================

# Create Change Log Function
def CreateChangeLogFile(SubFolderPath, ChangeLogTitle):

    try:

        # Naming the File Path
        FilePath = os.path.join(SubFolderPath, "Change Log.txt")

        # Creation the File with the Name Above
        with open(FilePath, "a") as file:

        # Writing to the File using the contents of the Master
            file.write(ChangeLogFileContents(ChangeLogTitle))

        # Error Handling
    except FileExistsError:
        print(f"{ChangeLogTitle} Change Log File already exsits.")

    except Exception as ErrorMessage:
        print(f"An unexpected error occurred: {ErrorMessage}")

# ===================================================================

# Creats Sub Folders Within a Specified Folder
def SubFolderCreator(SubFolderPath, ChangeLogTitle, SubFolderName):

    try:

        # Create Folder with name passed in and then tells the User in the CMD window "creation was successful".
        os.mkdir(SubFolderPath)
        print(f"Sub Folder '{SubFolderName}' created successfully.")

        # Calls the CreateChangeLog Function to create a .txt in each folder
        CreateChangeLogFile(SubFolderPath, ChangeLogTitle)
        time.sleep(0.05)
    
    # Error Handling
    except FileExistsError:
        print(f"File {SubFolderName} Already Exists")

    except Exception as ErrorMessage:
        print(f"An unexpected error occurred: {ErrorMessage}")

# ===================================================================

def CreateMiscellaneousFolders(FolderName):

    try:

        FolderNamingScheme = f"{FolderName} - {ParentFolder}"
        FolderPath = os.path.join(ParentFolder, FolderNamingScheme)

        os.mkdir(FolderPath)
        print(f"Sub Folder '{FolderNamingScheme}' created successfully.")

        for SubFolderName in SubFolderNames:

            SubFolderNamingScheme = f"{FolderName} - {ParentFolder} - {SubFolderName}"
            SubFolderPath = os.path.join(ParentFolder, FolderNamingScheme, SubFolderNamingScheme)

            # Passes down the Sub Folders Name, the Naming Scheme to later be turned into the "ChangeLogTitle" and the path of where then file will be created.
            SubFolderCreator(SubFolderPath, SubFolderNamingScheme, SubFolderName)

        print(colored("========================================================================", "light_blue"))
        print(colored(f"*** {FolderNamingScheme} has been created successfully ***", "light_red"))
        print(colored("========================================================================", "light_blue"))

        time.sleep(0.5)

    # Error Handling
    except FileExistsError:
        print(f"File {FolderName} Already Exists")

    except Exception as ErrorMessage:
        print(f"An unexpected error occurred: {ErrorMessage}")   

# ===================================================================

# Main Code
try: 

    # Create Parent Folder
    os.mkdir(ParentFolder)
    print(f"Parent Folder {ParentFolder} created successfully")

    # Factory Sub Folder Creation
    FactoryFolderNamingScheme = f"..{ParentFolder} - Factory Clone"
    FactoryCloneFolderPath = os.path.join(ParentFolder, FactoryFolderNamingScheme)

    os.mkdir(FactoryCloneFolderPath)
    print("Sub Folder Factory Clone created successfully.")

    # Create Sub Folders for Each Name in the Sub Folder List
    for SubFolderName in SubFolderNames:

        SubFolderNamingScheme = f".{ParentFolder} - {SubFolderName}"
        SubFolderPath = os.path.join(ParentFolder, SubFolderNamingScheme)

        # Passes down the Sub Folders Name, the Naming Scheme to later be turned into the "ChangeLogTitle" and the path of where then file will be created.
        SubFolderCreator(SubFolderPath, SubFolderNamingScheme, SubFolderName)

    print(colored("========================================================================", "light_blue"))
    print(colored(f"*** Main Clone Section has been created successfully ***", "light_red"))
    print(colored("========================================================================", "light_blue"))

    time.sleep(0.5)

    # Create Miscellaneous Folders from list
    for FolderName in Miscellaneous_Folders:

        CreateMiscellaneousFolders(FolderName)
    
    # Create Customer Specific (this is done seperate as we want it to be done seperatly)
    CustomerNamingScheme = f"Customer Specific - {ParentFolder}"
    CustomerSpecificFolderPath = os.path.join(ParentFolder, CustomerNamingScheme)
    SubFolderCreator(CustomerSpecificFolderPath, f"Customer Specific - {ParentFolder}", CustomerNamingScheme)
    
    # Removes the Change Log File that was created from the function as it is not needed.
    ChangeLogPath = os.path.join(CustomerSpecificFolderPath, "Change Log.txt")
    if os.path.exists(ChangeLogPath):
        os.remove(ChangeLogPath)

# Error Handling
except FileExistsError:
    print(colored(f"Parent Folder '{ParentFolder}' already exsits. \u03a7", "light_red"))

except Exception as ErrorMessage:
    print(f"An unexpected error occurred: {ErrorMessage}")

# if creation was a success, it tells the user that the Clone Folder Creation was a success.
else:
    print(colored("Folder Creation Complete \u2714", 'green'))

# Enter to exit out of the CMD Window. (Otherwise it would disapear after completion)
finally:
    input("Press Enter to exit...")
