from Functions import *

DOCNUM_list = list_dePickel("DOCNUM_list")      # TREC DOCUMENT ID s
DOCTEXT_list = list_dePickel("DOCTEXT_list")    # TREC DOCUMENT TEXT s

QUERYID_list = list_dePickel("QUERYID_list")      # TREC Query ID s
QUERYTEXT_list = list_dePickel("QUERYTEXT_list")  # TREC Query TEXT s

QID_list = list_dePickel("QID_list")
QueryDoc_list = list_dePickel("QueryDoc_list")
REL_list = list_dePickel("REL_list")



# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
from rank_bm25 import BM25Okapi, BM25L, BM25Plus
from Functions import *
from QEModels import *

corpus = DOCTEXT_list
tokenized_corpus = [doc.split(" ") for doc in corpus]

# Retrieval MODELS  ---------------------------------------------------------------------------------------------------
bm25 = BM25Okapi(tokenized_corpus)
bm25l = BM25L(tokenized_corpus)
bm25plus = BM25Plus(tokenized_corpus)

# RANKING --------------------------------------------------------------------------------------------------------------
# Original Query  - - - - - - - - -- - - - - -- - - -- - -- - -- - -- - - -- - -- - - - --- - - - - - -- - - -- - - -- -
runLines=[]
with open("robust-BM25-run.txt", "w")as frun:
    for i in range(len(QUERYTEXT_list)):
        query = QUERYTEXT_list[i]
        tokenized_query = query.split(" ")
        print(tokenized_query)

        #  BM25
        doc_scores_bm25 = bm25.get_scores(tokenized_query)
        bm25TopN = bm25.get_top_n(tokenized_query, corpus, n=1000)


        for j in bm25TopN:
            docnum = DOCNUM_list[DOCTEXT_list.index(j)]
            rank= bm25TopN.index(j)
            runLines.append("{} Q0 {} {} {} Default".format(QUERYID_list[i],docnum, rank+1, doc_scores_bm25[rank]))
            print("{} Q0 {} {} {} Default".format(QUERYID_list[i],docnum, rank+1, doc_scores_bm25[rank]))
        frun.writelines(runLines)

        #
