import os
import re

# Değiştirmek istediğiniz HTML kodu
old_code = '''<!--<div class="header-group">
            <div class="anw-group">
              <div class="zrg-title">
                <span class="top">Join now</span
                ><span class="bottom">AnimeRoman Group</span>
              </div>
              <div class="zrg-list">
                <div class="item">
                  <a
                    href="https://discord.gg/animeroman"
                    target="_blank"
                    class="zr-social-button dc-btn"
                    ><i class="fab fa-discord"></i
                  ></a>
                </div>
                <div class="item">
                  <a
                    href="https://tinyurl.com/2y2yy3ba"
                    target="_blank"
                    class="zr-social-button tl-btn"
                    ><i class="fab fa-telegram-plane"></i
                  ></a>
                </div>
                <div class="item">
                  <a
                    href="https://new.reddit.com/r/AnimeRomanZone/"
                    target="_blank"
                    class="zr-social-button rd-btn"
                    ><i class="fab fa-reddit-alien"></i
                  ></a>
                </div>
                <div class="item">
                  <a
                    href="https://twitter.com/AnimeRomanOfficial"
                    target="_blank"
                    class="zr-social-button tw-btn"
                    ><i class="fab fa-twitter"></i
                  ></a>
                </div>
              </div>
              <div class="clearfix"></div>
            </div>-->
        </div>'''

new_code = '''<!--<div class="header-group">
            <div class="anw-group">
              <div class="zrg-title">
                <span class="top">Join now</span
                ><span class="bottom">AnimeRoman Group</span>
              </div>
              <div class="zrg-list">
                <div class="item">
                  <a
                    href="https://discord.gg/animeroman"
                    target="_blank"
                    class="zr-social-button dc-btn"
                    ><i class="fab fa-discord"></i
                  ></a>
                </div>
                <div class="item">
                  <a
                    href="https://tinyurl.com/2y2yy3ba"
                    target="_blank"
                    class="zr-social-button tl-btn"
                    ><i class="fab fa-telegram-plane"></i
                  ></a>
                </div>
                <div class="item">
                  <a
                    href="https://new.reddit.com/r/AnimeRomanZone/"
                    target="_blank"
                    class="zr-social-button rd-btn"
                    ><i class="fab fa-reddit-alien"></i
                  ></a>
                </div>
                <div class="item">
                  <a
                    href="https://twitter.com/AnimeRomanOfficial"
                    target="_blank"
                    class="zr-social-button tw-btn"
                    ><i class="fab fa-twitter"></i
                  ></a>
                </div>
              </div>
              <div class="clearfix"></div>
            </div>
        </div>-->'''

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
