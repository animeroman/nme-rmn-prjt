import os
import re

# Değiştirmek istediğiniz HTML kodu
eski_kod = '''<script type="text/javascript" src="../js/search.js"'''

yeni_kod = ''' '''

# Klasör yolunu belirtin
klasor_yolu = 'C:/Users/aydin_000/Desktop/hiRoman'  # İlgili klasörün yolu

# Boşluk karakterlerini ve çok satırlı içeriği ele almak için regex'i düzeltin
eski_kod_regex = re.escape(eski_kod).replace(r'\ ', r'\s')

# Klasör içinde dolaşarak dosyaları işleyin
for klasor_yolu, alt_klasorler, dosya_listesi in os.walk(klasor_yolu):
    for dosya in dosya_listesi:
        if dosya.endswith('.html'):  # Sadece HTML dosyalarını işle
            dosya_yolu = os.path.join(klasor_yolu, dosya)
            with open(dosya_yolu, 'r', encoding='utf-8') as f:
                icerik = f.read()

            # Eski kodu yeni koda değiştir
            yeni_icerik = re.sub(eski_kod_regex, yeni_kod, icerik, flags=re.DOTALL)

            with open(dosya_yolu, 'w', encoding='utf-8') as f:
                f.write(yeni_icerik)

print("Process completed. Files have been updated.")