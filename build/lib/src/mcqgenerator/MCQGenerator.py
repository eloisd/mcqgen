import os
import json
import traceback
import pandas as pd 
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.logger import logging

# importing necessary packages from langchain
# from langchain.chat_models import ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import langchain_community

# Load environment variables from .env file
load_dotenv()

# Access environment variables with os.getenv()
key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key=key, model_name="gpt-4o-mini", temperature=0.7)

quiz_generator_template = '''
Text:{text}
You are an expert MCQ maker. Given the above text, your job is to create a quiz of {number} multiple choice questions for {subject} students in {tone} tone. 
Make sure the questions are not repeated and check all the questions to be conformed to the text.
Make sure to format your response like RESPONSE_JSON below and use it as a guide. Ensure to make {number} MCQs.
### RESPONSE_JSON
{response_json}

'''

quiz_generator_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template = quiz_generator_template
)

quiz_chain = LLMChain(llm=llm, prompt=quiz_generator_prompt, output_key="quiz", verbose=True)

quiz_evaluation_template="""
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
if the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
"""

quiz_evaluation_prompt = PromptTemplate(input_variables=["subject", "quiz"], template=quiz_evaluation_template)

review_chain=LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)


# Overall chain allowing to run the two chains in sequence
generate_evaluate_chain = SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "response_json"], output_variables=["quiz", "review"], verbose=True)


