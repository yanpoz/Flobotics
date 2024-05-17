import csv

def read_companies_from_csv(file_path: str) -> list[dict[str,str]]:
	with open(file_path, 'r', newline='') as csvfile:
		reader = csv.DictReader(csvfile)

		company_list = []
		for row in reader:
			company = {}
			company['company name'] = row['company name']
			company['stock code'] = row['stock code']
			company_list.append(company)
		return company_list
  

def save_companies_as_csv(file_path: str, companies: list[dict[str,str]]):
	with open(file_path, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		fieldnames = companies[0].keys()

		# Write the header row
		writer.writerow(fieldnames)

		# Write each dictionary as a row in the CSV
		for item in companies:
			writer.writerow(item.values())
