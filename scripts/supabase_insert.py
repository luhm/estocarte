from supabase_connection import supabase

# instructions: 1. comentar depois do uso, 2. manter as infos usadas para saber qual o próximo id a adicionar


# -------PRODUCTS TABLE--------
# response = (
#     supabase.table("products")
#     .insert({"id": 2, "name": "et_colorido", "size": "PP", "collection_id": 1})
#     .execute()
# )

# -------PRODUCT COLLECTIONS TABLE--------

# response = (
#     supabase.table("product_collections")
#     .insert([
#           {"id": 2, "name": "cerrado"},
#           {"id": 3, "name": "democracia e respeito"},
#           {"id": 4, "name": "pets"},
#           {"id": 5, "name": "letras"},
#           {"id": 6, "name": "desenhos"}])
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
#     supabase.table("raw_materials")
#     .insert([
#         {"id": 52, "type_id": 1, "size": "2.6", "color": "vermelho alaranjado", "comments": "sem codigo"}])
#     .execute()
# )

# -------RAW MATERIALS TYPE TABLE--------

# response = (
#     supabase.table("raw_materials_type")
#     .insert({"id": 9, "name": "hama bead hard"})
#     .execute()
# )
