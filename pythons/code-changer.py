import os
import re

# Değiştirmek istediğiniz HTML kodu
eski_kod = '''<div class="header-group">
            <div class="anw-group">
              <div class="zrg-title">
                <span class="top">Join now</span
                ><span class="bottom">HiAnime Group</span>
              </div>
              <div class="zrg-list">
                <div class="item">
                  <a
                    href="https://discord.gg/hianime"
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
                    href="https://new.reddit.com/r/HiAnimeZone/"
                    target="_blank"
                    class="zr-social-button rd-btn"
                    ><i class="fab fa-reddit-alien"></i
                  ></a>
                </div>
                <div class="item">
                  <a
                    href="https://twitter.com/HiAnimeOfficial"
                    target="_blank"
                    class="zr-social-button tw-btn"
                    ><i class="fab fa-twitter"></i
                  ></a>
                </div>
              </div>
              <div class="clearfix"></div>
            </div>'''

yeni_kod = '''<!--<div class="header-group">
            <div class="anw-group">
              <div class="zrg-title">
                <span class="top">Join now</span
                ><span class="bottom">HiAnime Group</span>
              </div>
              <div class="zrg-list">
                <div class="item">
                  <a
                    href="https://discord.gg/hianime"
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
                    href="https://new.reddit.com/r/HiAnimeZone/"
                    target="_blank"
                    class="zr-social-button rd-btn"
                    ><i class="fab fa-reddit-alien"></i
                  ></a>
                </div>
                <div class="item">
                  <a
                    href="https://twitter.com/HiAnimeOfficial"
                    target="_blank"
                    class="zr-social-button tw-btn"
                    ><i class="fab fa-twitter"></i
                  ></a>
                </div>
              </div>
              <div class="clearfix"></div>
            </div>-->'''

# Klasör yolunu belirtin
klasor_yolu = 'C:/Users/aydin_000/projects/nme-rmn-prjt'  # İlgili klasörün yolu

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
