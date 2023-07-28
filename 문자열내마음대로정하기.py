from typing import List

def solution(strings: List[str], n: int) -> List[str]:
    """
    Sorts list of strings based on the n-th character and dictionary order.
    """
    return sorted(strings, key=lambda x: (x[n], x))
