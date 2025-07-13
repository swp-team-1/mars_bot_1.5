# Quality assurance


## Automated tests

- **Tools used for testing:**  
  - `pytest` — the main framework for unit and integration tests in all parts of the project  
  - `pytest-asyncio` — for testing asynchronous code  
  - `unittest` and `unittest.mock` — for integration tests and mocking the database in the backend  

- **Tests that we implemented:**  
  - **Unit tests:**  
    - In the database connector repository:
      - Mock tests for user CRUD operations
      - Mock tests for conversation CRUD operations
      - Mock tests for log CRUD operations
      - Tests for user models
      - Tests for conversation models
      - Tests for log models
    - In the bot repository:
      - `test_start_new_user_unit`: Checks that the start function correctly handles a new user and prompts for a name.
      - `test_start_existing_user_unit`: Checks that the start function correctly handles an already registered user and ends the conversation.
      - `test_get_name_unit`: Verifies that the get_name function saves the user’s name and ends the conversation.
      - `test_cancel_unit`: Ensures the cancel function sends a cancellation message and ends the conversation.
      - `test_help_command_unit`: Checks that the help_command function sends the help message.
  - **Integration tests:**  
    - In the database connector repository:
      - Tests for user API endpoints
      - Tests for conversation API endpoints
      - Tests for log API endpoints
      - Tests for root and health endpoints
    - In the bot repository:
      - `test_full_registration_and_ask_integration`: Simulates a full registration flow and ensures the name is saved.
      - `test_ask_and_ask_handler_integration`: Simulates asking a question and getting a response from the model.
      - `test_cancel_clears_conv_id_integration`: Ensures that cancelling a conversation removes the conversation ID from the user’s context.
      - `test_start_network_error_integration`: Checks that the start function gracefully handles network errors.
      - `test_get_name_network_error_integration`: Checks that the get_name function gracefully handles network errors.

- **Where tests of each type are in the repository:**  
  - In the database connector repository:  
    - All tests are located in the `tests/` directory:
      - Unit tests:  
        - `tests/test_cruds_mock.py`  
        - `tests/test_models_user.py`  
        - `tests/test_models_conv.py`  
        - `tests/test_models_log.py`
      - Integration tests:  
        - `tests/test_api_integration.py`
    - You can see the full test suite [here](https://github.com/hermitdesu/SWP_DB/tree/main/tests).

  - In the bot repository:  
    - All tests are located in the `tests/test_all.py` file.  
    - You can see the full test suite [here](https://github.com/Black-persik/bot_aio/blob/tests/tests/test_all.py).