from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic
fire = Spell('Fire', 10, 100, 'black')
thunder = Spell('Thunder', 10, 100, 'black')
blizzard = Spell('Blizzard', 10, 100, 'black')
meteor = Spell('Meteor', 20, 200, 'black')
quake = Spell('Quake', 12, 120, 'black')

# Create White Magic
cure = Spell('Cure', 12, 120, 'white')
cura = Spell('Cura', 18, 200, 'white')

# Create some Items
potion = Item('Potion', 'potion', 'Heals 50 HP', 50)
hipotion = Item('Hi-Potion', 'potion', 'Heals 100 HP', 100)
superpotion = Item('Super Potion', 'potion', 'Heals 500 HP', 500)
elixer = Item('Elixer', 'elixer', 'Fully restores HP/MP of one party member', 9999)
hielixer = Item('MegaElixer', 'elixer', 'Fully restores party\'s HP/MP', 9999)

grenade = Item('Grenade', 'attack', 'Deals 500 damage', 500)

player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura])
emeny = Person(1200,65, 45, 25, [])

running = True

print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACKS!' + bcolors.ENDC)

while running:
    print('============================')
    player.choose_action()
    choice = input('Choose action:')
    index = int(choice) - 1
    print('You choose ' + choice)

    #choose attack
    if index == 0:
        damage = player.generate_damage()
        emeny.take_damage(damage)
        print('You attack for ' + str(damage) + ' points of damage. Emeny HP:' + str(emeny.get_hp()))
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input('Choose magic:')) - 1

        spell = player.magic[magic_choice]
        magic_damage = spell.generate_damage()

        current_mp = player.get_mp()

        #not enough mp, so choose action again
        if current_mp <= spell.cost:
            print(bcolors.FAIL + '\n Not enough Mp. \n', bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == 'white':
            player.heal(magic_damage)
            print(bcolors.OKBLUE + spell.name + ' heals for', str(magic_damage) + ' HP', bcolors.ENDC)
        elif spell.type == 'black':
            emeny.take_damage(magic_damage)
            print(bcolors.OKGREEN + spell.name + 'deals ' + str(magic_damage) + ' points of damage. Emeny HP:' + str(emeny.get_hp()), bcolors.ENDC)
    
    emeny.choice = 1
    emeny_damage = emeny.generate_damage()
    player.take_damage(emeny_damage)
    print('Emeny attack for', emeny_damage, 'points of damage. Player HP:', player.get_hp())

    print('============================')
    print(bcolors.FAIL + 'Emeny HP:', str(emeny.get_hp()) + ' /', str(emeny.get_max_hp()), bcolors.ENDC, '\n')
    print(bcolors.OKGREEN + 'Your HP:', str(player.get_hp()) + ' /', str(player.get_max_hp()), bcolors.ENDC)
    print(bcolors.OKBLUE + 'Your MP:', str(player.get_mp()) + ' /', str(player.get_max_mp()), bcolors.ENDC)
    
    if player.get_hp() <= 0:
        print(bcolors.FAIL + 'The Emeny wins!' + bcolors.ENDC)
        running = False
    elif emeny.get_hp() <= 0:
        print(bcolors.OKGREEN + 'You win!' + bcolors.ENDC)
        running = False
    