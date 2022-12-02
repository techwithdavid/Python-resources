import re


def match_text(txt_data):
     pattern = 'ab{4,8}'
      if re.search(pattern,  txt_data):  # search for pattern in txt_data
           return 'Match found'
       else:
           return('Match not found')

print(match_text("abc"))  # prints Match not found
print(match_text("aabbbbbc"))
