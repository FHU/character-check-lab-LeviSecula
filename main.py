#please work
def check_character(word, index):
   subject = word[index]
   if subject.isalpha():
       return "letter"
   elif subject.isdigit():
       return "digit"
   elif subject.isspace():
       return "white space"
   else:
       return "unknown"
   

if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))