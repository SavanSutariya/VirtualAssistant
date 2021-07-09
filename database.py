import sqlite3

def create_connection():
    """
    Connects to the database
    """
    connection = sqlite3.connect("memory.db")
    return connection

def get_questions_and_answers():
    con = create_connection()
    cur = con.cursor()
    cur.execute("select * from questionsAndAnswers")
    return cur.fetchall()

def insert_question_and_answer(question, answer):
    con = create_connection()
    cur = con.cursor()
    query = "INSERT INTO questionsAndAnswers VALUES('"+question+"','"+answer+"')"
    cur.execute(query)
    con.commit()

def get_answers_from_memory(question):
    rows = get_questions_and_answers()
    answer = ""
    for row in rows:
        if row[0].lower() in question.lower():
            answer = row[1]
            break
    return answer

def get_name(arg):
    con = create_connection()
    cur = con.cursor()
    query = "select * from memory where name = '"+arg+"'"
    cur.execute(query)
    return cur.fetchall()[0][1]

def change_assis_name(arg):
    con = create_connection()
    cur = con.cursor()
    query = "UPDATE memory SET value = '"+arg+"' WHERE name = 'assistant name'"
    cur.execute(query)
    con.commit()