# 🔐 PII Privacy Checker with MCP + Agentic AI

A privacy-focused AI agent that fetches data from URLs, scans for PII (Personally Identifiable Information), and returns safely redacted versions using Model Context Protocol (MCP) integration.

## Features

- **URL Data Fetching**: Securely fetch content from any URL
- **PII Detection**: Automatically detect emails, phone numbers, credit cards, and SSNs
- **Intelligent Redaction**: Replace sensitive information with safe markers
- **Interactive Web UI**: Easy-to-use Gradio interface
- **MCP Integration**: Uses Model Context Protocol for extensible tool integration
- **Gemini AI Powered**: Backed by Google's Gemini-2.5-flash model

## Detected PII Types

- **Email addresses**: Valid email format detection
- **Phone numbers**: 10-digit phone numbers
- **Credit cards**: 13-16 digit credit card patterns
- **SSN**: Social Security Numbers (XXX-XX-XXXX format)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd agent-mcp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with your Google API key:
```
GOOGLE_API_KEY=your_google_api_key_here
```

## Usage

### Starting the Application

Run the main application:
```bash
python agent.py
```

This will launch the Gradio web interface at the URL shown in the terminal (typically `http://127.0.0.1:7860`).

### Using the Interface

1. **Enter URL**: Input the URL of the webpage or file you want to analyze
2. **Click "Check for PII"**: The agent will fetch the content, scan for PII, and return the redacted version
3. **View Results**: The redacted content will appear in the output box

### Manual Python Usage

You can also use the agent programmatically:

```python
from agent import process_url

# Fetch and analyze content from a URL
result = process_url("https://example.com/data.txt")
print(result)
```

## Project Structure

- **`agent.py`**: Main application with Gradio UI and agent orchestration
- **`server.py`**: MCP server for PII scanning and redaction
- **`gemini_client.py`**: Google Gemini AI client configuration
- **`requirements.txt`**: Python dependencies

## Dependencies

- **fastmcp**: MCP server framework
- **agents**: AI agent framework
- **gradio**: Web interface
- **openai**: LLM client interface
- **python-dotenv**: Environment variable management
- **requests**: HTTP requests
- **uv**: Python package manager

## Requirements

- Python 3.8 or higher
- Google API key for Gemini access
- Internet connection for URL fetching and AI processing

## Security Features

- **Safe PII Detection**: Uses regex patterns to identify sensitive information
- **Secure Redaction**: Replaces PII with safe markers
- **No Data Storage**: Content is processed in-memory only
- **MCP Protocol**: Secure communication between components

## Example Output

Input (URL with personal data):
```
https://example.com/contact.txt
Content: "Contact John at john@email.com or call (555) 123-4567"
```

Output:
```
[REDACTED-EMAIL] or call [REDACTED-PHONE]
```

## Development

To modify or extend the PII detection patterns, edit the `patterns` dictionary in `server.py`:

```python
patterns = {
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "phone": r"\b\d{10}\b",
    "new_pattern": r"your_custom_regex_here"
}
```

## License

This project is open source and available under the MIT License.
