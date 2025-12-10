"""
Validation script for Tasks 4-6: UI Components

This script verifies that all UI components are correctly implemented.
"""

import ast
import re

def check_task_4():
    """Verify Task 4: Header Section"""
    print("=" * 60)
    print("Task 4: Build User Interface - Header Section")
    print("=" * 60)
    
    with open('app.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = {
        'Title': 'st.title("🔍 AI Content Detector")' in content or 'st.title(\'🔍 AI Content Detector\')' in content,
        'Subtitle/Description': 'st.markdown(' in content and 'paste your text' in content.lower(),
        'Model Information': 'st.info(' in content and 'MODEL_NAME' in content,
        'Usage Instructions': 'Simply paste' in content or 'click' in content.lower()
    }
    
    for check, passed in checks.items():
        status = "✅" if passed else "❌"
        print(f"{status} {check}: {'PASS' if passed else 'FAIL'}")
    
    all_passed = all(checks.values())
    print(f"\n{'✅ Task 4 PASSED' if all_passed else '❌ Task 4 FAILED'}\n")
    return all_passed

def check_task_5():
    """Verify Task 5: Input Section"""
    print("=" * 60)
    print("Task 5: Build User Interface - Input Section")
    print("=" * 60)
    
    with open('app.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = {
        'Text Area Widget': 'st.text_area(' in content,
        'Height Setting': 'height=200' in content or 'height = 200' in content,
        'Placeholder Text': 'placeholder=' in content and 'analyze' in content.lower(),
        'Analyze Button': 'st.button(' in content and 'Analyze' in content,
        'Empty Input Validation': 'not text_input' in content or 'text_input.strip()' in content,
        'Error Message': 'st.error(' in content and 'enter some text' in content.lower()
    }
    
    for check, passed in checks.items():
        status = "✅" if passed else "❌"
        print(f"{status} {check}: {'PASS' if passed else 'FAIL'}")
    
    all_passed = all(checks.values())
    print(f"\n{'✅ Task 5 PASSED' if all_passed else '❌ Task 5 FAILED'}\n")
    return all_passed

def check_task_6():
    """Verify Task 6: Results Section"""
    print("=" * 60)
    print("Task 6: Build User Interface - Results Section")
    print("=" * 60)
    
    with open('app.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = {
        'Conditional Rendering': 'if analyze_button:' in content,
        'Loading Spinner': 'st.spinner(' in content and 'Analyzing' in content,
        'Progress Bar': 'st.progress(' in content and 'ai_probability' in content.lower(),
        'Main Result Display': 'st.metric(' in content or ('AI Probability' in content and 'Human Probability' in content),
        'AI/Human Percentages': "results['ai_probability']" in content and "results['human_probability']" in content,
        'Success Message (Human)': 'st.success(' in content,
        'Warning Message (Mixed)': 'st.warning(' in content,
        'Error Message (AI)': 'st.error(' in content and 'appears to be' in content.lower(),
        'Confidence Level': "results['confidence_level']" in content or 'Confidence Level' in content
    }
    
    for check, passed in checks.items():
        status = "✅" if passed else "❌"
        print(f"{status} {check}: {'PASS' if passed else 'FAIL'}")
    
    all_passed = all(checks.values())
    print(f"\n{'✅ Task 6 PASSED' if all_passed else '❌ Task 6 FAILED'}\n")
    return all_passed

def main():
    """Run all validation checks"""
    print("\n" + "=" * 60)
    print("VALIDATION: Tasks 4-6 UI Components")
    print("=" * 60 + "\n")
    
    task4 = check_task_4()
    task5 = check_task_5()
    task6 = check_task_6()
    
    print("=" * 60)
    print("FINAL RESULTS")
    print("=" * 60)
    print(f"Task 4 (Header Section):  {'✅ PASSED' if task4 else '❌ FAILED'}")
    print(f"Task 5 (Input Section):   {'✅ PASSED' if task5 else '❌ FAILED'}")
    print(f"Task 6 (Results Section): {'✅ PASSED' if task6 else '❌ FAILED'}")
    print("=" * 60)
    
    if all([task4, task5, task6]):
        print("\n🎉 ALL TASKS PASSED! UI Implementation Complete! 🎉\n")
        return 0
    else:
        print("\n❌ Some tasks failed. Please review the implementation.\n")
        return 1

if __name__ == "__main__":
    exit(main())
