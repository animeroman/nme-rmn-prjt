import os
import re

# Değiştirmek istediğiniz HTML kodu
old_code = '''<ul class="nav sidebar_menu-list"></ul>'''

new_code = '''<ul class="nav sidebar_menu-list">
        <li class="nav-item active">
          <a class="nav-link" href="../home.html" title="Home">Home</a>
        </li>
        <li class="nav-item">
          <a href="javascript:void(0)" class="nav-link" title="Genre"
            ><strong>Genre</strong></a
          >
          <div
            data-toggle="collapse"
            data-target="#sidebar_subs_genre"
            aria-expanded="false"
            aria-controls="sidebar_subs_genre"
            class="toggle-submenu"
          >
            <i class="more-less fa fa-plus-square"></i>
          </div>
          <div
            class="multi-collapse sidebar_menu-sub collapse"
            id="sidebar_subs_genre"
          >
            <ul class="nav color-list sub-menu">
              <li class="nav-item">
                <a class="nav-link" href="../genre/action.html">Action</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/adventure.html">Adventure</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/cars.html">Cars</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/comedy.html">Comedy</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/dementia.html">Dementia</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/demons.html">Demons</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/drama.html">Drama</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/ecchi.html">Ecchi</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/fantasy.html">Fantasy</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/game.html">Game</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/harem.html">Harem</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/historical.html"
                  >Historical</a
                >
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/horror.html">Horror</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/isekai.html">Isekai</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/josei.html">Josei</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/kids.html">Kids</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/magic.html">Magic</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/marial-arts.html"
                  >Martial Arts</a
                >
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/mecha.html">Mecha</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/military.html">Military</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/music.html">Music</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/mystery.html">Mystery</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/parody.html">Parody</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/police.html">Police</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/psychological.html"
                  >Psychological</a
                >
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/romance.html">Romance</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/samurai.html">Samurai</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/school.html">School</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/sci-fi.html">Sci-Fi</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/seinen.html">Seinen</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/shoujo.html">Shoujo</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/shoujo-ai.html">Shoujo Ai</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/shounen.html">Shounen</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/shounen-ai.html"
                  >Shounen Ai</a
                >
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/slice-of-life.html"
                  >Slice of Life</a
                >
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/space.html">Space</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/sports.html">Sports</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/super-power.html"
                  >Super Power</a
                >
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/supernatural.html"
                  >Supernatural</a
                >
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/thriller.html">Thriller</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/vampire.html">Vampire</a>
              </li>

              <li class="nav-item nav-more">
                <a class="nav-link"><i class="fas fa-plus mr-2"></i>More</a>
              </li>
            </ul>
            <div class="clearfix"></div>
          </div>
        </li>
        <li class="nav-item">
          <a href="javascript:void(0)" class="nav-link" title="Season"
            ><strong>Season</strong></a
          >
          <div
            data-toggle="collapse"
            data-target="#sidebar_subs_season"
            aria-expanded="false"
            aria-controls="sidebar_subs_season"
            class="toggle-submenu"
          >
            <i class="more-less fa fa-plus-square"></i>
          </div>
          <div
            id="sidebar_subs_season"
            class="multi-collapse sidebar_menu-sub collapse"
          >
            <ul class="nav color-list sub-menu">
              <li class="nav-item">
                <a class="nav-link" href="../season/spring.html">Spring</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../season/summer.html">Summer</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../season/fall.html">Fall</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../season/winter.html">Winter</a>
              </li>
            </ul>
          </div>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="../subbed-anime.html" title="Subbed Anime"
            >Subbed Anime</a
          >
        </li>
        <li class="nav-item">
          <a class="nav-link" href="../dubbed-anime.html" title="Dubbed Anime"
            >Dubbed Anime</a
          >
        </li>
        <li class="nav-item">
          <a class="nav-link" href="../most-popular.html" title="Most Popular"
            >Most Popular</a
          >
        </li>
        <li class="nav-item">
          <a class="nav-link" href="../movie.html" title="Movies">Movies</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="../tv.html" title="TV Series">TV Series</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="../ova.html" title="OVAs">OVAs</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="../ona.html" title="ONAs">ONAs</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="../special.html" title="Specials"
            >Specials</a
          >
        </li>
      </ul>'''

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
