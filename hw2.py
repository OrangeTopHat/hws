import random, time


class Cat:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.hunger = 100
        self.happiness = 100
        self.dead = False

    def isalive(self):
        if self.energy < 0 or self.energy == 0:
            self.dead = True
            print("Котик помер від недостачі сну.")
            return self.dead

        elif self.happiness < 0 or self.happiness == 0:
            self.dead = True
            print("Котик помер від депресії.")
            return self.dead

        elif self.hunger < 0 or self.hunger  == 0:
            self.dead = True
            print("Котик помер від голоду.")
            return self.dead

    def live_a_day(self):
        actions = [self.eat, self.sleep, self.play,self.nothing]
        self.isalive()
        if self.dead == True:
            print(f"{self.name} помер...")
            self.status()
            breakpoint() # Я не знав як зупинити цикл тому що break не працював тому я використав breakpoint
        else:
            for i in range(1):
                random.choice(actions)()
            self.status()

    def eat(self):
        self.hunger = 100
        self.energy += 10
        self.happiness += 5
        print(f"{self.name} поснідав!")


    def sleep(self):
        self.energy = 100
        self.hunger -= 10
        self.happiness -= 20
        print(f"{self.name}, виспався й готовий на все!")

    def play(self):
        self.energy -= 50
        self.hunger -= 50
        self.happiness += 15
        print(f"{self.name} грається, він дуже кумедний!")

    def nothing(self):
        self.energy -= 20
        self.hunger -= 20
        self.happiness += 20
        print(f"{self.name} прогулявся по дому!")


    def status(self):
        print(f"{self.name} - Енергія: {self.energy}, Голод: {self.hunger}, Щастя: {self.happiness}")





cat = Cat("Димок")
while True:
    time.sleep(1)
    cat.live_a_day()
