#!/usr/bin/env python3
"""
Demonstration script showing model-specific prompt functionality
"""
import json
import os
from typing import Optional

def get_model_specific_prompt(model_name: str, custom_prompt: Optional[str] = None) -> str:
    """
    Get the appropriate prompt based on the model type and version.
    Falls back to custom prompt, then model-specific prompt, then default.
    """
    if custom_prompt:
        return custom_prompt
    
    try:
        # Load model prompts configuration
        model_prompts_path = os.path.join('files', 'model_prompts.json')
        with open(model_prompts_path, 'r') as f:
            model_prompts = json.load(f)
        
        # Normalize model name for lookup
        model_key = model_name.lower().strip()
        
        # Try exact match first
        if model_key in model_prompts:
            return model_prompts[model_key]["prompt"]
        
        # Try partial matches for common model patterns
        if "gpt-4o" in model_key:
            if "gpt-4o-2024-05-13" in model_prompts:
                return model_prompts["gpt-4o-2024-05-13"]["prompt"]
            elif "gpt-4o" in model_prompts:
                return model_prompts["gpt-4o"]["prompt"]
        elif "gpt-4-vision" in model_key or "gpt-4v" in model_key:
            if "gpt-4-vision" in model_prompts:
                return model_prompts["gpt-4-vision"]["prompt"]
        elif "gpt-4-turbo" in model_key:
            if "gpt-4-turbo" in model_prompts:
                return model_prompts["gpt-4-turbo"]["prompt"]
        elif "gpt-4" in model_key:
            if "gpt-4" in model_prompts:
                return model_prompts["gpt-4"]["prompt"]
        elif "gpt-35-turbo" in model_key or "gpt-3.5-turbo" in model_key:
            if "gpt-35-turbo" in model_prompts:
                return model_prompts["gpt-35-turbo"]["prompt"]
        
        # Fall back to default
        return model_prompts.get("default", {}).get("prompt", 
            "Extract everything you see in this image to markdown. Convert all charts such as line, pie and bar charts to markdown tables and include a note that the numbers are approximate.")
    
    except Exception as e:
        print(f"Error loading model prompts: {e}")
        # Return hardcoded default if file loading fails
        return "Extract everything you see in this image to markdown. Convert all charts such as line, pie and bar charts to markdown tables and include a note that the numbers are approximate."

def main():
    print("🚀 Model-Specific Prompt System Demonstration")
    print("=" * 70)
    
    # Test models with specific versions
    test_models = [
        # GPT-4o variants
        "gpt-4o-2024-11-20",
        "gpt-4o-2024-08-06", 
        "gpt-4o-2024-05-13",
        "gpt-4o",
        "gpt-4o-mini",
        "gpt-4o-mini-2024-07-18",
        
        # GPT-4 variants
        "gpt-4-1106-vision-preview",
        "gpt-4-vision-preview",
        "gpt-4-turbo-2024-04-09",
        "gpt-4-0125-preview", 
        "gpt-4-turbo",
        "gpt-4-0613",
        "gpt-4-32k",
        "gpt-4",
        
        # GPT-3.5 variants
        "gpt-35-turbo-0125",
        "gpt-35-turbo-1106",
        "gpt-35-turbo-16k", 
        "gpt-35-turbo",
        "gpt-3.5-turbo-16k",
        "gpt-3.5-turbo",
        
        # Claude variants
        "claude-3-opus",
        "claude-3-sonnet",
        "claude-3-haiku",
        
        # Unknown model
        "unknown-model-v2024"
    ]
    
    for model in test_models:
        print(f"\n📋 Model: {model}")
        print("-" * 40)
        
        prompt = get_model_specific_prompt(model)
        prompt_preview = prompt[:150] + "..." if len(prompt) > 150 else prompt
        
        print(f"Prompt length: {len(prompt)} characters")
        print(f"Preview: {prompt_preview}")
    
    # Special demonstration for version-specific behavior
    print("\n" + "=" * 70)
    print("🎯 VERSION-SPECIFIC TESTING")
    print("=" * 70)
    
    version_tests = [
        ("gpt-4o-2024-05-13", "Original version with specialized image citation handling"),
        ("gpt-4o-2024-08-06", "Updated version with improved document analysis"),
        ("gpt-4o-2024-11-20", "Latest version with enhanced structure preservation"),
        ("gpt-4o-mini", "Efficient mini version"),
        ("gpt-4-vision-preview", "Vision-focused GPT-4 variant"),
        ("gpt-4-turbo-2024-04-09", "Latest turbo version with enhanced capabilities")
    ]
    
    for model, description in version_tests:
        print(f"\n🔍 Testing: {model}")
        print(f"Description: {description}")
        prompt = get_model_specific_prompt(model)
        print(f"Prompt type: {'Custom version-specific' if len(prompt) > 200 else 'Generic fallback'}")
        print(f"Length: {len(prompt)} chars")
        
    print(f"\n📝 Key Benefits:")
    print("✅ Version-specific prompts for optimal performance")
    print("✅ Graceful fallback for unknown models")  
    print("✅ Maintains backward compatibility")
    print("✅ Easy to extend with new model versions")

if __name__ == "__main__":
    main()
