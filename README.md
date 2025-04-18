## Deployment on AWS

1. Create acount or login
2. Search -> "EC2"
3. click "Launch instance"
4. Complete forms
    * Name: mcqgen
    * OS: Ubuntu
    * Instance: t2.large
    * Key pair: Create
        * Name: mcqkey
        * RSA
        * .pem
    * 16GB
    * click launch
5. wait for initialization
6. click on the id
7. click on connect
8. Now that you are on the ubuntu server terminal, run the following command
    1. sudo apt update
    2. sudo apt-get update
    3. sudo apt upgrade -y
    4. sudo apt install git curl unzip tar make sudo vim wget zsh python3-pip -y
    5. sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    6. sudo chsh -s $(command -v zsh)
9. Install mcqgen from github
    1. git clone https://github.com/eloisd/mcqgen.git
    2. cd mcqgen 
    3. touch .env
    4. nano .env
        1. Enter your api keys
            OPENAI_API_KEY = ""
            HUGGINGFACE_API_KEY = ""
        2. press "ˆX" then "Y" then "enter"
    5. cat .env
    6. python3 -m venv mcqenv
    7. source mcqenv/bin/activate
    8. pip install -r requirements.txt
10. python3 -m streamlit run StreamLitApp.py
11. Go to "security" > "Edit rules" > "New rule"
12. Add port 8501
13. Don't forget to stop or delete the server