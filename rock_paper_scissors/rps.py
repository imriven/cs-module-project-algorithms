#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  options = ["rock", "paper", "scissors"]
  results = []

  def generate_hands(rounds_left, played_rounds=None):
    if not played_rounds:
      played_rounds = []
    if rounds_left == 0:
      results.append(played_rounds)
    else:
      for o in options:
        generate_hands(rounds_left - 1, [*played_rounds, o])

  generate_hands(n)

  return results 


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')