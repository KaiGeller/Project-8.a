#Kai Geller
#GitHub Username: KaiGeller
#5/17/2022
#This code will take the letters in a string and return the number of each letter in that string
string = "kfnefuqwfonqliuwfqiuwhHHHHH"
def count_letters(string):
    """This function will find the number of each letter in the word"""
    new_dictionary = {}
    string = string.upper()
    for attribute in string:
        if attribute in new_dictionary:
            new_dictionary[attribute] = new_dictionary[attribute]+1
        else:
            new_dictionary[attribute]=1
    return new_dictionary
