class Text:

    def __init__(self):
        self.text = ''
        self.font = ''
    
    def write(self, text):
        self.text += text

    def set_font(self, font):
        self.font = font
        
    def show(self):
        return f"[{self.font}]{self.text}[{self.font}]" if self.font else \
               f"{self.text}"
        pass

    def restore(self, restore):
        self.text = restore[0]
        self.font = restore[1]


class SavedText:

    def __init__(self):
        self.text_hist = []
        self.font_hist = []
    
    def save_text(self, text):
        self.text_hist.append(text.text)
        self.font_hist.append(text.font)
    
    def get_version(self, version):
        return self.text_hist[version] , self.font_hist[version]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()
    
    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
    
    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")
