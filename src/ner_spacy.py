import sys
from ner_spacy_core import NerSpacyCore

if __name__ == "__main__":
    # Initialising our application
    app = NerSpacyCore(sys.argv[1:]) 
    # Running our application 
    app.run()  