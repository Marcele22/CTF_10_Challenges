from datetime import datetime, date
import sys

FAKE_FLAG = "CTF{TH3_Fl4G_IS_A_n4m3}"
REAL_FLAG = "CTF{L3ST3R_M00RE}"
def parse_date(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None

def main():
    print("This calendar calculates the number of days between two dates. No Less, no More...")
    print("Format: YYYY-MM-DD")

    first = input("Enter first date: ").strip()
    second = input("Enter second date: ").strip()

    first_date = parse_date(first)

    if first == "Lester" and second == "Moore":
        print(REAL_FLAG)
        input("\nPress Enter to exit...")
        sys.exit(0)
    elif second == "Arizona" or first == "Arizona":
        print(FAKE_FLAG)
        input("\nPress Enter to exit...")
        sys.exit(0)
    elif first == "admin" or second == "admin":
        print("not even close")
        input("\nPress Enter to exit...")
    elif first == "root" or second == "root":
        print("famous tombstone in A...")
        input("\nPress Enter to exit...")
    second_date = parse_date(second)

    if not first_date or not second_date:
        print("Invalid date format.")
        input("\nPress Enter to exit...")
        sys.exit(1)

    diff = abs((second_date - first_date).days)
    print(f"Days between dates: {diff}")
    input("\nPress Enter to exit...")
if __name__ == "__main__":
    main()
