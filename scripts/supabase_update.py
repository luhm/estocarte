from supabase_connection import supabase

# instructions: 1. comentar depois do uso, 2. manter as infos usadas para saber qual o próximo id a adicionar


# -------PRODUCTS TABLE--------
# response = (
#     supabase.table("products")
#     .update({"name": "et galaxia roxo e azul"})
#     .eq("id", 2)
#     .execute()
# )

# -------PRODUCT COLLECTIONS TABLE--------

# response = (
#     supabase.table("product_collections")
#     .update({"id": X, "name": "X"})
#     .eq("id", X)
#     .execute()
# )

# -------PRODUCT RAW MATERIALS TABLE--------

# response = (
#     supabase.table("product_raw_materials")
#     .update({"raw_material_id": X, "product_id": "X", "raw_material_qntty": "X"})
#     .eq("id", X)
#     .execute()
# )

# -------RAW MATERIAL TABLE--------

# response = (
#     supabase.table("raw_materials")
#     .update({"name": "verde folha"})
#     .eq("id", 20)
#     .execute()
# )

# -------RAW MATERIALS TYPE TABLE--------

# response = (
#     supabase.table("raw_materials_type")
#     .update(
#             {"name": "ferramentas para producao"})
#     .eq("id", 6)
#     .execute()
# )
