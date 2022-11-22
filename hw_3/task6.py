import textwrap as tw
import argparse

parser = argparse.ArgumentParser(description = "take text from a file and write it to another file, reducing the number of characters in a line")
parser.add_argument('file1', type = str, help = 'Input file for analis')
parser.add_argument('file2', type = str, help = 'Input file for result')
args = parser.parse_args()


f1 = open(args.file1, 'r', encoding = "utf-8")
text = f1.readlines()
f1.close()

f2 = open(args.file2, 'w', encoding = "utf-8")
for line in text:
    if len(line) > 90:
        f2.write(tw.fill(line, width = 70))
    else:
        f2.write(line)
f2.close()

#f2 = open(args.file2, 'r', encoding = "utf-8")
#for line in f2:
#    print(len(line))
#f2.close()