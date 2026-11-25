# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 08:58:09 2026

@author: shama
"""

def display_names(names):
  print("Last Names (Forward Order):")
  for i in range(len(names)):
    print(names[i])


# Function to display the names in reverse order without built-in reverse methods
def display_names_reverse(names):
  print("\nLast Names (Reverse Order):")
  for i in range(len(names) - 1, -1, -1):
    print(names[i])


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

  display_names(last_names)
  display_names_reverse(last_names)


if __name__ == "__main__":
  main()