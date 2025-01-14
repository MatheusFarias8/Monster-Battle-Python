from time import sleep
from random import randint
from os import system, name

def main():

    # MENU
    bar()
    print('         WIN THE BATTLE AGAINST THE ORC!!!')
    bar()

    # USERNAME
    user = input('Username: ')
    player = Hero(name=user, health=100)

    # ORC
    orc = Monster('Orc', 100)

    while True:
        # CHECK
        if orc.health <= 0:
            clear()
            bar()
            print('YOU WON!!!\nCONGRATULATIONS, YOU ARE A TRUE WARRIOR!!!')
            print('Thanks for playing!!!\nBy: Matheus F.')
            bar()
            sleep(3)
            break
        if player.health <= 0:
            clear()
            bar()
            print('GAME OVER!!!\nF')
            print('Thanks for playing!!!\nBy: Matheus F.')
            bar()
            sleep(3)
            break

        # OPTIONS
        clear()
        bar()
        print('1 - ATTACK\n2 - POTION\n3 - EXIT')
        bar()
        health_bar(player.name, orc.name, player.health, orc.health)
        print()
        number = input(('Choice: '))

        # MOVES
        if number == '1':
            player.attack(randint(1, 20), monster=orc)

        if number == '2':
            player.potion(heal=randint(10, 20))

        if number == '3':
            break

        orc.attack(randint(0, 25), hero=player)


def clear():

    # CLEANING THE TERMINAL
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def bar():

    # PRINTING THE BAR
    print('-='*25)

def health_bar(player, monster, player_hp, monster_hp):

    #SHOWING THE HEALTH BAR
    print(player)
    print("\033[32m>\033[0m" * player_hp)
    print()
    print(monster)
    print('\033[31m>\033[0m' * monster_hp)

class Hero:

    # DUNDER
    def __init__(self, name, health):
        self.name = name
        self.health = health

    # METHODS
    def attack(self, damage, monster):
        clear()
        bar()
        print(f'{self.name} attack {monster}')
        print(f'The {monster} took {damage} damage!!!')
        monster.get_damage(damage)
        if monster.health < 1:
            print(f'The {monster} now has 0 HP!!!')
        else:
            print(f'The {monster} now has {monster.health} HP!!!')
        bar()
        sleep(4)

    def potion(self, heal):
        clear()
        bar()
        print(f'Potion used!!!\n+{heal} HP!!')
        self.health += heal
        print(f'You now have {self.health} HP')
        bar()
        sleep(4)

    def get_damage(self, amount):
        self.health -= amount
        if self.health < 1:
            print(f'You now have 0 HP!!!')
        else:
            print(f'You now have {self.health} HP!!!')

class Monster:

    # DUNDER
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def __str__(self):
        return (self.name)

    # METHODS
    def get_damage(self, amount):
        self.health -= amount

    def attack(self, damage, hero):
        clear()
        bar()
        print(f'{self.name} attacked you!!!')
        print(f'You took {damage} damage!!!')
        hero.get_damage(damage)
        bar()
        sleep(4)


if __name__ == "__main__":
    main()
