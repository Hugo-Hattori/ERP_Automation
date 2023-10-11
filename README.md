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

https://github.com/Hugo-Hattori/ERP_Automation/blob/08e9b049addee61caf9fafa155e3a854eb879af1/Automa%C3%A7%C3%A3o%20ERP.py#L23-L25


## Importing the Data
<p>By using the Pandas package it is possible to automatically import data from a database, such 
as an Excel file and export that data to the ERP System.</p>

https://github.com/Hugo-Hattori/ERP_Automation/blob/08e9b049addee61caf9fafa155e3a854eb879af1/Automa%C3%A7%C3%A3o%20ERP.py#L28-L41

## Image Recognition - PyAutoGui
<p>We will be using PyAutoGui's image recognition functionality to identify the Fill-In Fields
present in Fakturama's interface and then fill in those fields with data imported from the database.</p>

<p>For an instance, the image below is the "supplier_code.png" file used to locate the respective Fill-In Field.</p>

![supplier_code](https://github.com/Hugo-Hattori/ERP_Automation/assets/136493140/b0398bc9-3f1a-453b-a431-846426dbdb69)

https://github.com/Hugo-Hattori/ERP_Automation/blob/08e9b049addee61caf9fafa155e3a854eb879af1/Automa%C3%A7%C3%A3o%20ERP.py#L67-L69
