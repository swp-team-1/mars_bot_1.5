# Build and deployment

## Railway deployment instructions
The **_Railway_** service is used to deploy our project. To repeat the project deployment, you can follow these steps:

1. Register or log in to your Railway account

2. Click to button to deploy new project

![second_step](deploy_instruction_pictures/first_step.png)

3. And choose project to deploy from the Github

![third_step](deploy_instruction_pictures/second_step.png)

4. Add enviroment variables:

![fourth_step](deploy_instruction_pictures/third_step.png)

- 4.1 Set your bot token
- 4.2 Set webhook URL. You can find it in Settings -> Networking section

![fourth_second_step](deploy_instruction_pictures/fourth_step.png)

6. Deploy project and make adjustments according to the logs
![fifth_second_step](deploy_instruction_pictures/congradilations.png)

## 📦 Manual deployment

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