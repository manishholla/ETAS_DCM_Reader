import os
import tkinter.filedialog
import pandas as pd

def select_dcm_file():
    print("Please select the DCM file. Only '.dcm' files can be selected.")
    dcm_file = tkinter.filedialog.askopenfilename(title="Select DCM file", filetypes=[("DCM", ".dcm")])
    return dcm_file

def extract_data(dcm_file):
    desc = ['FESTWERT', 'KENNFELD', 'STUETZSTELLENVERTEILUNG', 'KENNLINIE', 'GRUPPENKENNFELD', 'FESTWERTEBLOCK', 'TEXTSTRING', 'FESTKENNLINIE', 'FESTKENNFELD', 'GRUPPENKENNLINIE']
    data_df = pd.DataFrame(columns=['Variable', 'Function', 'X', 'Y', 'Data'])
    current_variable = None
    current_function = None
    current_x = []
    current_y = []
    current_data = []

    with open(dcm_file) as file:
        for line in file:
            line = line.strip()
            if line.startswith(tuple(desc)):
                current_variable = line.split()[1]
                current_function = None
                current_x = []
                current_y = []
                current_data = []
            elif line.startswith('FUNKTION'):
                current_function = line.split()[1] if len(line.split()) > 1 else None
            elif line.startswith('ST_TX/X') or line.startswith('ST/X'):
                current_x.extend(line.split()[1:])
                continue
            elif line.startswith('ST_TX/Y') or line.startswith('ST/Y'):
                current_y.append(line.split()[1])
                continue
            elif line.startswith('WERT') or line.startswith('TEXT'):
                current_data.extend(line.split()[1:])

            if line == 'END':
                data_df.loc[len(data_df)] = [current_variable, current_function, current_x, current_y, current_data]
                current_variable = None
                current_function = None
                current_x = []
                current_y = []
                current_data = []

    return data_df

# User prompt to select DCM file
dcm_file = select_dcm_file()

# Retrieves the name of the DCM file
dcm_name = os.path.basename(dcm_file)

# Extract data with respective global variables
data_df = extract_data(dcm_file)

# Filter out None values and store 'Variable' column in a separate variable
labels = ', '.join(filter(None, data_df['Variable'].tolist()))

# Stores 'Function' column in a separate variable
functions = ', '.join(data_df['Function'].dropna().tolist())

# Stores the extracted data in JSON format
extracted_data = data_df.drop(0).to_json(orient="records")

# Print the extracted data
print(extracted_data)
print(labels)
print(functions)
print(dcm_name)


#API
# extracted_data                  Outputs data of a variable along with the function in JSON format
# dcm_name                        Name of input DCM
# labels                          Output labels from pandas dataframe in single line comma separated form
# functions                       Output functions from pandas dataframe in single line comma separated form

