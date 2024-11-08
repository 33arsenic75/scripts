import pandas as pd
import sqlite3
import os
main = pd.DataFrame()
Departments = ["COL", "ELL", "PYL", "MTL", "HUL","COP","ELP","PYP"]
def process_csv(file_path):
    global main
    global Departments
    df = pd.read_csv(file_path)
    for index, row in df.iterrows():
        if type(row[1]) != str or not any(substring in row[1] for substring in Departments):
            df.drop(index, axis=0, inplace=True)
    df['Sem'] = file_path[52:-4]
    main = pd.concat([main, df],ignore_index=True)
    

def generate_data(main):
    current_directory = os.path.join(os.getcwd(), 'data')

    # List all CSV files in the current directory
    csv_files = [file for file in os.listdir(current_directory) if file.endswith('.csv')]

    # Iterate through each CSV file and apply the function
    for csv_file in csv_files:
        file_path = os.path.join(current_directory, csv_file)
        process_csv(file_path)
        
def save_data():
    global main
    columns_to_drop = ['Unnamed: 0', 'Unnamed: 2', 'Unnamed: 5', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15',
                   'Unnamed: 16', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12']

    main.drop(columns=columns_to_drop, inplace=True)
    main.columns = ['Course_Name', 'Slot', 'Credit_Structure', 'Professor', 'Mail ID', 'Timings', 'Sem']
    main['Professor'] = main['Professor'].str.strip()
    main = main.sort_values(by='Sem', ascending=False)
    main = main.reset_index(drop=True)
    conn = sqlite3.connect("Course_Scrapper.db")
    main.to_sql("Course_Scrapper", conn, index=False, if_exists="replace")
    conn.close()
    main.to_csv('Course_Scrapper.csv')
    
    
if __name__ =='__main__':
    generate_data(main=main)
    save_data()
    