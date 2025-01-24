import numpy as np
from collections import deque
import heapq

# Lista rappresentativa della configurazione dell'ufficio per la definizione di "moe_current_office"
lst_current_office = [
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [" ", "M", " ", " ", "M", " ", " ", "M"],
    ["A", "M", " ", "A", "M", " ", "A", "M"],
    [" ", "M", " ", " ", "M", " ", " ", "M"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", "M", " ", " ", "M", " ", " ", "M"],
    ["A", "M", " ", "A", "M", " ", "A", "M"],
    [" ", "M", "C", " ", "M", "C", " ", "M"]
]

# Lista rappresentativa degli indici che identificano le posizioni di Ordirale all'interno della mappa
lst_index = [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20, 21, 22, 23],
    [24, 25, 26, 27, 28, 29, 30, 31],
    [32, 33, 34, 35, 36, 37, 38, 39],
    [40, 41, 42, 43, 44, 45, 46, 47],
    [48, 49, 50, 51, 52, 53, 54, 55],
    [56, 57, 58, 59, 60, 61, 62, 63]
]

def index_to_coordinates(index):
    """Converte un indice lineare in coordinate matrice (riga, colonna)."""
    return divmod(index, 8)

def is_valid_move(grid, row, col):
    """Verifica se una mossa è valida (all'interno della griglia e su una cella libera)."""
    return 0 <= row < 8 and 0 <= col < 8 and grid[row][col] == " "

def knight_moves():
    """Restituisce tutte le possibili mosse del cavallo in una scacchiera."""
    return [
        (-2, -1), (-2, 1), (2, -1), (2, 1),
        (-1, -2), (-1, 2), (1, -2), (1, 2)
    ]

def bfs_minimum_moves(grid, start, end):
    """Calcola il percorso minimo utilizzando BFS."""
    start_row, start_col = index_to_coordinates(start)
    end_row, end_col = index_to_coordinates(end)

    if not is_valid_move(grid, start_row, start_col) or not is_valid_move(grid, end_row, end_col):
        return np.nan

    if start == end:
        return 0

    visited = set()
    queue = deque([(start_row, start_col, 0)])  # (row, col, moves)

    while queue:
        row, col, moves = queue.popleft()

        if (row, col) == (end_row, end_col):
            return moves

        for dr, dc in knight_moves():
            new_row, new_col = row + dr, col + dc

            if (new_row, new_col) not in visited and is_valid_move(grid, new_row, new_col):
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, moves + 1))

    return np.inf

def move_current_office(int_starting_position, int_end_position):
    """
    Funzione che restituisce il numero di mosse necessarie a Ordirale per passare da int_starting_position
    a int_end_position all'interno di lst_current_office.
    """
    return bfs_minimum_moves(lst_current_office, int_starting_position, int_end_position)

def move_any_office(int_starting_position, int_end_position, lst_office_in):
    """
    Funzione che restituisce il numero di mosse necessarie a Ordirale per passare da int_starting_position
    a int_end_position all'interno di un ufficio qualsiasi rappresentato da lst_office_in.
    """
    return bfs_minimum_moves(lst_office_in, int_starting_position, int_end_position)

def heuristic(row, col, end_row, end_col):
    """Calcola la distanza di Manhattan come funzione euristica."""
    return abs(row - end_row) + abs(col - end_col)

def a_star_minimum_moves(grid, start, end):
    """Calcola il percorso minimo utilizzando l'algoritmo A*."""
    start_row, start_col = index_to_coordinates(start)
    end_row, end_col = index_to_coordinates(end)

    if not is_valid_move(grid, start_row, start_col) or not is_valid_move(grid, end_row, end_col):
        return np.nan

    if start == end:
        return 0

    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_row, start_col, 0))  # (priority, row, col, moves)

    while priority_queue:
        _, row, col, moves = heapq.heappop(priority_queue)

        if (row, col) == (end_row, end_col):
            return moves

        if (row, col) in visited:
            continue

        visited.add((row, col))

        for dr, dc in knight_moves():
            new_row, new_col = row + dr, col + dc

            if (new_row, new_col) not in visited and is_valid_move(grid, new_row, new_col):
                priority = moves + 1 + heuristic(new_row, new_col, end_row, end_col)
                heapq.heappush(priority_queue, (priority, new_row, new_col, moves + 1))

    return np.inf

def dijkstra_minimum_moves(grid, start, end):
    """Calcola il percorso minimo utilizzando l'algoritmo di Dijkstra."""
    start_row, start_col = index_to_coordinates(start)
    end_row, end_col = index_to_coordinates(end)

    if not is_valid_move(grid, start_row, start_col) or not is_valid_move(grid, end_row, end_col):
        return np.nan

    if start == end:
        return 0

    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_row, start_col))  # (cost, row, col)
    distances = { (start_row, start_col): 0 }

    while priority_queue:
        current_cost, row, col = heapq.heappop(priority_queue)

        if (row, col) == (end_row, end_col):
            return current_cost

        if (row, col) in visited:
            continue

        visited.add((row, col))

        for dr, dc in knight_moves():
            new_row, new_col = row + dr, col + dc
            new_cost = current_cost + 1

            if (new_row, new_col) not in visited and is_valid_move(grid, new_row, new_col):
                if (new_row, new_col) not in distances or new_cost < distances[(new_row, new_col)]:
                    distances[(new_row, new_col)] = new_cost
                    heapq.heappush(priority_queue, (new_cost, new_row, new_col))

    return np.inf

# Esempio di utilizzo
if __name__ == "__main__":
    start = 7  # Esempio di posizione iniziale
    end = 56   # Esempio di posizione finale

    print("Minimo numero di mosse (ufficio corrente, BFS):", move_current_office(start, end))
    print("Minimo numero di mosse (ufficio corrente, A*):", a_star_minimum_moves(lst_current_office, start, end))
    print("Minimo numero di mosse (ufficio corrente, Dijkstra):", dijkstra_minimum_moves(lst_current_office, start, end))

    # Test con un ufficio personalizzato
    custom_office = [
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "]
    ]
    print("Minimo numero di mosse (ufficio personalizzato, BFS):", move_any_office(start, end, custom_office))
    print("Minimo numero di mosse (ufficio personalizzato, A*):", a_star_minimum_moves(custom_office, start, end))
    print("Minimo numero di mosse (ufficio personalizzato, Dijkstra):", dijkstra_minimum_moves(custom_office, start, end))
