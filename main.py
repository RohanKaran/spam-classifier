import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from prediction import AIModel
from schema import MultipleTextQuery

app = FastAPI()

origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

spamClassifier = None


@app.on_event("startup")
def onStartup():
    global spamClassifier

    MODEL_DIR = Path("model")
    SPAM_HD_PATH = MODEL_DIR / 'spam_model.h5'
    SPAM_TOKENIZER_PATH = MODEL_DIR / 'spam_tokenizer.json'
    SPAM_METADATA_PATH = MODEL_DIR / 'spam_metadata.json'
    # actual loading of the classifier model
    spamClassifier = AIModel(
        modelPath=SPAM_HD_PATH,
        tokenizerPath=SPAM_TOKENIZER_PATH,
        metadataPath=SPAM_METADATA_PATH,
    )


@app.get('/')
def activateAppFromSleep():
    return {"message": "Hey there!"}


@app.get('/model-details')
def get_model_details():
    return spamClassifier.model.to_json()


@app.post('/prediction')
def prediction(query: MultipleTextQuery):
    results = spamClassifier.predict(query.texts)
    return results
