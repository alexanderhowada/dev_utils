from utils import string_to_cursor


s = "spark.sql(f\"\"\"\n\n\"\"\").display()"
string_to_cursor(s)


