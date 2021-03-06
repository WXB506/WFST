# coding=utf-8
import sys
# read .pyv file by console
vowel_set = ['a','o','e','i','u','v']
directory = './PYVs/'
destination_directory = './PYPs/'
fr = open(directory + sys.argv[1],'r')
name_extension = sys.argv[1].split('.')
file_name = name_extension[0] + '.pyp'
fw = open(destination_directory + file_name, 'w')
# load file
wordList = list(fr)
# deal with each line
for word in wordList:
    # deal with one line and several syllables, they are seperated by white espace.
    syllables = word.split()
    # foreach syllable, seperate rhymes.
    for syllable in syllables:
        # the 2nd character is the most important one 
        # becasue of the rules of composition between vowel and rhyme.
        # if one syllable has no more than 2 characters, keep all of them
        if syllable[0] in vowel_set:
            fw.write(syllable[:-1] + ' ')
        # if one syllable has more than 2 characters... 
        else:
            # if the 2nd character is a vowel, it is a seperator.
            if syllable[1] in vowel_set:
                fw.write(syllable[0]+' '+syllable[1:-1]+' ')
            # if it is the character 'r', it may be 'er'
            #   elif syllable[1] == 'r':
            #   fw.write(syllable + ' ')
            # the rhyme has two characters.
            else:
                fw.write(str(syllable[0:2])+' '+str(syllable[2:-1])+' ')
    fw.write('\n')
print('---------------------------------------')
print('Executing...\n')
print('Congratuation, new file ' + file_name + ' has been generated.')
print('---------------------------------------')
fr.close()
fw.close()
