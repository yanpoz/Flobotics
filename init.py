import csv

def parse_csv(filename) -> list[dict[str,str]]:
  with open(filename, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    company_list = []
    for row in reader:
      company = {}
      company['name'] = row['company name']
      company['code'] = row['stock code']
      company_list.append(company)
    return company_list

# Example usage
res = parse_csv("input.csv")
for item in res:
  print(f"Company Name: {item['name']}, Stock Code: {item['code']}")
