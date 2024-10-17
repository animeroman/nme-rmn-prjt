import os
import re

# Değiştirmek istediğiniz HTML kodu
eski_kod = '''<link rel="stylesheet" href="css/styles.minc619.css?v=1.0" />'''
yeni_kod = '''<link rel="stylesheet" href="../css/styles.minc619.css?v=1.0" />'''

# Klasör yolunu belirtin
ana_klasor_yolu = 'C:/Users/aydin_000/projects/nme-rmn-prjt'  # İlgili klasörün yolu

# Eski kodu regex ile hazırlayın
eski_kod_regex = re.escape(eski_kod)

# Klasör içinde dolaşarak dosyaları işleyin
for root, alt_klasorler, dosya_listesi in os.walk(ana_klasor_yolu):
    # Ana klasörü atla, sadece alt klasörleri işle
    if root == ana_klasor_yolu:
        continue
    
    for dosya in dosya_listesi:
        if dosya.endswith('.html'):  # Sadece HTML dosyalarını işle
            dosya_yolu = os.path.join(root, dosya)
            with open(dosya_yolu, 'r', encoding='utf-8') as f:
                icerik = f.read()

            # Eski kodu yeni koda değiştir
            yeni_icerik = re.sub(eski_kod_regex, yeni_kod, icerik, flags=re.DOTALL)

            with open(dosya_yolu, 'w', encoding='utf-8') as f:
                f.write(yeni_icerik)

print("Process completed. Files have been updated.")
