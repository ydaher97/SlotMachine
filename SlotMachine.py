import  random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 4,
    "B": 5,
    "C": 6,
    "D": 7
}

symbol_value = {
    "A" : 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_win(columns,lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]* bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols , symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
#random card
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("what would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount greater than zero")
        else:
            print("please anter number")
    return amount

def num_of_lines():
    while True:
        lines = input("enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print("enter valid number")
        else:
            print("please enter number")
    return lines
def get_bet():
    while True:
        amount = input("how much would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <=amount <= MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("please enter number")
    return amount




def spin(balance):
    lines = num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("your bet is more than your balance")

        else:
            break

    print(f"you are betting ${bet} on {lines} lines. Total bet is : ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_line = check_win(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}")
    print(f"you won on lines:", *winning_line)
    return  winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        answer = input("press enter to play(enter q to quit)")
        if answer == 'q':
            break
        balance += spin(balance)

    print(f"you left with ${balance}")
main()