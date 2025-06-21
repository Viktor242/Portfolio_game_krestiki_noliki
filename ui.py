"""
Пользовательский интерфейс для игры Крестики-нолики
"""

import tkinter as tk
from tkinter import messagebox
from config import *
from game_logic import GameLogic

class GameUI:
    """Класс для управления пользовательским интерфейсом"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.game_logic = GameLogic()
        self.buttons = []
        
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        """Настройка главного окна"""
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.resizable(WINDOW_RESIZABLE, WINDOW_RESIZABLE)
        self.center_window()
        
    def center_window(self):
        """Центрирует окно на экране"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_widgets(self):
        """Создает все виджеты интерфейса"""
        # Заголовок
        title_label = tk.Label(self.root, text=WINDOW_TITLE, 
                              font=FONTS['title'])
        title_label.grid(row=0, column=0, columnspan=BOARD_SIZE, 
                        pady=PADDING['title'])
        
        # Индикатор текущего игрока
        self.player_label = tk.Label(self.root, 
                                    text=MESSAGES['current_player'].format(self.game_logic.current_player),
                                    font=FONTS['player'])
        self.player_label.grid(row=1, column=0, columnspan=BOARD_SIZE, 
                              pady=PADDING['player'])
        
        # Игровое поле
        self.create_game_board()
        
        # Кнопка новой игры
        new_game_btn = tk.Button(self.root, text=MESSAGES['new_game'], 
                                font=FONTS['new_game'], command=self.new_game)
        new_game_btn.grid(row=BOARD_SIZE+2, column=0, columnspan=BOARD_SIZE, 
                         pady=PADDING['new_game'])
        
    def create_game_board(self):
        """Создает игровое поле"""
        for i in range(BOARD_SIZE):
            row = []
            for j in range(BOARD_SIZE):
                btn = tk.Button(self.root, text="", font=FONTS['button'], 
                               width=CELL_SIZE, height=2, bg=COLORS['background'],
                               command=lambda r=i, c=j: self.on_button_click(r, c))
                btn.grid(row=i+2, column=j, padx=PADDING['button'], 
                        pady=PADDING['button'])
                row.append(btn)
            self.buttons.append(row)
            
    def on_button_click(self, row, col):
        """Обработчик клика по кнопке"""
        if not self.game_logic.is_valid_move(row, col):
            return
            
        # Делаем ход
        move_result = self.game_logic.make_move(row, col)
        if not move_result:
            return
            
        # Обновляем интерфейс
        self.update_button(row, col)
        
        # Проверяем результат игры
        self.check_game_result()
        
        # Обновляем индикатор игрока
        if not self.game_logic.game_over:
            self.update_player_label()
            
    def update_button(self, row, col):
        """Обновляет текст кнопки"""
        self.buttons[row][col]['text'] = self.game_logic.board[row][col]
        
    def check_game_result(self):
        """Проверяет результат игры и показывает соответствующее сообщение"""
        if not self.game_logic.game_over:
            return
            
        if self.game_logic.winner:
            # Подсвечиваем выигрышную комбинацию
            self.highlight_winner()
            
            # Показываем сообщение о победе
            winner_message = (MESSAGES['x_wins'] if self.game_logic.winner == PLAYER_X 
                            else MESSAGES['o_wins'])
            messagebox.showinfo("Игра окончена", winner_message)
        else:
            # Ничья
            messagebox.showinfo("Игра окончена", MESSAGES['draw'])
            
    def highlight_winner(self):
        """Подсвечивает выигрышную комбинацию"""
        winning_positions = self.game_logic.get_winning_positions()
        for row, col in winning_positions:
            self.buttons[row][col].config(bg=COLORS['winner'])
            
    def update_player_label(self):
        """Обновляет индикатор текущего игрока"""
        self.player_label.config(text=MESSAGES['current_player'].format(self.game_logic.current_player))
        
    def new_game(self):
        """Начинает новую игру"""
        self.game_logic.reset_game()
        
        # Очищаем кнопки
        for row in self.buttons:
            for button in row:
                button.config(text="", bg=COLORS['background'])
                
        # Обновляем индикатор игрока
        self.update_player_label()
        
    def run(self):
        """Запускает приложение"""
        self.root.mainloop()
        
    def close(self):
        """Закрывает приложение"""
        self.root.destroy() 