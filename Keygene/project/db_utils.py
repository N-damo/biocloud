def select_sql(table, sql):
    query_result = table.get(sql)
    return query_result

def select_all(table, sql):
    query_result = table.select().where(sql)
    return query_result

def excute_sql(table, sql):
    query_result = table.raw(sql)
    return query_result.execute()

def raw_sql(table, sql):
    query = table.raw(sql)
    return query