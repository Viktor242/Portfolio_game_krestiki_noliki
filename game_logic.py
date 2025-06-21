"""
Логика игры Крестики-нолики
"""

from config import BOARD_SIZE, PLAYER_X, PLAYER_O

class GameLogic:
    """Класс для управления логикой игры"""
    
    def __init__(self):
        self.board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.current_player = PLAYER_X
        self.game_over = False
        self.winner = None
        
    def make_move(self, row, col):
        """
        Делает ход в указанную позицию
        
        Args:
            row (int): Строка (0-2)
            col (int): Столбец (0-2)
            
        Returns:
            bool: True если ход был сделан, False если позиция занята
        """
        if self.game_over or self.board[row][col] != '':
            return False
            
        self.board[row][col] = self.current_player
        
        # Проверяем победителя
        if self.check_winner(row, col):
            self.game_over = True
            self.winner = self.current_player
            return True
            
        # Проверяем ничью
        if self.is_board_full():
            self.game_over = True
            self.winner = None
            return True
            
        # Смена игрока
        self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X
        return True
        
    def check_winner(self, last_row, last_col):
        """
        Проверяет, есть ли победитель после последнего хода
        
        Args:
            last_row (int): Строка последнего хода
            last_col (int): Столбец последнего хода
            
        Returns:
            bool: True если есть победитель
        """
        player = self.board[last_row][last_col]
        
        # Проверка строки
        if all(self.board[last_row][col] == player for col in range(BOARD_SIZE)):
            return True
            
        # Проверка столбца
        if all(self.board[row][last_col] == player for row in range(BOARD_SIZE)):
            return True
            
        # Проверка главной диагонали
        if last_row == last_col:
            if all(self.board[i][i] == player for i in range(BOARD_SIZE)):
                return True
                
        # Проверка побочной диагонали
        if last_row + last_col == BOARD_SIZE - 1:
            if all(self.board[i][BOARD_SIZE-1-i] == player for i in range(BOARD_SIZE)):
                return True
                
        return False
        
    def get_winning_positions(self):
        """
        Возвращает позиции выигрышной комбинации
        
        Returns:
            list: Список кортежей (row, col) выигрышных позиций
        """
        if not self.game_over or self.winner is None:
            return []
            
        player = self.winner
        winning_positions = []
        
        # Проверяем строки
        for row in range(BOARD_SIZE):
            if all(self.board[row][col] == player for col in range(BOARD_SIZE)):
                return [(row, col) for col in range(BOARD_SIZE)]
                
        # Проверяем столбцы
        for col in range(BOARD_SIZE):
            if all(self.board[row][col] == player for row in range(BOARD_SIZE)):
                return [(row, col) for row in range(BOARD_SIZE)]
                
        # Проверяем главную диагональ
        if all(self.board[i][i] == player for i in range(BOARD_SIZE)):
            return [(i, i) for i in range(BOARD_SIZE)]
            
        # Проверяем побочную диагональ
        if all(self.board[i][BOARD_SIZE-1-i] == player for i in range(BOARD_SIZE)):
            return [(i, BOARD_SIZE-1-i) for i in range(BOARD_SIZE)]
            
        return []
        
    def is_board_full(self):
        """
        Проверяет, заполнено ли поле
        
        Returns:
            bool: True если поле заполнено
        """
        return all(self.board[row][col] != '' 
                  for row in range(BOARD_SIZE) 
                  for col in range(BOARD_SIZE))
                  
    def reset_game(self):
        """Сбрасывает игру в начальное состояние"""
        self.board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.current_player = PLAYER_X
        self.game_over = False
        self.winner = None
        
    def get_board_state(self):
        """
        Возвращает текущее состояние поля
        
        Returns:
            list: Копия игрового поля
        """
        return [row[:] for row in self.board]
        
    def is_valid_move(self, row, col):
        """
        Проверяет, является ли ход допустимым
        
        Args:
            row (int): Строка
            col (int): Столбец
            
        Returns:
            bool: True если ход допустим
        """
        return (0 <= row < BOARD_SIZE and 
                0 <= col < BOARD_SIZE and 
                self.board[row][col] == '' and 
                not self.game_over)
                
    def get_game_status(self):
        """
        Возвращает статус игры
        
        Returns:
            dict: Словарь с информацией о статусе игры
        """
        return {
            'current_player': self.current_player,
            'game_over': self.game_over,
            'winner': self.winner,
            'board': self.get_board_state()
        } 