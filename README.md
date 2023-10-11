# ERP Automation


## Project's Objective
<p>This project's objective is to automate Data Entry in an ERP System. ERP, short for Enterprise
Resource Planning is an information system that links all the data and processes of an organization
into a single system. The interconnection can be seen from a functional perspective (finance, accounting,
human resources, manufacturing, marketing, sales, purchasing, etc.) and from a systemic perspective (transaction
processing systems, management information systems, decision support systems, etc.).</p>

<p>For this project we will be using Fakturama, an open source german ERP System and we will
transfering fictional product data from an external database to Fakturama.</p>


### Packages used:
+ pyautogui
+ pyperclip
+ subprocess
+ pandas
+ time
 

## Subprocess Package
<p>The subprocess.Popen method allows the python script to start an executable file. With this
we can open Fakturama by using a python script.</p>


## Importing the Data
<p>By using the Pandas package it is possible to automatically import data from a database, such 
as an Excel file and export that data to the ERP System.</p>


## Image Recognition - PyAutoGui
<p>We will be using PyAutoGui's image recognition functionality to identify the Fill-In Fields
present in Fakturama's interface and then fill in those fields with data imported from the database.</p>
