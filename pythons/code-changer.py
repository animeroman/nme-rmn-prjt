import os
import re

# Değiştirmek istediğiniz HTML kodu
old_code = '''
        <!--Begin: main-sidebar-->
        <div id="main-sidebar">
          <section class="block_area block_area_sidebar block_area-genres">
            <div class="block_area-header">
              <div class="float-left bah-heading mr-4">
                <h2 class="cat-heading">Genres</h2>
              </div>
              <div class="clearfix"></div>
            </div>
            <div class="block_area-content">
              <div class="cbox cbox-genres">
                <ul class="ulclear color-list sb-genre-list sb-genre-less">
                  <li><a href="action.html" title="Action">Action</a></li>

                  <li>
                    <a href="adventure.html" title="Adventure">Adventure</a>
                  </li>

                  <li><a href="cars.html" title="Cars">Cars</a></li>

                  <li><a href="comedy.html" title="Comedy">Comedy</a></li>

                  <li>
                    <a href="dementia.html" title="Dementia">Dementia</a>
                  </li>

                  <li><a href="demons.html" title="Demons">Demons</a></li>

                  <li><a href="drama.html" title="Drama">Drama</a></li>

                  <li><a href="ecchi.html" title="Ecchi">Ecchi</a></li>

                  <li><a href="fantasy.html" title="Fantasy">Fantasy</a></li>

                  <li><a href="game.html" title="Game">Game</a></li>

                  <li><a href="harem.html" title="Harem">Harem</a></li>

                  <li>
                    <a href="historical.html" title="Historical">Historical</a>
                  </li>

                  <li><a href="horror.html" title="Horror">Horror</a></li>

                  <li><a href="isekai.html" title="Isekai">Isekai</a></li>

                  <li><a href="josei.html" title="Josei">Josei</a></li>

                  <li><a href="kids.html" title="Kids">Kids</a></li>

                  <li><a href="magic.html" title="Magic">Magic</a></li>

                  <li>
                    <a href="marial-arts.html" title="Martial Arts"
                      >Martial Arts</a
                    >
                  </li>

                  <li><a href="mecha.html" title="Mecha">Mecha</a></li>

                  <li>
                    <a href="military.html" title="Military">Military</a>
                  </li>

                  <li><a href="music.html" title="Music">Music</a></li>

                  <li><a href="mystery.html" title="Mystery">Mystery</a></li>

                  <li><a href="parody.html" title="Parody">Parody</a></li>

                  <li><a href="police.html" title="Police">Police</a></li>

                  <li>
                    <a href="psychological.html" title="Psychological"
                      >Psychological</a
                    >
                  </li>

                  <li><a href="romance.html" title="Romance">Romance</a></li>

                  <li><a href="samurai.html" title="Samurai">Samurai</a></li>

                  <li><a href="school.html" title="School">School</a></li>

                  <li><a href="sci-fi.html" title="Sci-Fi">Sci-Fi</a></li>

                  <li><a href="seinen.html" title="Seinen">Seinen</a></li>

                  <li><a href="shoujo.html" title="Shoujo">Shoujo</a></li>

                  <li>
                    <a href="shoujo-ai.html" title="Shoujo Ai">Shoujo Ai</a>
                  </li>

                  <li><a href="shounen.html" title="Shounen">Shounen</a></li>

                  <li>
                    <a href="shounen-ai.html" title="Shounen Ai">Shounen Ai</a>
                  </li>

                  <li>
                    <a href="slice-of-life.html" title="Slice of Life"
                      >Slice of Life</a
                    >
                  </li>

                  <li><a href="space.html" title="Space">Space</a></li>

                  <li><a href="sports.html" title="Sports">Sports</a></li>

                  <li>
                    <a href="super-power.html" title="Super Power"
                      >Super Power</a
                    >
                  </li>

                  <li>
                    <a href="supernatural.html" title="Supernatural"
                      >Supernatural</a
                    >
                  </li>

                  <li>
                    <a href="thriller.html" title="Thriller">Thriller</a>
                  </li>

                  <li><a href="vampire.html" title="Vampire">Vampire</a></li>
                </ul>
                <div class="clearfix"></div>
                <button class="btn btn-sm btn-block btn-showmore mt-2"></button>
              </div>
            </div>
          </section>
          <section class="block_area block_area_sidebar block_area-realtime">
            <div class="block_area-header">
              <div class="float-left bah-heading mr-4">
                <h2 class="cat-heading">Top Airing</h2>
              </div>
              <div class="clearfix"></div>
            </div>
            <div class="block_area-content">
              <div class="cbox cbox-list cbox-realtime">
                <div class="cbox-content">
                  <div class="anif-block-ul">
                    <ul class="ulclear">
                      <li>
                        <div class="film-poster item-qtip" data-id="100">
                          <img
                            data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/bcd84731a3eda4f4a306250769675065.jpg"
                            class="film-poster-img lazyload"
                            alt="One Piece"
                          />
                        </div>
                        <div class="film-detail">
                          <h3 class="film-name">
                            <a
                              href="../one-piece-100.html"
                              title="One Piece"
                              class="dynamic-name"
                              data-jname="One Piece"
                              >One Piece</a
                            >
                          </h3>
                          <div class="fd-infor mt-2">
                            <div class="tick">
                              <div class="tick-item tick-sub">
                                <i class="fas fa-closed-captioning mr-1"></i
                                >1114
                              </div>

                              <div class="tick-item tick-dub">
                                <i class="fas fa-microphone mr-1"></i>1085
                              </div>

                              <div class="dot"></div>
                              TV
                            </div>
                          </div>
                        </div>
                        <div class="film-fav wl-item" data-movieid="100">
                          <i class="fa fa-plus"></i>
                        </div>
                        <div class="clearfix"></div>
                      </li>

                      <li>
                        <div class="film-poster item-qtip" data-id="19146">
                          <img
                            data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/af4938d7388aad3438e443e74b02531e.jpg"
                            class="film-poster-img lazyload"
                            alt="Boku no Hero Academia 7th Season"
                          />
                        </div>
                        <div class="film-detail">
                          <h3 class="film-name">
                            <a
                              href="../my-hero-academia-season-7-19146.html"
                              title="Boku no Hero Academia 7th Season"
                              class="dynamic-name"
                              data-jname="Boku no Hero Academia 7th Season"
                              >My Hero Academia Season 7</a
                            >
                          </h3>
                          <div class="fd-infor mt-2">
                            <div class="tick">
                              <div class="tick-item tick-sub">
                                <i class="fas fa-closed-captioning mr-1"></i>12
                              </div>

                              <div class="tick-item tick-dub">
                                <i class="fas fa-microphone mr-1"></i>10
                              </div>

                              <div class="dot"></div>
                              TV
                            </div>
                          </div>
                        </div>
                        <div class="film-fav wl-item" data-movieid="19146">
                          <i class="fa fa-plus"></i>
                        </div>
                        <div class="clearfix"></div>
                      </li>

                      <li>
                        <div class="film-poster item-qtip" data-id="19109">
                          <img
                            data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/f9b501458823539b6a2004f2cdb98a4a.jpg"
                            class="film-poster-img lazyload"
                            alt="Tensei shitara Slime Datta Ken 3rd Season"
                          />
                        </div>
                        <div class="film-detail">
                          <h3 class="film-name">
                            <a
                              href="../that-time-i-got-reincarnated-as-a-slime-season-3-19109.html"
                              title="Tensei shitara Slime Datta Ken 3rd Season"
                              class="dynamic-name"
                              data-jname="Tensei shitara Slime Datta Ken 3rd Season"
                              >That Time I Got Reincarnated as a Slime Season
                              3</a
                            >
                          </h3>
                          <div class="fd-infor mt-2">
                            <div class="tick">
                              <div class="tick-item tick-sub">
                                <i class="fas fa-closed-captioning mr-1"></i>17
                              </div>

                              <div class="tick-item tick-dub">
                                <i class="fas fa-microphone mr-1"></i>15
                              </div>

                              <div class="dot"></div>
                              TV
                            </div>
                          </div>
                        </div>
                        <div class="film-fav wl-item" data-movieid="19109">
                          <i class="fa fa-plus"></i>
                        </div>
                        <div class="clearfix"></div>
                      </li>

                      <li>
                        <div class="film-poster item-qtip" data-id="323">
                          <img
                            data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/3b185ed9d10aa300bb0cb7fc35b84999.jpg"
                            class="film-poster-img lazyload"
                            alt="Detective Conan"
                          />
                        </div>
                        <div class="film-detail">
                          <h3 class="film-name">
                            <a
                              href="../case-closed-323.html"
                              title="Detective Conan"
                              class="dynamic-name"
                              data-jname="Detective Conan"
                              >Case Closed</a
                            >
                          </h3>
                          <div class="fd-infor mt-2">
                            <div class="tick">
                              <div class="tick-item tick-sub">
                                <i class="fas fa-closed-captioning mr-1"></i
                                >1131
                              </div>

                              <div class="tick-item tick-dub">
                                <i class="fas fa-microphone mr-1"></i>123
                              </div>

                              <div class="dot"></div>
                              TV
                            </div>
                          </div>
                        </div>
                        <div class="film-fav wl-item" data-movieid="323">
                          <i class="fa fa-plus"></i>
                        </div>
                        <div class="clearfix"></div>
                      </li>

                      <li>
                        <div class="film-poster item-qtip" data-id="9688">
                          <img
                            data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/fc1904280b9effa1624c0d2b2652aa52.jpg"
                            class="film-poster-img lazyload"
                            alt="Super Dragon Ball Heroes"
                          />
                        </div>
                        <div class="film-detail">
                          <h3 class="film-name">
                            <a
                              href="../super-dragon-ball-heroes-9688.html"
                              title="Super Dragon Ball Heroes"
                              class="dynamic-name"
                              data-jname="Super Dragon Ball Heroes"
                              >Super Dragon Ball Heroes</a
                            >
                          </h3>
                          <div class="fd-infor mt-2">
                            <div class="tick">
                              <div class="tick-item tick-sub">
                                <i class="fas fa-closed-captioning mr-1"></i>20
                              </div>

                              <div class="dot"></div>
                              ONA
                            </div>
                          </div>
                        </div>
                        <div class="film-fav wl-item" data-movieid="9688">
                          <i class="fa fa-plus"></i>
                        </div>
                        <div class="clearfix"></div>
                      </li>

                      <li>
                        <div class="film-poster item-qtip" data-id="19254">
                          <img
                            data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/b210daff9a85c7b6e42d82d578ee90b2.jpg"
                            class="film-poster-img lazyload"
                            alt="Tokidoki Bosotto Russia-go de Dereru Tonari no Alya-san"
                          />
                        </div>
                        <div class="film-detail">
                          <h3 class="film-name">
                            <a
                              href="../alya-sometimes-hides-her-feelings-in-russian-19254.html"
                              title="Tokidoki Bosotto Russia-go de Dereru Tonari no Alya-san"
                              class="dynamic-name"
                              data-jname="Tokidoki Bosotto Russia-go de Dereru Tonari no Alya-san"
                              >Alya Sometimes Hides Her Feelings in Russian</a
                            >
                          </h3>
                          <div class="fd-infor mt-2">
                            <div class="tick">
                              <div class="tick-item tick-sub">
                                <i class="fas fa-closed-captioning mr-1"></i>5
                              </div>

                              <div class="tick-item tick-dub">
                                <i class="fas fa-microphone mr-1"></i>3
                              </div>

                              <div class="tick-item tick-eps">12</div>

                              <div class="dot"></div>
                              TV
                            </div>
                          </div>
                        </div>
                        <div class="film-fav wl-item" data-movieid="19254">
                          <i class="fa fa-plus"></i>
                        </div>
                        <div class="clearfix"></div>
                      </li>

                      <li>
                        <div class="film-poster item-qtip" data-id="19237">
                          <img
                            data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/6511271f7f9ca415411b234df57125ed.jpg"
                            class="film-poster-img lazyload"
                            alt="Hazurewaku no &#34;Joutai Ijou Skill&#34; de Saikyou ni Natta Ore ga Subete wo Juurin suru made"
                          />
                        </div>
                        <div class="film-detail">
                          <h3 class="film-name">
                            <a
                              href="../failure-frame-i-became-the-strongest-and-annihilated-everything-with-low-level-spells-19237.html"
                              title="Hazurewaku no &#34;Joutai Ijou Skill&#34; de Saikyou ni Natta Ore ga Subete wo Juurin suru made"
                              class="dynamic-name"
                              data-jname="Hazurewaku no &#34;Joutai Ijou Skill&#34; de Saikyou ni Natta Ore ga Subete wo Juurin suru made"
                              >Failure Frame: I Became the Strongest and
                              Annihilated Everything With Low-Level Spells</a
                            >
                          </h3>
                          <div class="fd-infor mt-2">
                            <div class="tick">
                              <div class="tick-item tick-sub">
                                <i class="fas fa-closed-captioning mr-1"></i>5
                              </div>

                              <div class="tick-item tick-eps">12</div>

                              <div class="dot"></div>
                              TV
                            </div>
                          </div>
                        </div>
                        <div class="film-fav wl-item" data-movieid="19237">
                          <i class="fa fa-plus"></i>
                        </div>
                        <div class="clearfix"></div>
                      </li>

                      <li>
                        <div class="film-poster item-qtip" data-id="19133">
                          <img
                            data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/259ca4ad41fd80081677b04a880c7d4b.jpg"
                            class="film-poster-img lazyload"
                            alt="Yozakura-san Chi no Daisakusen"
                          />
                        </div>
                        <div class="film-detail">
                          <h3 class="film-name">
                            <a
                              href="../mission-yozakura-family-19133.html"
                              title="Yozakura-san Chi no Daisakusen"
                              class="dynamic-name"
                              data-jname="Yozakura-san Chi no Daisakusen"
                              >Mission: Yozakura Family</a
                            >
                          </h3>
                          <div class="fd-infor mt-2">
                            <div class="tick">
                              <div class="tick-item tick-sub">
                                <i class="fas fa-closed-captioning mr-1"></i>17
                              </div>

                              <div class="tick-item tick-dub">
                                <i class="fas fa-microphone mr-1"></i>7
                              </div>

                              <div class="dot"></div>
                              TV
                            </div>
                          </div>
                        </div>
                        <div class="film-fav wl-item" data-movieid="19133">
                          <i class="fa fa-plus"></i>
                        </div>
                        <div class="clearfix"></div>
                      </li>

                      <li>
                        <div class="film-poster item-qtip" data-id="18397">
                          <img
                            data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/4b145f650126e400b69e783e3d6cdd2a.jpg"
                            class="film-poster-img lazyload"
                            alt="Pokemon (2023)"
                          />
                        </div>
                        <div class="film-detail">
                          <h3 class="film-name">
                            <a
                              href="../pokemon-horizons-the-series-18397.html"
                              title="Pokemon (2023)"
                              class="dynamic-name"
                              data-jname="Pokemon (2023)"
                              >Pokémon Horizons: The Series</a
                            >
                          </h3>
                          <div class="fd-infor mt-2">
                            <div class="tick">
                              <div class="tick-item tick-sub">
                                <i class="fas fa-closed-captioning mr-1"></i>59
                              </div>

                              <div class="tick-item tick-dub">
                                <i class="fas fa-microphone mr-1"></i>40
                              </div>

                              <div class="dot"></div>
                              TV
                            </div>
                          </div>
                        </div>
                        <div class="film-fav wl-item" data-movieid="18397">
                          <i class="fa fa-plus"></i>
                        </div>
                        <div class="clearfix"></div>
                      </li>

                      <li>
                        <div class="film-poster item-qtip" data-id="19229">
                          <img
                            data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/009a25ddb8db9e068e16effd7e93f30e.jpg"
                            class="film-poster-img lazyload"
                            alt="Ore wa Subete wo &#34;Parry&#34; suru: Gyaku Kanchigai no Sekai Saikyou wa Boukensha ni Naritai"
                          />
                        </div>
                        <div class="film-detail">
                          <h3 class="film-name">
                            <a
                              href="../i-parry-everything-19229.html"
                              title="Ore wa Subete wo &#34;Parry&#34; suru: Gyaku Kanchigai no Sekai Saikyou wa Boukensha ni Naritai"
                              class="dynamic-name"
                              data-jname="Ore wa Subete wo &#34;Parry&#34; suru: Gyaku Kanchigai no Sekai Saikyou wa Boukensha ni Naritai"
                              >I Parry Everything</a
                            >
                          </h3>
                          <div class="fd-infor mt-2">
                            <div class="tick">
                              <div class="tick-item tick-sub">
                                <i class="fas fa-closed-captioning mr-1"></i>5
                              </div>

                              <div class="tick-item tick-eps">12</div>

                              <div class="dot"></div>
                              TV
                            </div>
                          </div>
                        </div>
                        <div class="film-fav wl-item" data-movieid="19229">
                          <i class="fa fa-plus"></i>
                        </div>
                        <div class="clearfix"></div>
                      </li>
                    </ul>
                    <div class="clearfix"></div>
                  </div>
                  <div class="clearfix"></div>
                </div>
              </div>
            </div>
          </section>
        </div>
        <!--/End: main-sidebar-->'''

new_code = ''' '''

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
