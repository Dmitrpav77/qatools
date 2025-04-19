from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    salary: int = None
    mobile: str = None
    date_of_birth: str = None
    age: int = None
    department: str = None
    current_address: str = None
    permanent_address: str = None