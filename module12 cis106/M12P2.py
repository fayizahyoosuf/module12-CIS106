# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:06:43 2026

@author: shama
"""

def display_names_and_scores(names, scores):
  print("Student Last Names and Exam Scores (Forward Order):")
  for i in range(len(names)):
    print(f"{names[i]}: {scores[i]}")


# Function to display last names and exam scores in reverse order without built-in methods
def display_names_and_scores_reverse(names, scores):
  print("\nStudent Last Names and Exam Scores (Reverse Order):")
  for i in range(len(names) - 1, -1, -1):
    print(f"{names[i]}: {scores[i]}")


# Main program
def main():
  last_names = [
      "Smith",
      "Johnson",
      "Williams",
      "Brown",
      "Jones",
      "Garcia",
      "Miller",
      "Davis",
      "Rodriguez",
      "Martinez",
  ]

  exam_scores = [88, 92, 79, 85, 95, 91, 76, 84, 90, 89]

  display_names_and_scores(last_names, exam_scores)
  display_names_and_scores_reverse(last_names, exam_scores)


if __name__ == "__main__":
  main()