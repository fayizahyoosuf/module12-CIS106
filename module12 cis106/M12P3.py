import os

# Create students.txt automatically if it doesn't exist in the current folder
if not os.path.exists("students.txt"):
    with open("students.txt", "w") as f:
        f.write("Smith\n88\n")
        f.write("Johnson\n92\n")
        f.write("Williams\n79\n")
        f.write("Brown\n85\n")
        f.write("Jones\n95\n")
        f.write("Garcia\n91\n")
        f.write("Miller\n76\n")
        f.write("Davis\n84\n")
        f.write("Rodriguez\n90\n")
        f.write("Martinez\n89\n")


def load_data(filename):
    names = []
    scores = []
    with open(filename, "r") as file:
        lines = [line.strip() for line in file if line.strip() != ""]
        for i in range(0, len(lines), 2):
            names.append(lines[i])
            scores.append(int(lines[i + 1]))
    return names, scores


def display_names_and_scores(names, scores):
    print("Student Last Names and Exam Scores (Forward Order):")
    for i in range(len(names)):
        print(names[i], scores[i])


def display_names_and_scores_reverse(names, scores):
    print("\nStudent Last Names and Exam Scores (Reverse Order):")
    for i in range(len(names) - 1, -1, -1):
        print(names[i], scores[i])


def display_high_low(names, scores):
    high_var = 0
    high_index = 0
    low_var = 999
    low_index = 0

    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i

    print("\nHighest Score:", names[high_index], high_var)
    print("Lowest Score:", names[low_index], low_var)


def main():
    last_names, exam_scores = load_data("students.txt")
    display_names_and_scores(last_names, exam_scores)
    display_names_and_scores_reverse(last_names, exam_scores)
    display_high_low(last_names, exam_scores)


if __name__ == "__main__":
    main()
