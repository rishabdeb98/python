def greet(name: str = "Guest") -> str:
    """Return a friendly greeting. Uses 'Guest' when name is empty/whitespace."""
    clean = (name or "").strip()
    if not clean:
        clean = "Guest"
    return f"Hello, {clean.title()}! Welcome!"
