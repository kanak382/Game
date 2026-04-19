import tkinter as tk
import random

# ---------------- BASE CLASS ---------------- #
class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None

    def make_choice(self):
        pass


# ---------------- HUMAN PLAYER ---------------- #
class HumanPlayer(Player):
    def make_choice(self, choice):
        valid_choices = ["Rock", "Paper", "Scissors"]

        if choice not in valid_choices:
            return False

        self.choice = choice
        return True


# ---------------- COMPUTER PLAYER ---------------- #
class ComputerPlayer(Player):
    def make_choice(self):
        self.choice = random.choice(["Rock", "Paper", "Scissors"])


# ---------------- GAME CLASS ---------------- #
class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("600x500")

        # -------- BACKGROUND IMAGE OPTION -------- #
     
        self.bg_image = tk.PhotoImage(file="bg.png")
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        


        # -------- PLAYERS -------- #
        self.human = HumanPlayer("You")
        self.computer = ComputerPlayer("Computer")

        # -------- SCORES -------- #
        self.human_score = 0
        self.computer_score = 0
        self.rounds_played = 0

        # -------- UI -------- #
        self.title = tk.Label(root, text="Rock Paper Scissors",
                              font=("Arial", 20, "bold"), bg="lightgrey")
        self.title.pack(pady=10)

        self.result_label = tk.Label(root, text="Start the Game!",
                                     font=("Arial", 14), bg="lightblue")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root,
            text="You: 0 | Computer: 0 | Rounds: 0",
            font=("Arial", 12), bg="lightblue")
        self.score_label.pack(pady=5)

        # -------- BUTTONS -------- #
        frame = tk.Frame(root, bg="lightblue")
        frame.pack(pady=20)

        for choice in ["Rock", "Paper", "Scissors"]:
            # btn = tk.Button(frame, text=choice, width=10, height=2,
            #                 command=lambda c=choice: self.play_round(c))
             btn = tk.Button(frame, text=choice, width=10, height=2,
                            command=self.play_round(choice))
             btn.pack(side="left", padx=10)

        # -------- RESET BUTTON -------- #
        self.reset_btn = tk.Button(root, text="Restart Game",
                                   command=self.reset_game)
        self.reset_btn.pack(pady=10)

    # -------- PLAY ROUND -------- #
    def play_round(self, user_choice):
        # Human choice
        valid = self.human.make_choice(user_choice)
        if not valid:
            self.result_label.config(text="Invalid Choice!")
            return

        # Computer choice
        self.computer.make_choice()

        # Determine winner
        result = self.determine_winner()

        # Update stats
        self.rounds_played += 1

        # if result == "Human":
        if result == "You":
            self.human_score += 1
        elif result == "Computer":
            self.computer_score += 1

        # Display result
        self.result_label.config(
            text=f"You chose {self.human.choice}\n"
                 f"Computer chose {self.computer.choice}\n"
                 f"{result if result=='Draw' else result + ' Wins!'}"
        )

        self.update_score()

    # -------- DETERMINE WINNER -------- #
    def determine_winner(self):
        h = self.human.choice
        c = self.computer.choice

        if h == c:
            return "Draw"

        if (h == "Rock" and c == "Scissors") or \
           (h == "Scissors" and c == "Paper") or \
           (h == "Paper" and c == "Rock"):
            # return "Human"
            return "You"

        return "Computer"

    # -------- UPDATE SCORE -------- #
    def update_score(self):
        self.score_label.config(
            text=f"You: {self.human_score} | "
                 f"Computer: {self.computer_score} | "
                 f"Rounds: {self.rounds_played}"
        )

    # -------- RESET GAME -------- #
    def reset_game(self):
        self.human_score = 0
        self.computer_score = 0
        self.rounds_played = 0

        self.result_label.config(text="Game Reset! Play Again.")
        self.update_score()

    # -------- START GAME -------- #
    def start_game(self):
        self.root.mainloop()


# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    game.start_game()