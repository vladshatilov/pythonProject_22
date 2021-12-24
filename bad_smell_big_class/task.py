class Obj:
    def defense(self):
        pass

    def move(self):
        pass

    def on_fire(self):
        pass


class Warrior(Obj):
    def move(self):
        pass

    def attack(self):
        pass


class Healer(Warrior):
    def heal(self):
        pass


class Tree(Obj):
    def tree_defense(self):
        pass


class Trap(Obj):
    def trap_attack(self):
        print("It's a trap!")
