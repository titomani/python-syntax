
def uppercase(word,msw):
    uppercase_list = []
    for char in word: 
      if char[0] == msw:
       uppercase_list.append(char.upper())
    print(uppercase_list) 



uppercase(['she','auh','fuh'], {'s','a'})

'''original_list = ['water','air','earth','fire']
uppercase_list = []
for words in original_list:
    uppercase_list.append(words.upper())
print(uppercase_list)'''