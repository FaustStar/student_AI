import random
information = []


class Student:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(50, 100)
        self.happiness = random.randint(40, 100)
        self.intelligence = random.randint(0, 100)
        self.edu_performance = random.randint(0, 100)
        self.work_ability = random.choice(['lazy', 'hard-working', 'ordinary'])

    def update(self, action):
        if action == '[\'entertain\']':
            self.health -= random.randint(4, 7)
            self.happiness += random.randint(8, 12)
            self.edu_performance -= random.randint(10, 15)
        elif action == '[\'study\']':
            self.health -= random.randint(4, 7)
            self.happiness -= random.randint(3, 6)
            self.edu_performance += random.randint(8, 13)
        else:
            self.health += random.randint(9, 15)
            self.happiness += random.randint(3, 7)
            self.edu_performance -= random.randint(4, 6)


class Controller:
    def __init__(self, step, *students):
        self.list = [*students]
        self.__step = step

    @property
    def step(self):
        return self.__step

    @step.setter
    def step(self, step):
        if step > 0:
            self.__step = step
        else:
            print('You can\'t use negative numbers!')

    def output(self, i):
        print(f'Their current condition: Health: {self.list[i].health},Happiness: {self.list[i].happiness},\
Education performance: {self.list[i].edu_performance}')

    def update(self):
        for i in range(len(self.list)):
            print(f'_______________________________________Information about a student - {self.list[i].name}__________________________________')
            count = 0
            while count < self.__step:
                print(f'{count + 1} month(s) later')
                count += 1

                if self.list[i].work_ability == 'lazy':
                    action = str(random.choices(['entertain', 'study', 'rest'], weights=[0.5, 0.1, 0.4]))
                elif self.list[i].work_ability == 'hard-working':
                    action = str(random.choices(['entertain', 'study', 'rest'], weights=[0.05, 0.7, 0.25]))
                else:
                    action = str(random.choices(['entertain', 'study', 'rest'], weights=[0.3, 0.4, 0.3]))
                self.list[i].update(action)

                if self.list[i].health <= 0:
                    print(f'Student {self.list[i].name} died...')
                    print('---------------------')
                    information.append(f'{self.list[i].name} died')
                    break
                elif self.list[i].edu_performance <= 0:
                    print(f'Student {self.list[i].name} was expelled...')
                    print('---------------------')
                    information.append(f'{self.list[i].name} was expelled')
                    break
                else:
                    print(f'{self.list[i].name} decided to {action}.')
                    if self.list[i].health >= 100:
                        self.list[i].health = 100
                        self.output(i)
                    elif self.list[i].happiness >= 100:
                        self.list[i].happiness = 100
                        self.output(i)
                    elif self.list[i].happiness <= 0:
                        self.list[i].happiness = 0
                        self.list[i].health -= 1
                        self.output(i)
                    elif self.list[i].edu_performance >= 100:
                        self.list[i].edu_performance = 100
                        self.output(i)
                    else:
                        self.output(i)
                print('---------------------')
            if count == self.__step:
                information.append(f'{self.list[i].name} graduated from University')


def input_name():
    return input('Input the name of the student: ')


def main():
    print('Welcome to The Student Game!')
    student1 = Student(input_name())
    print(f'Condition of {student1.name}: Health: {student1.health}, Happiness: {student1.happiness}, \
Intelligence: {student1.intelligence}, Education performance: {student1.edu_performance}, Feature: {student1.work_ability}')
    student2 = Student(input_name())
    print(f'Condition of {student2.name}: Health: {student2.health}, Happiness: {student2.happiness}, \
Intelligence: {student2.intelligence}, Education performance: {student2.edu_performance}, Feature: {student2.work_ability}')
    student3 = Student(input_name())
    print(f'Condition of {student3.name}: Health: {student3.health}, Happiness: {student3.happiness}, \
Intelligence: {student3.intelligence}, Education performance: {student3.edu_performance}, Feature: {student3.work_ability}')
    step = 48
    controller = Controller(step, student1, student2, student3)
    controller.update()
    print('_________________________________Results of the students_____________________________________')
    for i in range(len(information)):
        print(information[i])


main()
