import os
import re

# Değiştirmek istediğiniz HTML kodu
eski_kod = '''<div id="main-sidebar">
            <section class="block_area block_area_sidebar block_area-realtime">
              <div class="block_area-header">
                <div class="float-left bah-heading mr-2">
                  <h2 class="cat-heading">Top 10</h2>
                </div>
                <div class="float-right bah-tab-min">
                  <ul class="nav nav-pills nav-fill nav-tabs anw-tabs">
                    <li class="nav-item">
                      <a
                        data-toggle="tab"
                        href="#top-viewed-day"
                        class="nav-link active"
                        >Today</a
                      >
                    </li>
                    <li class="nav-item">
                      <a
                        data-toggle="tab"
                        href="#top-viewed-week"
                        class="nav-link"
                        >Week</a
                      >
                    </li>
                    <li class="nav-item">
                      <a
                        data-toggle="tab"
                        href="#top-viewed-month"
                        class="nav-link"
                        >Month</a
                      >
                    </li>
                  </ul>
                </div>
                <div class="clearfix"></div>
              </div>
              <div class="block_area-content">
                <div class="cbox cbox-list cbox-realtime">
                  <div class="cbox-content">
                    <div class="tab-content">
                      <div
                        id="top-viewed-day"
                        class="anif-block-ul anif-block-chart tab-pane active"
                      >
                        <ul class="ulclear">
                          <li class="item-top">
                            <div class="film-number"><span>01</span></div>
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
                                  href="one-piece-100.html"
                                  title="One Piece"
                                  class="dynamic-name"
                                  data-jname="One Piece"
                                  >One Piece</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >1114
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>1085
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="item-top">
                            <div class="film-number"><span>02</span></div>
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
                                  href="my-hero-academia-season-7-19146.html"
                                  title="Boku no Hero Academia 7th Season"
                                  class="dynamic-name"
                                  data-jname="Boku no Hero Academia 7th Season"
                                  >My Hero Academia Season 7</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >12
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>10
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="item-top">
                            <div class="film-number"><span>03</span></div>
                            <div class="film-poster item-qtip" data-id="806">
                              <img
                                data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/bd5ae1d387a59c5abcf5e1a6a616728c.jpg"
                                class="film-poster-img lazyload"
                                alt="Bleach"
                              />
                            </div>
                            <div class="film-detail">
                              <h3 class="film-name">
                                <a
                                  href="bleach-806.html"
                                  title="Bleach"
                                  class="dynamic-name"
                                  data-jname="Bleach"
                                  >Bleach</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >366
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>366
                                  </div>

                                  <div class="tick-item tick-eps">366</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>04</span></div>
                            <div class="film-poster item-qtip" data-id="355">
                              <img
                                data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/9cbcf87f54194742e7686119089478f8.jpg"
                                class="film-poster-img lazyload"
                                alt="Naruto: Shippuuden"
                              />
                            </div>
                            <div class="film-detail">
                              <h3 class="film-name">
                                <a
                                  href="naruto-shippuden-355.html"
                                  title="Naruto: Shippuuden"
                                  class="dynamic-name"
                                  data-jname="Naruto: Shippuuden"
                                  >Naruto: Shippuden</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >500
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>500
                                  </div>

                                  <div class="tick-item tick-eps">500</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>05</span></div>
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
                                  href="that-time-i-got-reincarnated-as-a-slime-season-3-19109.html"
                                  title="Tensei shitara Slime Datta Ken 3rd Season"
                                  class="dynamic-name"
                                  data-jname="Tensei shitara Slime Datta Ken 3rd Season"
                                  >That Time I Got Reincarnated as a Slime
                                  Season 3</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >17
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>15
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>06</span></div>
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
                                  href="alya-sometimes-hides-her-feelings-in-russian-19254.html"
                                  title="Tokidoki Bosotto Russia-go de Dereru Tonari no Alya-san"
                                  class="dynamic-name"
                                  data-jname="Tokidoki Bosotto Russia-go de Dereru Tonari no Alya-san"
                                  >Alya Sometimes Hides Her Feelings in
                                  Russian</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >5
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>3
                                  </div>

                                  <div class="tick-item tick-eps">12</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>07</span></div>
                            <div class="film-poster item-qtip" data-id="2404">
                              <img
                                data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/f58b0204c20ae3310f65ae7b8cb9987e.jpg"
                                class="film-poster-img lazyload"
                                alt="Black Clover"
                              />
                            </div>
                            <div class="film-detail">
                              <h3 class="film-name">
                                <a
                                  href="black-clover-2404.html"
                                  title="Black Clover"
                                  class="dynamic-name"
                                  data-jname="Black Clover"
                                  >Black Clover</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >170
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>170
                                  </div>

                                  <div class="tick-item tick-eps">170</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>08</span></div>
                            <div class="film-poster item-qtip" data-id="19223">
                              <img
                                data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/d6b6d4a43555afa74323871b9dcf107e.jpg"
                                class="film-poster-img lazyload"
                                alt="Mob kara Hajimaru Tansaku Eiyuutan"
                              />
                            </div>
                            <div class="film-detail">
                              <h3 class="film-name">
                                <a
                                  href="a-nobodys-way-up-to-an-exploration-hero-lv-19223.html"
                                  title="Mob kara Hajimaru Tansaku Eiyuutan"
                                  class="dynamic-name"
                                  data-jname="Mob kara Hajimaru Tansaku Eiyuutan"
                                  >A Nobody&#39;s Way Up to an Exploration Hero
                                  LV</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >6
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>09</span></div>
                            <div class="film-poster item-qtip" data-id="19107">
                              <img
                                data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/1f06eb0baf5520aa639b546fc189400d.jpg"
                                class="film-poster-img lazyload"
                                alt="Kimetsu no Yaiba: Hashira Geiko-hen"
                              />
                            </div>
                            <div class="film-detail">
                              <h3 class="film-name">
                                <a
                                  href="demon-slayer-kimetsu-no-yaiba-hashira-training-arc-19107.html"
                                  title="Kimetsu no Yaiba: Hashira Geiko-hen"
                                  class="dynamic-name"
                                  data-jname="Kimetsu no Yaiba: Hashira Geiko-hen"
                                  >Demon Slayer: Kimetsu no Yaiba Hashira
                                  Training Arc</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >8
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>5
                                  </div>

                                  <div class="tick-item tick-eps">8</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>10</span></div>
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
                                  href="failure-frame-i-became-the-strongest-and-annihilated-everything-with-low-level-spells-19237.html"
                                  title="Hazurewaku no &#34;Joutai Ijou Skill&#34; de Saikyou ni Natta Ore ga Subete wo Juurin suru made"
                                  class="dynamic-name"
                                  data-jname="Hazurewaku no &#34;Joutai Ijou Skill&#34; de Saikyou ni Natta Ore ga Subete wo Juurin suru made"
                                  >Failure Frame: I Became the Strongest and
                                  Annihilated Everything With Low-Level
                                  Spells</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >5
                                  </div>

                                  <div class="tick-item tick-eps">12</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>
                        </ul>
                      </div>
                      <div
                        id="top-viewed-week"
                        class="anif-block-ul anif-block-chart tab-pane"
                      >
                        <ul class="ulclear">
                          <li class="item-top">
                            <div class="film-number"><span>01</span></div>
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
                                  href="one-piece-100.html"
                                  title="One Piece"
                                  class="dynamic-name"
                                  data-jname="One Piece"
                                  >One Piece</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >1114
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>1085
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="item-top">
                            <div class="film-number"><span>02</span></div>
                            <div class="film-poster item-qtip" data-id="806">
                              <img
                                data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/bd5ae1d387a59c5abcf5e1a6a616728c.jpg"
                                class="film-poster-img lazyload"
                                alt="Bleach"
                              />
                            </div>
                            <div class="film-detail">
                              <h3 class="film-name">
                                <a
                                  href="bleach-806.html"
                                  title="Bleach"
                                  class="dynamic-name"
                                  data-jname="Bleach"
                                  >Bleach</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >366
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>366
                                  </div>

                                  <div class="tick-item tick-eps">366</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="item-top">
                            <div class="film-number"><span>03</span></div>
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
                                  href="my-hero-academia-season-7-19146.html"
                                  title="Boku no Hero Academia 7th Season"
                                  class="dynamic-name"
                                  data-jname="Boku no Hero Academia 7th Season"
                                  >My Hero Academia Season 7</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >12
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>10
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>04</span></div>
                            <div class="film-poster item-qtip" data-id="355">
                              <img
                                data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/9cbcf87f54194742e7686119089478f8.jpg"
                                class="film-poster-img lazyload"
                                alt="Naruto: Shippuuden"
                              />
                            </div>
                            <div class="film-detail">
                              <h3 class="film-name">
                                <a
                                  href="naruto-shippuden-355.html"
                                  title="Naruto: Shippuuden"
                                  class="dynamic-name"
                                  data-jname="Naruto: Shippuuden"
                                  >Naruto: Shippuden</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >500
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>500
                                  </div>

                                  <div class="tick-item tick-eps">500</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>05</span></div>
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
                                  href="alya-sometimes-hides-her-feelings-in-russian-19254.html"
                                  title="Tokidoki Bosotto Russia-go de Dereru Tonari no Alya-san"
                                  class="dynamic-name"
                                  data-jname="Tokidoki Bosotto Russia-go de Dereru Tonari no Alya-san"
                                  >Alya Sometimes Hides Her Feelings in
                                  Russian</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >5
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>3
                                  </div>

                                  <div class="tick-item tick-eps">12</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>06</span></div>
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
                                  href="that-time-i-got-reincarnated-as-a-slime-season-3-19109.html"
                                  title="Tensei shitara Slime Datta Ken 3rd Season"
                                  class="dynamic-name"
                                  data-jname="Tensei shitara Slime Datta Ken 3rd Season"
                                  >That Time I Got Reincarnated as a Slime
                                  Season 3</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >17
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>15
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>07</span></div>
                            <div class="film-poster item-qtip" data-id="19107">
                              <img
                                data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/1f06eb0baf5520aa639b546fc189400d.jpg"
                                class="film-poster-img lazyload"
                                alt="Kimetsu no Yaiba: Hashira Geiko-hen"
                              />
                            </div>
                            <div class="film-detail">
                              <h3 class="film-name">
                                <a
                                  href="demon-slayer-kimetsu-no-yaiba-hashira-training-arc-19107.html"
                                  title="Kimetsu no Yaiba: Hashira Geiko-hen"
                                  class="dynamic-name"
                                  data-jname="Kimetsu no Yaiba: Hashira Geiko-hen"
                                  >Demon Slayer: Kimetsu no Yaiba Hashira
                                  Training Arc</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >8
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>5
                                  </div>

                                  <div class="tick-item tick-eps">8</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>08</span></div>
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
                                  href="failure-frame-i-became-the-strongest-and-annihilated-everything-with-low-level-spells-19237.html"
                                  title="Hazurewaku no &#34;Joutai Ijou Skill&#34; de Saikyou ni Natta Ore ga Subete wo Juurin suru made"
                                  class="dynamic-name"
                                  data-jname="Hazurewaku no &#34;Joutai Ijou Skill&#34; de Saikyou ni Natta Ore ga Subete wo Juurin suru made"
                                  >Failure Frame: I Became the Strongest and
                                  Annihilated Everything With Low-Level
                                  Spells</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >5
                                  </div>

                                  <div class="tick-item tick-eps">12</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>09</span></div>
                            <div class="film-poster item-qtip" data-id="2404">
                              <img
                                data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/f58b0204c20ae3310f65ae7b8cb9987e.jpg"
                                class="film-poster-img lazyload"
                                alt="Black Clover"
                              />
                            </div>
                            <div class="film-detail">
                              <h3 class="film-name">
                                <a
                                  href="black-clover-2404.html"
                                  title="Black Clover"
                                  class="dynamic-name"
                                  data-jname="Black Clover"
                                  >Black Clover</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >170
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>170
                                  </div>

                                  <div class="tick-item tick-eps">170</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>10</span></div>
                            <div class="film-poster item-qtip" data-id="19255">
                              <img
                                data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/41adea817f66830f8d965562c2d62e03.jpg"
                                class="film-poster-img lazyload"
                                alt="Kami no Tou: Ouji no Kikan"
                              />
                            </div>
                            <div class="film-detail">
                              <h3 class="film-name">
                                <a
                                  href="tower-of-god-season-2-19255.html"
                                  title="Kami no Tou: Ouji no Kikan"
                                  class="dynamic-name"
                                  data-jname="Kami no Tou: Ouji no Kikan"
                                  >Tower of God Season 2</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >4
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>2
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>
                        </ul>
                      </div>
                      <div
                        id="top-viewed-month"
                        class="anif-block-ul anif-block-chart tab-pane"
                      >
                        <ul class="ulclear">
                          <li class="item-top">
                            <div class="film-number"><span>01</span></div>
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
                                  href="one-piece-100.html"
                                  title="One Piece"
                                  class="dynamic-name"
                                  data-jname="One Piece"
                                  >One Piece</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >1114
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>1085
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="item-top">
                            <div class="film-number"><span>02</span></div>
                            <div class="film-poster item-qtip" data-id="19107">
                              <img
                                data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/1f06eb0baf5520aa639b546fc189400d.jpg"
                                class="film-poster-img lazyload"
                                alt="Kimetsu no Yaiba: Hashira Geiko-hen"
                              />
                            </div>
                            <div class="film-detail">
                              <h3 class="film-name">
                                <a
                                  href="demon-slayer-kimetsu-no-yaiba-hashira-training-arc-19107.html"
                                  title="Kimetsu no Yaiba: Hashira Geiko-hen"
                                  class="dynamic-name"
                                  data-jname="Kimetsu no Yaiba: Hashira Geiko-hen"
                                  >Demon Slayer: Kimetsu no Yaiba Hashira
                                  Training Arc</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >8
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>5
                                  </div>

                                  <div class="tick-item tick-eps">8</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="item-top">
                            <div class="film-number"><span>03</span></div>
                            <div class="film-poster item-qtip" data-id="806">
                              <img
                                data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/bd5ae1d387a59c5abcf5e1a6a616728c.jpg"
                                class="film-poster-img lazyload"
                                alt="Bleach"
                              />
                            </div>
                            <div class="film-detail">
                              <h3 class="film-name">
                                <a
                                  href="bleach-806.html"
                                  title="Bleach"
                                  class="dynamic-name"
                                  data-jname="Bleach"
                                  >Bleach</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >366
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>366
                                  </div>

                                  <div class="tick-item tick-eps">366</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>04</span></div>
                            <div class="film-poster item-qtip" data-id="355">
                              <img
                                data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/9cbcf87f54194742e7686119089478f8.jpg"
                                class="film-poster-img lazyload"
                                alt="Naruto: Shippuuden"
                              />
                            </div>
                            <div class="film-detail">
                              <h3 class="film-name">
                                <a
                                  href="naruto-shippuden-355.html"
                                  title="Naruto: Shippuuden"
                                  class="dynamic-name"
                                  data-jname="Naruto: Shippuuden"
                                  >Naruto: Shippuden</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >500
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>500
                                  </div>

                                  <div class="tick-item tick-eps">500</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>05</span></div>
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
                                  href="my-hero-academia-season-7-19146.html"
                                  title="Boku no Hero Academia 7th Season"
                                  class="dynamic-name"
                                  data-jname="Boku no Hero Academia 7th Season"
                                  >My Hero Academia Season 7</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >12
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>10
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>06</span></div>
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
                                  href="alya-sometimes-hides-her-feelings-in-russian-19254.html"
                                  title="Tokidoki Bosotto Russia-go de Dereru Tonari no Alya-san"
                                  class="dynamic-name"
                                  data-jname="Tokidoki Bosotto Russia-go de Dereru Tonari no Alya-san"
                                  >Alya Sometimes Hides Her Feelings in
                                  Russian</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >5
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>3
                                  </div>

                                  <div class="tick-item tick-eps">12</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>07</span></div>
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
                                  href="that-time-i-got-reincarnated-as-a-slime-season-3-19109.html"
                                  title="Tensei shitara Slime Datta Ken 3rd Season"
                                  class="dynamic-name"
                                  data-jname="Tensei shitara Slime Datta Ken 3rd Season"
                                  >That Time I Got Reincarnated as a Slime
                                  Season 3</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >17
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>15
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>08</span></div>
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
                                  href="failure-frame-i-became-the-strongest-and-annihilated-everything-with-low-level-spells-19237.html"
                                  title="Hazurewaku no &#34;Joutai Ijou Skill&#34; de Saikyou ni Natta Ore ga Subete wo Juurin suru made"
                                  class="dynamic-name"
                                  data-jname="Hazurewaku no &#34;Joutai Ijou Skill&#34; de Saikyou ni Natta Ore ga Subete wo Juurin suru made"
                                  >Failure Frame: I Became the Strongest and
                                  Annihilated Everything With Low-Level
                                  Spells</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >5
                                  </div>

                                  <div class="tick-item tick-eps">12</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>09</span></div>
                            <div class="film-poster item-qtip" data-id="2404">
                              <img
                                data-src="https://cdn.noitatnemucod.net/thumbnail/300x400/100/f58b0204c20ae3310f65ae7b8cb9987e.jpg"
                                class="film-poster-img lazyload"
                                alt="Black Clover"
                              />
                            </div>
                            <div class="film-detail">
                              <h3 class="film-name">
                                <a
                                  href="black-clover-2404.html"
                                  title="Black Clover"
                                  class="dynamic-name"
                                  data-jname="Black Clover"
                                  >Black Clover</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >170
                                  </div>

                                  <div class="tick-item tick-dub">
                                    <i class="fas fa-microphone mr-1"></i>170
                                  </div>

                                  <div class="tick-item tick-eps">170</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>

                          <li class="">
                            <div class="film-number"><span>10</span></div>
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
                                  href="i-parry-everything-19229.html"
                                  title="Ore wa Subete wo &#34;Parry&#34; suru: Gyaku Kanchigai no Sekai Saikyou wa Boukensha ni Naritai"
                                  class="dynamic-name"
                                  data-jname="Ore wa Subete wo &#34;Parry&#34; suru: Gyaku Kanchigai no Sekai Saikyou wa Boukensha ni Naritai"
                                  >I Parry Everything</a
                                >
                              </h3>
                              <div class="fd-infor">
                                <div class="tick">
                                  <div class="tick-item tick-sub">
                                    <i class="fas fa-closed-captioning mr-1"></i
                                    >5
                                  </div>

                                  <div class="tick-item tick-eps">12</div>
                                </div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </li>
                        </ul>
                      </div>
                      <div class="clearfix"></div>
                    </div>
                    <div class="clearfix"></div>
                  </div>
                </div>
              </div>
            </section>
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
                    <li>
                      <a href="genre/action.html" title="Action">Action</a>
                    </li>

                    <li>
                      <a href="genre/adventure.html" title="Adventure"
                        >Adventure</a
                      >
                    </li>

                    <li><a href="genre/cars.html" title="Cars">Cars</a></li>

                    <li>
                      <a href="genre/comedy.html" title="Comedy">Comedy</a>
                    </li>

                    <li>
                      <a href="genre/dementia.html" title="Dementia"
                        >Dementia</a
                      >
                    </li>

                    <li>
                      <a href="genre/demons.html" title="Demons">Demons</a>
                    </li>

                    <li><a href="genre/drama.html" title="Drama">Drama</a></li>

                    <li><a href="genre/ecchi.html" title="Ecchi">Ecchi</a></li>

                    <li>
                      <a href="genre/fantasy.html" title="Fantasy">Fantasy</a>
                    </li>

                    <li><a href="genre/game.html" title="Game">Game</a></li>

                    <li><a href="genre/harem.html" title="Harem">Harem</a></li>

                    <li>
                      <a href="genre/historical.html" title="Historical"
                        >Historical</a
                      >
                    </li>

                    <li>
                      <a href="genre/horror.html" title="Horror">Horror</a>
                    </li>

                    <li>
                      <a href="genre/isekai.html" title="Isekai">Isekai</a>
                    </li>

                    <li><a href="genre/josei.html" title="Josei">Josei</a></li>

                    <li><a href="genre/kids.html" title="Kids">Kids</a></li>

                    <li><a href="genre/magic.html" title="Magic">Magic</a></li>

                    <li>
                      <a href="genre/marial-arts.html" title="Martial Arts"
                        >Martial Arts</a
                      >
                    </li>

                    <li><a href="genre/mecha.html" title="Mecha">Mecha</a></li>

                    <li>
                      <a href="genre/military.html" title="Military"
                        >Military</a
                      >
                    </li>

                    <li><a href="genre/music.html" title="Music">Music</a></li>

                    <li>
                      <a href="genre/mystery.html" title="Mystery">Mystery</a>
                    </li>

                    <li>
                      <a href="genre/parody.html" title="Parody">Parody</a>
                    </li>

                    <li>
                      <a href="genre/police.html" title="Police">Police</a>
                    </li>

                    <li>
                      <a href="genre/psychological.html" title="Psychological"
                        >Psychological</a
                      >
                    </li>

                    <li>
                      <a href="genre/romance.html" title="Romance">Romance</a>
                    </li>

                    <li>
                      <a href="genre/samurai.html" title="Samurai">Samurai</a>
                    </li>

                    <li>
                      <a href="genre/school.html" title="School">School</a>
                    </li>

                    <li>
                      <a href="genre/sci-fi.html" title="Sci-Fi">Sci-Fi</a>
                    </li>

                    <li>
                      <a href="genre/seinen.html" title="Seinen">Seinen</a>
                    </li>

                    <li>
                      <a href="genre/shoujo.html" title="Shoujo">Shoujo</a>
                    </li>

                    <li>
                      <a href="genre/shoujo-ai.html" title="Shoujo Ai"
                        >Shoujo Ai</a
                      >
                    </li>

                    <li>
                      <a href="genre/shounen.html" title="Shounen">Shounen</a>
                    </li>

                    <li>
                      <a href="genre/shounen-ai.html" title="Shounen Ai"
                        >Shounen Ai</a
                      >
                    </li>

                    <li>
                      <a href="genre/slice-of-life.html" title="Slice of Life"
                        >Slice of Life</a
                      >
                    </li>

                    <li><a href="genre/space.html" title="Space">Space</a></li>

                    <li>
                      <a href="genre/sports.html" title="Sports">Sports</a>
                    </li>

                    <li>
                      <a href="genre/super-power.html" title="Super Power"
                        >Super Power</a
                      >
                    </li>

                    <li>
                      <a href="genre/supernatural.html" title="Supernatural"
                        >Supernatural</a
                      >
                    </li>

                    <li>
                      <a href="genre/thriller.html" title="Thriller"
                        >Thriller</a
                      >
                    </li>

                    <li>
                      <a href="genre/vampire.html" title="Vampire">Vampire</a>
                    </li>
                  </ul>
                  <div class="clearfix"></div>
                  <button
                    class="btn btn-sm btn-block btn-showmore mt-2"
                  ></button>
                </div>
              </div>
            </section>
          </div>'''

yeni_kod = ''' '''

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
