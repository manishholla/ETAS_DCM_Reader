# ETAS_DCM_Reader

## About ETAS_DCM_Reader

ETAS_DCM_Reader is a code written in python to read DCM file and outputs necessary data:
  1. Extracted Data- Data containing the variable names, function names and the field data with respect to the variables in JSON list format enclosed in square brackets ("[]").
  2. DCM Name- Name of the DCM file
  3. Variables- Name of the variables in single line format separated by comma (",").
  4. Functions- Name of the functions in single line format separated by comma (",").

## ETAS DCM Documentation

It follows the standard ASCET DAMOS format and is coded as per ETAS Technical Format. You may find more information by visiting here: [DCM File Formats Technical Note](https://www.etas.com/download-center-files/products_ASCET_Software_Products/TechNote_DCM_File_Formats.pdf)

## Note 
![Warning-PNG-Clipart-removebg-preview](https://github.com/manishholla/ETAS_DCM_Reader/assets/29548788/f5f8c2e3-e3bc-427f-a864-1062e2fa9142)

The code only accept DCM file extension. Any other format will not be parsed by the code.

## Using ETAS_DCM_Reader

When the code is run in the Python supported IDE, a pop-up will open asking the user to select the DCM. 

[image tkinter]

Post selecting the DCM file, the code reads the file line-by-line and stores the information in Pandas Dataframe. At the end of the file (after the last line), the code stops and outputs the stored data in multiple ways. They are mentioned below.

A Sample DCM file is provided. Please run the code and us it to verify the output. The output will look as shown below:
  
  ### Extracted Data
Using the attached DCM, the output is generated as follows:
![extracted_data](https://github.com/manishholla/ETAS_DCM_Reader/assets/29548788/d05b4c4e-ef4b-4434-aacf-2d11ff37b027)

The data is in JSON list format. All the data that is stored in the DCM is passed into this JSON list (no loss of data). This passed data is stored in a global standalone variable called
    
    extracted_data

User may call this and perform several operations as per his/her requirement to modify the data

### DCM Name
The name of the file is also stored in the Dataframe and is thrown at the end into a standalone variable called 

    dcm_name

This can be called marking the stored data (extracted_data). Using the attached DCM, the output is generated as follows:

![dcm_name](https://github.com/manishholla/ETAS_DCM_Reader/assets/29548788/f1dc5f98-c875-4119-b481-0840405f3436)



### Labels
It is the output line which contains the name of all the variables present in the DCM file. They are separated by comma (","). This data is stored in a standalone variable called

    labels

There may be some use cases where it is not necessary to store all the data but just the variable names. User can call this and store the DCM variables apart from the 'extracted_data'. Using the attached DCM, the output is generated as follows:

![labels](https://github.com/manishholla/ETAS_DCM_Reader/assets/29548788/accbd49e-8e7f-4f29-a943-3e30cec4b78a)


### Functions
It is the list of functions corresponding to the 'labels' denoted by "FUNKTION" in the DCM file as per ETAS standards (Please read the ETAS documentation linked above). The output functions are separated by comma (","). This is stored in a standalone variable called 

    functions

There may be some use cases where it is not necessary to store all the data but just the function names. User can call this and store the DCM functions apart from the 'extracted_data'. Using the attached DCM, the output is generated as follows: 

![functions](https://github.com/manishholla/ETAS_DCM_Reader/assets/29548788/3bfe33fe-1e06-42db-baf0-e6848d987ff8)


### End Notes

Multiple operations can be perfomed using this code and modifying as per the requirement. The extracted data can also be plotted into heatmaps, pie charts, bar graphs, etc., using libraries like plotly, matplotlib and so on.
