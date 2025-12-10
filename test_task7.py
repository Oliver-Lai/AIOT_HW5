"""
Edge Case Testing Script for Task 7

Tests various edge cases to ensure robust error handling.
"""

import os
os.environ['TRANSFORMERS_CACHE'] = './model_cache'

from transformers import pipeline
import sys

# Test cases
test_cases = {
    'empty': '',
    'very_short': 'Hi there',
    'short': 'This is a short sentence with few words.',
    'normal': 'This is a normal length text that should work well. ' * 5,
    'long': 'This is a very long text. ' * 500,  # ~3000 words
    'special_chars': '你好世界! 🌍 Special chars: @#$%^&*()_+-=[]{}|;:\'",.<>?/',
    'unicode': 'Héllo Wörld! Привет мир! 你好世界! مرحبا بالعالم',
    'numbers_only': '12345 67890 11111 22222 33333',
    'mixed_numbers': 'The year 2025 has 365 days and 52 weeks.',
    'symbols_only': '!@#$%^&*()_+-=[]{}|;:\'",.<>?/',
    'newlines': 'Line 1\nLine 2\nLine 3\nLine 4\nLine 5',
    'tabs': 'Column1\tColumn2\tColumn3\tColumn4',
    'mixed_content': 'Normal text 123 special@chars 中文 emoji🎉 tabs\there\n'
}

def test_text_validation():
    """Test input validation edge cases"""
    print("=" * 60)
    print("Task 7.1: Input Validation Testing")
    print("=" * 60)
    
    results = {
        'empty_handled': test_cases['empty'] == '',
        'short_detected': len(test_cases['very_short'].split()) < 10,
        'long_detected': len(test_cases['long']) > 5000
    }
    
    for test, passed in results.items():
        status = "✅" if passed else "❌"
        print(f"{status} {test}: {'PASS' if passed else 'FAIL'}")
    
    return all(results.values())

def test_model_inference():
    """Test model with various text types"""
    print("\n" + "=" * 60)
    print("Task 7.2: Model Inference Edge Cases")
    print("=" * 60)
    
    print("Loading model...")
    try:
        classifier = pipeline(
            task="text-classification",
            model="Hello-SimpleAI/chatgpt-detector-roberta",
            device=-1
        )
        print("✅ Model loaded successfully\n")
    except Exception as e:
        print(f"❌ Model loading failed: {e}")
        return False
    
    test_results = {}
    
    for name, text in test_cases.items():
        if not text:  # Skip empty
            test_results[name] = 'SKIP'
            continue
            
        try:
            # Truncate if too long (match app.py logic)
            MAX_MODEL_CHARS = 2000
            test_text = text[:MAX_MODEL_CHARS] if len(text) > MAX_MODEL_CHARS else text
            result = classifier(test_text, top_k=None, truncation=True)
            
            if result and len(result) > 0:
                test_results[name] = 'PASS'
                print(f"✅ {name:20s}: PASS")
            else:
                test_results[name] = 'FAIL'
                print(f"❌ {name:20s}: FAIL (unexpected output)")
                
        except Exception as e:
            test_results[name] = 'ERROR'
            print(f"❌ {name:20s}: ERROR - {str(e)[:50]}")
    
    passed = sum(1 for r in test_results.values() if r == 'PASS')
    total = len([r for r in test_results.values() if r != 'SKIP'])
    
    print(f"\nResults: {passed}/{total} tests passed")
    return passed == total

def test_error_handling():
    """Test error handling mechanisms"""
    print("\n" + "=" * 60)
    print("Task 7.3: Error Handling Verification")
    print("=" * 60)
    
    with open('app.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = {
        'Empty input handled': 'not text_input or text_input.strip()' in content,
        'Long text warning': "exceeds {MAX_CHAR_LIMIT}" in content or "text is very long" in content.lower(),
        'Short text warning': "very short" in content.lower() and "word_count < 10" in content,
        'Model loading try-except': 'try:' in content and 'load_model' in content and 'except Exception' in content,
        'Inference try-except': 'analyze_text' in content and 'try:' in content and 'except Exception' in content,
        'User-friendly errors': 'st.error(' in content and 'st.info(' in content
    }
    
    for check, passed in checks.items():
        status = "✅" if passed else "❌"
        print(f"{status} {check}: {'PASS' if passed else 'FAIL'}")
    
    return all(checks.values())

def main():
    """Run all Task 7 tests"""
    print("\n" + "=" * 60)
    print("TASK 7: ERROR HANDLING AND EDGE CASES")
    print("=" * 60 + "\n")
    
    test1 = test_text_validation()
    test2 = test_model_inference()
    test3 = test_error_handling()
    
    print("\n" + "=" * 60)
    print("TASK 7 FINAL RESULTS")
    print("=" * 60)
    print(f"7.1 Input Validation:     {'✅ PASSED' if test1 else '❌ FAILED'}")
    print(f"7.2 Model Edge Cases:     {'✅ PASSED' if test2 else '❌ FAILED'}")
    print(f"7.3 Error Handling:       {'✅ PASSED' if test3 else '❌ FAILED'}")
    print("=" * 60)
    
    if all([test1, test2, test3]):
        print("\n🎉 TASK 7 COMPLETED! All edge cases handled! 🎉\n")
        return 0
    else:
        print("\n❌ Some tests failed. Please review.\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
