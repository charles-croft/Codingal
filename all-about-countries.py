class Australia():
    def capital(self):
        print("Canberra is the capital of Australian Capital Territory and Australia")
    def language(self):
        print("English is the official language of Australia.")
    def type(self):
        print("Australia is a developed country.")
class UK():
    def capital(self):
        print("London is the capital of the U.K.")
    def language(self):
        print("English is the official language of the U.K.")
    def type(self):
        print("England is a developed country.")
aus = Australia()
eng = UK()
for country in (aus, eng):
    country.capital()
    country.language()
    country.type()