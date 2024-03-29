from dataclasses import dataclass, field  # Import the 'field' function explicitly
import random
import string

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))

@dataclass
class Student:
    name: str
    surname: str = ""
    active: bool = True
    login: str = ""
    id: str = field(default_factory=generate_id)
