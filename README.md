# CSV Matching Script

## Description

This Python script reads two CSV files (`data.csv` and `input.csv`), compares the first and last names from each file, and returns a new CSV file (`results.csv`) containing rows where both the first name and last name match in the same row.

- `data.csv` should have the following headers:

- `input.csv` should have the following headers:

The script will match based on the `Prénom usuel` from `data.csv` with `First Name` from `input.csv` and `NomPersonne` with `Last Name`.

## Requirements

- Python 3.x
- `pandas` library (install using `pip install pandas`)
- `data.csv` containing the main list of entries
- `input.csv` containing the list where you want them to be batched
- to export your contact from android you can use https://contacts.google.com/
- to export your contact from facebook / instagram, you need to follow https://sourcetable.com/export-csv/contacts-from-facebook
- to export your contact from Linkedin, you need to follow https://www.linkedin.com/pulse/how-export-linkedin-contacts-excel-2024-guide-evaboot-zoale/

## How to Use

1. Place the `data.csv` and `input.csv` files in the same directory as the `main.py` script.
2. Run the script using the following command:

    ```bash
    python main.py
    ```

3. The script will generate a `results.csv` file containing rows where both the first name and last name match across the two CSV files.

## Example

### Sample `data.csv`:
```csv
Politesse,NomPersonne,Prénom usuel,Date de naissance,Sexe,Lieux d'origine,Adressage,RueMaison,Numéro postal
M.,Doe,John,1980-01-01,Male,City,Address,Street,12345
Mme,Smith,Jane,1985-06-15,Female,City,Address,Street,54321
