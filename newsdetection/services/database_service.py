from database import get_connection


def register_user(username, email, password):

    conn = get_connection()
    cursor = conn.cursor()

    # Check email already exists
    cursor.execute(
        "SELECT * FROM users WHERE email=%s",
        (email,)
    )

    user = cursor.fetchone()

    if user:
        cursor.close()
        conn.close()
        return False

    query = """
        INSERT INTO users(username,email,password)
        VALUES(%s,%s,%s)
    """

    cursor.execute(query, (username, email, password))

    conn.commit()

    cursor.close()
    conn.close()

    return True


def login_user(email, password):

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT * FROM users
        WHERE email=%s AND password=%s
    """

    cursor.execute(query, (email, password))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user




def save_prediction(user_id, title, news_text, language, prediction, confidence):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
        INSERT INTO prediction_history
        (user_id,title,news_text,language,prediction,confidence)
        VALUES(%s,%s,%s,%s,%s,%s)
    """

    try:
        
        cursor.execute(
        query,
        (
            user_id,
            title,
            news_text,
            language,
            prediction,
            confidence
        )
        )

        conn.commit()
    
    
    except Exception as e:

        conn.rollback()

        raise
    
    

    finally:

        cursor.close()
        conn.close()

    return True


def get_history(user_id):

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT *
        FROM prediction_history
        WHERE user_id=%s
        ORDER BY created_at DESC
    """

    cursor.execute(query, (user_id,))

    history = cursor.fetchall()

    cursor.close()
    conn.close()

    return history




def save_chat(user_id, question, answer):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO chat_history
    (user_id, question, answer)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (user_id, question, answer))
    conn.commit()

    cursor.close()
    conn.close()


def get_chat_history(user_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT * FROM chat_history
    WHERE user_id=%s
    ORDER BY created_at DESC
    """

    cursor.execute(query, (user_id,))
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data