import csv

def get_companies_from_csv(filename) -> list[dict[str,str]]:
  with open(filename, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    company_list = []
    for row in reader:
      company = {}
      company['name'] = row['company name']
      company['code'] = row['stock code']
      company_list.append(company)
    return company_list
