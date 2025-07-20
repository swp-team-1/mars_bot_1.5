# 📄 Instructions for Using Our API

Our endpoints are divided into two APIs:

- AI Model API – the main API used to interact with the model.

- Database Connector API – an internal API used to communicate with the database.

Below are the instructions for using each API:

## AI Model API endpoints:

**POST** **/send_response** - requires only question and responses with one string answer.

- Request body:
```
{
    "question": "string"
}
```

- Response body:
```
"string"
```

**POST** **/send_respose_with_history** - requires question and telegram user id, responses with one string answer taking into account the history of user.

- Request body:
```
{
  "question": "string",
  "user_id": 0
}
```

- Response body:
```
"string"
```

## Database Connector API endpoints:
