"""
Project: Password Checker
Date:
Description:

"""
import string
#Definitions
def is_long_enough(pwd):
    if len(pwd) < 8:
        raise ValueError(f"{pwd} Not enough characters. Must be at least 8 characters.")
    return pwd

def is_valid(pwd, string_set, msg):
    for ch in pwd:
        if ch in string_set:
            return pwd
    raise ValueError(msg)
    
def has_upper(pwd):
    return is_valid(pwd, string.ascii_uppercase, f"{pwd} Must have at least 1 uppercase function.")
           

def has_lower(pwd):
    return is_valid(pwd, string.ascii__lowercase, f"{pwd} Must have at least 1 lowercase function.")

def has_digit(pwd):
    return is_valid(pwd, string.digits f"{pwd} Must have at least 1 lowercase function.")
            return True
    return False

def special(pwd):
    specials = "!@#$%^&*-"
    return is_valid(pwd, specials)

def main(): #main function needs all programs for automated testing
    #Define file names
    IN_FILE_NAME = "pwd.txt"
    INVALID_FILE_NAME = "invalid003.txt"
    VALID_FILE_NAME = "valid003.txt"
    
    print("Password Checker: Opening Files...")
    in_file = open(IN_FILE_NAME, 'r')
    out_file_valid = open(VALID_FILE_NAME, 'w')
    out_file_invalid = open(INVALID_FILE_NAME, 'w')
    
    for line in in_file:
        line = line.strip()
        try:
            all([is_long_enough(line),
                 has_upper(line),
                 has_lower(line),
                 has_digit(line),
                 special(line)])
            print(line,file= out_file_valid)
        except ValueError as e:
                  print(str(e), file =out_file_invalid)
        if len(line) < 8:
            print(f"{line} Not enough characters. Must be at least 8 characters.", file = out_file_invalid)
            continue
        if not has_upper(line):
            print(f"{line} Must have at least 1 uppercase function.", file = out_file_invalid)
            continue
        if not has_lower(line):
            print(f"{line} Must have at least 1 lowercase function.", file = out_file_invalid)
            continue
        if not has_digit(line):
            print(f"{line} Must have at least 1 digit 0-9.", file = out_file_invalid)
            continue
        if not special(line):
            print(f"{line} Must have at least 1 special character(!@#$%^&*-).", file = out_file_invalid)
            continue
        print(line, file = out_file_valid)
    print("Check completed.")    
    in_file.close
    out_file_valid.close
    out_file_invalid.close
        
if __name__ == "__main__":
    main()