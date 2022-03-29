
#**Report of monaco Racing** 
_______________________________________________________

This Flask web application reads pilot data from three files 
**_abbreviations.txt, start.log, end.log_** sorts them by results, writes 
these results to the database. 

The application has a web interface.

To launch the application, you need to create a database, to do this, 
go to the _create_db.py_ file and run the script. This will create a database.
After that, go to the main folder, then _app.py_ and launch the app.

The app has a swagger to use go to http://127.0.0.1:5000/apidocs/.