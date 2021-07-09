import random 

list_word = ["ball","cat"]

def get_word():
    with open("word.txt", "r") as f:
        word_list = f.read().split()
    return(random.choice(word_list).upper())

def play(word):
    tries = 6
    guessed = False
    guess_word  = "_" * len(word)
    guessed_word = []
    guessed_letter=[]
    print("=============================================================")
    print("----------------------WELCOM TO HANGMAN----------------------")
    print("\n")
    print(hangman_figure(tries))
    print(guess_word)
    print("\n")

    while not guessed and tries>0:

        guess = input("Enter your guess: ").upper()

        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letter:
                print("Already guessed ",guess)
                print(guess_word)
                print("\n")
            elif guess not in word:
                tries-=1
                print(hangman_figure(tries))
                print("Wrong guess",guess)
                guessed_letter.append(guess)
                print("Remainig tries = ",tries)
                print(guess_word)
                print("\n")
            else:
                print("letter guessed correctly")
                word_as_list = list(guess_word)
                for i in range (len(word)):
                    if word[i] == guess:
                        word_as_list[i]=guess
                guess_word = "".join(word_as_list)
                if guess_word == word:
                    guessed = True
                print(hangman_figure(tries))
                print(guess_word)
                print("Remainig tries = ",tries)
                print("\n")

        elif len(guess)==len(word) and guess.isalpha():

            if guess in guessed_word:
                print("Already guessed ",guess)
                print(guess_word)
                print("\n")

            elif guess == word:
                guessed = True
                guess_word = word
                print(hangman_figure(tries))
                print(guess_word)
                print("\n")
            
            else:
                tries-=1
                print(hangman_figure(tries))
                print("Wrong guess ",guess)
                print("Remainig tries = ",tries)
                print(guess_word)
                print("\n")

        else:
            print("Invalid guess")
            print("\n")

    if guessed == True:
        print("Congtatz you have guessed it right \n")
    else:
        print("You failed Man is hung")
        print("Correct Answer is "+word+"\n")
    

def hangman_figure(tries):
    fig = [ """  
             --------------------
             |         |
             |         O
             |        \\|/
             |         |
             |        / \\
             |     
             
            """
            ,
            """  
             --------------------
             |         |
             |         O
             |        \\|
             |         |
             |        / \\
             |     
             
            """ 
            ,
            """  
             --------------------
             |         |
             |         O
             |         |
             |         |
             |        / \\
             |     
             
            """
            ,
            """  
             --------------------
             |         |
             |         O
             |         |
             |         |
             |          \\
             |     
             
            """
            ,
            """  
             --------------------
             |         |
             |         O
             |         |
             |         |
             |          
             |     
             
            """
            ,
            """  
             --------------------
             |         |
             |         O
             |         
             |         
             |         
             |     
             
            """
            ,
            """  
             --------------------
             |         
             |         
             |        
             |         
             |        
             |     
             
            """

            
    ]
    return(fig[tries])


if __name__ == '__main__':
    word = get_word()
    play(word)
    while input("Do you want to play again ? :  ").upper() == "Y":
        word = get_word()
        play(word)



