# AI Search Configuration Validation Changes

## Summary
Modified the codebase to only write results to AI Search when the required search service variables (`search_service_name`, `search_admin_key`, `search_index_name`, and `search_api_version`) are properly populated (not "[redacted]", empty, or None).

## Files Modified

### 1. `doc2md_utils.py`
- **Added**: `should_index_to_ai_search()` function to validate AI Search configuration
- **Modified**: `create_index()` function to check configuration before creating index
- **Modified**: `index_content()` function to check configuration before indexing documents
- **Behavior**: Functions now return early with informative messages if AI Search is not configured

### 2. `docker/main.py`
- **Enhanced**: `should_index()` function to check for "[redacted]" values and empty strings
- **Modified**: `background_task()` function to provide informative messages when indexing is skipped
- **Enhanced**: `/create-index` endpoint to validate parameters before creating index
- **Enhanced**: `/test-search` endpoint to validate parameters before testing search
- **Enhanced**: `/chat` endpoint to validate parameters before performing search operations
- **Behavior**: All AI Search operations now validate configuration and provide helpful error messages

### 3. `docker/test-process-document.ipynb`
- **Added**: Configuration validation before index creation operations
- **Behavior**: Index creation is skipped with informative message if AI Search variables are not configured

### 4. `test-query.ipynb`
- **Added**: Configuration validation before creating SearchClient
- **Modified**: SearchClient creation to be conditional based on configuration
- **Behavior**: Displays warning message if AI Search is not configured, sets clients to None

### 5. `analyze_datasheets.ipynb`
- **Added**: Configuration validation before creating SearchClient instances
- **Modified**: Both SearchClient creation points to be conditional
- **Behavior**: Displays warning message and creates empty dataframe if AI Search is not configured

## Validation Logic
All validation checks for the following conditions in search variables:
- `None` values
- Empty strings (`""`)
- Whitespace-only strings
- Placeholder values (`"[redacted]"`)

## User Experience Improvements
- **Clear Messages**: Users now receive informative messages when AI Search operations are skipped
- **Graceful Degradation**: Applications continue to work for non-search operations even when AI Search is not configured
- **Consistent Validation**: Same validation logic applied across all entry points (API endpoints, notebooks, utility functions)
- **Error Prevention**: Prevents failed API calls to Azure AI Search when credentials are not properly configured

## Backward Compatibility
- All changes are backward compatible
- Existing functionality works unchanged when AI Search is properly configured
- No breaking changes to API interfaces
