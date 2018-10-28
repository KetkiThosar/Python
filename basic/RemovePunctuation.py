#This program removes punctuations from the string

#define punctuation

punctuations='''!--,'''

my_str="Hello , He said !!!!! ---- and went."


no_punc= ""

for char in my_str:
    if char not in punctuations:
        no_punc=no_punc+char


print(no_punc)