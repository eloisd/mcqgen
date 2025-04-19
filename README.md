# MCQ Generator Application

A web application that generates multiple-choice questions from PDF and text files using AI.

## A. Deploy Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/eloisd/mcqgen.git
   ```

2. **Navigate to project directory**
   ```bash
   cd mcqgen
   ```

3. **Create and configure environment variables**
   ```bash
   touch .env
   nano .env
   ```
   
   Enter your API keys:
   ```
   OPENAI_API_KEY = "your_openai_api_key"
   ```
   
   Save the file (press "ˆX" then "Y" then "enter")

4. **Verify environment file**
   ```bash
   cat .env
   ```

5. **Create and activate virtual environment**
   ```bash
   python3 -m venv mcqenv
   source mcqenv/bin/activate
   ```

6. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

7. **Run the application**
   ```bash
   python3 -m streamlit run StreamLitApp.py
   ```

## B. Deployment on Heroku

1. **Make sure you have a Heroku account**
   - Sign up at [heroku.com](https://heroku.com) if you don't already have an account

2. **Install the Heroku CLI**
   - Download and install from [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
   - Verify installation with `heroku --version`

3. **Log in to Heroku via CLI**
   ```bash
   heroku login
   ```

4. **Create a new Heroku app**
   ```bash
   heroku create mcqgen-app
   ```
   (Replace "mcqgen-app" with your preferred unique app name)

5. **Set up environment variables**
   - Add your OpenAI API key to Heroku:
   ```bash
   heroku config:set OPENAI_API_KEY=your_openai_api_key
   ```
   <!-- - If you're using HuggingFace, add that too:
   ```bash
   heroku config:set HUGGINGFACE_API_KEY=your_huggingface_api_key
   ``` -->

6. **Make sure your Procfile is correctly configured**
   - Your current Procfile has:
   ```
   web: sh setup.sh && streamlit run StreamLitApp.py
   ```
   - This is correct if your main file is indeed named StreamLitApp.py at the root level

7. **Add setup.sh file**
   ```bash
   #!/bin/bash
   mkdir -p ~/.streamlit
   cat > ~/.streamlit/config.toml << EOF
   [server]
   headless = true
   port = $PORT
   enableCORS = false
   EOF
   ```
   - Make sure the file has the proper permissions:
   ```bash
   chmod +x setup.sh
   ```

8. **Commit all changes to git**
   ```bash
   git add .
   git commit -m "Preparing for Heroku deployment"
   ```

9. **Push to Heroku**
   ```bash
   git push heroku main
   ```
   (Use `git push heroku master` if your branch is named "master" instead of "main")

10. **Open your app**
    ```bash
    heroku open
    ```

### Additional Deployment Tips
- **Monitor logs to troubleshoot**
  ```bash
  heroku logs --tail
  ```

### Delete Your App
  ```bash
  heroku apps:destroy
  ```

  - Verify that it's done 
  ```bash
  heroku apps --all
  ```

## C. Deployment on AWS

1. **Set up AWS EC2 instance**
   - Create account or login on AWS
   - Search for "EC2"
   - Click "Launch instance"
   - Complete forms:
     * Name: mcqgen
     * OS: Ubuntu
     * Instance: t2.large
     * Key pair: Create
       * Name: mcqkey
       * RSA
       * .pem
     * 16GB
     * Click launch

2. **Connect to your instance**
   - Wait for initialization
   - Click on the instance ID
   - Click on "Connect"

3. **Set up the server environment**
   ```bash
   sudo apt update
   sudo apt-get update
   sudo apt upgrade -y
   sudo apt install git curl unzip tar make sudo vim wget zsh python3-pip -y
   sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
   sudo chsh -s $(command -v zsh)
   ```

4. **Clone the repository**
   ```bash
   git clone https://github.com/eloisd/mcqgen.git
   ```

5. **Navigate to project directory**
   ```bash
   cd mcqgen
   ```

6. **Create and configure environment variables**
   ```bash
   touch .env
   nano .env
   ```
   
   Enter your API keys:
   ```
   OPENAI_API_KEY = "your_openai_api_key"
   ```
   
   Save the file (press "ˆX" then "Y" then "enter")

7. **Verify environment file**
   ```bash
   cat .env
   ```

8. **Create and activate virtual environment**
   ```bash
   python3 -m venv mcqenv
   source mcqenv/bin/activate
   ```

9. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

10. **Run the application**
    ```bash
    python3 -m streamlit run StreamLitApp.py
    ```

11. **Configure security settings**
    - Go to "Security" > "Edit rules" > "New rule"
    - Add port 8501
    - Apply changes

12. **Access your application via browser**
    - Use your EC2 instance's public IP address with port 8501
    - Example: http://your-ec2-ip-address:8501

13. **Important: Clean up resources**
    - Don't forget to stop or delete the server when not in use to avoid charges