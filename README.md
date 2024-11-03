# Fine-Tuning Large Language Models for Sentiment Analysis on Earnings Call Transcripts

This repository contains Jupyter notebooks for fine-tuning large language models (LLMs) on a custom sentiment dataset of earnings call transcript sentences. The fine-tuning is performed in Google Colab to leverage its GPU resources and make the process accessible.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Notebook](#notebook)
- [Dataset](#dataset)
- [Usage](#usage)

---

### Project Overview

This repository fine-tunes a pre-trained language model (such as GPT, RoBERTa) on custom datasets to improve performance on specific tasks. Fine-tuning can help the model provide more accurate responses, adapt to specialized vocabularies, or improve accuracy in particular domains.

### Requirements
These notebooks are designed to run in Google Colab, so there's no need to install dependencies locally. There are cells to install the mandatory package in the notebooks.

- Python 3.8+
- `transformers` library by Hugging Face (for model loading and fine-tuning)
- `torch` (for PyTorch models and training)
- `pandas` (for data processing)
- `scikit-learn` (for evaluation metrics)

### Notebook
The repository includes the following Jupyter notebooks:

1. `Finetune_ChatGPT.ipynb`: Notebook for fine-tuning ChatGPT 3.5-turbo on the self-labelled sentiment dataset.

2. `Finetune_RoBERTa.ipynb`: Notebook for fine-tuning the RoBERTa model on the same dataset.

Each notebook is self-contained and includes:

- Instructions for setting up the Google Colab environment.
- Code to load and preprocess the dataset.
- Model configuration and fine-tuning steps.
- Evaluation of the fine-tuned model's performance on a test set.

### Dataset
The dataset `sentences_with_sentiment.csv` consists of sentiment-labeled sentences from earnings call transcripts. Each sentence is manually labeled with its sentiment (positive, negative, or neutral), making it suitable for supervised fine-tuning.

- Data Format: Ensure your dataset is in CSV format, with columns such as `text` and `sentiment`.
- Data Preparation: The notebooks include data loading and preprocessing steps, so you can upload your dataset directly to Google Colab and follow the instructions.


### Usage

1. Open each notebook in Google Colab:
- You can upload the notebook to your Google Drive and open it with Colab.

2. Follow the setup instructions in each notebook to install dependencies and upload your dataset.

3. Run each cell sequentially to:
- Load and preprocess the dataset.
- Configure the model.
- Fine-tune the model on your dataset.
- Evaluate model performance.

4. Saving the Fine-Tuned Model
