from django.db import connection

class SQL: 
    def dict_convert(row, x):
        resultsList = []
        for r in row:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)

        return resultsList

    def slq_select(campos, tabela, criterios):
        cursor = connection.cursor()
        cursor.execute("SELECT %s FROM %s %s" % (campos, tabela, criterios))
        row = cursor.fetchall()
        x = cursor.description

        resultsList = SQL.dict_convert(row, x)

        return resultsList
    
    def sql_insert(tabela, campos, dados):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO %s (%s) VALUES (%s)" % (tabela, campos, dados))
        
    def sql_update(tabela, campos, pk):
        cursor = connection.cursor()
        cursor.execute("UPDATE %s SET %s WHERE id=%s" % (tabela, campos, pk))
        
    def sql_delete(tabela, pk):
        cursor = connection.cursor()
        cursor.execute("DELETE FROM %s WHERE id='%s'" % (tabela, pk))
        
        
