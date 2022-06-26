def _format_ncc(string: str) -> str:
    return f"{string} - {string}"

def format_ncc_list(list: list) -> list:
    return [_format_ncc(i) for i in list]