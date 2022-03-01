from fastapi import FastAPI

import pathlib

from model import AIModel
from config import getSettings
from schema import SingleTextQuery, MultipleTextQuery

app = FastAPI()

# globally-accessible objects:
spamClassifier = None


@app.on_event("startup")
def onStartup():
    global spamClassifier
    #
    # settings = getSettings()
    #
    # location of the model data files
    API_BASE_DIR = pathlib.Path("")
    print(API_BASE_DIR)
    MODEL_DIR = API_BASE_DIR.parent / "model"
    SPAM_HD_PATH = MODEL_DIR / 'spam_model.h5'
    SPAM_TOKENIZER_PATH = MODEL_DIR / 'spam_tokenizer.json'
    SPAM_METADATA_PATH = MODEL_DIR / 'spam_metadata.json'
    # actual loading of the classifier model
    spamClassifier = AIModel(
        modelPath=SPAM_HD_PATH,
        tokenizerPath=SPAM_TOKENIZER_PATH,
        metadataPath=SPAM_METADATA_PATH,
    )


@app.post('/prediction')
def single_text_prediction(query: SingleTextQuery):
    result = spamClassifier.predict([query.text])[0]
    return result


@app.post('/predictions')
def multiple_text_predictions(query: MultipleTextQuery):
    results = spamClassifier.predict(query.texts)
    return results
