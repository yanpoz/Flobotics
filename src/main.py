from get_companies_from_csv import get_companies_from_csv


def main():
    res = get_companies_from_csv("input.csv")
    for item in res:
        print(f"Company Name: {item['name']}, Stock Code: {item['code']}")



if __name__ == '__main__': 
    main()