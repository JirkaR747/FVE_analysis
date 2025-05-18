"""
Modul s pomocnými funkcemi pro validaci vstupů.
"""

def validate_non_negative(name: str, *values):
    """Ověří, že všechny předané hodnoty jsou nezáporné."""
    for v in values:
        if v < 0:
            raise ValueError(f"{name} musí být nezáporné, ale bylo zadáno {v}")
