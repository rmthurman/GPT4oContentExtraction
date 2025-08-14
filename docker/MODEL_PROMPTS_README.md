# Model-Specific Prompt System

This repository now includes a model-specific prompt system that automatically provides different default prompts based on the GPT model being used.

## Overview

The system addresses the issue where different OpenAI models (gpt-4o, gpt-4-vision, gpt-35-turbo, etc.) perform better with different prompt styles and structures.

## How It Works

### 1. Model Prompts Configuration
- Configuration stored in `docker/files/model_prompts.json`
- Each model has a specific prompt optimized for its capabilities
- Fallback mechanism to default prompt for unknown models

### 2. Automatic Prompt Selection
The `get_model_specific_prompt()` function:
- Takes the model name as input
- Returns the appropriate prompt for that model
- Falls back gracefully to default prompts

### 3. Integration Points
- **Image Processing**: `extract_markdown_from_image()` now uses model-specific prompts
- **Web Interface**: Form defaults now use model-specific prompts
- **Settings**: Template loading considers model type

## Supported Models

| Model | Prompt Strategy |
|-------|----------------|
| `gpt-4o-2024-05-13` | Specialized for image citation referencing with URL parsing |
| `gpt-4o` | Enhanced markdown extraction with structure preservation |
| `gpt-4-vision` | Document analysis focus with visual element handling |
| `gpt-4-turbo` | Balanced approach with accuracy emphasis |
| `gpt-4` | Thorough analysis with comprehensive content extraction |
| `gpt-35-turbo` | Simple, efficient markdown conversion |
| `default` | Basic extraction for unknown models |

## Special Case: gpt-4o-2024-05-13

This model includes a specialized prompt designed to handle image references in the format:
```
||https://example.com/image.png||
Content text here
```

Expected output format:
```
Success: The capital of Canada is Ottawa.
[img1.png](https://www.test.com)
```

## Testing

Run the demonstration script:
```bash
cd docker
python test_model_prompts.py
```

## Configuration

To add a new model or modify existing prompts, edit `docker/files/model_prompts.json`:

```json
{
    "your-model-name": {
        "prompt": "Your custom prompt here..."
    }
}
```

## Files Modified

- `docker/main.py`: Added `get_model_specific_prompt()` function and integrated it
- `docker/files/model_prompts.json`: Model-specific prompt configuration
- `docker/Dockerfile`: Updated to include the new configuration file
- `docker/test_model_prompts.py`: Demonstration and testing script

## Backward Compatibility

The system maintains full backward compatibility:
- Existing custom prompts in settings are still respected
- Default behavior preserved for unknown models
- All existing API endpoints continue to work unchanged
