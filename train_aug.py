def read_file(filename):
    temp_list = []
    file = open(filename, "rt", encoding='utf-8-sig')
    while True:
        line = file.readline()
        if line == "": break
        temp_list.append(line)
    file.close()
    return temp_list

def write_file(filename):
    file = open(filename, "wt", encoding='utf-8-sig')
    for i in range(len(train_list)):
        file.write(train_list[i])
    file.close()

def preprocess(sentence):
    new_sentence = ""
    for i in range(len(sentence)):
        if sentence[i].isdigit():
            pass
        else:
            new_sentence += sentence[i]
    return new_sentence

for i in range(8):  
    train_list = []
    filename = "train" + str(i+1) + ".txt"
    temp_list = read_file(filename)
    for j in range(len(temp_list)):
        train_list.append(temp_list[j])
        train_list.append(preprocess(temp_list[j]))
        for short_sentence in temp_list[j].split("."):
            if len(short_sentence.strip()) >= 1:
                train_list.append((short_sentence.strip()) + "\n")
                train_list.append(preprocess(short_sentence.strip()) + "\n")
    write_file(filename)