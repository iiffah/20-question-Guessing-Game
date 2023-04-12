class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
    
    def ask(self):
        while True:
            try:
                guess = input(self.prompt).strip().lower()
            except EOFError:
                print("Goodbye!")
                return None
            
            if guess == "quit":
                print("Goodbye!")
                return None
            
            if guess == self.answer:
                print("Correct!")
                return True
            else:
                print("Incorrect. Try again!")
        

class Game:
    def __init__(self):
        self.questions = [
            Question("Is the archery sport an Olympic sport?", "no"),
            Question("Is the archery sport played with a bow and arrow?", "yes"),
            Question("Is the archery sport played indoors?", "no"),
            Question("Is the archery sport played on a field?", "yes"),
            Question("Is the archery sport a team sport?", "no"),
            Question("Is the archery sport primarily played by men?", "no"),
            Question("Is the archery sport played with a target?", "yes"),
            Question("Is the archery sport played with a moving target?", "no"),
            Question("Is the archery sport played with a crossbow?", "no"),
            Question("Is the archery sport played with a recurve bow?", "no"),
            Question("Is the archery sport played with a longbow?", "yes"),
            Question("Is the archery sport played with a compound bow?", "no"),
            Question("Is the archery sport popular in Asia?", "no"),
            Question("Is the archery sport popular in Europe?", "yes"),
            Question("Is the archery sport popular in the United States?", "yes"),
            Question("Is the archery sport a contact sport?", "no"),
            Question("Is the archery sport played with a quiver?", "yes"),
            Question("Is the archery sport played with a finger tab?", "yes"),
            Question("Is the archery sport played with a release aid?", "no"),
            Question("Is the archery sport played with a sight?", "no")
        ]
        self.target_sport = "traditional archery"
    
    def play(self):
        print("Welcome to the Traditional Archery Sports Twenty Questions game!")
        print("You have 20 questions to guess the archery sport I'm thinking of.")
        print("If you need to quit, just type 'quit'.\n")
        
        num_guesses = 0
        for q in self.questions:
            num_guesses += 1
            print(f"Question {num_guesses}:")
            result = q.ask()
            
            if result is None:
                return
            
            if num_guesses == 20:
                print("Sorry, you've run out of questions!")
                return
            
            if result:
                break
        
        print(f"\nCongratulations! You guessed the archery sport: {self.target_sport}.")
        print("Thanks for playing!")

game = Game()
game.play()
