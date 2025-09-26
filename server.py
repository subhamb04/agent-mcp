import re
from fastmcp import FastMCP

mcp = FastMCP("PII Privacy Server")

patterns = {
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "phone": r"\b\d{10}\b",
    "credit_card": r"\b(?:\d[ -]*?){13,16}\b",
    "ssn": r"\b\d{3}-\d{2}-\d{4}\b"
}

@mcp.tool
def scan_document(text: str) -> dict:
    """Scan text and return sensitive info findings."""
    findings = []
    for label, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            findings.append({"type": label, "value": match.group()})
    return {"findings": findings}

@mcp.tool
def redact_document(text: str) -> str:
    """Redact sensitive info from text."""
    redacted = text
    for label, pattern in patterns.items():
        redacted = re.sub(pattern, f"[REDACTED-{label.upper()}]", redacted)
    return redacted

if __name__ == "__main__":
    mcp.run()
