import tkinter as tk
from tkinter import messagebox

def make_move(row, col):
    global current_player, game_over
    
    if game_over or buttons[row][col]['text'] != "":
        return
        
    buttons[row][col]['text'] = current_player
    
    # Проверяем победителя
    if check_winner():
        game_over = True
        highlight_winner()
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        return
        
    # Проверяем ничью
    if is_board_full():
        game_over = True
        messagebox.showinfo("Игра окончена", "Ничья!")
        return
        
    # Смена игрока
    current_player = "O" if current_player == "X" else "X"
    player_label.config(text=f"Ход игрока: {current_player}")

def check_winner():
    # Проверка строк
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
            
    # Проверка столбцов
    for i in range(3):
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
            
    # Проверка диагоналей
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
        
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
        
    return False

def highlight_winner():
    # Находим выигрышную комбинацию и подсвечиваем её
    for i in range(3):
        # Строки
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            for j in range(3):
                buttons[i][j].config(bg="#90EE90")
            return
            
    for i in range(3):
        # Столбцы
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            for j in range(3):
                buttons[j][i].config(bg="#90EE90")
            return
            
    # Диагонали
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="#90EE90")
        buttons[1][1].config(bg="#90EE90")
        buttons[2][2].config(bg="#90EE90")
        return
        
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="#90EE90")
        buttons[1][1].config(bg="#90EE90")
        buttons[2][0].config(bg="#90EE90")

def is_board_full():
    for row in buttons:
        for button in row:
            if button['text'] == "":
                return False
    return True

def new_game():
    global current_player, game_over
    current_player = "X"
    game_over = False
    player_label.config(text=f"Ход игрока: {current_player}")
    
    for row in buttons:
        for button in row:
            button.config(text="", bg="#f0f0f0")

# Создаем главное окно
root = tk.Tk()
root.title("Крестики-нолики")
root.geometry("295x500")
root.resizable(False, False)

# Игровые переменные
current_player = "X"
buttons = []
game_over = False

# Заголовок
title = tk.Label(root, text="Крестики-нолики", font=("Arial", 16, "bold"))
title.grid(row=0, column=0, columnspan=3, pady=10)

# Индикатор игрока
player_label = tk.Label(root, text=f"Ход игрока: {current_player}", font=("Arial", 12))
player_label.grid(row=1, column=0, columnspan=3, pady=5)

# Игровое поле
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(root, text="", font=("Arial", 20, "bold"), 
                       width=5, height=2, bg="#f0f0f0",
                       command=lambda r=i, c=j: make_move(r, c))
        btn.grid(row=i+2, column=j, padx=2, pady=2)
        row.append(btn)
    buttons.append(row)

# Кнопка новой игры
new_game_btn = tk.Button(root, text="Новая игра", font=("Arial", 12), command=new_game)
new_game_btn.grid(row=5, column=0, columnspan=3, pady=10)

# Запускаем игру
root.mainloop()