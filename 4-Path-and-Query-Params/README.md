# Path Parameters:

These are the dynamic segments of a URL path used to identify a specific resource.

It is extensively used in `Retrieve`, `Update` and `Delete` operations for data in the database.

## Path() Function:

It is used to provide metadata, validation rules and documentation hints for path parameters in your API endpoint.

## HTTP Status Code:

These are 3-digit numbers returned by a web server to indicate the result of a client's request.

They help the client understand:

- Whether the request was successful.

- Whether something was wrong.

- What kind of issue occured.

---

2xx : The request was successfully received and processed.

3xx : Further action needs to be taken.

4xx : Something is wrong with the request from the client.

5xx : Something is wrong on the server side.

## HTTPException:

It is a special built-in exception used to return custom HTTP error response when something goes wrong in your API.

---

# Query Paramters:

These are the optional key-value pairs appended to the end of the URL, used to pass additional data to the server in an HTTP request. These are used for filtering, sorting, searching and pagination operations.

- The `?` marks the start of query paramter.

- Multiple query paramters are separated by `&`.

## Query() Function:

It is a utility function provided by FastAPI to declare, validate and document query paramters in API endpoints.