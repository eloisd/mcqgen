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
# from langchain_community.llms import HuggingFaceHub

# Load environment variables from .env file
load_dotenv()

# Access environment variables with os.getenv()
openai_key = os.getenv("OPENAI_API_KEY")
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACE_API_KEY")

model1= "gpt-3.5-turbo"
model2= "gpt-4o"
# model3 = "mistralai/Mistral-7B-Instruct-v0.3"
# model4 = "meta-llama/Meta-Llama-3-8B-Instruct"
# model5 = "meta-llama/Meta-Llama-3-8B"

llm1 = ChatOpenAI(openai_api_key=openai_key, model_name=model1, temperature=0.7)
llm2 = ChatOpenAI(openai_api_key=openai_key, model_name=model2, temperature=0.7)
# llm3 = HuggingFaceHub(repo_id=model3, model_kwargs={'temperature':1,'max_new_tokens': 1000})
# llm4 = HuggingFaceHub(repo_id=model4, model_kwargs={'temperature':1})

quiz_generator_template = '''
Text:{text}
You are an expert MCQ maker. Given the above text, your job is to create a quiz of {number} multiple choice questions for {subject} students in {tone} tone. 
Make sure the questions are not repeated and check all the questions to be conformed to the text. Ensure to make {number} MCQs.
Make sure to format your response like RESPONSE_JSON below and use it as a guide. 
###RESPONSE_JSON:
{response_json}

'''

quiz_generator_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template = quiz_generator_template
)

quiz_chain = LLMChain(llm=llm1, prompt=quiz_generator_prompt, output_key="quiz", verbose=True)

quiz_evaluation_template="""
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
if the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}

Check from an expert French Writer of the above quiz:
"""

quiz_evaluation_prompt = PromptTemplate(input_variables=["subject", "quiz"], template=quiz_evaluation_template)

review_chain=LLMChain(llm=llm1, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)


# Overall chain allowing to run the two chains in sequence
generate_evaluate_chain = SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "response_json"], output_variables=["quiz", "review"], verbose=True)

