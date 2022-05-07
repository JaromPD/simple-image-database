
# Overview

This program was made to experiment with and learn SQL Realational Databases. To do that I made sure this program would be able to insert to a database, modify items within that database, delete items in the database, and query data from it as well. I also wanted to make sure I knew how to use that data stored in the table in a useful way.

The image_database program allows users to upload their images to an images database. To do this the program takes a user's image's date it was taken, name of the image, and a url to access that photo (I used Imgur, but you can use whatever you want). The program then allows these images to be deleted, modified, displayed on the web, or saved to the user's computer. There is also an option to display the whole database sorted by lowest to highest date.

I wrote this program in order to have a small database of my own photos that doesn't take up much space on my PC. I like to take photos as a hobby, but many of the image files are very large and take up a lot of space. This program allows me to keep them uploaded online and retrieve them anytime I have an internet connection. This keeps the amount of space needed to use these images low since I don't need to have the file downloaded to view a photo, and I can only download the photos I need at a given time.

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

I am using the sqlite3 library to create this SQL database.

The current layout of the images table is pretty simple. There are rows for each image that contain the columns date, name, and url.

<center>images<br>
<center>| date | name | url |

# Development Environment

This program was developed with Visual Studio Code.

I used Python for the whole projected, and used sqlite3, the url library, the webbrowser library and Pillow.

# Useful Websites

* [Stack Overflow](https://stackoverflow.com/questions/31768051/unable-to-download-image-using-python)

* [Stack Overflow](https://stackoverflow.com/questions/5333244/how-to-display-a-jpg-file-in-python)

* [Imgur](https://imgur.com/)

# Future Work

* Add new sorting options.

* Save pictures to user specified download folder.

* Make a UI.

* Possibly convert to a cloud database.