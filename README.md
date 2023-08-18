# OdooModule-RealEstate
This is first module I made with Odoo using python codes with xml.

This is a small project that let's me explore and know more about Odoo development using Python scripts. 

# Descriptions of the insides of the folder that was used
The manifest and init files outside of all the folders are an important files. The manifest is the description of the module House-Estates, it has the name, description, version of the module. This is also where you connect the xml files of the program. The init file is the one that connects the files together working with other init files.

The model folder indicates the Variables of the things that needs to be filled inside the database or the forms of the House Estate/Available/Houses. The init file there is just the one to import it so that it connects with the other files.

The security folder has the ir.model.access.csv it contains the ability of the user to read, write, edit and delete any information that will be written on the form and will be stored on the database of the computer, it is also vital to connect the main name of the models files from the models folder.

The views folder has all the xml files where the program will then based the look of the program where the user would see the menu items and the items under the menu. It is also responsible for aligning the things inside the form that will be stored on the database.

# Note
This program is a test program and is not nearly as complete. It is still in progress.

# Update 18-8-23
I put some active checkbox where if the user would click Active Contract it will be seen while if its not checked it will go archived or the not active contracts. Also did a selection field that has a default value of new. I changed the design of the form, added a notebook and page to it for the description to be separated. 
The last thing I added was I made the name more visible by making it bigger. 
