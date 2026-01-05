from supabase_connection import supabase

# instructions: 1. comentar depois do uso, 2. manter as infos usadas para saber qual o próximo id a adicionar


# -------PRODUCTS TABLE--------
response = (
    supabase.table("products")
    .insert({"id": 2, "name": "et_colorido", "size": "PP", "collection_id": 1})
    .execute()
)

# -------PRODUCT COLLECTIONS TABLE--------

# response = (
#     supabase.table("product_collections")
#     .insert({"id": X, "name": "X"})
#     .execute()
# )

# -------PRODUCT RAW MATERIALS TABLE--------

# response = (
#     supabase.table("product_raw_materials")
#     .insert({"raw_material_id": X, "product_id": "X", "raw_material_qntty": "X"})
#     .execute()
# )

# -------RAW MATERIAL TABLE--------

# response = (
#     supabase.table("raw_material")
#     .insert({"id": X, "type_id": X, "size": "X", "color": "X"})
#     .execute()
# )

# -------RAW MATERIALS TYPE TABLE--------

# response = (
#     supabase.table("raw_materials_type")
#     .insert({"id": X, "name": "X"})
#     .execute()
# )
