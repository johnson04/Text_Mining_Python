#-------------------------------------------------------------------------------
# Name:        ExploreTxtData.py
# Purpose:     Load the following three text data files:
#                   en_US.blogs.txt
#                   en_US.news.txt
#                   en_US.twitter.txt
#              and conduct some exploratory analysis
#
# Author:      Chuan
#
# Created:     30/10/2014
# Copyright:   (c) Chuan 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time

class UsEnText:
    def __init__(self, file_name = "en_US.blogs.txt", file_path = "../final/en_US/"):
        self.file_path  = file_path
        self.file_name  = file_name
        self.file       = file_path + file_name
        self.text       = []
        self.num_lines  = 0
        self.line_width = 0
        self.__load_data__()

    def __load_data__(self):
        with open(self.file, "r") as text_file:
            print "--Loading text file %s" %self.file_name,
            for line in text_file:
                self.text.append(line)
                if self.line_width < len(line):
                    self.line_width = len(line)
                self.num_lines += 1
                if self.num_lines % 50000 == 0:
                    print ".",

        print "\nText loaded, close the file.\n"
        time.sleep(0.5)
        text_file.close()

def main():
    file_list = ["en_US.blogs.txt", "en_US.news.txt", "en_US.twitter.txt"]
##    Blogs     = UsEnText(file_list[0])
##    print Blogs.num_lines, Blogs.line_width

##    News      = UsEnText(file_list[1])
##    print News.num_lines, News.line_width

    Tweets    = UsEnText(file_list[2])
    print Tweets.num_lines, Tweets.line_width
    word_freq_love = 0
    word_freq_hate = 0
    sentence_freq  = 0
    for lines in Tweets.text:
        if "love" in lines:
            word_freq_love += 1
##            print lines
        if "hate" in lines:
            word_freq_hate += 1
##            print lines
        if "biostats" in lines:
            print lines
        if "A computer once beat me at chess, but it was no match for me at kickboxing" in lines:
            sentence_freq += 1
            print lines
    print word_freq_love, "/", word_freq_hate, "=", str(word_freq_love/word_freq_love)
    print sentence_freq

if __name__ == '__main__':
    main()
