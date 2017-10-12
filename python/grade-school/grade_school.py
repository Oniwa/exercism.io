class School(object):
    def __init__(self, name):
        self.grades = {1: [],
                       2: [],
                       3: [],
                       4: [],
                       5: [],
                       6: [],
                       7: [],
                       8: [],
                       9: [],
                       }

    def add(self, name, grade_number):
        self.grades[grade_number].append(name)

    def grade(self, grade_number):
        return self.grades[grade_number]

    def sort(self):
        sorted_list = []
        for _ in range(1, 10):
            if self.grades[_]:
                sorted_list.append((_, tuple(sorted(self.grades[_]))))

        return sorted_list
