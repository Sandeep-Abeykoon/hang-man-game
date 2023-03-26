# Importing modules and packages
import random



def rand_word():
    """This function selects a random word from the word list
       and shows the blank spaces to the user"""
    win_list=[]
    word=word_list[random.randrange(20)]
    hint=hint_list[word_list.index(word)]
    print("_ " * len(word),"(HINT :",hint,")\n")
    
    for x in range(len(word)):
        win_list.append("_")
    return word, win_list





def word_progress(win_list):
    """This function joins the win_list and prints the word progression"""
    print(' '.join(win_list))
    print()





def game():
    """This function runs the program for a single round
       """
    word, win_list = rand_word()
    guess_list=[]
    correct=0
    chance=len(word)
    while(chance!=0):

        # If the player guessed the word
        if correct==len(word):
            print("\nYay you got it!!!, The word is",word)
            print("-----------------------------------------------------------------------------")
            break
        print()
        print("chances :",chance)
        letter=str(input("Letter : ")).lower()

        # Checks and validates the user inpur
        if ((len(letter))>1) or letter.isnumeric():
            print()
            print("Please enter a valid input")
            continue

        # Checks whether the letter is guessed
        if letter in guess_list:
            print("You have already guessed this letter\n")
            word_progress(win_list)
            continue
        else:
            guess_list.append(letter)
        print()

        # Checks weather letter is in the word
        if letter in word:
                for i in range(len(word)):
                    if word[i]==letter:
                        win_list[i]=letter
                        correct+=1
                word_progress(win_list)
        else:
            print("The letter is not in the word")
            word_progress(win_list)
            chance-=1
    return  chance, word  


       
                   
# Initializing the Word list and the Hint list           
word_list=['banana','monkey','tomato','eraser','pencil',
           'computer','python','motorcycle','monitor',
           'hospital','doctor','information','mouse',
           'speaker','calendar','apple','laptop',
           'lorry','electricity','stethoscope']


hint_list=["A yellow colour fruit",
           "An animal which mostly live in trees",
           "Mostly round, red colour vegetable",
           "Used to rub out something written",
           "Used for drawing and writing",
           "An electronic machine which perform inputs, process and outputs",
           "An interpreted programming language",
           "A vehicle that has no pedals",
           "A device used for observing digital display",
           "An institution that provides facilities for disease diagnosis",
           "A person who is qualified to treat people",
           "Data is processed into?",
           "Movable computer device",
           "Electronic device which provides audio output",
           "Used to check date",
           "A tasty fruit",
           "A portable computer",
           "A vehicle which is basically used to transport cargo",
           "A form of energy",
           "An instrument used by a doctor"]
              










