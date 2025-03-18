from transformers import AutoTokenizer, AutoModelForSequenceClassification
from typing import Tuple
import torch
import transformers

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert").to(device)

labels = ["positive", "negative", "neutral"]

def estimate_sentiment(news, max_length=512):
    if news:
        truncated_news = news[:max_length]
        tokens = tokenizer(truncated_news, return_tensors="pt", padding="max_length", max_length=max_length).to(device)
        result = model(tokens["input_ids"], attention_mask = tokens["attention_mask"])[
            "logits"
        ]
        result = torch.nn.functional.softmax(torch.sum(result, 0), dim=-1)
        probability = result[torch.argmax(result)]
        sentiment = labels[torch.argmax(result)]
        return probability.item(), sentiment
    else:
        return "neutral"

if __name__ == "__main__":
    from Finbert_Utils import estimate_sentiment
    tensor, sentiment = estimate_sentiment(['traders were right when predicting the market!', 'market answered correctly as expected!'])
    print(estimate_sentiment("This is a great movie!"))
    print(torch.cuda.is_available())
    print(transformers.__version__)