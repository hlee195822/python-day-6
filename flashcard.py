flashcard = [
    {"question": "what is my name", "answer": "Hank"},
    {"question": "what car do you like", "answer": "Audi"},
    {"question": "what engine does a4 use", "answer": "Ea888"},
]
'''
Task:t tell the user to buy
Input: None
Side Effect: prints a goobye message to terminal
Return: None
'''

def quit_app():
    print("thanks for studing come back soon or you'll fall")


'''
Task: Selects and Retriveves a Random elements in the flashcards list
Input: flashcards list
Side Effect:None
Return: the Flashcards (dictionary)
'''

def get_random_question(cards):
    random_card = random.choice(cards)
    return random_card

'''
Task: Display the questiion
Input: Question Crads
Side Effect: print the question test in the Terminal
Return:None
'''

def show_question():
    questiion =card["question"]
    print("Question:", questiion)



'''
Task: Display the answer
Input: Question cards
Side Effect: print the answer test in the Terminal
Return: None
'''

def quit_app():
    show_answer(card)
    answer =card["answer"]
    print("Answer", answer)


def main():
    while True:
      chosen_card = get_random_question(flashcard)
      show_question(chosen_card)

      user_chice = input("Enter Q to quit, type anything else to continue")
      if user_chice =="Q":
        quit_app()

      else:
         show_answer(chosen_card)

main()