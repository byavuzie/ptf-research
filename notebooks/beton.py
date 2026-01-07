import pandas as pd
import numpy as np

# --- DATA PREPARATION (Re-defining data to ensure file generation) ---

# 1. Footings (Temeller)
footings_data = [
    {"Mark": "F1", "Col_Mark": "C3", "Count": 1, "L_mm": 800, "B_mm": 800, "Dmin_mm": 150, "Dmax_mm": 400, "Col_L_mm": 200, "Col_B_mm": 200},
    {"Mark": "F2", "Col_Mark": "C1", "Count": 1, "L_mm": 1550, "B_mm": 1350, "Dmin_mm": 150, "Dmax_mm": 400, "Col_L_mm": 300, "Col_B_mm": 200},
    {"Mark": "F2", "Col_Mark": "C4", "Count": 1, "L_mm": 1550, "B_mm": 1350, "Dmin_mm": 150, "Dmax_mm": 400, "Col_L_mm": 300, "Col_B_mm": 200},
    {"Mark": "F2", "Col_Mark": "C6", "Count": 1, "L_mm": 1550, "B_mm": 1350, "Dmin_mm": 150, "Dmax_mm": 400, "Col_L_mm": 300, "Col_B_mm": 200},
    {"Mark": "F2", "Col_Mark": "C7", "Count": 1, "L_mm": 1550, "B_mm": 1350, "Dmin_mm": 150, "Dmax_mm": 400, "Col_L_mm": 300, "Col_B_mm": 200},
    {"Mark": "F2", "Col_Mark": "C10", "Count": 1, "L_mm": 1550, "B_mm": 1350, "Dmin_mm": 150, "Dmax_mm": 400, "Col_L_mm": 400, "Col_B_mm": 200},
    {"Mark": "F2", "Col_Mark": "C11", "Count": 1, "L_mm": 1550, "B_mm": 1350, "Dmin_mm": 150, "Dmax_mm": 400, "Col_L_mm": 400, "Col_B_mm": 200},
    {"Mark": "F2", "Col_Mark": "C12", "Count": 1, "L_mm": 1550, "B_mm": 1350, "Dmin_mm": 150, "Dmax_mm": 400, "Col_L_mm": 400, "Col_B_mm": 200},
    {"Mark": "F3", "Col_Mark": "C2", "Count": 1, "L_mm": 2050, "B_mm": 1850, "Dmin_mm": 150, "Dmax_mm": 400, "Col_L_mm": 300, "Col_B_mm": 200},
    {"Mark": "F3", "Col_Mark": "C5", "Count": 1, "L_mm": 2050, "B_mm": 1850, "Dmin_mm": 150, "Dmax_mm": 400, "Col_L_mm": 400, "Col_B_mm": 200},
    {"Mark": "F3", "Col_Mark": "C8", "Count": 1, "L_mm": 2050, "B_mm": 1850, "Dmin_mm": 150, "Dmax_mm": 400, "Col_L_mm": 400, "Col_B_mm": 200},
    {"Mark": "F3", "Col_Mark": "C9", "Count": 1, "L_mm": 2050, "B_mm": 1850, "Dmin_mm": 150, "Dmax_mm": 400, "Col_L_mm": 400, "Col_B_mm": 200},
]

# 2. Columns (Kolonlar)
columns_data = [
    {"Col_Mark": "C1", "Count": 1, "L_mm": 300, "B_mm": 200, "H_sub_m": 1.2, "H_super_m": 3.0},
    {"Col_Mark": "C2", "Count": 1, "L_mm": 300, "B_mm": 200, "H_sub_m": 1.2, "H_super_m": 3.0},
    {"Col_Mark": "C3", "Count": 1, "L_mm": 200, "B_mm": 200, "H_sub_m": 1.2, "H_super_m": 3.0},
    {"Col_Mark": "C4", "Count": 1, "L_mm": 300, "B_mm": 200, "H_sub_m": 1.2, "H_super_m": 3.0},
    {"Col_Mark": "C5", "Count": 1, "L_mm": 400, "B_mm": 200, "H_sub_m": 1.2, "H_super_m": 3.0},
    {"Col_Mark": "C6", "Count": 1, "L_mm": 300, "B_mm": 200, "H_sub_m": 1.2, "H_super_m": 3.0},
    {"Col_Mark": "C7", "Count": 1, "L_mm": 300, "B_mm": 200, "H_sub_m": 1.2, "H_super_m": 3.0},
    {"Col_Mark": "C8", "Count": 1, "L_mm": 400, "B_mm": 200, "H_sub_m": 1.2, "H_super_m": 3.0},
    {"Col_Mark": "C9", "Count": 1, "L_mm": 400, "B_mm": 200, "H_sub_m": 1.2, "H_super_m": 3.0},
    {"Col_Mark": "C10", "Count": 1, "L_mm": 400, "B_mm": 200, "H_sub_m": 1.2, "H_super_m": 3.0},
    {"Col_Mark": "C11", "Count": 1, "L_mm": 400, "B_mm": 200, "H_sub_m": 1.2, "H_super_m": 3.0},
    {"Col_Mark": "C12", "Count": 1, "L_mm": 400, "B_mm": 200, "H_sub_m": 1.2, "H_super_m": 3.0},
]

# 3. Beams (Kirişler)
beams_data = [
    {"Type": "Plinth Beams (Substructure)", "Count": 1, "Total_Length_m": 69.0, "Width_mm": 200, "Depth_mm": 300},
    {"Type": "Floor Beams (Superstructure)", "Count": 1, "Total_Length_m": 69.0, "Width_mm": 200, "Depth_mm": 400},
]

# 4. Slabs (Döşemeler)
slabs_data = [
    {"Type": "S1 Slab (100mm)", "Count": 1, "Area_m2": 60.0, "Thickness_mm": 100},
    {"Type": "S2 Sunken Slab (125mm)", "Count": 1, "Area_m2": 5.0, "Thickness_mm": 125},
]

# 5. Stairs (Merdiven)
stairs_data = [
    {"Item": "Staircase (Waist slab + Steps + Landing)", "Volume_m3": 1.8}
]

# --- CALCULATION ---

def calculate_project_volumes():
    # Footings
    footing_rows = []
    for f in footings_data:
        L = f["L_mm"] / 1000.0
        B = f["B_mm"] / 1000.0
        h_rect = f["Dmin_mm"] / 1000.0
        h_trap = (f["Dmax_mm"] - f["Dmin_mm"]) / 1000.0
        cL = f["Col_L_mm"] / 1000.0
        cB = f["Col_B_mm"] / 1000.0
        A1 = L * B
        A2 = cL * cB
        vol_rect = A1 * h_rect
        vol_trap = (h_trap / 3.0) * (A1 + A2 + np.sqrt(A1 * A2))
        total_vol = (vol_rect + vol_trap) * f["Count"]
        row = f.copy()
        row["Vol_Rect_m3"] = round(vol_rect, 3)
        row["Vol_Trap_m3"] = round(vol_trap, 3)
        row["Total_Vol_m3"] = round(total_vol, 3)
        footing_rows.append(row)
    df_footings = pd.DataFrame(footing_rows)
    
    # Columns
    col_rows = []
    for c in columns_data:
        area = (c["L_mm"] * c["B_mm"]) / 1e6
        vol_sub = area * c["H_sub_m"] * c["Count"]
        vol_super = area * c["H_super_m"] * c["Count"]
        row = c.copy()
        row["Area_m2"] = area
        row["Vol_Sub_m3"] = round(vol_sub, 3)
        row["Vol_Super_m3"] = round(vol_super, 3)
        row["Total_Vol_m3"] = round(vol_sub + vol_super, 3)
        col_rows.append(row)
    df_columns = pd.DataFrame(col_rows)

    # Beams
    beam_rows = []
    for b in beams_data:
        vol = b["Total_Length_m"] * (b["Width_mm"]/1000) * (b["Depth_mm"]/1000) * b["Count"]
        row = b.copy()
        row["Volume_m3"] = round(vol, 3)
        beam_rows.append(row)
    df_beams = pd.DataFrame(beam_rows)

    # Slabs
    slab_rows = []
    for s in slabs_data:
        vol = s["Area_m2"] * (s["Thickness_mm"]/1000) * s["Count"]
        row = s.copy()
        row["Volume_m3"] = round(vol, 3)
        slab_rows.append(row)
    df_slabs = pd.DataFrame(slab_rows)

    # Stairs
    df_stairs = pd.DataFrame(stairs_data)

    # Summary
    summary_rows = [
        {"Category": "Temeller (Substructure)", "Volume_m3": df_footings["Total_Vol_m3"].sum()},
        {"Category": "Kolonlar - Filiz (Substructure)", "Volume_m3": df_columns["Vol_Sub_m3"].sum()},
        {"Category": "Kolonlar - Kat (Superstructure)", "Volume_m3": df_columns["Vol_Super_m3"].sum()},
        {"Category": "Hatıllar / Plinth Beams", "Volume_m3": df_beams[df_beams["Type"].str.contains("Plinth")]["Volume_m3"].sum()},
        {"Category": "Kat Kirişleri / Floor Beams", "Volume_m3": df_beams[df_beams["Type"].str.contains("Floor")]["Volume_m3"].sum()},
        {"Category": "Döşemeler / Slabs", "Volume_m3": df_slabs["Volume_m3"].sum()},
        {"Category": "Merdiven / Stairs", "Volume_m3": df_stairs["Volume_m3"].sum()},
    ]
    df_summary = pd.DataFrame(summary_rows)
    total_concrete = df_summary["Volume_m3"].sum()
    df_summary.loc[len(df_summary)] = {"Category": "TOPLAM (Net)", "Volume_m3": total_concrete}
    df_summary.loc[len(df_summary)] = {"Category": "Zayi (%5)", "Volume_m3": total_concrete * 0.05}
    df_summary.loc[len(df_summary)] = {"Category": "GENEL TOPLAM (Sipariş)", "Volume_m3": total_concrete * 1.05}

    return df_summary, df_footings, df_columns, df_beams, df_slabs, df_stairs

df_summ, df_foot, df_col, df_beam, df_slab, df_stair = calculate_project_volumes()

# Export
output_file = "Beton_Metraj_Hesabi_Proje_Odevi.xlsx"
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    df_summ.to_excel(writer, sheet_name='Ozet_Tablo', index=False)
    df_foot.to_excel(writer, sheet_name='Temeller', index=False)
    df_col.to_excel(writer, sheet_name='Kolonlar', index=False)
    df_beam.to_excel(writer, sheet_name='Kirisler', index=False)
    df_slab.to_excel(writer, sheet_name='Dosemeler', index=False)
    df_stair.to_excel(writer, sheet_name='Merdiven', index=False)
    
    workbook = writer.book
    for sheet_name in writer.sheets:
        worksheet = writer.sheets[sheet_name]
        worksheet.set_column(0, 10, 25)

print(output_file)