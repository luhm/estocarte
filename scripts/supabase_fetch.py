from supabase_connection import supabase

# instructions: 1. comentar depois do uso, 2. manter as infos usadas para saber qual o próximo id a adicionar


# -------PRODUCTS TABLE--------

response = (
    supabase.table("products")
    .select("*")
    .execute()
)

# -------PRODUCT COLLECTIONS TABLE--------

# response = (
#     supabase.table("product_collections")
#     .select("*")
#     .execute()
# )

# -------PRODUCT RAW MATERIALS TABLE--------

# response = (
#     supabase.table("product_raw_materials")
#     .select("*")
#     .execute()
# )

# -------RAW MATERIAL TABLE--------

# response = (
#     supabase.table("raw_material")
#     .select("*")
#     .execute()
# )

# -------RAW MATERIALS TYPE TABLE--------

# response = (
#     supabase.table("raw_materials_type")
#     .select("*")
#     .execute()
# )