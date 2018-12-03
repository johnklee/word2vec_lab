#!/usr/bin/env python3
# -*- coding: utf-8 -*-  
  
import logging  
import sys  
  
from gensim.corpora import WikiCorpus  
  
def main():  
  
    if len(sys.argv) != 2:  
        print("Usage: python3 " + sys.argv[0] + " wiki_data_path")  
        exit()  
  
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)  
    wiki_corpus = WikiCorpus(sys.argv[1], dictionary={})  
    texts_num = 0  
  
    with open("wiki_texts.txt",'w',encoding='utf-8') as output:  
        for text in wiki_corpus.get_texts():
            str_text = list(map(lambda t:t.decode('utf-8'), text))
            #print("text={}".format(str_text)) 
            output.write(' '.join(str_text) + '\n')  
            texts_num += 1  
            if texts_num % 1000 == 0:  
                logging.info("Done with %d articles" % texts_num)
  
if __name__ == "__main__":  
    main()  
