from utils import string_to_cursor


s = "spark.sql(f\"\"\"\n\n\"\"\").toPandas()"
string_to_cursor(s)


