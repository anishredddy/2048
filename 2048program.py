import tkinter as tk
from logic import *

class Game2048(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("2048")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.game_board = tk.Canvas(self, width=400, height=400, bg="#bbada0")
        self.game_board.grid(row=0, column=0, padx=10, pady=10)

        #self.score_label = tk.Label(self, text="Score: 0", font=("Arial", 20))
        #self.score_label.grid(row=1, column=0)

        self.new_game_button = tk.Button(self, text="New Game", command=self.new_game)
        self.new_game_button.grid(row=2, column=0)

        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Up>", self.move_up)
        self.master.bind("<Down>", self.move_down)

        self.new_game()

    def new_game(self):
        self.game_board.delete("all")
        self.mat = start_game()
        self.draw_board()

        #self.score = 0
        #self.score_label.config(text="Score: 0")

    def draw_board(self):
        for i in range(4):
            for j in range(4):
                x0, y0 = j * 100, i * 100
                x1, y1 = x0 + 100, y0 + 100
                tile_color = {
                    0: "#cdc1b4",
                    2: "#eee4da",
                    4: "#ede0c8",
                    8: "#f2b179",
                    16: "#f59563",
                    32: "#f67c5f",
                    64: "#f65e3b",
                    128: "#edcf72",
                    256: "#edcc61",
                    512: "#edc850",
                    1024: "#edc53f",
                    2048: "#edc22e",
                }
                value = self.mat[i][j]
                color = tile_color.get(value, "#ff0000")
                self.game_board.create_rectangle(x0, y0, x1, y1, fill=color, outline=color)
                if value:
                    self.game_board.create_text(x0 + 50, y0 + 50, text=str(value), font=("Arial", 30, "bold"))

    def move_left(self, event):
        self.mat = move_left(self.mat)
        self.update_game()

    def move_right(self, event):
        self.mat = move_right(self.mat)
        self.update_game()

    def move_up(self, event):
        self.mat = move_up(self.mat)
        self.update_game()

    def move_down(self, event):
        self.mat = move_down(self.mat)
        self.update_game()

    def game_over(self):
        self.game_board.create_rectangle(0, 0, 400, 400, fill="gray", stipple="gray12")
        self.game_board.create_text(200, 150, text="Game Over", font=("Arial", 36, "bold"), fill="white")
    
    def game_won(self):
        self.game_board.create_rectangle(0, 0, 400, 400, fill="gray", stipple="gray12")
        self.game_board.create_text(200, 150, text="You Won!", font=("Arial", 36, "bold"), fill="white")

    
    '''
    
	def get_current_score(mat):
        # calculate the current score
        score=0
        for i in range(4):
            for j in range(4):
                score =score+mat[i][j]
        return score
	'''	


    def update_game(self):
        game_state=checking(self.mat)
        if(game_state==0):
            self.game_over()
            return
        elif(game_state==2):
            self.game_won()
            return
        

		
        
        else:
            self.draw_board()
            #self.score=get_current_score(self.mat)
            #self.score_label.config(text="Score: {}".format(self.score))
            self.mat=generate_new_mat(self.mat)
        
        
    
	



root = tk.Tk()
game = Game2048(root)
game.mainloop()