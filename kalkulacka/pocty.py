ans:float = 0

def plus(a:float, b:float) -> None:
    save(a+b)

def multi(a:float, b:float) -> None:
    save(a*b)

def save(a: float) -> None:
    global ans
    ans = a

def result() -> float:
    return ans