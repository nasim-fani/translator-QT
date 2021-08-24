from typing import List
from db_connection import cur, conn
class Model:
    @staticmethod
    def get_attribute(model_name: str, schema: str = 'public'):
        get_model_attribute_query = "SELECT column_name  FROM information_schema.columns WHERE table_schema = %s AND table_name   = %s;"
        cur.execute(get_model_attribute_query, (schema, model_name))
        rows = cur.fetchall()
        attributes = {}
        counter = 1
        for row in rows:
            attributes[row[0]] = counter
            counter = counter + 1
        return attributes
    @classmethod
    def select(cls, model_name: str, output_column: List[str] = [], schema_name: str = 'public', condition=None):
        insertion_query = "select "
        all_attrs = cls.get_attribute(model_name=model_name)
        exist_columns_in_db=[]
        for column in output_column:
            if column in all_attrs.keys():
                exist_columns_in_db.append(column)

        if exist_columns_in_db == []:
            insertion_query += "*"
        else:
            insertion_query += ",".join(exist_columns_in_db)
        insertion_query+=" from {}.{}".format(schema_name, model_name)
        if condition is not None:
            insertion_query+=" where {}".format(condition)
        # print(insertion_query)
        cur.execute(insertion_query)
        rows = cur.fetchall()
        return rows
    @classmethod
    def update(cls, model_name: str, update_array: dict,
               schema_name: str = 'public', condition=None):
        update_query = 'update {}.{} set '.format(schema_name, model_name)
        all_attrs = cls.get_attribute(model_name=model_name)
        exist_columns_in_db = []
        for key, value in update_array.items():
            if key in all_attrs.keys():
                exist_columns_in_db.append({
                    "field_name": key,
                    "field_value": value
                })
        isFirst=True
        for item in exist_columns_in_db:
            if isFirst:
                update_query+= '{}={}'.format(item['field_name'], item['field_value'])
                isFirst=False
            else:
                update_query +=','+ '{}={}'.format(item['field_name'], item['field_value'])
        if condition is not None:
            update_query+=' where {}'.format(condition)
        # print(update_query)
        cur.execute(update_query)
        conn.commit()

#sample of using Model

# model = Model()
# print(model.get_attribute("wordnet"))
# print(model.select(model_name="wordnet",condition="id=93155"))
# model.update(model_name="wordnet",update_array={"id":93100},condition="id=93155")
# print(model.select(model_name="wordnet",condition="id=93100"))
# model.update(model_name="wordnet",update_array={"id":93155},condition="id=93100")
# print(model.select(model_name="wordnet",condition="id=93155"))