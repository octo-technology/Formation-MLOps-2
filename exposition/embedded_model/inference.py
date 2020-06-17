from ...formation_indus_ds_avancee.train_and_predict import predict_with_io
from ...formation_indus_ds_avancee.feature_engineering import prepare_features_with_io
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({
        "status": "ok"
    })

@app.route('/predict')
def predict():
    DATA_PATH = '../../data/la-haute-borne-data-2017-2020.csv'
    FEATURES_PATH = 'prepared_features'
    prepare_features_with_io(DATA_PATH, FEATURES_PATH, training_mode=False)
    predict_with_io(FEATURES_PATH)
