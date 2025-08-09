class Human:
    def __init__(self,name):
        self.name=name
        self.head = self.Head()

    def info(self):
        print('hello my name is ',self.name)

    class Head:
        def __init__(self):
            self.brain = self.Brain()

        def talk(self):
            print('talk')    

        class Brain:
            def think(self):
                print('think')

human = Human('prajwal')

human.info()
human.head.talk()
human.head.brain.think()