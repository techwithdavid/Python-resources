from array import array
p = array('u', [u'\u0050', u'\u0059', u'\u0054',
          u'\u0048', u'\u004F', u'\u004E'])
print(p)
q = p.tounicode()
print(q)
