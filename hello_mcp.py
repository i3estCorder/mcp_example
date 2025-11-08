"""Simple FastMCP server providing sample greeting and time utilities."""
from datetime import datetime, timezone
from typing import Optional

from fastmcp import FastMCP

app = FastMCP(
    name="simple-fastmcp",
    instructions=(
        "A minimal example MCP server implemented with FastMCP. "
        "Use the available tools to greet users or check the current time."
    ),
)


@app.tool()
def say_hello(name: Optional[str] = None) -> str:
    """Return a friendly greeting for the provided name.

    Parameters
    ----------
    name:
        The person to greet. If None or empty, defaults to "there".

    Returns
    -------
    str:
        A friendly greeting message.

    Examples
    --------
    >>> say_hello("Alice")
    'Hello, Alice!'
    >>> say_hello("")
    'Hello, there!'
    """
    if not name or not name.strip():
        return "Hello, there!"

    clean_name = name.strip()
    return f"Hello, {clean_name}!"


@app.tool()
def current_time() -> str:
    """Return the current UTC time as an ISO-8601 string.

    The returned timestamp is timezone-aware and omits sub-second precision
    to keep the example output stable between runs.

    Returns
    -------
    str:
        Current UTC time in ISO-8601 format (e.g., "2024-01-01T12:00:00+00:00").

    Examples
    --------
    >>> current_time()
    '2024-01-01T12:00:00+00:00'
    """
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


if __name__ == "__main__":
    app.run()
