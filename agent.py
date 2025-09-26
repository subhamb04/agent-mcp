import asyncio
import gradio as gr
from agents.mcp import MCPServerStdio
from agents import Agent, Runner, function_tool
from gemini_client import client  # <-- replace with your OpenAI/Gemini client
import sys, os

# --- MCP Servers ---
mcp_fetch = MCPServerStdio(params={
    "command": "uvx",
    "args": ["mcp-server-fetch"],
    "client_session_timeout_seconds": 30
})

mcp_pii = MCPServerStdio(params={
    "command": "python",
    "args": ["server.py"],  # your custom PII server
    "client_session_timeout_seconds": 30
})


# --- Main logic ---
async def run_agent(url: str):
    async with mcp_fetch, mcp_pii:
        agent = Agent(
            name="PrivacyAssistant",
            model=client,
            instructions="You are a privacy assistant. Fetch data from URL, scan for PII, and return a safe version.",
            mcp_servers=[mcp_fetch, mcp_pii],
        )

        query = f"""
        Fetch {url}, scan the content for PII, and give me a safe redacted version.
        """
        result = await Runner.run(agent, query)
        return result.final_output


def process_url(url: str):
    return asyncio.run(run_agent(url))


# --- Gradio UI ---
with gr.Blocks() as demo:
    gr.Markdown("## 🔐 PII Privacy Checker with MCP + Agentic AI")

    url_input = gr.Textbox(label="Enter URL to fetch data", placeholder="https://example.com/data.txt")
    output = gr.Textbox(
        label="Safe Redacted Output",
        lines=15,          # bigger height
        max_lines=30,      # allow scroll if too long
        placeholder="Sanitized text will appear here..."
    )

    submit = gr.Button("Check for PII")
    submit.click(fn=process_url, inputs=url_input, outputs=output)

demo.launch()
