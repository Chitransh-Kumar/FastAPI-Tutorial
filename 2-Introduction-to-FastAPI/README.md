# FastAPI:

It is a modern, high-performance web framework for building APIs with python.

- `Starlette`: It manages how your API receives requests and sends back requests.

- `Pydantic`: It is used to check if the data coming into your API is correct and in the right format.

---

## How API information flow works?

1. Client sends request.

2. Web Server receives it.

3. Web server talks to ASGI. 

4. ASGI passes request to FastAPI.

5. Response goes back in reverse order.

---

## Two types of SGI:

1. WSGI: Used in Flask. It can handle one request at a time (synchronous nature).

2. ASGI: Used in FastAPI. It can handle multiple requests at a time (asynchronous nature).