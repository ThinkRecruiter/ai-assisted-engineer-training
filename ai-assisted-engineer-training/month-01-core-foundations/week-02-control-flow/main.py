def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D/F"

scores = [95, 72, 88, 61]

if __name__ == "__main__":
    grades = [grade(s) for s in scores]
    print("Grades:", grades)