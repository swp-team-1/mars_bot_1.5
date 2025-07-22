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
    <a href="https://swp-team-1.github.io/mars_bot_1.5/"><strong>Explore the docs »</strong></a>
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
    <li><a href="#usage-guide">Usage Guide</a></li>
    <li><a href="#feature-roadmap">Feature Roadmap</a></li>
    <li><a href="https://hermitdesu.github.io/mars_bot_1.5/development/">Development (on github pages)</a></li>
    <li><a href="https://hermitdesu.github.io/mars_bot_1.5/quality_assurance/">Quality Assurance (on github pages)</a></li>
    <li><a href="https://hermitdesu.github.io/mars_bot_1.5/deployment/">Build & Deployment (on github pages)</a></li>
    <li><a href="#architecture">Architecture</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contacts">Contacts</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
</ol>

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

### 🐳 Docker Deployment

To run the project locally using Docker:
1. Clone the repository:
```bash
git clone https://github.com/swp-team-1/mars_bot_1.5.git
cd mars_bot_1.5
```
2. Create an .env file:

- Copy the example and fill in your configuration:
```bash
cp .env.example .env
```
- Edit .env and provide your values, for example:
```bash
TELEGRAM_BOT_TOKEN="your_telegram_bot_token"
```
3. Build the Docker image:
```bash
docker build --network=host -t mars-bot .
```
4. Run the Docker container:
```bash
docker run --env-file .env mars-bot
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

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



## 📬 Contacts


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


## 📚 Documentation
[Documenttation on Github Pages](https://swp-team-1.github.io/mars_bot_1.5/)

- [CONTRIBUTING.md](docs/CONTRIBUTING.md)
- [Quality Attribute Scenarios](docs/quality-assurance/quality-attribute-scenarios.md)
- [Quality assurance](https://github.com/swp-team-1/database_conector/tree/main/tests)
- [CI Workflow](https://github.com/swp-team-1/database_conector/blob/main/.github/workflows/test.yml)
- [CD Process](docs/automation/continuous-delivery.md)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
  
## 🏗 Architecture
- [Static View](docs/architecture/static-view.md)
- [Dynamic View](docs/architecture/dynamic-view.md)
- [Deployment View](docs/architecture/deployment-view.md)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## How to use API(for customer)

## Fine-tuning AI Model (for customer)

> **Why this is important:**  
> This section is necessary so that the customer can independently repeat the process of training the model, understand the data requirements and the steps necessary for successful fine-tuning. Following these instructions, you will be able to get a similar result without additional consultations.

📄 **Complete step-by-step instructions:**
[Fine_Tune_guide-1.pdf](./docs/Fine_Tune_guide-1.pdf)


