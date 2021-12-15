#Python OOP

class Profile:
    '''
    Example:
    my = Profile("Suntipap")
    my.company = "ublgroup"
    my.hobby = ["Running","Python Programming","Game"]
    print(my.name)
    my.show_email()
    my.show_hobby()
    print("------------")

    friend = Profile("John")
    print(friend.name)
    friend.show_email()
    my.show_myart()
    '''


    def __init__(self,name):
        self.name = name
        self.company = ""
        self.hobby = []
        self.art = '''

            _._     _,-'""`-._
            (,-.`._,'(       |\`-/|
                `-.-' \ )-`( , o o)
                    `-    \`_`"'-
        
        '''

    def show_email(self):
        if self.company != "":
            print("{}@{}.com".format(self.name.lower(),self.company))
        else:
            print(f"{self.name.lower()}@gmail.com")

    def show_myart(self):
        print(self.art)

    def show_hobby(self):
        if len(self.hobby) != 0:
            print("-----my hobbies-------")
            for i,h in enumerate(self.hobby,start=1):
                print(i,h)
        else:
            print("No Hobby")


if __name__ == "__main__":
    my = Profile("Suntipap")
    my.company = "ublgroup"
    my.hobby = ["Running","Python Programming","Game"]
    print(my.name)
    my.show_email()
    my.show_hobby()
    print("------------")

    friend = Profile("Sudchaya")
    print(friend.name)
    friend.show_email()
    my.show_myart()
    #help(my)