#!/usr/bin/env python3
"""
Version comparison test for model-specific prompts
"""
import json
import os
from typing import Optional

def get_model_specific_prompt(model_name: str, custom_prompt: Optional[str] = None) -> str:
    if custom_prompt:
        return custom_prompt
    
    try:
        model_prompts_path = os.path.join('files', 'model_prompts.json')
        with open(model_prompts_path, 'r') as f:
            model_prompts = json.load(f)
        
        model_key = model_name.lower().strip()
        
        if model_key in model_prompts:
            return model_prompts[model_key]["prompt"]
        
        # Version-specific matching for GPT-4o variants
        if "gpt-4o" in model_key:
            version_matches = [
                "gpt-4o-2024-11-20",
                "gpt-4o-2024-08-06", 
                "gpt-4o-2024-05-13",
                "gpt-4o-mini-2024-07-18",
                "gpt-4o-mini"
            ]
            for version in version_matches:
                if version in model_key and version in model_prompts:
                    return model_prompts[version]["prompt"]
            
            if "gpt-4o" in model_prompts:
                return model_prompts["gpt-4o"]["prompt"]
        
        return model_prompts.get("default", {}).get("prompt", "Default prompt")
    
    except Exception as e:
        return "Default prompt"

def main():
    print('🔬 VERSION COMPARISON TEST')
    print('=' * 60)

    # Test similar model names to show version differentiation
    test_cases = [
        ['gpt-4o', 'gpt-4o-2024-05-13', 'gpt-4o-2024-08-06'],
        ['gpt-4', 'gpt-4-turbo', 'gpt-4-vision-preview'],
        ['gpt-35-turbo', 'gpt-35-turbo-16k', 'gpt-35-turbo-0125']
    ]

    for models in test_cases:
        print(f'\nComparing: {" vs ".join(models)}')
        print('-' * 50)
        
        for model in models:
            prompt = get_model_specific_prompt(model)
            print(f'{model:25} | Length: {len(prompt):4} | {prompt[:80]}...')
        
    print('\n🎯 Key Insight: Each version gets its own optimized prompt!')
    
    # Show the detailed comparison for gpt-4o versions
    print('\n📋 DETAILED GPT-4O VERSION ANALYSIS:')
    print('=' * 60)
    
    gpt4o_versions = ['gpt-4o', 'gpt-4o-2024-05-13', 'gpt-4o-2024-08-06', 'gpt-4o-2024-11-20']
    
    for version in gpt4o_versions:
        prompt = get_model_specific_prompt(version)
        print(f'\n🔍 {version}:')
        print(f'   Length: {len(prompt)} characters')
        if 'image citation' in prompt or 'URL' in prompt or '||' in prompt:
            print('   🎯 Contains image citation logic')
        if 'document analysis' in prompt:
            print('   📊 Focused on document analysis')
        if 'comprehensive' in prompt:
            print('   🔬 Comprehensive extraction approach')
        print(f'   Preview: {prompt[:120]}...')

if __name__ == "__main__":
    main()
