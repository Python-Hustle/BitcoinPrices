"""
BITCOIN PRICES CHECK PROGRAM
"""
from Prices import data_extraction, show_data

if __name__ == '__main__':
    print("M A I N  P R O G R A M")
    result = data_extraction()
    show_data(result)