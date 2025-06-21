import pytest
import sys
import os

# Добавляем путь к основному модулю
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import TicTacToe

class TestTicTacToe:
    """Тесты для игры Крестики-нолики"""
    
    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.game = TicTacToe()
        # Не запускаем mainloop для тестов
        self.game.root.withdraw()
        
    def teardown_method(self):
        """Очистка после каждого теста"""
        self.game.root.destroy()
        
    def test_initial_state(self):
        """Тест начального состояния игры"""
        assert self.game.current_player == "X"
        assert self.game.game_over == False
        assert len(self.game.buttons) == 3
        assert len(self.game.buttons[0]) == 3
        
        # Проверяем, что все кнопки пустые
        for row in self.game.buttons:
            for button in row:
                assert button['text'] == ""
                
    def test_player_switch(self):
        """Тест смены игрока"""
        # Первый ход
        self.game.on_click(0, 0)
        assert self.game.current_player == "O"
        
        # Второй ход
        self.game.on_click(0, 1)
        assert self.game.current_player == "X"
        
    def test_invalid_move(self):
        """Тест недопустимого хода"""
        # Заполняем клетку
        self.game.buttons[0][0]['text'] = "X"
        
        # Пытаемся сделать ход в занятую клетку
        initial_player = self.game.current_player
        self.game.on_click(0, 0)
        
        # Игрок не должен измениться
        assert self.game.current_player == initial_player
        
    def test_horizontal_win(self):
        """Тест победы по горизонтали"""
        # X | X | X
        #   |   |  
        #   |   |  
        self.game.on_click(0, 0)  # X
        self.game.on_click(1, 0)  # O
        self.game.on_click(0, 1)  # X
        self.game.on_click(1, 1)  # O
        self.game.on_click(0, 2)  # X - победа!
        
        assert self.game.game_over == True
        
    def test_vertical_win(self):
        """Тест победы по вертикали"""
        # X |   |  
        # X |   |  
        # X |   |  
        self.game.on_click(0, 0)  # X
        self.game.on_click(0, 1)  # O
        self.game.on_click(1, 0)  # X
        self.game.on_click(1, 1)  # O
        self.game.on_click(2, 0)  # X - победа!
        
        assert self.game.game_over == True
        
    def test_diagonal_win(self):
        """Тест победы по диагонали"""
        # X |   |  
        #   | X |  
        #   |   | X
        self.game.on_click(0, 0)  # X
        self.game.on_click(0, 1)  # O
        self.game.on_click(1, 1)  # X
        self.game.on_click(1, 0)  # O
        self.game.on_click(2, 2)  # X - победа!
        
        assert self.game.game_over == True
        
    def test_draw(self):
        """Тест ничьей"""
        # X | O | X
        # X | O | O
        # O | X | X
        moves = [
            (0, 0), (0, 1), (0, 2),  # Первая строка
            (1, 0), (1, 1), (1, 2),  # Вторая строка
            (2, 0), (2, 1), (2, 2)   # Третья строка
        ]
        
        for row, col in moves:
            self.game.on_click(row, col)
            
        assert self.game.game_over == True
        
    def test_new_game(self):
        """Тест новой игры"""
        # Делаем несколько ходов
        self.game.on_click(0, 0)
        self.game.on_click(0, 1)
        
        # Начинаем новую игру
        self.game.new_game()
        
        # Проверяем сброс состояния
        assert self.game.current_player == "X"
        assert self.game.game_over == False
        
        # Проверяем, что все кнопки очищены
        for row in self.game.buttons:
            for button in row:
                assert button['text'] == ""
                assert button['bg'] == "#f0f0f0"
                
    def test_is_board_full(self):
        """Тест проверки заполненности поля"""
        # Пустое поле
        assert self.game.is_board_full() == False
        
        # Заполняем поле
        for i in range(3):
            for j in range(3):
                self.game.buttons[i][j]['text'] = "X"
                
        assert self.game.is_board_full() == True
        
    def test_game_over_prevents_moves(self):
        """Тест, что после окончания игры нельзя делать ходы"""
        # Создаем победу
        self.game.on_click(0, 0)  # X
        self.game.on_click(1, 0)  # O
        self.game.on_click(0, 1)  # X
        self.game.on_click(1, 1)  # O
        self.game.on_click(0, 2)  # X - победа!
        
        # Пытаемся сделать ход после победы
        initial_player = self.game.current_player
        self.game.on_click(2, 2)
        
        # Игрок не должен измениться
        assert self.game.current_player == initial_player

if __name__ == "__main__":
    pytest.main([__file__]) 