# IB-Exam-Review

This project helps students review for their IB exams using OpenAI's GPT-3 language model. It extracts questions and answers from an IB exam markscheme PDF file, and prompts the student to answer those questions. The student's answer is evaluated for correctness and given a score out of the total marks for that question.

## Setup

1. Clone this repository:

```
git clone https://github.com/sallywoolweaver/IB-Exam-Review.git
cd ib-exam-review
```

2. Create a `.env` file with your OpenAI API key:

OPENAI_API_KEY=<your-api-key>



3. Install the required Python packages:

```
pip install -r requirements.txt
```


4. Download the IB exam markscheme PDF file and place it in the `data` directory.

## Usage

1. Run the script:

text_review.py



2. Follow the prompts to answer the questions.

- If you want to skip a question, enter "skip".

3. Receive feedback and scores for your answers.

