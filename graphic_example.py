
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width)/2

sentence = raw_input("What would you like to type")

print
print ' '*left_margin+'+' + "-"*(box_width-2) + '+'
print ' '*left_margin+'|'
print ' '*left_margin+'|' + sentence
print ' '*left_margin+'|'
print ' '*left_margin+'+'
