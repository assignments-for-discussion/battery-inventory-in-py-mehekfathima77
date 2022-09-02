import os
import numpy

def count_batteries_by_usage(cycles):
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
  for test_bucketing_by_number_of_cycles in count_batteries_by_usage:
    if test_bucketing_by_number_of_cycles < 400:
      print ("lowCount")
      elif test_bucketing_by_number_of_cycles in range(400,920):
        print ("mediumCount")
        else test_bucketing_by_number_of_cycles >= 920 :
          print ("highCount")
