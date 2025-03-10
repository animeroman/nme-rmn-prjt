import os
import re

# Değiştirmek istediğiniz HTML kodu
old_code = '''<div class="pagination-pages pagination pagination-lg">
                          <li class="page-item active">
                            <a title="Page 1" class="page-link" href="">1</a>
                          </li>
                          <li class="page-item">
                            <a title="Page 2" class="page-link" href="">2</a>
                          </li>
                          <li class="page-item">
                            <a title="Page 3" class="page-link" href="">3</a>
                          </li>
                        </div>'''

new_code = '''<div class="pagination-pages pagination pagination-lg"></div>'''

# Klasör yolunu belirtin
folder_path = 'C:/Users/User1/projects/AnimeRoman'  # İlgili klasörün yolu

# Boşluk karakterlerini ve çok satırlı içeriği ele almak için regex'i düzeltin
old_code_regex = re.escape(old_code).replace(r'\ ', r'\s')

# Klasör içinde dolaşarak dosyaları işleyin
for folder_path, alt_folders, file_list in os.walk(folder_path):
    for dosya in file_list:
        if dosya.endswith('.html'):  # Sadece HTML dosyalarını işle
            dosya_yolu = os.path.join(folder_path, dosya)
            with open(dosya_yolu, 'r', encoding='utf-8') as f:
                icerik = f.read()

            # Eski kodu yeni koda değiştir
            yeni_icerik = re.sub(old_code_regex, new_code, icerik, flags=re.DOTALL)

            with open(dosya_yolu, 'w', encoding='utf-8') as f:
                f.write(yeni_icerik)

print("Process completed. Files have been updated.")
