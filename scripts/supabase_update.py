from supabase_connection import supabase

# instructions: 1. comentar depois do uso, 2. manter as infos usadas para saber qual o próximo id a adicionar


# -------PRODUCTS TABLE--------
# response = (
#     supabase.table("products")
#     .update({"id": X, "name": "X", "size": "X", "collection_id": X})
#     .eq("id", X)
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
#     .update({"comments": "codigo: toy factory 32"})
#     .eq("id", 5)
#     .execute()
# )

# -------RAW MATERIALS TYPE TABLE--------

response = (
    supabase.table("raw_materials_type")
    .update(
            {"name": "hama bead soft"})
    .eq("id", 1)
    .execute()
)
