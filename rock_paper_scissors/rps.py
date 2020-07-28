#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    hands = [ 'rock', 'paper', 'scissors']
    # Your code here
    def rps(options, n):
      if n == 0:
        return [[]]
      else:
        options = rps(options, n-1)
        new_options = []
      for h in hands:
        for o in options:
          new_options.append(o+[h])
      return new_options
    
    return rps([],n)



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')