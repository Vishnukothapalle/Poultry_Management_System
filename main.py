from database import table_creation
from data_insertion import insertion
from analysis import analysis

def main():
    table_creation()
    insertion()
    analysis()

if __name__ == "__main__":
    main()