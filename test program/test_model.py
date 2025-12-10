"""
Simple test script to verify the analyze_text function works correctly
"""

import os
os.environ['TRANSFORMERS_CACHE'] = './model_cache'

from transformers import pipeline

MODEL_NAME = "openai-community/roberta-base-openai-detector"

print("🔄 Loading model...")
classifier = pipeline(
    task="text-classification",
    model=MODEL_NAME,
    device=-1
)

print("✅ Model loaded successfully!\n")

# Test with AI-generated text (typical ChatGPT response)
ai_text = """
Artificial intelligence has revolutionized numerous industries in recent years. 
From healthcare to finance, AI-powered systems are enabling more efficient 
decision-making and automation. Machine learning algorithms can now analyze 
vast amounts of data to identify patterns and make predictions with remarkable accuracy.
"""

# Test with human-written text
human_text = """
Hey! So I went to that new coffee shop yesterday and omg their latte was amazing!! 
The barista was super nice too. We should totally go there sometime, what do you think? 
Also did you finish that homework assignment yet? I'm still stuck on question 3 lol
"""

print("=" * 60)
print("Test 1: AI-Generated Text")
print("=" * 60)
result = classifier(ai_text, return_all_scores=True)
print(f"Raw result: {result}")

if isinstance(result, list) and len(result) > 0:
    scores = result[0] if isinstance(result[0], list) else result
    for item in scores:
        label = item.get('label', '')
        score = item.get('score', 0.0)
        print(f"  {label}: {score*100:.1f}%")

print("\n" + "=" * 60)
print("Test 2: Human-Written Text")
print("=" * 60)
result = classifier(human_text, return_all_scores=True)
print(f"Raw result: {result}")

if isinstance(result, list) and len(result) > 0:
    scores = result[0] if isinstance(result[0], list) else result
    for item in scores:
        label = item.get('label', '')
        score = item.get('score', 0.0)
        print(f"  {label}: {score*100:.1f}%")

print("\n✅ All tests completed!")
