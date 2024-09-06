class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word+' ( '+self.meaning+')'
flash = []
print("Welcome to flashcard application")

while True:
    word = input("Enter the word: ")
    meaning = input(" Meaning of the word: ")
    flash.append(flashcard(word,meaning))
    option = int(input("Enter 1 if you want to stop, otherwise enter 0:\n"))

    if(option):
        break

for i in flash:
    print(">",i)