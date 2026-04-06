
class Student:
    
    def __init__(self, name, grade_level):
        self.name = name
        self.grade_level = grade_level
        self.scores = []

    def add_score(self, score):
        if score >= 0 and score <= 100:
            self.scores.append(score)
            print("Score", score, "added for", self.name)
        else:
            print("Invalid score for", self.name)

    def average(self):
        if len(self.scores) == 0:
            return 0.0
        total = 0
        for s in self.scores:
            total = total + s
        return total / len(self.scores)

    def letter_grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def profile(self):
        print("Name:", self.name)
        print("Grade Level:", self.grade_level)
        print("Scores:", self.scores)
        print("Average:", round(self.average(), 2))
        print("Letter Grade:", self.letter_grade())
        print()


# Create 4 student objects
student1 = Student("Shrivansh", 10)
student2 = Student("Harika", 11)
student3 = Student("Ali", 11)
student4 = Student("Mojahid", 12)


# Add scores 
student1.add_score(85)
student1.add_score(78)
student1.add_score(90)

student2.add_score(92)
student2.add_score(88)
student2.add_score(95)

student3.add_score(60)
student3.add_score(70)
student3.add_score(65)

student4.add_score(50)
student4.add_score(55)
student4.add_score(58)


# Print student's profile 
print("\n--- Student Profiles ---\n")
student1.profile()
student2.profile()
student3.profile()
student4.profile()