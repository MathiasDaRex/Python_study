text = "Yoyoyo duuuuude\nThis is some awesome text\nHave a nice day!\nCode well!\n"
text2 = "The text has been overwritten"
text3 = "Bro pls append me\nSee ya"
 
with open('test33.txt','w') as file:
    file.write(text)
#	 we can overwrite it adding another text
#    file.write(text2)
#	 And we can also append text from a file
    file.write(text3)