import csv

def get_column_from_csv(filename, feature: str) -> list[str]:
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row[feature] for row in reader]
