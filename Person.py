class Person:

    def __init__(self, h, l, f, s):
        self.handle = str(h)
        self.link = str(l)
        self.first_condition = f
        self.second_condition = s
    
    def display(self):
        print("Handle: " + self.handle)
        print("Link: " + self.link)
        print("First condition: " + str(self.first_condition))
        print("Second condition: " + str(self.second_condition))
    
    def to_string(self):
        return("Handle: " + self.handle + "\n" + "Link: " + self.link + "\n" + "FIRST_CONDITION: " + str(self.first_condition) + "\n" + "SECOND_CONDITION: " + str(self.second_condition) + "\n")