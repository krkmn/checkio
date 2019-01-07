VOWELS = "aeiou"

import time
class Chat:

    def __init__(self):
          self.objects = []

    def show_human_dialogue(self):
        dialogue_lines = []
        for being in self.objects:
            for line in being.dialogue:
                dialogue_lines.append((being.name, line[0], line[1]))

        dialogue_lines = sorted(dialogue_lines, key = lambda x: x[2], reverse=False)

        whole_dialogue = f""
        for line in dialogue_lines:
            whole_dialogue += f"{line[0]} said: {line[1]}\n"

        print(whole_dialogue)
        return whole_dialogue.strip()

    def show_robot_dialogue(self):

        dialogue_lines = []

        for being in self.objects:

            for line in being.dialogue:
                discourse = ''
                for char in line[0]:

                    if char.lower() in VOWELS:
                        discourse += '0'
                    else:
                        discourse += '1'
                dialogue_lines.append((being.name, discourse, line[1]))


        dialogue_lines = sorted(dialogue_lines, key = lambda x: x[2], reverse=False)

        whole_dialogue = f""
        for line in dialogue_lines:
            whole_dialogue += f"{line[0]} said: {line[1]}\n"

        # whole_dialogue = f"{self.human.name} said: {human_dialogue}\n{self.robot.name} said: {robot_dialogue}"
        return whole_dialogue.strip()


    def connect_human(self, human):
        self.objects.append(human)

    def connect_robot(self, robot):
        self.objects.append(robot)


class Human:
    def __init__(self, name):
        self.name = name
        self.dialogue = []

    def send(self, dialogue):
        time.sleep(0.001)
        self.dialogue.append((dialogue, time.time()))

class Robot:
    def __init__(self, name):
        self.name = name
        self.dialogue = []

    def send(self, dialogue):
        time.sleep(0.001)
        self.dialogue.append((dialogue,time.time()))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

    print("Coding complete? Let's try tests!")