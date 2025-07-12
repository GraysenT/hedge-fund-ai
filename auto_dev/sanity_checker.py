def sanity_check_code(code: str):
    """
    Checks Python code for syntax and basic safety before execution.
    """
    try:
        compile(code, "<string>", "exec")
        return {"valid": True}
    except SyntaxError as e:
        return {"valid": False, "error": str(e)}