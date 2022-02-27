# https://github.com/Huffon/klue-transformers-tutorial를 일부 활용

import pickle
import torch
from sentence_transformers import util

with open('model.pickle', 'rb') as f:
    model = pickle.load(f)

with open('data.pickle', 'rb') as f:
    document_embedding_list = pickle.load(f)

def get_first_candidate(document_embeddings, query_embedding, class_index):
    top_k = 10
    cos_scores = util.pytorch_cos_sim(query_embedding, document_embeddings)[0]
    top_results = torch.topk(cos_scores, k=top_k)

    global nearest_neighbors
    for i, (score, idx) in enumerate(zip(top_results[0], top_results[1])):
        nearest_neighbors.append([class_index+1, score.item(), docs_list[class_index][idx]])
    
    return top_results[0][0].item()

def read_file(filename):
    temp_list = []
    file = open(filename, "rt", encoding='utf-8-sig')
    while True:
        line = file.readline()
        if line == "": break
        temp_list.append(line)
    file.close()
    return temp_list

def get_most_frequent_item(List):
    return max(set(List), key = List.count)

def preprocess(sentence):
    new_sentence = ""
    for i in range(len(sentence)):
        if sentence[i].isdigit():
            pass
        else:
            new_sentence += sentence[i]
    return new_sentence

docs_list = []
for i in range(8):
    docs_list.append(read_file("train" + str(i+1) + ".txt"))

input_output_pair = [
    [1, 6],
    [2, 5],
    [3, 6],
    [4, 1],
    [5, 1],
    [6, 2],
    [7, 2],
    [8, 2],
    [9, 3],
    [10, 3],
    [11, 4],
    [12, 4],
    [13, 4],
    [14, 4],
    [15, 5],
    [16, 5],
    [17, 5],
    [18, 5],
    [19, 6]
]

lower_grades = [4, 6, 7, 8, 10, 11, 12, 15]
lower_correct = 0
lower_incorrect = 0
upper_correct = 0
upper_incorrect = 0

summary = []
for pair in input_output_pair:
    queries = read_file("test" + str(pair[0]) + ".txt")

    num_correct = 0
    num_incorrect = 0

    for i in range(len(queries)):    
        freq_list = []
        small_queries = []
        small_queries.append(queries[i])

        for small_query in small_queries:
            query_embedding = model.encode(preprocess(small_query))
            nearest_neighbors = []        

            max_score = -1
            max_index = -1
            
            for j in range(len(docs_list)):
                score = get_first_candidate(document_embedding_list[j], query_embedding, j)
                if max_score < score:
                    max_score = score
                    max_index = j+1
            
            freq_list.append(max_index)

        max_index = get_most_frequent_item(freq_list)
        nearest_neighbors = sorted(nearest_neighbors,key=lambda l:l[1], reverse=True)

        freq_list = []
        for j in range(10):        
            freq_list.append(nearest_neighbors[j][0])
        prediction = get_most_frequent_item(freq_list)
        
        print("")
        print("correct answer:", pair[1])
        print("prediction:", prediction)
        print("query:", queries[i])
        print("freq_list:", freq_list)
        print("nearest_neighbors: ")
        for j in range(len(nearest_neighbors)):
            print(nearest_neighbors[j])

        if str(pair[1]) == str(prediction):
            num_correct+=1
        else:
            num_incorrect+=1
        
        
    if pair[0] in lower_grades:
        lower_correct += num_correct
        lower_incorrect += num_incorrect
    else:
        upper_correct += num_correct
        upper_incorrect += num_incorrect

    summary.append([str(pair[0]), num_correct, num_incorrect])


for i in range(len(summary)):
    print(summary[i])

print("lower:", lower_correct, lower_incorrect, lower_correct/(lower_correct+lower_incorrect))
print("upper:", upper_correct, upper_incorrect, upper_correct/(upper_correct+upper_incorrect))
