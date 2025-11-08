"""Simple FastMCP server providing sample greeting and time utilities."""
from datetime import datetime, timezone

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
    """Return a friendly greeting for the provided ``name``.

    Parameters
    ----------
    name:
        The person to greet.
    """
    clean_name = name.strip() or "there"
    return f"Hello, {clean_name}!"


@app.tool()
def current_time() -> str:
    """Return the current UTC time as an ISO-8601 string.

    The returned timestamp is timezone-aware and omits sub-second precision to
    keep the example output stable between runs.
    """
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


if __name__ == "__main__":
    app.run()
