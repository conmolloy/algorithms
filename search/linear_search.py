def linear_search(hay_stack: list[str], needle: str) -> bool:
    for hay in hay_stack:
        if hay == needle:
            return True
    return False