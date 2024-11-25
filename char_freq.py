from pprint import pprint

sentence = "This is a common interview question!"
myDict = {}

# for char in sentence:
#     if (char in myDict):
#         myDict[char] += 1
#     else:
#         myDict[char] = 1

# pprint(myDict, width=1)
# max_value = max(myDict.values())

# winners = dict(filter(lambda key: key[1] == max_value, myDict.items()))
# pprint(winners, width=1)

char_occurrence = {}
for char in sentence:
    char_occurrence[char] = char_occurrence.get(char, 0) + 1

pprint(char_occurrence)

winners = {}
max_value = float("-inf")

for key, value in char_occurrence.items():
    if value > max_value:
        max_value = value
        winners = {key: value}
    elif value == max_value:
        winners[key] = value

pprint(winners)


pprint(char_occurrence.items())
