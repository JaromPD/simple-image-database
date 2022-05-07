import sqlite3
import urllib.request
import webbrowser
from PIL import Image
import os

# The connection to the database is established.
connection = sqlite3.connect('images.db')
# The cursor is created.
cursor = connection.cursor()

# The table is made if it doesn't already exist.
cursor.execute("CREATE TABLE IF NOT EXISTS images (date TEXT, name TEXT, url TEXT)")

def add_new_image():
    '''Adds an image to the database'''

    # User input is taken.
    date = input("Date: ")
    name = input("Name: ")
    url = input("Url: ")

    # Checks to see if the name is already in use.
    if image_exists(name):
        print(f"Image with name {name} already exists!")
    else:
        # The info is added.
        values = (date, name, url)
        cursor.execute("INSERT INTO images VALUES (?, ?, ?)", values)
        # It is committed to the database.
        connection.commit()

def remove_image():
    '''Removes the image from the database.'''

    # Name is taken.
    name = input("What is the name?: ")

    # Chcecks to see if there is an image with that name to be removed.
    if image_exists():

        # Image is deleted from database.
        values = (name, )
        cursor.execute("DELETE FROM images WHERE name = ?", values)
        connection.commit()
    else:
        print(f"Image with name {name} doesn't exist!")

def modify_image():
    '''Alters an image's info such as date, name, and url.'''

    # Name is taken.
    name = input("What is the name?: ")

    # Checks to see that image with that name exists.
    if image_exists(name):

        # Prints the menu
        print("What would you like to modify?\n    1. Date\n    2. Name\n    3. Url")
        
        # Makes sure the input is an integer.
        while True:
            try:
                user_selection = int(input("> "))
                break
            except:
                print("Must be an integer!")

        # Takes the new data.
        new_data = input(f"What is the new data?: ")
        values = (new_data, name)

        # Applies that new data to the user's selection of date, name, or url.
        match user_selection:
            case 1:
                cursor.execute("UPDATE images SET date = ? WHERE name = ?", values)
                modifier = "date"
            case 2:
                cursor.execute("UPDATE images SET name = ? WHERE name = ?", values)
                modifier = "name"
            case 3:
                cursor.execute("UPDATE images SET url = ? WHERE name = ?", values)
                modifier = "url"

        # The change is saved
        connection.commit()

    else: 
        print(f"Image with name {name} doesn't exist!")

def save_image(url, fpath):
    '''The image is saved to the computer.'''

    urllib.request.urlretrieve(url, fpath)

def display_data():
    '''The data in the database is displayed.'''

    # It is listed from lowest date to highest.    
    cursor.execute("SELECT * FROM images ORDER BY name DESC")
    print("{:>10}  {:>10}  {:>10}".format("date", "name", "url"))
    for item in cursor.fetchall():
        print("{:>10}  {:>10}  {:>10}".format(item[0], item[1], item[2]))


def display_image_web(url):
    webbrowser.open(url)

def get_image_data(cursor):
    user_search = input("Which image?: ") 
    if image_exists(user_search):

        values = (user_search, )
        cursor.execute("SELECT * FROM images WHERE name = ?", values)
        image_info = cursor.fetchall()
        return image_info
    else:
        print(f"Image with name {user_search} doesn't exist!")

def image_exists(name):
    values = (name,)
    cursor.execute("SELECT * FROM images WHERE name = ?", values)
    image_info = cursor.fetchall()
    if len(image_info) == 0:
        return False
    else:
        return True

# TEST URLS: Spori https://i.imgur.com/gs78unU.jpg
#            Rexburg https://i.imgur.com/wdqytYA.jpg
#            Moon https://i.imgur.com/AcuwXyB.jpg

def main(cursor):
    menu = True
    while menu:
        print(
            """
            ---- Welcome to my simple image database! ----

            What would you like to do?
                1. Add image to database.
                2. Remove image from database.
                3. Modify image in database.
                4. Display image from database.
                5. Save image from database.
                6. Display database.
                7. Quit.
            """)

        while True:
            try: 
                user_choice = int(input("> "))
                break
            except:
                print("Selection must be an integer!")


        match user_choice:
            case 1:
                add_new_image()
            case 2:
                remove_image()
            case 3:
                modify_image()
            case 4:
                image_info = get_image_data(cursor)
                for data in image_info:
                    url = data[2]
                display_image_web(url)
            case 5:
                image_info = get_image_data(cursor)
                for data in image_info:
                    name = data[1]
                    url = data[2]

                path = name + ".jpg"
                save_image(url, path)
            case 6:
                display_data()
            case 7:
                menu = False

main(cursor)