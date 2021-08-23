#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

def freq_dict(filename):
  dictionary = {}

  f = open(filename, 'r')
  text_as_big_string = f.read()
  text_as_list = sorted([word.lower() for word in text_as_big_string.split()])

  for word in text_as_list:
    if word in dictionary:
      dictionary[word] += 1
    else:
      dictionary[word] = 1

  f.close()

  return dictionary


def choose_2nd_tuple_value(tuple):
  return tuple[1]


def top_20_words(dictionary):

  list_of_tuples = []
  for key in dictionary.keys():
      list_of_tuples.append((key, dictionary[key]))
  sorted_list_of_tuples = sorted(list_of_tuples, key = choose_2nd_tuple_value, reverse = True)

  tuples_for_top_20_words = sorted_list_of_tuples[:min(len(sorted_list_of_tuples),20)]
  top_20_words = [tuple[0] for tuple in tuples_for_top_20_words]
  return top_20_words




def print_words(filename):

  d = freq_dict(filename)

  for key in d.keys():
    print(key, d[key])


def print_top(filename):

  d = freq_dict(filename)

  for word in top_20_words(d):
    print(word, d[word])



# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
