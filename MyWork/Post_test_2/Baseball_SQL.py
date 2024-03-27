import sqlite3
from dataclasses import dataclass

conn = sqlite3.connect('Baseball.sqlite')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Player';")
result = c.fetchall()
conn.close()


# drop table if exists Player;

# CREATE TABLE IF NOT EXISTS Player (playerID INTEGER PRIMARY KEY not null, batOrder integer, firstName text not null, lastName text not null, position text not null, atBats integer, hits integer);

# insert into Player values
#         (1, 1, "Tommy", "La Stella", "3B", 1316, 360),
#         (2, 2, "Mike", "Yastrzemski", "RF", 563, 168),
#         (3, 3, "Donovan", "Solano", "2B", 1473, 407),
#         (4, 4, "Buster", "Posey", "C", 4575, 1380),
#         (5, 5, "Brandon", "Belt", "1B", 3811, 1003),
#         (6, 6, "Brandon", "Crawford", "SS", 4402, 1099),
#         (7, 7, "Alex", "Dickerson", "LF", 586, 160),
#         (8, 8, "Austin", "Slater", "CF", 569, 147),
#         (9, 9, "Kevin", "Gausman", "P", 56, 2);


@dataclass
class Player:
    playerID: int
    batOrder: int
    firstName: str = ''
    lastName: str = ''
    position: str = ''
    atBats: int = 0
    hits: int = 0

    @property
    def fullName(self):
        return f'{self.firstName} {self.lastName}'

    @property
    def battingAvg(self) -> float:
        try:
            avg = self.hits / self.atBats
            return avg
        except ZeroDivisionError:
            return 0.0

    def __str__(self):
        return f"{self.playerID}{self.batOrder}{self.fullName:40}{self.position:6}{self.atBats:>6d}{self.hits:>8d}{self.avg:>10.3f}"


@dataclass
class Lineup:
    __player_list: list

    @property
    def count(self):
        return len(self.__player_list)

    def addPlayer(self, player: Player):
        self.__player_list.append(player)

    def removePlayer(self, number):
        self.__player_list.pop(number-1)

    def __iter__(self):
        for player in self.__player_list:
            yield player


def title():
    print("=" * 75)
    print("\t\t\t\t\tBaseball Team Manager")

    print("MENU OPTIONS")
    print("1 - Display lineup\n2 - Add player\n3 - Remove player")
    print("4 - Update batting order\n5 - Update player data\n6 - Exit\n")
    position = "positions\nC, 1B, 2B, 3b, ss, lf, cf, rf, f"
    print(position.upper())
    print("=" * 75)


def get_pos():
    pos_list = ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'F']
    while True:
        pos = input("Position: ").upper()
        if pos not in pos_list:
            print(f"Invalid position.\n Valid positions: {pos_list}")
        else:
            return pos


def get_at_bats():
    while True:
        try:
            at_bats = int(input("At Bats: "))
        except ValueError:
            print("Invalid integer.")
            continue

        if at_bats < 0 or at_bats > 5000:
            print("Invalid entry.")
        else:
            return at_bats


def get_hits(at_bats):
    while True:
        try:
            hits = int(input("Hits: "))
        except ValueError:
            print("Invalid integer.")
            continue

        if hits < 0 or hits > at_bats:
            print("Invalid entry.")
        else:
            return hits


def add():
    Lineup.add_player()


def player_list():
    lineup = Lineup()
    print(f"{'':3}{'Player':40}{'POS':6}{'AB':>6}{'H':>8}{'AVG':>10}")
    print("-" * 75)
    for player in lineup:
        print(player)


def main():
    title()
    print("")
    menu = 0
    while menu != 6:
        menu = int(input("\nMenu option: "))
        if menu == 1:
            # Display Lineup
            player_list()
        elif menu == 2:
            # Add Player
            add()
        elif menu == 3:
            # Remove Player
            num = input("Number of player to remove.")
            Lineup.removePlayer(num)
        elif menu == 4:
            # Update batting order
            pass
        elif menu == 5:
            # Update player data
            pass
        elif menu == 6:
            # Exit
            break
        else:
            print("Invalid entry, please try again.")
            menu = int(input("\nMenu option: "))
    print("Bye!")


if __name__ == "__main__":
    main()
