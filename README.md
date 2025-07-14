<!-- Improved compatibility of back to top link -->
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]

<!-- HEADER -->
<br />
<div align="center">
  <a href="https://github.com/swp-team-1/mars_bot_1.5">
    <img src="docs/Logo.png" alt="Logo" width="250" height="250">
  </a>

  <h3 align="center">Multi Agent Recommender System (MARS)</h3>

  <p align="center">
    A Telegram Bot and API that helps users with namaz-related questions using a multi-agent recommender architecture.
    <br />
    <a href="https://hermitdesu.github.io/mars_bot_1.5/"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://drive.google.com/file/d/1pu5FLFF-mL6AW8gWz7RMm9B7M8P0bstP/view">📺 Watch Demo Video</a>
    <br />
    <a href="https://t.me/mvp_1_5_bot">🌐 View Product</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#project-goal-and-description">Project Goal and Description</a></li>
    <li><a href="#project-context-diagram">Project Context Diagram</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage Guide</a></li>
    <li><a href="#roadmap">Feature Roadmap</a></li>
    <li><a href="#development">Development</a></li>
    <li><a href="#quality-assurance">Quality Assurance</a></li>
    <li><a href="#build-and-deployment">Build & Deployment</a></li>
    <li><a href="#architecture">Architecture</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## 🧭 Project Goal and Description

The goal of this project is to build a multi-agent recommendation system that assists users with Islamic prayer guidance through an interactive Telegram bot. The system is backed by a FastAPI server and uses MongoDB to store users and conversations.


### Key Objectives:
- Provide helpful recommendations and answers about namaz in a conversational way.
- Maintain and analyze user interactions to improve personalized responses.

### System Structure:
- A **Telegram bot** (using `python-telegram-bot`) that communicates with users.
- A **FastAPI backend** that handles data storage, business logic, and API routing.
- A **MongoDB database** accessed via the async `motor` driver.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## 🧩 Project Context Diagram

![Project Context Diagram](structure/Project_context_diagram.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🛠️ Built With

[![Python][Python-shield]][Python-url]
[![FastAPI][FastAPI-shield]][FastAPI-url]
[![MongoDB][Mongo-shield]][Mongo-url]
[![Motor][Motor-shield]][Motor-url]
[![Telegram Bot API][Telegram-shield]][Telegram-url]
[![Pydantic][Pydantic-shield]][Pydantic-url]
[![Dotenv][Dotenv-shield]][Dotenv-url]
[![Uvicorn][Uvicorn-shield]][Uvicorn-url]
[![HTTPX][Httpx-shield]][Httpx-url]
[![Requests][Requests-shield]][Requests-url]
[![Docker][Docker-shield]][Docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Entry criteria

| **TO DO**               | **In progress**       | **In review**               | **Ready to deploy**     | **User testing**       | **DONE**          |
|-------------------------------------|----------------------------------|----------------------------------------|------------------------------------|-----------------------------------|-----------------------------|
| - Discussion problem with team members<br><br>- Prioritize among issues<br><br>- A performer has been appointed<br><br>- A branch has been created in the repository | - Prioritize among issues<br><br>- Issues are estimated<br><br>- MR has been created | - Code fully implemented and self-reviewed<br><br>- Pass all tests<br><br>- Branch rebased on main<br><br>- min 2 reviewers assigned | - MR is approved<br><br>- The documentation is updated<br><br>- All tasks for this issue are closed | - Test Environment Ready<br><br>- Customer is informed | - Deployment is done<br><br>- Documentation is done<br><br>- Testing is complete |

## Kanban board
[**Link to the Kanban board**](https://drive.google.com/file/d/1lvN3w-KCPvQyGvFbfXvM-mOQlku4nOV4/view?usp=sharing) or this [**link**](https://drive.google.com/file/d/1SAXZeP9y6pCJRFgHrx-MF7KEN2ItJ8R5/view?usp=sharing), if you have account in Miro 
## 🛣️ Feature Roadmap

- [x] Bot can understand the context
- [x] Bot can understand the app structure
- [x] User can create multiple conversation
- [x] User can ask everything about namaz
- [ ] User can send voice messages
- [ ] Endpoint for Namaz.app
- [ ] Provide the explanation how model work

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## 📘 Usage Guide

### 🤖 Telegram Bot

You can use our bot by launching it using the [provided link](https://t.me/mvp_1_5_bot). No further action is required.


### 🌐 FastAPI Backend

To use the recommender system you can contact us to get API endpoints.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## 🚀 Getting Started

### Railway Deployment instructions
The **_Railway_** service is used to deploy our project. To repeat the project deployment, you can follow these steps:
1. Register or log in to your Railway account
2. Click to button to deploy new project<br>
![second_step](docs/deploy_instruction_pictures/first_step.png)
3. And choose project to deploy from the Github
![third_step](docs/deploy_instruction_pictures/second_step.png)
4. Add enviroment variables:
![fourth_step](docs/deploy_instruction_pictures/third_step.png)
- 4.1 Set your bot token
- 4.2 Set webhook URL. You can find it in Settings -> Networking section
![fourth_second_step](docs/deploy_instruction_pictures/fourth_step.png)
6. Deploy project and make adjustments according to the logs
![fifth_second_step](docs/deploy_instruction_pictures/congradilations.png)

<<<<<<< patch-2
### 📦 Manual deployment

1. Clone the repo:
   ```bash
   git clone https://github.com/swp-team-1/mars_bot_1.5.git
   cd mars_bot_1.5
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Create an `.env` file (copy from `.env.example`) and configure:
   ```env
   BOT_TOKEN=your_telegram_bot_token
   MONGODB_URI=your_mongodb_connection_uri
   ```

5. Run services:
   ```bash
   uvicorn main:app --reload      # FastAPI backend
   python bot_main.py             # Telegram bot
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## 🚀 Contributing

Contributions make the open source community an incredible place to learn and grow. Any help is **greatly appreciated**!

Have an idea to improve `mars_bot_1.5`? Fork the repo, make your changes, and open a pull request. Or just open an issue with the tag `enhancement`.

1. Fork the project  
2. Create your branch (`git checkout -b feature/MyFeature`)  
3. Commit your changes (`git commit -m 'Add MyFeature'`)  
4. Push (`git push origin feature/MyFeature`)  
5. Open a pull request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## 🌟 Top Contributors

<a href="https://github.com/swp-team-1/mars_bot_1.5/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=swp-team-1/mars_bot_1.5" alt="Top contributors" />
</a>



## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## 📬 Contact


- Black-persik – [@black_persik](https://t.me/black_persik)  
- tabletka_812 – [@tabletka_812](https://t.me/tabletka_812)  
- eerterr – [@eerterr](https://t.me/eerterr)  
- Leo_Vesin – [@Leo_Vesin](https://t.me/Leo_Vesin)  
- Desgun4ik – [@Desgun4ik](https://t.me/Desgun4ik)
- Project: [github.com/swp-team-1/mars_bot_1.5](https://github.com/swp-team-1/mars_bot_1.5)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## 🙏 Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) – Telegram Bot Framework  
- [FastAPI](https://github.com/tiangolo/fastapi) – Web framework  
- [Motor](https://github.com/mongodb/motor) – Async MongoDB driver  
- [python-dotenv](https://github.com/theskumar/python-dotenv) – Manage environment variables  
- [contrib.rocks](https://contrib.rocks) – Contributor avatars


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/swp-team-1/mars_bot_1.5.svg?style=for-the-badge
[contributors-url]: https://github.com/swp-team-1/mars_bot_1.5/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/swp-team-1/mars_bot_1.5.svg?style=for-the-badge
[forks-url]: https://github.com/swp-team-1/mars_bot_1.5/network/members
[stars-shield]: https://img.shields.io/github/stars/swp-team-1/mars_bot_1.5.svg?style=for-the-badge
[stars-url]: https://github.com/swp-team-1/mars_bot_1.5/stargazers
[issues-shield]: https://img.shields.io/github/issues/swp-team-1/mars_bot_1.5.svg?style=for-the-badge
[issues-url]: https://github.com/swp-team-1/mars_bot_1.5/issues
[license-shield]: https://img.shields.io/github/license/swp-team-1/mars_bot_1.5.svg?style=for-the-badge
[license-url]: https://github.com/swp-team-1/mars_bot_1.5/blob/main/LICENSE


[Python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[FastAPI-shield]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/

[Mongo-shield]: https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white
[Mongo-url]: https://www.mongodb.com/

[Motor-shield]: https://img.shields.io/badge/Motor-00ACD7?style=for-the-badge
[Motor-url]: https://motor.readthedocs.io/

[Telegram-shield]: https://img.shields.io/badge/python--telegram--bot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white
[Telegram-url]: https://docs.python-telegram-bot.org/

[Pydantic-shield]: https://img.shields.io/badge/Pydantic-00B2FF?style=for-the-badge&logo=pydantic&logoColor=white
[Pydantic-url]: https://docs.pydantic.dev/

[Dotenv-shield]: https://img.shields.io/badge/dotenv-0A0A0A?style=for-the-badge
[Dotenv-url]: https://pypi.org/project/python-dotenv/

[Uvicorn-shield]: https://img.shields.io/badge/Uvicorn-008489?style=for-the-badge&logo=uvicorn&logoColor=white
[Uvicorn-url]: https://www.uvicorn.org/

[Httpx-shield]: https://img.shields.io/badge/HTTPX-003569?style=for-the-badge
[Httpx-url]: https://www.python-httpx.org/

[Requests-shield]: https://img.shields.io/badge/Requests-2C8EBB?style=for-the-badge
[Requests-url]: https://requests.readthedocs.io/

[Docker-shield]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/



=======
## Continuous Integration

Our project uses two separate CI pipelines: one for the database connector and one for the bot.

#### Database connector CI

- **CI Workflow:** [`.github/workflows/test.yml`](https://github.com/hermitdesu/SWP_DB/blob/main/.github/workflows/test.yml)

- **Static Analysis and Testing Tools Used:**
  - **pytest:** Runs automated tests to verify code correctness.
  - **flake8:** Ensures code style consistency and catches simple errors.
  - **bandit:** Scans the codebase for security vulnerabilities.

- **Where to See CI Workflow Runs:**  
  You can view all connector CI workflow runs for this project here:  
  [GitHub Actions Runs](https://github.com/hermitdesu/SWP_DB/actions)

---

#### Bot CI

- **CI Workflow:** [`bot_aio/.github/workflows/test.yml`](https://github.com/Black-persik/bot_aio/blob/tests/.github/workflows/test.yml)

- **Static Analysis and Testing Tools Used:**
  - **flake8:** Ensures code style consistency and catches both critical and stylistic errors.
  - **mypy:** Checks for type errors and enforces type safety.
  - **pytest:** Runs automated tests to verify code correctness.

- **Where to See CI Workflow Runs:**  
  You can view all bot CI workflow runs for this project here:  
  [GitHub Actions Runs](https://github.com/Black-persik/bot_aio/actions)


## Quality assurance

### Automated tests

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
  
### Quality attribute scenarios
[**Description of quality scenarios**](docs/quality-assurance/quality-attribute-scenarios.md)

## 📚 Documentation

- [CONTRIBUTING.md](docs/CONTRIBUTING.md)
- [Quality Attribute Scenarios](docs/quality-assurance/quality-attribute-scenarios.md)
- [Automated Tests](docs/quality-assurance/automated-tests.md)
- [CI Workflow](https://github.com/swp-team-1/database_conector/blob/main/.github/workflows/test.yml)
- [CD Process](docs/automation/continuous-delivery.md)
- ### 🏗 Architecture
- [Static View](docs/architecture/static-view.md)
- [Dynamic View](docs/architecture/dynamic-view.md)
- [Deployment View](docs/architecture/deployment-view.md)
>>>>>>> main
