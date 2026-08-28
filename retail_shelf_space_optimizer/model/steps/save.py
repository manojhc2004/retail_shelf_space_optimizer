from config import *

# file saving
def save_(file,title="finalrules_.csv"):
    
    file.to_csv(title,index=False)
    print("file is saved successfully!")
    logging.info("final rule file saved successfully")