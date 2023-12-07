import typing

def f1(x: int, y: str):
    ...

print(tuple(typing.get_type_hints(f1).values()))