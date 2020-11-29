user = {
        'name':'123',
        'gender':'123',
        }  
query = []
for key,value in user.items():
    if value !=None:
        print(key + '=' + " '{}' ".format(value))
        query.append(key + '=' + " '{}' ".format(value))  
    query = ','.join(query)
    sql = """ Update flask_api.users Set {} where id = "{}"
    """