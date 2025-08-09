import csv

def format_candidate(first, last, title):
    return f"{first} {last} — {title}"

if __name__ == "__main__":
    print("Hello, Landing Point!")
    # Read a sample CSV and print formatted lines
    try:
        with open("sample_candidates.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(format_candidate(row["first_name"], row["last_name"], row["title"]))
    except FileNotFoundError:
        print("No sample_candidates.csv found. Add one to try the loop!")