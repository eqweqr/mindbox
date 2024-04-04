from pyspark.sql import SparkSession
from datetime import datetime, date

spark = SparkSession.builder.getOrCreate()

def products_with_categories(category, product, relation):
    try:
        result = product.\
            join(relation, product.id == relation.product_id, 'left').\
            join(category, category.id == relation.category_id, 'inner').\
            select(product.name, category.name)
    except Exception:
        raise
    return result