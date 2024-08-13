# File-Format-Converter

**Overview**


The objective of this project is to develop solutions based on the design provided. In this case, the source data was obtained in the form of CSV files from a MySQL DB.

To improve the efficiency of our data engineering pipelines, we need to convert these CSV files into JSON files, since JSON is better to use in downstream applications than CSV files. The scope of this project involves converting CSV files into JSON files.



**Data Model Details**

![image](https://github.com/user-attachments/assets/42e4edbd-b4f4-405c-9beb-6b46388e9370)


**Design**

![image](https://github.com/user-attachments/assets/da3d8ec1-9e89-4223-95ec-4cb0dfe59bb7)


**Setup Instructions**
1. Setup the Project Using VSCode

2. Make sure you have set up a virtual environment (creating venv, requirements.txt, etc.,) and installed dependencies for the project.

3. It is essential that you deploy the application with the core logic.

4. Run the project after setting all the environment variables.

5. Take appropriate steps to handle the exception



**Validation Steps**
1. You should check whether the data in the files has been converted properly.

2. Make sure the target folder has been created and populated with JSON files and confirm that the schema structure was accurately reflected from the CSV file. (Hint: Refer to schemas.json)

3. Take the count of records in the CSV files and compare it to the number of records in the JSON files.


**Technologies Used**
1. Programming Language – Python

2. Pandas – For Converting CSV to Dataframe and then Dataframe into JSON.
