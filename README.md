# ETAS DCM Reader v2

## About ETAS_DCM_Reader_v2

This is a Python based script that extracts data from `.dcm` files (commonly used in automotive calibration) and outputs the results in JSON format. It supports extracting all data, functions, or variables separately based on user-specified modes.


## ETAS DCM Documentation

It follows the standard ASCET DAMOS format and is coded as per ETAS Technical Format. You may find more information by visiting here: [DCM File Formats Technical Note](https://www.etas.com/download-center-files/products_ASCET_Software_Products/TechNote_DCM_File_Formats.pdf)


## Note 
![Warning-PNG-Clipart-removebg-preview](https://github.com/manishholla/ETAS_DCM_Reader/assets/29548788/f5f8c2e3-e3bc-427f-a864-1062e2fa9142)

The code only accepts DCM file extension. Any other format will not be parsed by the code.

## Features
- **File Selection**: Uses a Tkinter file dialog to select `.dcm` files. One can also pass the file URI directly to `dcm_file`
- **Data Extraction**: Parses key data: Function, Variable, Description, and associated X/Y/Z values from `.dcm` files. If values for any axis is not available, it returns `""`.
- **Flexible Output**: Returns JSON-formatted data in three modes:

  - `all`: Full extracted data including function names, variable names, descriptions, and data values.  
  - `functions`: List of unique function names.  
  - `variables`: List of unique variable names.  
  
The above functionality depends on it is called from the constructor. Example:\
	- for `all` - `output_all = extract_data(dcm_file, mode='all')`\
	- for `functions` - `output_functions = extract_data(dcm_file, mode='functions')`\
	- for `variables` - `output_variables = extract_data(dcm_file, mode='variables')`

- **Output**: Returns the full extracted data into a JSON formatted human readable data and prints results to the console.

## Requirements

- **Python 3.x**: Ensure Python is installed on your system.
- **Tkinter**: Comes bundled with Python (this can be removed if file URI is passed directly).

## Installation

1. **Clone or Download**: 
   - Clone this repository or download the script file (`dcm_reader_v2.py`) from [here](https://github.com/manishholla/ETAS_DCM_Reader/blob/main/v2/dcm_reader_v2.py).
2. **Verify Python**: 
   - Run `python --version` or `python3 --version` in your terminal to confirm Python is installed.
3. **No Dependencies**: The script uses only standard Python libraries (`os`, `tkinter.filedialog`, `json`).

## Usage
4. **Run the Script**:
   ```bash
   python3 dcm_reader_v2.py
   ```
   - A file dialog will prompt you to select a `.dcm` file. For testing, you can use the Example.DCM file available in this repository under [/DCM/](https://github.com/manishholla/ETAS_DCM_Reader/blob/main/DCM/) .

5. **Output**:
   - The script processes the file and outputs JSON-formatted data in three modes:
     - **All Data**: Printed to the console.
     - **Functions**: Printed to the console.
     - **Variables**: Printed to the console.

6. **Modes**:
   - The `extract_data()` function accepts a `mode` parameter:
     - `'all'`: Returns full extracted data.
     - `'functions'`: Returns unique function names.
     - `'variables'`: Returns unique variable names.
   - Example usage within Python:
     ```python
     output = extract_data("path/to/file.dcm", mode="all")
     print(output)  # JSON string
     ```

## Code Structure

- **`select_dcm_file()`**: Opens a file dialog to select a `.dcm` file.
- **`extract_data(dcm_file, mode='all')`**:
  - Parses the `.dcm` file line-by-line.
  - Recognizes keywords (e.g., `FESTWERT`, `KENNFELD`) and specific tags (`FUNKTION`, `ST_TX/X`, etc.).
  - Returns JSON-formatted strings based on the specified mode.
- **`main()`**: Orchestrates file selection, data extraction, file writing, and printing.

## Example Output

For a `.dcm` file with content like:
```
FUNKTION Func1
FESTWERT Var1
ST_TX/X "1" "2"
WERT "10"
```
Running the script produces:
- **All Data**:
  ```json
  {
      "DCM Name": "example.dcm",
      "Extracted Data": [
          {
              "Function": "Func1",
              "Variable": "Var1",
              "Description": null,
              "Data": {
                  "X": ["1", "2"],
                  "Y": null,
                  "Values": ["10"]
              }
          }
      ]
  }
  ```
- **Functions**:
  ```json
  {
      "DCM Name": "example.dcm",
      "DCM Functions": "Func1"
  }
  ```
- **Variables**:
  ```json
  {
      "DCM Name": "example.dcm",
      "DCM Variables": "Var1"
  }
  ```

## Notes

- **Quote Handling**: The current version does not strip quotes from values (e.g., `"\"SomeMode\""` remains as-is). If there is a space in the value like `Some Mode` then the output will be:
``` text
                    "\"Some",
                    "Mode\""
```
 
- If you need quote stripping, modify the parsing logic in `extract_data()`.
- **Error Handling**: Basic mode validation is included; expand as needed for robustness.

## Contributing

Feel free to fork this project, submit pull requests, or report issues if you encounter bugs or have suggestions!
