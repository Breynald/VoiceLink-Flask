sql_queries = {
    'check_repeat_email': 'SELECT * FROM user_data WHERE email = %s;',
    'insert_new_account': 'INSERT INTO user_data (uuid, username, email, password) VALUES (%s, %s, %s, %s);',
    'check_email_and_password': 'SELECT * FROM user_data WHERE email = %s AND password = %s;',
    
}