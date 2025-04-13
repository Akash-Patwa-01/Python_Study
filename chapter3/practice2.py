letter = ''' Dear <|Name|>
 you are selected!
  <|Date|>

'''

print(letter.replace("<|Name|>", "Akash").replace(" <|Date|>", "15 April 2025")) # this is called chaining of functions