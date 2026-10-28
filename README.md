# Real-Time Multi-Class Prompt Injection Detection Using Quantized DistilBERT

## Project Overview
This project detects prompt injection attempts in Large Language Model (LLM) systems using a fine-tuned and quantized DistilBERT model.

The system classifies prompts into four categories:
- **Benign:** Normal prompts.
- **Direct Injection:** Prompts that attempt to manipulate model instructions directly.
- **Indirect Injection:** Malicious instructions embedded in external or retrieved content.
- **Jailbreak:** Prompts designed to bypass model restrictions.

## Technologies Used
- Python
- DistilBERT
- Hugging Face Transformers
- FastAPI
- Streamlit
- Model Quantization

## Key Features
- Four-class prompt classification.
- Transformer-based text classification.
- Model quantization for more efficient inference.
- FastAPI prediction interface.
- Streamlit user interface.

## Project Workflow
1. Prepare and preprocess the labelled dataset.
2. Tokenize prompts using the DistilBERT tokenizer.
3. Fine-tune the model for four-class classification.
4. Evaluate the model using classification metrics.
5. Integrate predictions into the application interface.

## Repository Contents
- `PromptInjectionDetection.ipynb` — notebook for model development and experimentation.

## How to Run
Open the notebook in Google Colab or Jupyter Notebook and execute its cells in order after installing the required dependencies.

## Future Improvements
- Evaluate on unseen prompt injection examples.
- Measure inference time and memory usage.
- Improve generalization to new attack patterns.

## Author
Pooja Thota

GitHub: https://github.com/Poojathota27
