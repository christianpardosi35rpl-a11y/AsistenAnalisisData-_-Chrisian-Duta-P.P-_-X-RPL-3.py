dataset_nilai = [85, 90, 80, 75, 95]

jumlah = 0

for n in dataset_nilai:
    jumlah = jumlah + n

rata_rata = jumlah / len(dataset_nilai)

print("Daftar Nilai:", dataset_nilai)
print("Total Nilai:", jumlah)
print("Rata-rata:", rata_rata)

if rata_rata >= 90:
    print("Kesimpulan: Sangat Baik")
elif rata_rata >= 80:
    print("Kesimpulan: Baik")
elif rata_rata >= 70:
    print("Kesimpulan: Cukup")
else:
    print("Kesimpulan: Perlu Belajar Lagi")


