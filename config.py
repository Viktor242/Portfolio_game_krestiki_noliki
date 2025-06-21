"""
Конфигурация для игры Крестики-нолики
"""

# Настройки окна
WINDOW_TITLE = "Крестики-нолики"
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 350
WINDOW_RESIZABLE = False

# Настройки игрового поля
BOARD_SIZE = 3
CELL_SIZE = 5  # ширина и высота кнопки в символах

# Цвета
COLORS = {
    'background': '#f0f0f0',
    'winner': '#90EE90',  # светло-зеленый
    'button_hover': '#e0e0e0',
    'text': '#000000'
}

# Шрифты
FONTS = {
    'title': ('Arial', 16, 'bold'),
    'player': ('Arial', 12),
    'button': ('Arial', 20, 'bold'),
    'new_game': ('Arial', 12)
}

# Игровые символы
PLAYER_X = "X"
PLAYER_O = "O"

# Сообщения
MESSAGES = {
    'x_wins': "Игрок X победил!",
    'o_wins': "Игрок O победил!",
    'draw': "Ничья!",
    'new_game': "Новая игра",
    'current_player': "Ход игрока: {}"
}

# Настройки отступов
PADDING = {
    'title': 10,
    'player': 5,
    'button': 2,
    'new_game': 10
} 