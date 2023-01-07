import numpy as np
import pandas as pd
import tensorflow as tf
import autokeras as ak

# Initialize the structured data classifier.
clf = ak.StructuredDataClassifier(
    column_names=[
        'Blue_Traditional_Scoring_High',
        'Blue_Traditional_Scoring_Low',
        'Blue_Technical_Scoring',
        'Blue_Autonomous_Scoring',
        'Blue_Endgame',
        'Blue_Fouls',
        'Blue_Defense',
        'Red_Traditional_Scoring_High',
        'Red_Traditional_Scoring_Low',
        'Red_Technical_Scoring',
        'Red_Autonomous_Scoring',
        'Red_Endgame',
        'Red_Fouls',
        'Red_Defense'
    ],
    max_trials=10,  # It tries 10 different models.
    overwrite=True,
)


# Feed the structured data classifier with training data.
clf.fit(
    'data/wonlost.csv',
    'blue_won',
    # Split the training data and use the last 15% as validation data.
    validation_split=0.15,
    epochs=10,
)

# Predict with the best model.
predicted_y = clf.predict('data/wonlost.csv')
# Evaluate the best model with testing data.
print(clf.evaluate('data/wonlost.csv', "survived"))
