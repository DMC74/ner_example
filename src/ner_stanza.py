import sys
from ner_stanza_core import NerStanzaCore

if __name__ == "__main__":
    # Initialising our application
    app = NerStanzaCore(sys.argv[1:]) 
    # Running our application 
    app.run()  