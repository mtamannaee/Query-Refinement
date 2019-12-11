import random , math

def termfinder(query):
    term = "today"
    return term

def find_similarity(query, relevantTerm):
    return random.random()

def similarity_rank(vector):
    return sorted(range(len(vector)), key=vector.__getitem__)[0]

def findhighest(similarity_list):
    topTerm = similarity_rank(similarity_list)
    print(topTerm)
    index = similarity_list.index(int(topTerm))
    return index


def twinfinder(query):
    Tokens = ["today", "synonym","similar", "MostFrequentbigram"]
    tokenized_query = query.split(" ")
    similarity_list=[]
    word_twin =[]
    for token in tokenized_query:
        relevantTerm = Tokens[0] #     FIX THIS          find a most relevant Term
        similarity = find_similarity(query, relevantTerm) # FIX THIS
        similarity_list.append(similarity)# calculate similarity between the most relevant token and the whole query
        word_twin.append([token,relevantTerm])

    # highest_sim_index = findhighest(similarity_list)
    highest_sim_index = 0
    expansion_twin= word_twin[highest_sim_index]
    return expansion_twin

# ----------------------------------------------------------------------------------------------------------------------
# Pickeling Functions --------------------------------------------------------------------------------------------------
import pickle

def list_Pickel(l, filename):
    with open("{}.pickel".format(filename), "wb") as fp:
        pickle.dump(l, fp)
# l = [1,2,3,4]
# listPickel(l, "l")

def list_dePickel(filename):
    with open("{}.pickel".format(filename), "rb") as fp:
        l = pickle.load(fp)
        return l
# l = list_dePickel("l")
# print(l)
# -----------------------------------------------------------------------------------------------------------------------


