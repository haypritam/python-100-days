import pandas

data=pandas.read_csv("nato_phonetic_alphabet.csv")

dict={row.letter:row.code for(index,row) in data.iterrows()}

user=input("enter a word: ")
result=[dict[i.upper()] for i in user]
print(result)

