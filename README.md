# Secure Python REST API

A beginner-friendly REST API built with Python and FastAPI
demonstrating fundamental API security principles.

## Features

- API key authentication
- Input validation
- Environment-based secrets management
- Constant-time secret comparison
- Automated security tests
- Swagger API documentation

## Installation

pip install -r requirements.txt

## Usage

Generate an API key:

    export API_KEY=$(openssl rand -hex 32)

Start the server:

    uvicorn main:app --reload

## Testing

    pytest -v

## Limitations

This educational project uses in-memory storage and
a shared API key. It is not production-ready.
