"""Simple FastMCP server providing a greeting tool."""
from datetime import datetime

from fastmcp import FastMCP

app = FastMCP(
    name="simple-fastmcp",
    instructions=(
        "A minimal example MCP server implemented with FastMCP. "
        "Use the available tools to greet users or check the current time."
    ),
)


@app.tool()
def say_hello(name: str) -> str:
    """Return a friendly greeting for the provided name."""
    return f"Hello, {name}!"


@app.tool()
def current_time() -> str:
    """Return the current UTC time as an ISO-8601 string."""
    return datetime.utcnow().isoformat()


if __name__ == "__main__":
    app.run()
