class Allergies(object):
    def __init__(self, score):
        self.lst = []
        self.score = score
        self.binary_score = list('{0:08b}'.format(self.score))
        self.allergens = {'eggs': False,
                          'peanuts': False,
                          'shellfish': False,
                          'strawberries': False,
                          'tomatoes': False,
                          'chocolate': False,
                          'pollen': False,
                          'cats': False,
                          }

        self.analyze_score()

    def is_allergic_to(self, allergen):
        return self.allergens[allergen]

    def analyze_score(self):
        self.allergens['eggs'] = self.binary_score[-1]
        self.allergens['peanuts'] = self.binary_score[-2]
        self.allergens['shellfish'] = self.binary_score[-3]
        self.allergens['strawberries'] = self.binary_score[-4]
        self.allergens['tomatoes'] = self.binary_score[-5]
        self.allergens['chocolate'] = self.binary_score[-6]
        self.allergens['pollen'] = self.binary_score[-7]
        self.allergens['cats'] = self.binary_score[-8]

        for key in self.allergens:
            if int(self.allergens[key]) == 1:
                self.lst.append(key)
                self.allergens[key] = True
            else:
                self.allergens[key] = False
