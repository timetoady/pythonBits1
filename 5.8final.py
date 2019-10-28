import re
def file_load():
    fin = open(input("Enter the input file name: "))
    text = fin.read()
    word_list = re.findall(r'\b\w[\w-]*\b', text.upper())
    return word_list

def main():
    text = file_load()
    word_dict = {}
    count = 0
    for word in text:
        if word not in word_dict:
            count = 1
            word_dict.update({word : count})
        elif word in word_dict:
            count = word_dict.get(word)
            word_dict[word] = count+1
    for item in sorted(word_dict):
        print("{} {}".format(item,word_dict[item]))


if __name__ == "__main__":
    main()
