maths_mark = int(input("Enter Maths mark: "))
english_mark = int(input("Enter English mark: "))

passed_both = maths_mark >= 50 and english_mark >= 50

print("Did the student pass in both Maths and English: ",passed_both)
