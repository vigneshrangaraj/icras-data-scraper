import db

local_conn = db.get_local_connection()
cursor_query_local = local_conn.cursor(buffered=True)
query = ("select * from agencies")
cursor_query_local.execute(query)

print("total " + str(cursor_query_local.rowcount))