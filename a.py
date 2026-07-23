

@app.get("/score/v2")
def score_v2(a: int, b: str, c: int) -> int:
    calcul(a, b, c)


def app():
    a = 1
    b = ""
    c = 36
    requests.get((a, b, c)