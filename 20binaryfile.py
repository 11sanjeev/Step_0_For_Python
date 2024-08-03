import pickle
# phonebook = {
#     'a':'1',
#     'b':'2',
#     'c':'3',
#     'd':'4'
# }
# with open('data.txt','wb') as bin:
#     pickle.dump(phonebook,bin)

with open('data.txt','rb') as bin:
    data = pickle.load(bin)
    print(data)