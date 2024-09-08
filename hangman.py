import random

word_list = ["happy", "harsh", "demon", "sad", "cry", "camel"]
lifes = 5
game_over = False
correct_letter = []

#length and computer selecting word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word)

#Blanks
placeholder = ""
for letter in range(word_length):
    placeholder += "_"    
print(placeholder)

#guess and check
while not game_over:
    
    if lifes == 0:
        print("\t\t\t*************YOU Lost THE GAME*************\t\t\t")
        game_over = True
    
    display = ""
    guess = input("Guess a letter: ").lower()
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    
    #edge cases
    
    if "_" not in display:
        print("\t\t\t*************YOU WON THE GAME*************\t\t\t")
        game_over = True
    if guess not in chosen_word:
        lifes -= 1
    
    print(display)
    print(f"Lifes left = {lifes}")