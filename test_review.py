import pdfplumber
import openai
import re
from dotenv import load_dotenv
import os

# Load API keys from .env file
load_dotenv()



openai.api_key =  os.getenv("OPEN_API_KEY")

def evaluate_answer(prompt, student_answer, correct_answer, marks):
    chat_prompt = [
        {"role": "system", "content": "You are a helpful assistant that can evaluate the correctness of student answers. Provide detailed feedback and grade based on the markschemes. Tell the student how many marks they would have received, and if they did not get full marks how they could improve their answer."},
        {"role": "user", "content": f"Question: {prompt} (Total marks: {marks})\nStudent Answer: {student_answer}\nCorrect Answer: {correct_answer}\nProvide marks based on the markscheme and provide detailed feedback."},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_prompt,
        max_tokens=250,
        n=1,
        stop=None,
        temperature=0.5,
    )
    result = response['choices'][0]['message']['content']

    return result

def extract_answers(pdf_path):
    answers = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            for line in text.split('\n'):
                if line.strip() and line[0].isdigit() and line[-1] == ']':
                    answers.append(line)

    return answers

def extract_marks(line):
    return int(re.search(r'\[(\d+)\]', line).group(1))

def extract_questions(pdf_path):
    questions = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            for line in text.split('\n'):
                if line.strip() and line[0].isdigit() and line[-1] == ']':
                    marks = extract_marks(line)
                    questions.append((line, marks))

    return questions

test_file = "/Users/sallywoolweaver/Code/IB Exam Review/Computer_science_paper_1__SL.pdf"
markscheme_file = "/Users/sallywoolweaver/Code/IB Exam Review/Computer_science_paper_1__SL_markscheme.pdf"

questions = extract_questions(test_file)
answers = extract_answers(markscheme_file)

for i, (question, marks) in enumerate(questions):
    student_answer = input(question + "\nYour answer: ")

    correct_answer = answers[i].split(". ")[1].rsplit("[", 1)[0].strip()
    prompt = question.split(". ")[1].rsplit("[", 1)[0].strip()
    if student_answer == 'skip':
        print("skipped")
    else:
        feedback = evaluate_answer(prompt, student_answer, correct_answer, marks)
        print(feedback)
