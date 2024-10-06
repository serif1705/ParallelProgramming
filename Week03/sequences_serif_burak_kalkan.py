def remove_duplicates(seq: list) -> list:

    return list(dict.fromkeys(seq))

def list_counts(seq: list) -> dict:
  
    return {x: seq.count(x) for x in seq}

def reverse_dict(d: dict) -> dict:

    return {value : key for key, value in d.items()}
