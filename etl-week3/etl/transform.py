from validation import DataRow
from load import insert


def validate_data(df): 
    for _, row in df.iterrows():
        try:
            validated = DataRow(**row)
            insert(validated)
            #cur.execute("INSERT INTO users (id, name, email) VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING",
            #        (row['id'], row['name'], row['email']))
        except:
            pass
        
