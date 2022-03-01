from fastapi import FastAPI

import pathlib

from model import AIModel
from schema import MultipleTextQuery

app = FastAPI()

spamClassifier = None


@app.on_event("startup")
def onStartup():
    global spamClassifier

    MODEL_DIR = pathlib.Path("model")
    SPAM_HD_PATH = MODEL_DIR / 'spam_model.h5'
    SPAM_TOKENIZER_PATH = MODEL_DIR / 'spam_tokenizer.json'
    SPAM_METADATA_PATH = MODEL_DIR / 'spam_metadata.json'
    # actual loading of the classifier model
    spamClassifier = AIModel(
        modelPath=SPAM_HD_PATH,
        tokenizerPath=SPAM_TOKENIZER_PATH,
        metadataPath=SPAM_METADATA_PATH,
    )


@app.post('/predictions')
def multiple_text_predictions(query: MultipleTextQuery):
    results = spamClassifier.predict(query.texts)
    return results
