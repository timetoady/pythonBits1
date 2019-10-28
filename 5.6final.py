"""
decmal to bianry
generalize code, put in function
check remainder, add remainder, instead of using number, use number as index into table.
"""
hexTable = {'10': 'A', '11': 'B', '12': 'C',
            '13': 'D', '14': 'E', '14': 'F',}

def decimalToRep(value, base):
    bstring = ""
    while value > 0:
        remainder = value % base
        value = value // base
        if remainder > 9:
            remainder = hexTable[str(remainder)]    
        bstring = str(remainder) + bstring  
    return str(bstring)

def main():
    print(decimalToRep(10,10))
    print(decimalToRep(28,16))
    print(decimalToRep(10,8))
    print(decimalToRep(10,2))


if __name__ == "__main__":
    main()