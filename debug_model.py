"""
Debug script to check actual model output
"""

import os
os.environ['TRANSFORMERS_CACHE'] = './model_cache'

from transformers import pipeline

classifier = pipeline(
    task="text-classification",
    model="Hello-SimpleAI/chatgpt-detector-roberta",
    device=-1
)

# Test with obvious AI text
ai_text = """Artificial intelligence has become an integral part of modern society, revolutionizing 
numerous industries and transforming the way we live and work. Machine learning algorithms 
enable computers to learn from data and make intelligent decisions without explicit 
programming."""

# Test with obvious human text
human_text = """Hey! So I went to that new coffee shop yesterday and omg their latte was amazing!! 
The barista was super nice too, like really friendly. We should totally go there sometime."""

print("Testing AI text:")
result = classifier(ai_text, top_k=None, truncation=True)
print(f"Raw result: {result}")
print()

print("Testing Human text:")
result = classifier(human_text, top_k=None, truncation=True)
print(f"Raw result: {result}")
