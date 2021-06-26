import random

totalScore = []
print("Plese only use upper case letters when answering")

class user:
    def __init__(self):
        self.geoScore = 0
        self.phyScore = 0
        self.location = input("Which continent do you live on?")
        self.name = input(
            "What is your first and last name (suggested format: First + space + Last)\nexample: Michael Jordan"
        )

    def getScore(self):
        print("Geography score is: " + str(self.geoScore) + " points.\n")
        print("Physics score is: " + str(self.phyScore) + " points.\n")

    def getLocation(self):
        print(self.location)

    def getName(self):
        print(self.name)

    def updateGeoScore(self):
        self.geoScore = self.geoScore + 1

    def updatePhyScore(self):
        self.phyScore = self.phyScore + 1


class questionBank:
    def __init__(self):
        #instead of having 1 question array, split into 3 arrays for easy medium & hard
        self.geoQuestionArray = []
        self.phyQuestionArray = []
        self.geoAnswerArray = []
        self.phyAnswerArray = []
        self.totalQuestions = 20
        self.questions()

    def questions(self):
        self.geoQuestionArray.append(
            "What is the capitol of California?\nA San Diego \nB Sacremento\nC Fremont\nD San Franciso"
        )
        self.geoQuestionArray.append(
            "What is the capitol of Nevada?\nA Carson City \nB Las Vegas\nC Ohio\nD Oklahoma City"
        )
        self.geoQuestionArray.append(
            "Which river flows through the Grand Canyon??\nA Colorado River  \nB Nile River \nC American River"
        )
        self.geoQuestionArray.append(
            "What is the capitol of Utah?\nA Salt Lake City \nB Indiana")
        self.geoQuestionArray.append(
            "What is the 50th state in the nation ?\nA Hawaii \nB Alaska")
        self.geoQuestionArray.append(
            "What is the capitol of Alaska\nA Juneau \nB Alaska City")
        self.geoQuestionArray.append(
            "What is the capitol city of the United States\nA Washington \nB Washington DC"
        )
        self.geoQuestionArray.append(
            "What is the capitol city of the India\nA Mumbai \nB New Delhi \nC Calcutta \nD Jabalpur"
        )
        self.geoQuestionArray.append(
            "What is the capitol of Louisiana \nA Washington \nB Baton Rouge \nC Sacramento  \nD Fremont")
        self.geoQuestionArray.append(
            "What is the capitol of Turkey \nA Italy \nB London \nC Istanbul"
        )

        self.phyQuestionArray.append(
            "Starting from rest, object one falls freely for 4.0 seconds, and object two falls freely for 8.0 seconds. Compared to object one, object two falls: ?\nA  half far \nB twice far \nC three times as far \nD four times as far"
        )

        self.phyQuestionArray.append(
            "A car starts from rest, and uniformily accelerates to a final speed of 20 m/s in a time of 15.0s. How far does the car travel during this time?\nA 150m\nB 300m \nC 450m \nD 600m"
        )

        self.phyQuestionArray.append(
            "A rocket near the surface of the earth is accelerating vertically upwards at 10 meters per second squared. The rocket releases an instrument package/ Immediately releases after the acceleration of the instrument package is: ?\nA 20m/s2 up \nB 10m/s2 up \nC 0 \nD 10m/s2 down"
        )

        self.phyQuestionArray.append(
            "A car goes around a curve at 20 m/s. If the radius of the curve is 50m, what is the centrepital acceleration of the car.: ?\nA 8m/s2\nB 10m/s2 \nC 0m/s2 \nD 8m"
        )

        self.phyQuestionArray.append(
            "Professor Brown holds on to the end of the minute hand of a clock atop city hall. If the minute hand is 4.0 m long, what is the professor's centrepital acceleration. ?\nA 1*10 to the power -5\nB 1.22 times 10 to the power of -5 \nC 0m/s2 \nD 8 times 5 squared"
        )

        self.phyQuestionArray.append(
            "What is the formula for speed? \nA s=d/t \nB t=d/s \nC s=t/d  \nD s/d"
        )

        self.phyQuestionArray.append(
            "A pivot point on a liver is called a  \nA  Pulley \nB fulcrum \nC work  \nD energy "
        )

        self.phyQuestionArray.append(
            "Is gravity a force  \nA Maybe  \nB No  \nC Not sure  \nD Yes  ")

        self.phyQuestionArray.append(
            "The magnitude of earthquakes is measused on the ____ scale  \nA richter scale  \nB Sismograph \nC Metric scale  \nD meters "
        )

        self.phyQuestionArray.append(
            "Suppose an object is in free fall. Each second the object falls \nA same time \nB With the same speed \nC same distance   \nD A larger distance than in the second before"
        )

        self.phyQuestionArray.append(
            "Ignoring air resistance an object falling towards the surface of the Earth has a velocity that is  \nA  Instantaneous \nB Constant  \nC Decrease   \nD Increase"
        )

        self.geoAnswerArray.append("B")
        self.geoAnswerArray.append("A")
        self.geoAnswerArray.append("A")
        self.geoAnswerArray.append("A")
        self.geoAnswerArray.append("A")
        self.geoAnswerArray.append("A")
        self.geoAnswerArray.append("B")
        self.geoAnswerArray.append("B")
        self.geoAnswerArray.append("B")
        self.geoAnswerArray.append("C")

        self.phyAnswerArray.append("D")
        self.phyAnswerArray.append("A")
        self.phyAnswerArray.append("D")
        self.phyAnswerArray.append("A")
        self.phyAnswerArray.append("B")
        self.phyAnswerArray.append("A")

        self.phyAnswerArray.append("B")

        self.phyAnswerArray.append("D")
        self.phyAnswerArray.append("A")
        self.phyAnswerArray.append("D")


def startQuiz():
    # IndexUsed is a data structure called Dictionary
    geoIndexUsed = {}
    phyIndexUsed = {}
    student = user()
    bank = questionBank()

    # Present Geography Quiz
    for i in range(10):
        geoIndex = random.randint(0, 9)
        while (geoIndex in geoIndexUsed):
            geoIndex = random.randint(0, 9)
        geoIndexUsed[geoIndex] = "True"
        answer = input(bank.geoQuestionArray[geoIndex])
        if answer == bank.geoAnswerArray[geoIndex]:
            student.updateGeoScore()
        else:
            print("Sorry your answer isn't correct, the correct answer is" +
                  bank.geoAnswerArray[geoIndex] + "\n")

    #Present Physics Quiz
    for i in range(10):
        phyIndex = random.randint(0, 9)
        while (phyIndex in phyIndexUsed):
            phyIndex = random.randint(0, 9)
        phyIndexUsed[phyIndex] = "True"
        answer = input(bank.phyQuestionArray[phyIndex])
        if answer == bank.phyAnswerArray[phyIndex]:
            student.updatePhyScore()
        else:
            print("Sorry your answer isn't correct, the correct answer is" +
                  bank.phyAnswerArray[phyIndex] + "\n")

    student.getScore()
    # do a if statement, if condition is met, display the website
    if (student.geoScore < 5):
        print(
            "Unfortunately you didn't do great on this quiz. However, I've found this website that can help to improve your skill\n"
        )
        print(" https://online.seterra.com/en/vgp/3063")
    if (student.phyScore < 5):
        print(
            "Unfortunately you didn't do great on this quiz. However, I've found this website that can help to improve your skill\n"
        )
        print(
            "https://www.khanacademy.org/science/high-school-physics/one-dimensional-motion-2/motion-with-constant-acceleration-2/v/choosing-kinematic-equations"
        )

    totalScore.append(student)


def printTotal():
    for i in totalScore:
        print("User Name:" + str(i.name) + "\n")
        print("User Region:" + str(i.location) + "\n")
        print("User Geography Score:" + str(i.geoScore) + "\n")
        print("User Science Score:" + str(i.phyScore) + "\n")


def startProgram(flagg):
    if (str(flagg) == "1"):
        startQuiz()
        return ()
    elif (str(flagg) == "2"):
        if (len(totalScore) == 0):
            print("There is no valid score entry, program exiting...")
            return ()
        else:
            printTotal()
            return ()
    else:
        print("Invalid option, program exiting...")
        return ()
    return ()


def main():
    while (True):
        flagg = input(
            "Please enter your option, 1: take the test, 2: check scores")
        startProgram(flagg)


if __name__ == "__main__":
    main()
