import pandas as pd


def main():
    # Read the CSV files
    data_df = pd.read_csv('data.csv')
    input_phone_df = pd.read_csv('input_phone.csv')
    input_linkedin_df = pd.read_csv('input_linkedin.csv')

    # Combine input and linkedin data
    combined_input_df = pd.concat([input_phone_df[['First Name', 'Last Name']], input_linkedin_df[['First Name', 'Last Name']]])

    # Drop duplicates if any exist between the two input files
    combined_input_df = combined_input_df.drop_duplicates()

    # Filter the entries where First Name and Last Name match
    result_df = pd.merge(
        data_df,
        combined_input_df,
        left_on=['Prénom usuel', 'NomPersonne'],
        right_on=['First Name', 'Last Name']
    )

    # Write the result to a new CSV file
    result_df.to_csv('results.csv', index=False)


if __name__ == "__main__":
    main()
