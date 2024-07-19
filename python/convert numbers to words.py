# write a program which converts numbers to words
phone=input("Phone: ")
digits={
"1": "One",
"2": "Two",
"3": "Three",
"4": "Four",
"5": "Five",
"6": "Six",
"7": "Seven",#stores digits as words
"8": "Eight",
"9": "Nine",
"10": "Ten"
}

output= ""
for ch in phone:#ch represents characters
    output +=digits.get(ch, "!")#output is digit entered as word if error "!"
print(output)#.get grabs digit entered