
import argparse
import glob
import json
import logging
import os
import pandas as pd    
import spacy
import time

#Create and configure logger using the basicConfig() function  
logging.basicConfig(filename="NerSpacyCore.log",  
               format='%(asctime)s %(message)s',  
               filemode='w')  

#Creating an object of the logging  
logger = logging.getLogger('ner_spacy')

#Setting the threshold of logger to DEBUG  
logger.setLevel(logging.DEBUG)  

class NerSpacyCore:
    def __init__(self, argv):
        self.argv = argv

    def run(self):
        logger.debug("NerSpacyCore.run:")
        self.args = self.parse_args()
        self.init_pipeline('english')
        df = self.load_data()
        start = time.time()
        logger.debug("Start Time:" + str(start))
        df['ner'] = df['contents'].apply(self.spacy_ner)
        stop = time.time()
        logger.debug("Stop Time:" + str(stop))
        logger.debug("Total Time:" + str((stop - start)))
        print(df)


    def parse_args(self):
        """
        Parses CLI arguments 
        """
        logger.debug("NerSpacyCore.parse_args: loading and checking parameters")
        parser = argparse.ArgumentParser()
        parser.add_argument('--test_corpus', type=str, help="file path for test file corpus")
        args = parser.parse_args(args=self.argv)
        return args

    def load_data(self):
        folder_path = self.args.test_corpus # corpus file path
        file_list = glob.glob(folder_path + "/*.txt")

        df = pd.DataFrame()
        for i in range (0,len(file_list)):
            file_path = file_list[i]
            file_name = os.path.basename(file_path)
            content = open(file_path, "r").read()    
            df = pd.concat([df, pd.DataFrame(data = {"filename" : [file_name], "contents" : [content]})])
        return df

    def init_pipeline(self, language):
        logger.debug("NerSpacyCore.spacy_version:" + str(spacy.__version__))
        # self.pipeline =  spacy.load('en_core_web_sm')
        self.pipeline =  spacy.load('en_core_web_lg')


    def spacy_ner(self, content):
        doc = self.pipeline(content)
        ners = []
        for ent in doc.ents:
            print(f'{ent.text}\t{ent.label_}') 
            entry=(ent.text,ent.label_)
            ners.append(entry)        
        return json.dumps(dict(ners))




