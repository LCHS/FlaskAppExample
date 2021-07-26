class AppUtils:

    @staticmethod
    def make_search_query(email, name):
        if name:
            name_query = {'$regex': f'.*{name}.*'}
        else:
            name_query = {'$regex': f'.*.*'}
        if email:
            email_query = {'$regex': f'.*{email}.*'}
        else:
            email_query = {'$regex': f'.*.*'}
        query = {'name': name_query, 'email': email_query}
        return query

    @staticmethod
    def object_id_to_string(id_dict):
        id_dict['_id'] = str(id_dict['_id'])
        return id_dict
