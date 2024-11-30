# DPS-AI-Challenge

A time series forecasting project that predicts alcohol-related accidents using SARIMAX model.

## Data Set

- The model is trained on historical data from 2000 to 2020.
Source: [Open Data München](https://opendata.muenchen.de/dataset/5e73a82b-7cfb-40cc-9b30-45fe5a3fa24e/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7/download/monatszahlen2405_verkehrsunfaelle_export_31_05_24_r.csv)

## Features

- Time series forecasting using SARIMAX model
- Jupyter notebook with data analysis and model training
- Deployed on Heroku


## Project Structure

- `mission1/Classic-AI-Challenge.ipynb`: Jupyter notebook containing data analysis and model training
- `mission1/data/`: Folder containing the data set
- `mission1/output/`: The plot of the data containing the training (black) and the test (red) set, the predicted (green) and the ground truth value (blue) for January 2021
- `app.py`: Flask application with prediction endpoint
- `request.py`: Sent a POST request to the deployed model
- `requirements.txt`: Project dependencies
- `Procfile`: Heroku deployment configuration

## Dependencies

- Flask
- pandas
- statsmodels
- numpy
- scikit-learn
- gunicorn (for deployment)

## Deployment

The application is deployed on Heroku and can be accessed at:
https://dps-ai-challenge-andreea-2341b9cca97c.herokuapp.com/predict

