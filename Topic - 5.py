import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# membaca data dari file Data Sales .csv
file_path = r"D:\#KULIAH\SEM-2\Statistik dan Probabilitas\topic-5\Data Sales.csv"
df = pd.read_csv(file_path, encoding="windows-1252", delimiter=";")

# menampilkan daftar kolom
print("Kolom yang tersedia:", df.columns)

# memastikan kolom numerik dikonversi dengan benar agar dapat dianalisis
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce").fillna(0) # mengkonversi 'Sales' ke numerik dan ganti NaN dengan 0
df["Year"] = pd.to_numeric(df["Year"], errors="coerce") # mengkonversi 'Year' ke numerik

# --------------------------------------------------------------------------------#
# 1. Distribusi Frekuensi Kategori Produk pada tahun 2014 dan Visualisasikan
# --------------------------------------------------------------------------------#

df_2014 = df[df["Year"] == 2014] # memfilter data untuk tahun 2014

if not df_2014.empty:
    category_counts = df_2014["Category"].value_counts() # menghitung jumlah masing - masing kategori produk
    colors = sns.color_palette("husl", len(category_counts)) # membuat warna yang berbeda di setiap kategori

    # membuat pie chart untuk mendistribusikan kategori produk
    plt.figure(figsize=(8, 8))
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title("Distribusi Kategori Produk (2014)")
    plt.axis('equal') # mengatur pie chart agar berbentuk lingkaran
    plt.show()
else:
    print("⚠️ Tidak ada data untuk tahun 2014!")

# --------------------------------------------------------------------------------#
# 2. Distribusi Frekuensi Produk dengan kategori Furniture dan Visualisasikan
# --------------------------------------------------------------------------------#

df_furniture = df_2014[df_2014["Category"] == "Furniture"] # memfilter dat auntuk kategori Furniture pada tahun 2014

if not df_furniture.empty:
    furniture_counts = df_furniture["Sub-Category"].value_counts() # menghitung jumlah masing - masing sub-kategori dalam kategori "Furniture"

    # membuat bar chart untuk distribusi sub-kategori furniture
    plt.figure(figsize=(8, 5))
    sns.barplot(x=furniture_counts.index, y=furniture_counts.values, palette="coolwarm")
    plt.xlabel("Sub-Kategori Produk (Furniture)")
    plt.ylabel("Frekuensi")
    plt.title("Distribusi Frekuensi Produk dalam Kategori Furniture (2014)")
    plt.xticks(rotation=45) # mengatur label sumbu x agar lebih mudah dibaca
    plt.show()
else:
    print("⚠️ Tidak ada data untuk kategori Furniture!")

# --------------------------------------------------------------------------------#
# 3. Distribusi Frekuensi Produk dengan kategori Technology dan Visualisasikan
# --------------------------------------------------------------------------------#

df_2014_tech = df_2014[df_2014["Category"] == "Technology"] # memfilter data untuk kategori Teknologi pada tahun 2014

if not df_2014_tech.empty:
    top_tech_product = df_2014_tech.groupby("Product Name")["Sales"].sum().nlargest(1) # mengelompokkan data berdasarkan nama produk dan menghitung total penjualan masing - masing produk
    print("Produk Teknologi dengan Penjualan Tertinggi pada Tahun 2014:") # menampilkan produk dengan penjualan tertinggi
    print(top_tech_product)
else:
    print("⚠️ Tidak ada data untuk kategori Technology pada tahun 2014.")

# --------------------------------------------------------------------------------#
# 4. Grafik pembelian barang per tahun di kota DKI Jakarta (tahun 2014 - 2017)
# --------------------------------------------------------------------------------#

df_jakarta = df[df["City"] == "DKI Jakarta"] # memfilter data untuk kota DKI Jakarta

transactions_per_year = df_jakarta.groupby("Year").size() # menghitung jumlah transaksi per tahun

if not transactions_per_year.empty:
    plt.figure(figsize=(10, 5)) # membuat line chart jumlah transaksi per tahun
    sns.lineplot(x=transactions_per_year.index, y=transactions_per_year.values, marker='o', color='b')
    plt.title('Grafik Frekuensi Transaksi per Tahun di DKI Jakarta (2014-2017)', fontsize=14)
    plt.xlabel('Tahun', fontsize=12)
    plt.ylabel('Frekuensi Transaksi', fontsize=12)
    plt.grid(True)
    plt.show()
else:
    print("⚠️ Tidak ada transaksi di DKI Jakarta untuk periode 2014-2017.")

# --------------------------------------------------------------------------------#
# 5. Peluang pembeli tipe Corporate membeli barang kategori Office Supplies pada 2015
# --------------------------------------------------------------------------------#

df_2015 = df[df["Year"] == 2015] # memfilter data untuk tahun 2015

total_transactions_2015 = len(df_2015) # menghitung  total transaksi pada tahun 2015

corporate_office_supplies = df_2015[(df_2015["Segment"] == "Corporate") & (df_2015["Category"] == "Office Supplies")] # memfilter data untuk transaksi Corporate pada kategori Office Supplies pada tahun 2015
corporate_office_supplies_count = len(corporate_office_supplies)

probability_corporate_office_supplies = ( # menghitung peluang pembelian Corporate pada kategori Office Supplies pada tahun 2015
    corporate_office_supplies_count / total_transactions_2015 if total_transactions_2015 > 0 else 0
)

# menampilkan hasil perhitungan peluang pembelian Corporate pada kategori Office Supplies pada tahun 2015
print(f"Total transaksi tahun 2015: {total_transactions_2015}")
print(f"Jumlah transaksi Corporate - Office Supplies: {corporate_office_supplies_count}")
print(f"Peluang: {probability_corporate_office_supplies:.4f}")