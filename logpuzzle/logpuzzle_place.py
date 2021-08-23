#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
#import urllib
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def sorter_func(url):

  return re.findall(r'\w+\-(\w+)\.jpg' , url)[0]


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""

#' /edu/languages/google-python-class/images/puzzle/a-baag.jpg '

  underscore_index = filename.find('_')
  hostname = filename[underscore_index+1:]

  f = open(filename, 'r')
  file_as_string  = f.read()
  puzzle_urls = re.findall(r' (\S*puzzle\S*) ', file_as_string)

  list_of_urls = ['http://' + hostname + puzzle_url for puzzle_url in puzzle_urls]

  list_of_urls = sorted(list(dict.fromkeys(list_of_urls)),key=sorter_func) #converting list to dict keys and back again to get rid of duplicates (and sorting)

  return list_of_urls

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """

#this is just copied from the solution (and adapted for Python 3...)

  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

  index = open(os.path.join(dest_dir, 'index.html'), 'w')
  index.write('<html><body>\n')

  i = 0
  for img_url in img_urls:
    local_name = 'img%d' % i
    print('Retrieving...', img_url)
    urllib.request.urlretrieve(img_url, os.path.join(dest_dir, local_name))

    index.write('<img src="%s">' % (local_name,))
    i += 1

  index.write('\n</body></html>\n')
  index.close()



def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
