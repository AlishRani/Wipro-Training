import csv
import os

def write_csv(filename):
    data = [
        {"name": "Poornima", "age": 30},
        {"name": "Raju", "age": 25}
    ]

    columnnames = ["name", "age"]

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columnnames)
        writer.writeheader()
        writer.writerows(data)

    print("CSV file written successfully")


# Function to read data from CSV
def read_csv(filename):
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        print("\nReading CSV file:")
        for row in reader:
            print(f"Name: {row['name']}, Age: {row['age']}")


def delete_csv(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted successfully")
    else:
        print("File does not exist")


filename = "myfile.csv"

write_csv(filename)
read_csv(filename)

# Uncomment below if you want to delete file
# delete_csv(filename)