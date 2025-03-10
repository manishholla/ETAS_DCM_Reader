import os
import tkinter.filedialog
import json


def select_dcm_file():
    print("Please select the DCM file. Only '.dcm' files can be selected.")
    dcm_file = tkinter.filedialog.askopenfilename(title="Select DCM file", filetypes=[("DCM", ".dcm")])
    return dcm_file


def extract_data(dcm_file):
    keywords = ['FESTWERT', 'KENNFELD', 'STUETZSTELLENVERTEILUNG', 'KENNLINIE', 'GRUPPENKENNFELD', 'FESTWERTEBLOCK',
            'TEXTSTRING', 'FESTKENNLINIE', 'FESTKENNFELD', 'GRUPPENKENNLINIE']
    extracted_data = []
    variable = None
    description = None
    function = None
    x_values = []
    y_values = []
    data_values = []

    with open(dcm_file) as file:
        for line in file:
            line = line.strip()
            if line.startswith(tuple(keywords)):
                if variable is not None:
                    extracted_data.append({
                        "Function": function,
                        "Variable": variable,
                        "Description": description,
                        "Data": {
                            "X": x_values if x_values else None,
                            "Y": y_values if y_values else None,
                            "Values": data_values
                        }
                    })
                variable = line.split()[1]
                function = None
                description = None
                x_values = []
                y_values = []
                data_values = []
            elif line.startswith('FUNKTION'):
                function = line.split()[1] if len(line.split()) > 1 else None
            elif line.startswith('LANGNAME'):
                description = ' '.join(line.split()[1:]).strip('\"\\')
            elif line.startswith('ST_TX/X') or line.startswith('ST/X'):
                x_values.extend(line.split()[1:])
            elif line.startswith('ST_TX/Y') or line.startswith('ST/Y'):
                y_values.append(line.split()[1])
            elif line.startswith('WERT') or line.startswith('TEXT'):
                data_values.extend(line.split()[1:])

        if variable is not None and function is not None:
            extracted_data.append({
                "Function": function,
                "Variable": variable,
                "Description": description,
                "Data": {
                    "X": x_values if x_values else None,
                    "Y": y_values if y_values else None,
                    "Values": data_values
                }
            })

        extracted_data = [data for data in extracted_data if data['Function'] is not None]

        functions = ', '.join(sorted(list(set([data['Function'] for data in extracted_data]))))
        variables = ', '.join(sorted(list(set([data['Variable'] for data in extracted_data]))))

        return {
            "DCM Name": os.path.basename(dcm_file),
            "Extracted Data": extracted_data,
            "DCM Variables": variables,
            "DCM Functions": functions
        }


def main():
    dcm_file = select_dcm_file()
    output_json = extract_data(dcm_file)
    print(json.dumps(output_json, indent=4))


if __name__ == "__main__":
    main()
