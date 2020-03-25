def hello_generator():
    yield "hello"
    yield "world"
    yield "one"
    yield "more"
    yield "time"


for term in hello_generator():
    print(term)
