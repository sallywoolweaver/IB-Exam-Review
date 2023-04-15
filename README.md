# IB-Exam-Review

This project helps students review for their IB exams using OpenAI's GPT-3 language model. It extracts questions and answers from an IB exam markscheme PDF file and the IB exam question file, and prompts the student to answer those questions. The student's answer is evaluated for correctness and given a score out of the total marks for that question.

## Setup

1. [Sign up for OpenAI's API](https://beta.openai.com/signup/)


2. Clone this repository:

```
git clone https://github.com/sallywoolweaver/IB-Exam-Review.git
cd ib-exam-review
```

3. Create a `.env` file with your OpenAI API key:

OPENAI_API_KEY=<your-api-key>



4. Install the required Python packages:

```
pip install pdfplumber openai python-dotenv

```


5. Download the IB exam markscheme PDF file and exam question PDF file and update the code to the files location (lines 60 & 61).

## Usage

1. Run the script:

text_review.py



2. Follow the prompts to answer the questions.

- If you want to skip a question, enter "skip".

3. Receive feedback and scores for your answers.

