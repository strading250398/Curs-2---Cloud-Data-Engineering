

def este_valid(email):
    if '@' not in email:
        return False
    
    if '''.''' not in email:
        return False
    
    username = email.split(''@'')