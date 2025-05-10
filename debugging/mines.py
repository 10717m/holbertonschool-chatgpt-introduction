def check_win(self):
    for y in range(self.height):
        for x in range(self.width):
            if (y * self.width + x) not in self.mines and not self.revealed[y][x]:
                return False
    return True

def play(self):
    while True:
        self.print_board()
        if self.check_win():
            self.print_board(reveal=True)
            print("Congratulations! You've won the game.")
            break
        # ... rest of existing code ...
