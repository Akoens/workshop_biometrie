import csv

def main():
    with open("spreadsheet_biometrie.csv", encoding="UTF-8") as biometric_file:

        bio_data = csv.reader(biometric_file)
        for row in bio_data:
            print(row)
            # length = row[3]
            # width = row[4]






if __name__ == "__main__":
    main()