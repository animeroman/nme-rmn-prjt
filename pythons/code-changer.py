import os
import re

# Değiştirmek istediğiniz HTML kodu
old_code = '''<!-- Google tag (gtag.js) -->
    <script
      async
      src="https://www.googletagmanager.com/gtag/js?id=G-R34F2GCSBW"
    ></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        dataLayer.push(arguments);
      }
      gtag("js", new Date());

      gtag("config", "G-R34F2GCSBW");
    </script>'''

new_code = '''<!-- Google tag (gtag.js) -->
    <!-- <script
      async
      src="https://www.googletagmanager.com/gtag/js?id=G-R34F2GCSBW"
    ></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        dataLayer.push(arguments);
      }
      gtag("js", new Date());

      gtag("config", "G-R34F2GCSBW");
    </script> -->'''

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
