# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 10:27:21 2026

@author: shama
"""

import os


def create_sample_file():
  if not os.path.exists("players.txt"):
    with open("players.txt", "w") as file:
      file.write("Ohtani\n0.310\n")
      file.write("Judge\n0.322\n")
      file.write("Betts\n0.289\n")
      file.write("Soto\n0.288\n")
      file.write("Freeman\n0.282\n")
      file.write("Harper\n0.285\n")
      file.write("Trout\n0.263\n")
      file.write("Altuve\n0.295\n")
      file.write("Ramirez\n0.279\n")
      file.write("Witt\n0.332\n")


def load_data(names, averages):
  with open("players.txt", "r") as file:
    for i in range(10):
      names.append(file.readline().strip())
      averages.append(file.readline().strip())


def display_players(names, averages):
  print("Player Last Names and Batting Averages:")
  for i in range(len(names)):
    print(f"{names[i]}: {averages[i]}")


def search_player(names, averages, target):
  found = False
  for i in range(len(names)):
    if names[i] == target:
      print(f"Player Found: {names[i]} - Batting Average: {averages[i]}")
      found = True

  if not found:
    print("Name not found")


def main():
  names = []
  averages = []

  create_sample_file()
  load_data(names, averages)
  display_players(names, averages)

  search_name = input(
      "Enter a player's last name to search (or 'quit' to exit): "
  )
  while search_name != "quit" and search_name != "QUIT" and search_name != "Quit":
    search_player(names, averages, search_name)
    search_name = input(
        "Enter a player's last name to search (or 'quit' to exit): "
    )

  print("Exiting search.")


if __name__ == "__main__":
  main()