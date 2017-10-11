class Garden(object):
    def __init__(self, rows, **students):
        self.rows = rows.split('\n')
        self.number_of_children = int(len(self.rows[0])/2)
        self.plant_types = {"R": "Radishes",
                            "G": "Grass",
                            "C": "Clover",
                            "V": "Violets",
                            }

        if bool(students):
            self.student_names = students['students']
            self.student_names.sort()
        else:
            self.student_names = ['Alice',
                                  'Bob',
                                  'Charlie',
                                  'David',
                                  'Eve',
                                  'Fred',
                                  'Ginny',
                                  'Harriet',
                                  'Ileana',
                                  'Joseph',
                                  'Kincaid',
                                  'Larry',
                                  ]

        self.plants_students_planted = {}

        self.process_plants()

    def plants(self, name):
        return self.plants_students_planted[name]

    def process_plants(self):
        count = 0
        plants_planted = []
        while count < self.number_of_children:
            plants_planted.append(self.plant_types[self.rows[0][0 + (2 * count)]])
            plants_planted.append(self.plant_types[self.rows[0][1 + (2 * count)]])
            plants_planted.append(self.plant_types[self.rows[1][0 + (2 * count)]])
            plants_planted.append(self.plant_types[self.rows[1][1 + (2 * count)]])
            self.plants_students_planted[self.student_names[count]] = plants_planted
            plants_planted = []
            count += 1
