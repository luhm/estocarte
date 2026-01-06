from supabase_connection import supabase

# instructions: 1. comentar depois do uso, 2. manter as infos usadas para saber qual o próximo id a adicionar


# -------PRODUCTS TABLE--------
# response = (
#     supabase.table("products")
#     .insert([{"id": 8, "name": "bandeira pt", "size": "PP", "collection_id": 3},
#              {"id": 9, "name": "foice e martelo", "size": "M", "collection_id": 3},
#              {"id": 10, "name": "mao fechada", "size": "P", "collection_id": 3},
#              {"id": 11, "name": "mao fechada", "size": "M", "collection_id": 3},
#              {"id": 12, "name": "unicornio gay", "size": "PP", "collection_id": 3},
#              {"id": 13, "name": "coracao gay", "size": "PP", "collection_id": 3, "comments": "o corpo dele pode ser preto ou branco"},
#              {"id": 14, "name": "coracao gay pastel", "size": "PP", "collection_id": 3, "comments": "o corpo dele pode ser preto ou branco"},
#              {"id": 15, "name": "coracao gay dark", "size": "PP", "collection_id": 3, "comments": "o corpo dele pode ser preto ou branco"}])
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
#     .insert([{"raw_material_id": 32, "product_id": 9, "raw_material_qntty": 89},
#              ])
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
#     .insert([{"id": 10, "name": "lapis"},
#              {"id": 11, "name": "caneta"}])
#     .execute()
# )
