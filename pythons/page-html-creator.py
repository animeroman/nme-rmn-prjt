import json
import os
import requests  

# Load the JSON data from the URL
file_url = 'https://raw.githubusercontent.com/animeroman/RomanAPI/refs/heads/main/export.json'

response = requests.get(file_url)
if response.status_code != 200:
    raise Exception(f"Failed to fetch JSON file: {response.status_code}")

data = response.json()  # Convert response to JSON

# Directory to save the HTML files
# output_dir = 'C:/Users/User1/projects/AnimeRoman/page'
output_dir = 'C:/Users/User1/projects/AnimeRoman/watch'
os.makedirs(output_dir, exist_ok=True)

# Loop through each entry in the JSON
for entry in data:
    # Get the page name
    english_name = entry.get('animeEnglish', '')
    original_name = entry.get('animeOriginal', '')
    japanese_name = entry.get('japanese', '')
    end_date = entry.get('dateEnd', '')
    start_date = entry.get('dateStart', '')
    anime_description = entry.get('description', '')
    anime_duration = entry.get('duration', '')
    page_name = entry.get('page', '')
    eposide_count = entry.get('eposideCount', '')
    poster_url = entry.get('poster', '')
    anime_rated = entry.get('rated', '')
    anime_score = entry.get('score', '')
    anime_season = entry.get('season', '')
    anime_type = entry.get('type', '')

    # Ensure the page_name is valid for a filename
    if not page_name:
        continue  # Skip empty names

    page_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in page_name)  # Sanitize filename

    # Define the HTML template with dynamic poster insertion
    html_page_code = f"""<!doctype html>
<html lang="en">
  <head>
    <title>
      Watch {english_name} Sub/Dub online Free with with no ads or optional ads
      - AnimeRoman
    </title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="robots" content="index,follow" />
    <meta http-equiv="content-language" content="en" />
    <meta
      name="description"
      content="The Ultimate Site to Watch {english_name} Online for Free in Sub/Dub Versions, with the option to Embed Your Favorite Episodes!"
    />
    <meta
      name="keywords"
      content="{english_name} English Sub/Dub, free {english_name} online, watch {english_name} online, watch {english_name} free, download {english_name} anime, download {english_name} free, {english_name} OVA episodes, {english_name} OVA free, watch {english_name} OVA, download {english_name} OVA, latest {english_name} OVA"
    />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="attack-on-titan-112.html" />
    <meta
      property="og:title"
      content="Watch {english_name} Sub/Dub online Free with with no ads or optional ads - AnimeRoman"
    />
    <meta property="og:image" content="images/capture.png" />
    <meta property="og:image:width" content="650" />
    <meta property="og:image:height" content="350" />
    <meta
      property="og:description"
      content="The Ultimate Site to Watch {english_name} Online for Free in Sub/Dub Versions, with the option to Embed Your Favorite Episodes!"
    />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1"
    />
    <meta name="apple-mobile-web-app-status-bar" content="#202125" />
    <meta name="theme-color" content="#202125" />
    <link rel="shortcut icon" href="../favicon.ico" type="image/x-icon" />
    <link
      rel="apple-touch-icon"
      sizes="180x180"
      href="../images/apple-touch-icon.png"
    />
    <link
      rel="icon"
      type="image/png"
      sizes="32x32"
      href="../favicon-32x32.png"
    />
    <link
      rel="icon"
      type="image/png"
      sizes="16x16"
      href="../favicon-16x16.png"
    />
    <link
      rel="mask-icon"
      href="../images/safari-pinned-tab.svg"
      color="#badfff"
    />
    <meta name="msapplication-TileColor" content="#95784d" />
    <link rel="icon" sizes="192x192" href="../images/icons-192.png" />
    <link rel="icon" sizes="512x512" href="../images/icons-512.png" />
    <link rel="manifest" href="manifest.json" />
    <!-- Google tag (gtag.js) -->
    <!-- <script
      async
      src="https://www.googletagmanager.com/gtag/js?id=G-R34F2GCSBW"
    ></script> -->

    <!--Begin: Stylesheet-->
    <link rel="stylesheet" href="../css/bootstrap.min.css" />
    <link rel="stylesheet" href="../font/bootstrap-icons.css" />
    <link rel="stylesheet" href="../css/all.css" />
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/icon?family=Material+Icons"
    />
    <link rel="stylesheet" href="../css/styles.css" />
    <!-- <link rel="stylesheet" href="../css/styles.minc619.css?v=1.0" /> -->
    <!--End: Stylesheet-->
  </head>
  <body>
    <div id="sidebar_menu_bg"></div>
    <div id="sidebar_menu">
      <button class="btn btn-radius btn-sm btn-secondary toggle-sidebar">
        <i class="fas fa-angle-left mr-2"></i>Close menu
      </button>
      <div class="sb-setting">
        <div class="header-setting">
          <div class="hs-toggles">
            <a
              href=""
              class="hst-item"
              id="random2"
              data-toggle="tooltip"
              data-original-title="Watch random anime"
            >
              <div class="hst-icon"><i class="fas fa-question"></i></div>
              <div class="name"><span>Random</span></div>
            </a>
            <div
              class="hst-item mr-0"
              data-toggle="tooltip"
              title="Select language of anime name to display."
            >
              <div class="select-anime-name toggle-lang">
                <span class="en">EN</span><span class="jp">JP</span>
              </div>
              <div class="name"><span>Anime Name</span></div>
            </div>
            <div class="clearfix"></div>
          </div>
        </div>
      </div>
      <ul class="nav sidebar_menu-list">
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
                <a class="nav-link" href="../genre/drama.html">Drama</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/fantasy.html">Fantasy</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/game.html">Game</a>
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
      </ul>
      <div class="clearfix"></div>
    </div>
    <div id="wrapper" data-id="112" data-page="detail">
      <div id="header" class="">
        <div class="container">
          <div id="mobile_menu"><i class="fa fa-bars"></i></div>
          <a href="../index.html" id="logo">
            <img src="../images/logo7e0c.png?v=0.1" alt="AnimeRoman" />
            <div class="clearfix"></div>
          </a>
          <div id="search">
            <div class="search-content">
              <form action="../filter.html?keyword=+" autocomplete="off">
                <a href="../filter.html?keyword=+" class="filter-icon"
                  >Filter</a
                >
                <input
                  type="text"
                  class="form-control search-input"
                  name="keyword"
                  placeholder="Search anime..."
                  required
                />
                <div
                  class="nav search-result-pop"
                  id="search-suggest"
                  style="display: none"
                >
                  <div class="result"></div>
                </div>
                <button type="submit" class="search-icon">
                  <i class="fas fa-search"></i>
                </button>
              </form>
            </div>
          </div>
          <!-- <div class="header-group">
            <div class="anw-group">
              <div class="zrg-title">
                <span class="top">Join now</span
                ><span class="bottom">AnimeRoman Group</span>
              </div>
              <div class="zrg-list">
                <div class="item">
                  <a
                    href="https://discord.gg/AnimeRoman"
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
            </div> -->
        </div>
        <div class="header-setting">
          <div class="hs-toggles">
            <a
              href=""
              class="hst-item"
              id="random"
              data-toggle="tooltip"
              data-original-title="Watch random anime"
            >
              <div class="hst-icon"><i class="fas fa-question"></i></div>
              <div class="name"><span>Random</span></div>
            </a>
            <div
              class="hst-item"
              data-toggle="tooltip"
              title="Select language of anime name to display."
            >
              <div class="select-anime-name toggle-lang">
                <span class="en">EN</span><span class="jp">JP</span>
              </div>
              <div class="name"><span>Anime Name</span></div>
            </div>
            <div class="clearfix"></div>
          </div>
        </div>

        <div id="pick_menu">
          <div class="pick_menu-ul">
            <ul class="ulclear">
              <li class="pmu-item pmu-item-home">
                <a class="pmu-item-icon" href="../home.html" title="Home">
                  <img
                    src="../images/pick-home.svg"
                    data-toggle="tooltip"
                    data-placement="right"
                    title="Home"
                  />
                </a>
              </li>
              <li class="pmu-item pmu-item-movies">
                <a class="pmu-item-icon" href="../movie.html" title="Movies">
                  <img
                    src="../images/pick-movies.svg"
                    data-toggle="tooltip"
                    data-placement="right"
                    title="Movies"
                  />
                </a>
              </li>
              <li class="pmu-item pmu-item-show">
                <a class="pmu-item-icon" href="../tv.html" title="TV Series">
                  <img
                    src="../images/pick-show.svg"
                    data-toggle="tooltip"
                    data-placement="right"
                    title="TV Series"
                  />
                </a>
              </li>
              <li class="pmu-item pmu-item-popular">
                <a
                  class="pmu-item-icon"
                  href="../most-popular.html"
                  title="Most Popular"
                >
                  <img
                    src="../images/pick-popular.svg"
                    data-toggle="tooltip"
                    data-placement="right"
                    title="Most Popular"
                  />
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div id="header_right"></div>
        <div id="mobile_search"><i class="fa fa-search"></i></div>
        <div class="clearfix"></div>
      </div>
    </div>
    <div class="clearfix"></div>
    <!--Begin: Main-->
    <div id="main-wrapper" class="layout-page layout-page-detail">
      <!-- Detail -->
      <div id="ani_detail">
        <div class="ani_detail-stage">
          <div class="container">
            <div class="anis-cover-wrap">
              <div class="anis-cover"></div>
            </div>
            <div class="anis-content">
              <div class="anisc-poster">
                <div class="film-poster">
                  <img
                    src="{poster_url}"
                    class="film-poster-img"
                    alt="{english_name}"
                  />
                </div>
              </div>
              <div class="anisc-detail">
                <div class="prebreadcrumb">
                  <nav aria-label="breadcrumb">
                    <ol class="breadcrumb">
                      <li class="breadcrumb-item">
                        <a href="../season/{anime_season}.html"
                          >{anime_season}</a
                        >
                      </li>
                      <li class="breadcrumb-item">
                        <a href="../{anime_type}.html">anime_type</a>
                      </li>
                      <li
                        class="breadcrumb-item dynamic-name active"
                        data-jname="{original_name}"
                      >
                        english_name
                      </li>
                    </ol>
                  </nav>
                </div>
                <h2
                  class="film-name dynamic-name"
                  data-jname="{original_name}"
                ></h2>
                <div id="mal-sync"></div>
                <div class="film-stats">
                  <div class="tick">
                    <div class="tick-item tick-pg">{anime_rated}</div>

                    <div class="tick-item tick-sub">
                      <i class="fas fa-closed-captioning mr-1">0</i>
                    </div>

                    <div class="tick-item tick-dub">
                      <i class="fas fa-microphone mr-1">0</i>
                    </div>

                    <div class="tick-item tick-eps">{eposide_count}</div>

                    <span class="dot"></span>
                    <span class="item item-type">{anime_type}</span>
                    <span class="dot"></span>
                    <span class="item item-duration">{anime_duration}</span>
                    <div class="clearfix"></div>
                  </div>
                </div>

                <div class="film-buttons">
                  <a
                    href="../watch/{page_name}.html"
                    class="btn btn-radius btn-primary btn-play"
                    ><i class="fas fa-play mr-2"></i>Watch now</a
                  >

                  <div class="dr-fav" id="watch-list-content"></div>
                </div>
                <div class="film-description m-hide">
                  <div class="text">{anime_description}</div>
                </div>
              </div>
              <div class="anisc-info-wrap">
                <div class="anisc-info">
                  <div class="item item-title w-hide">
                    <span class="item-head">Overview:</span>
                    <div class="text"></div>
                  </div>
                  <div class="item item-title">
                    <span class="item-head">Japanese:</span>
                    <span class="name">{japanese_name}</span>
                  </div>

                  <div class="item item-title">
                    <span class="item-head">Synonyms:</span>
                    <span class="name"></span>
                  </div>

                  <div class="item item-title">
                    <span class="item-head">Aired:</span>
                    <span class="name">{start_date} to {end_date}</span>
                  </div>
                  <div class="item item-title">
                    <span class="item-head">Season:</span>
                    <span class="name">{anime_season}</span>
                  </div>
                  <div class="item item-title">
                    <span class="item-head">Duration:</span>
                    <span class="name">{anime_duration}</span>
                  </div>
                  <div class="item item-title">
                    <span class="item-head">Status:</span>
                    <span class="name"></span>
                  </div>
                  <div class="item item-title">
                    <span class="item-head">MAL Score:</span>
                    <span class="name">{anime_score}</span>
                  </div>

                  <div class="item item-list">
                    <span class="item-head">Genres:</span>
                  </div>

                  <div class="item item-title">
                    <span class="item-head">Studios:</span>
                  </div>

                  <div class="item item-title">
                    <span class="item-head">Producers:</span>
                  </div>
                </div>
                <div class="clearfix"></div>
              </div>
              <div class="clearfix"></div>
            </div>
          </div>
        </div>
      </div>
      <div class="container">
        <div id="main-content">
          <section class="block_area block_area_category">
            <div class="block_area-header">
              <div class="float-left bah-heading mr-4">
                <h2 class="cat-heading">Collections</h2>
              </div>
              <div class="clearfix"></div>
            </div>
            <div class="tab-content">
              <div
                class="block_area-content block_area-list film_list film_list-grid film_list-wfeature"
              >
                <div class="film_list-wrap connection-wrapper">
                  <div class="loading-relative loading-connection">
                    <div class="loading">
                      <div class="span1"></div>
                      <div class="span2"></div>
                      <div class="span3"></div>
                    </div>
                  </div>
                </div>
                <div class="clearfix"></div>
              </div>
            </div>
          </section>

          <section class="block_area block_area_category">
            <div class="block_area-header">
              <div class="float-left bah-heading mr-4">
                <h2 class="cat-heading">Recommendations</h2>
              </div>
              <div class="clearfix"></div>
            </div>
            <div class="tab-content">
              <div
                class="block_area-content block_area-list film_list film_list-grid film_list-wfeature"
              >
                <div class="film_list-wrap recommned-wrapper">
                  <div class="loading-relative">
                    <div class="loading">
                      <div class="span1"></div>
                      <div class="span2"></div>
                      <div class="span3"></div>
                    </div>
                  </div>
                </div>
                <div class="clearfix"></div>
              </div>
            </div>
          </section>
          <div class="clearfix"></div>
        </div>
      </div>
    </div>
    <div class="clearfix"></div>
    <div id="footer">
      <div id="footer-about">
        <div class="container">
          <div class="footer-top">
            <a href="../home.html" class="footer-logo">
              <img src="../images/logo7e0c.png?v=0.1" alt="AnimeRoman" />
              <div class="clearfix"></div>
            </a>
            <div class="clearfix"></div>
          </div>
          <div class="footer-az">
            <div class="block mb-3">
              <span class="ftaz">A-Z LIST</span
              ><span class="size-s"
                >Finding anime alphabetically from A to Z.</span
              >
            </div>
            <ul class="ulclear az-list">
              <li><a href="az-list.html">All</a></li>
              <li><a href="az-list/other.html">#</a></li>
              <li><a href="az-list/0-9.html">0-9</a></li>

              <li><a href="az-list/A.html">A</a></li>

              <li><a href="az-list/B.html">B</a></li>

              <li><a href="az-list/C.html">C</a></li>

              <li><a href="az-list/D.html">D</a></li>

              <li><a href="az-list/E.html">E</a></li>

              <li><a href="az-list/F.html">F</a></li>

              <li><a href="az-list/G.html">G</a></li>

              <li><a href="az-list/H.html">H</a></li>

              <li><a href="az-list/I.html">I</a></li>

              <li><a href="az-list/J.html">J</a></li>

              <li><a href="az-list/K.html">K</a></li>

              <li><a href="az-list/L.html">L</a></li>

              <li><a href="az-list/M.html">M</a></li>

              <li><a href="az-list/N.html">N</a></li>

              <li><a href="az-list/O.html">O</a></li>

              <li><a href="az-list/P.html">P</a></li>

              <li><a href="az-list/Q.html">Q</a></li>

              <li><a href="az-list/R.html">R</a></li>

              <li><a href="az-list/S.html">S</a></li>

              <li><a href="az-list/T.html">T</a></li>

              <li><a href="az-list/U.html">U</a></li>

              <li><a href="az-list/V.html">V</a></li>

              <li><a href="az-list/W.html">W</a></li>

              <li><a href="az-list/X.html">X</a></li>

              <li><a href="az-list/Y.html">Y</a></li>

              <li><a href="az-list/Z.html">Z</a></li>
            </ul>
            <div class="clearfix"></div>
          </div>
          <div class="footer-links">
            <ul class="ulclear">
              <li>
                <a href="terms.html" title="Terms of service"
                  >Terms of service</a
                >
              </li>
            </ul>
            <div class="clearfix"></div>
          </div>
          <div class="about-text">
            Disclaimer: AnimeRoman is a free streaming site with no ads,
            allowing you to watch Movies, TV series, OVA, ONA, Special and anime
            episodes without registration. All content is embedded by users or
            linked from third-party services, and no files are stored on our
            servers. Please note, all media is provided by non-affiliated third
            parties.
          </div>
          <p class="copyright">© AnimeRoman.com, 2025</p>
        </div>
      </div>
    </div>

    <script src="../www.google.com/recaptcha/api4a96.js?render=6Lc7dH8pAAAAAIGw-BOEYDAZvcs3afxf6XHaLsQL&amp;hl=en"></script>

    <script
      src="../js/socket.io.min.js"
      integrity="sha384-/KNQL8Nu5gCHLqwqfQjA689Hhoqgi2S84SNUxC3roTe4EhJ9AfLkp8QiQcU8AMzI"
      crossorigin="anonymous"
    ></script>
    <script type="text/javascript" src="../js/app.minffaf.js?v=1.4"></script>

    <script type="module" src="../js/recommend.js" async="async"></script>
    <script type="module" src="../js/page-page.js" async="async"></script>
  </body>
</html>
"""

    html_watchpage_code = f"""<!doctype html>
<html lang="en">
  <head>
    <title>
      Watch {english_name} Sub/Dub online Free with with no ads or optional ads
      - AnimeRoman
    </title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="robots" content="index,follow" />
    <meta http-equiv="content-language" content="en" />
    <meta name="description" content="{anime_description}" />
    <meta
      name="keywords"
      content="{english_name} English Sub/Dub, free {english_name} online, watch {english_name} online, watch {english_name} free, download {english_name} anime, download {english_name} free, {english_name} OVA episodes, {english_name} OVA free, watch {english_name} OVA, download {english_name} OVA, latest {english_name} OVA"
    />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{page_name}.html" />
    <meta
      property="og:title"
      content="Watch {english_name} Sub/Dub online Free with with no ads or optional ads - AnimeRoman"
    />
    <meta property="og:image" content="../images/capture.png" />
    <meta property="og:image:width" content="650" />
    <meta property="og:image:height" content="350" />
    <meta property="og:description" content="{anime_description}" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1"
    />
    <meta name="apple-mobile-web-app-status-bar" content="#202125" />
    <meta name="theme-color" content="#202125" />
    <link rel="shortcut icon" href="../favicon.ico" type="image/x-icon" />
    <link
      rel="apple-touch-icon"
      sizes="180x180"
      href="../images/apple-touch-icon.png"
    />
    <link
      rel="icon"
      type="image/png"
      sizes="32x32"
      href="../favicon-32x32.png"
    />
    <link
      rel="icon"
      type="image/png"
      sizes="16x16"
      href="../favicon-16x16.png"
    />
    <link
      rel="mask-icon"
      href="../images/safari-pinned-tab.svg"
      color="#badfff"
    />
    <meta name="msapplication-TileColor" content="#95784d" />
    <link rel="icon" sizes="192x192" href="../images/icons-192.png" />
    <link rel="icon" sizes="512x512" href="../images/icons-512.png" />
    <link rel="manifest" href="../manifest.json" />
    <!-- Google tag (gtag.js) -->
    <!-- <script
      async
      src="https://www.googletagmanager.com/gtag/js?id=G-R34F2GCSBW"
    ></script> -->

    <!--Begin: Stylesheet-->
    <link rel="stylesheet" href="../css/bootstrap.min.css" />
    <link rel="stylesheet" href="../font/bootstrap-icons.css" />
    <link rel="stylesheet" href="../css/all.css" />
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/icon?family=Material+Icons"
    />
    <link rel="stylesheet" href="../css/styles.css" />
    <!-- <link rel="stylesheet" href="../css/styles.minc619.css?v=1.0" /> -->
    <!--End: Stylesheet-->
  </head>
  <body>
    <div id="sidebar_menu_bg"></div>
    <div id="sidebar_menu">
      <button class="btn btn-radius btn-sm btn-secondary toggle-sidebar">
        <i class="fas fa-angle-left mr-2"></i>Close menu
      </button>
      <div class="sb-setting">
        <div class="header-setting">
          <div class="hs-toggles">
            <a
              href=""
              class="hst-item"
              id="random2"
              data-toggle="tooltip"
              data-original-title="Watch random anime"
            >
              <div class="hst-icon"><i class="fas fa-question"></i></div>
              <div class="name"><span>Random</span></div>
            </a>
            <div
              class="hst-item mr-0"
              data-toggle="tooltip"
              title="Select language of anime name to display."
            >
              <div class="select-anime-name toggle-lang">
                <span class="en">EN</span><span class="jp">JP</span>
              </div>
              <div class="name"><span>Anime Name</span></div>
            </div>
            <div class="clearfix"></div>
          </div>
        </div>
      </div>
      <ul class="nav sidebar_menu-list">
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
                <a class="nav-link" href="../genre/drama.html">Drama</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/fantasy.html">Fantasy</a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="../genre/game.html">Game</a>
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
                <a class="nav-link" href="../genre/shounen.html">Shounen</a>
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
      </ul>
      <div class="clearfix"></div>
    </div>
    <div id="wrapper" data-id="7190" data-page="watch">
      <div id="header" class="">
        <div class="container">
          <div id="mobile_menu"><i class="fa fa-bars"></i></div>
          <a href="../index.html" id="logo">
            <img src="../images/logo7e0c.png?v=0.1" alt="AnimeRoman" />
            <div class="clearfix"></div>
          </a>
          <div id="search">
            <div class="search-content">
              <form action="../filter.html?keyword=+" autocomplete="off">
                <a href="../filter.html?keyword=+" class="filter-icon"
                  >Filter</a
                >
                <input
                  type="text"
                  class="form-control search-input"
                  name="keyword"
                  placeholder="Search anime..."
                  required
                />
                <div class="suggestion-place"></div>
                <div
                  class="nav search-result-pop"
                  id="search-suggest"
                  style="display: none"
                >
                  <div class="result"></div>
                </div>
                <button type="submit" class="search-icon">
                  <i class="fas fa-search"></i>
                </button>
              </form>
            </div>
          </div>
          <div class="header-setting">
            <div class="hs-toggles">
              <a
                href=""
                class="hst-item"
                id="random"
                data-toggle="tooltip"
                data-original-title="Watch random anime"
              >
                <div class="hst-icon"><i class="fas fa-question"></i></div>
                <div class="name"><span>Random</span></div>
              </a>
              <div
                class="hst-item"
                data-toggle="tooltip"
                title="Select language of anime name to display."
              >
                <div class="select-anime-name toggle-lang">
                  <span class="en">EN</span><span class="jp">JP</span>
                </div>
                <div class="name"><span>Anime Name</span></div>
              </div>
              <div class="clearfix"></div>
            </div>
          </div>

          <div id="pick_menu">
            <div class="pick_menu-ul">
              <ul class="ulclear">
                <li class="pmu-item pmu-item-home">
                  <a class="pmu-item-icon" href="../home.html" title="Home">
                    <img
                      src="../images/pick-home.svg"
                      data-toggle="tooltip"
                      data-placement="right"
                      title="Home"
                    />
                  </a>
                </li>
                <li class="pmu-item pmu-item-movies">
                  <a class="pmu-item-icon" href="../movie.html" title="Movies">
                    <img
                      src="../images/pick-movies.svg"
                      data-toggle="tooltip"
                      data-placement="right"
                      title="Movies"
                    />
                  </a>
                </li>
                <li class="pmu-item pmu-item-show">
                  <a class="pmu-item-icon" href="../tv.html" title="TV Series">
                    <img
                      src="../images/pick-show.svg"
                      data-toggle="tooltip"
                      data-placement="right"
                      title="TV Series"
                    />
                  </a>
                </li>
                <li class="pmu-item pmu-item-popular">
                  <a
                    class="pmu-item-icon"
                    href="../most-popular.html"
                    title="Most Popular"
                  >
                    <img
                      src="../images/pick-popular.svg"
                      data-toggle="tooltip"
                      data-placement="right"
                      title="Most Popular"
                    />
                  </a>
                </li>
              </ul>
            </div>
          </div>

          <div id="header_right"></div>
          <div id="mobile_search"><i class="fa fa-search"></i></div>
          <div class="clearfix"></div>
        </div>
      </div>
      <div class="clearfix"></div>
      <div
        id="main-wrapper"
        class="layout-page layout-page-detail layout-page-watchtv"
      >
        <div id="ani_detail">
          <div class="ani_detail-stage">
            <div class="container">
              <div class="anis-cover-wrap">
                <div class="anis-cover"></div>
              </div>
              <div class="anis-watch-wrap">
                <div class="prebreadcrumb">
                  <nav aria-label="breadcrumb">
                    <ol class="breadcrumb">
                      <li class="breadcrumb-item">
                        <a
                          href="../season/{anime_season}.html"
                          title="{anime_season}"
                          >{anime_season}</a
                        >
                      </li>
                      <li class="breadcrumb-item">
                        <a href="../{anime_type}.html">{anime_type}</a>
                      </li>
                      <li
                        class="breadcrumb-item dynamic-name active"
                        data-jname="{original_name}"
                      >
                        {english_name}
                      </li>
                    </ol>
                  </nav>
                </div>
                <div class="anis-watch anis-watch-tv">
                  <div class="watch-player">
                    <div class="player-frame">
                      <div
                        class="loading-relative loading-box"
                        id="embed-loading"
                        style=""
                      >
                        <div class="loading">
                          <div class="span1"></div>
                          <div class="span2"></div>
                          <div class="span3"></div>
                        </div>
                      </div>
                      <iframe
                        id="iframe-embed"
                        src=""
                        frameborder="0"
                        referrerpolicy="strict-origin"
                        allow="autoplay; fullscreen; geolocation; display-capture; picture-in-picture"
                        webkitallowfullscreen=""
                        mozallowfullscreen=""
                        style=""
                      ></iframe>
                    </div>
                    <!-- <div class="player-frame">
                      <div
                        class="loading-relative loading-box"
                        id="embed-loading"
                      >
                        <div class="loading">
                          <div class="span1"></div>
                          <div class="span2"></div>
                          <div class="span3"></div>
                        </div>
                      </div>
                      <iframe
                        id="iframe-embed"
                        src="#"
                        frameborder="0"
                        referrerpolicy="strict-origin"
                        allow="autoplay; fullscreen; geolocation; display-capture; picture-in-picture"
                        webkitallowfullscreen
                        mozallowfullscreen
                      ></iframe>
                    </div> -->
                    <div class="player-controls">
                      <div class="player-item" data-src="#">
                        <a
                          href="javascript:;"
                          class="btn"
                          data-toggle="modal"
                          data-target="#modalcharacters"
                          >Copy Embed</a
                        >
                      </div>
                      <div class="pc-item pc-toggle pc-autoplay">
                        <div
                          class="toggle-basic quick-settings"
                          data-option="auto_play"
                        >
                          <span class="tb-name">Auto Play</span>
                          <span class="tb-result"></span>
                        </div>
                      </div>
                      <div class="pc-item pc-toggle pc-autonext">
                        <div
                          class="toggle-basic quick-settings"
                          data-option="auto_next"
                        >
                          <span class="tb-name">Auto Next</span>
                          <span class="tb-result"></span>
                        </div>
                      </div>
                      <div class="pc-right">
                        <div class="pc-item pc-control block-prev" style="">
                          <a
                            class="btn btn-sm btn-prev"
                            href="javascript:;"
                            onclick="prevEpisode()"
                            ><i class="fas fa-backward mr-2"></i>Prev</a
                          >
                        </div>
                        <div class="pc-item pc-control block-next" style="">
                          <a
                            class="btn btn-sm btn-next"
                            href="javascript:;"
                            onclick="nextEpisode()"
                            >Next<i class="fas fa-forward ml-2"></i
                          ></a>
                        </div>
                      </div>
                      <div class="clearfix"></div>
                    </div>
                  </div>
                  <div class="player-servers">
                    <div class="loading-relative lr-2">
                      <div class="loading">
                        <div class="span1"></div>
                        <div class="span2"></div>
                        <div class="span3"></div>
                      </div>
                    </div>
                  </div>

                  <div id="episodes-content">
                    <div class="seasons-block">
                      <div id="detail-ss-list" class="detail-seasons">
                        <div class="detail-infor-content">
                          <div class="ss-choice">
                            <div class="ssc-list">
                              <div id="ssc-list" class="ssc-button">
                                <div class="ssc-label">List of episodes:</div>
                              </div>
                            </div>
                            <div class="clearfix"></div>
                          </div>
                        </div>
                      </div>
                      <div class="clearfix"></div>
                    </div>
                    <div class="loading-relative lr-1">
                      <div class="loading">
                        <div class="span1"></div>
                        <div class="span2"></div>
                        <div class="span3"></div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="anis-watch-detail">
                  <div class="anis-content">
                    <div class="anisc-poster">
                      <div class="film-poster">
                        <img
                          src="{poster_url}"
                          class="film-poster-img"
                          alt="{english_name}"
                        />
                      </div>
                    </div>
                    <div class="anisc-detail">
                      <h2 class="film-name">
                        <a
                          href="../{page_name}.html"
                          class="text-white dynamic-name"
                          title="{english_name}"
                          data-jname="{original_name}"
                        ></a>
                      </h2>
                      <div class="film-stats">
                        <div class="tick">
                          <div class="tick-item tick-pg">{anime_rated}</div>

                          <div class="tick-item tick-sub">
                            <i class="fas fa-closed-captioning mr-1">0</i>
                          </div>

                          <div class="tick-item tick-dub">
                            <i class="fas fa-microphone mr-1">0</i>
                          </div>

                          <div class="tick-item tick-eps">{eposide_count}</div>

                          <span class="dot"></span>
                          <span class="item item-type">{anime_type}</span>
                          <span class="dot"></span>
                          <span class="item item-duration"
                            >{anime_duration}</span
                          >
                          <div class="clearfix"></div>
                        </div>
                      </div>
                      <div class="film-description m-hide">
                        <div class="text">{anime_description}</div>
                      </div>
                      <div class="block">
                        <a
                          href="../page/{page_name}.html"
                          class="btn btn-xs btn-light"
                          >View detail</a
                        >
                      </div>
                    </div>
                    <div class="clearfix"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="container">
        <div id="main-content">
          <section class="block_area block_area_category">
            <div class="block_area-header">
              <div class="float-left bah-heading mr-4">
                <h2 class="cat-heading">Collections</h2>
              </div>
              <div class="clearfix"></div>
            </div>
            <div class="tab-content">
              <div
                class="block_area-content block_area-list film_list film_list-grid film_list-wfeature"
              >
                <div class="film_list-wrap connection-wrapper">
                  <div class="loading-relative loading-connection">
                    <div class="loading">
                      <div class="span1"></div>
                      <div class="span2"></div>
                      <div class="span3"></div>
                    </div>
                  </div>
                </div>
                <div class="clearfix"></div>
              </div>
            </div>
          </section>

          <section class="block_area block_area_category">
            <div class="block_area-header">
              <div class="float-left bah-heading mr-4">
                <h2 class="cat-heading">Recommendations</h2>
              </div>
              <div class="clearfix"></div>
            </div>
            <div class="tab-content">
              <div
                class="block_area-content block_area-list film_list film_list-grid film_list-wfeature"
              >
                <div class="film_list-wrap recommned-wrapper">
                  <div class="loading-relative">
                    <div class="loading">
                      <div class="span1"></div>
                      <div class="span2"></div>
                      <div class="span3"></div>
                    </div>
                  </div>
                </div>
                <div class="clearfix"></div>
              </div>
            </div>
          </section>
          <div class="clearfix"></div>
        </div>
      </div>
      <div class="clearfix"></div>
      <div id="footer">
        <div id="footer-about">
          <div class="container">
            <div class="footer-top">
              <a href="../home.html" class="footer-logo">
                <img src="../images/logo7e0c.png?v=0.1" alt="AnimeRoman" />
                <div class="clearfix"></div>
              </a>
              <div class="clearfix"></div>
            </div>
            <div class="footer-az">
              <div class="block mb-3">
                <span class="ftaz">A-Z LIST</span
                ><span class="size-s"
                  >Finding anime alphabetically from A to Z.</span
                >
              </div>
              <ul class="ulclear az-list">
                <li><a href="../az-list.html">All</a></li>
                <li><a href="../az-list/other.html">#</a></li>
                <li><a href="../az-list/0-9.html">0-9</a></li>

                <li><a href="../az-list/A.html">A</a></li>

                <li><a href="../az-list/B.html">B</a></li>

                <li><a href="../az-list/C.html">C</a></li>

                <li><a href="../az-list/D.html">D</a></li>

                <li><a href="../az-list/E.html">E</a></li>

                <li><a href="../az-list/F.html">F</a></li>

                <li><a href="../az-list/G.html">G</a></li>

                <li><a href="../az-list/H.html">H</a></li>

                <li><a href="../az-list/I.html">I</a></li>

                <li><a href="../az-list/J.html">J</a></li>

                <li><a href="../az-list/K.html">K</a></li>

                <li><a href="../az-list/L.html">L</a></li>

                <li><a href="../az-list/M.html">M</a></li>

                <li><a href="../az-list/N.html">N</a></li>

                <li><a href="../az-list/O.html">O</a></li>

                <li><a href="../az-list/P.html">P</a></li>

                <li><a href="../az-list/Q.html">Q</a></li>

                <li><a href="../az-list/R.html">R</a></li>

                <li><a href="../az-list/S.html">S</a></li>

                <li><a href="../az-list/T.html">T</a></li>

                <li><a href="../az-list/U.html">U</a></li>

                <li><a href="../az-list/V.html">V</a></li>

                <li><a href="../az-list/W.html">W</a></li>

                <li><a href="../az-list/X.html">X</a></li>

                <li><a href="../az-list/Y.html">Y</a></li>

                <li><a href="../az-list/Z.html">Z</a></li>
              </ul>
              <div class="clearfix"></div>
            </div>
            <div class="footer-links">
              <ul class="ulclear">
                <li>
                  <a href="../terms.html" title="Terms of service"
                    >Terms of service</a
                  >
                </li>
              </ul>
              <div class="clearfix"></div>
            </div>
            <div class="about-text">
              Disclaimer: AnimeRoman is a free streaming site with no ads,
              allowing you to watch Movies, TV series, OVA, ONA, Special and
              anime episodes without registration. All content is embedded by
              users or linked from third-party services, and no files are stored
              on our servers. Please note, all media is provided by
              non-affiliated third parties.
            </div>
            <p class="copyright">© AnimeRoman.com, 2025</p>
          </div>
        </div>
      </div>

      <!--End: Modal-->
      <div
        class="modal fade premodal premodal-characters"
        id="modalcharacters"
        tabindex="-1"
        role="dialog"
        aria-hidden="true"
      ></div>
      <!--End: Modal-->

      <script src="../www.google.com/recaptcha/api4a96.js"></script>

      <script src="../js/socket.io.min.js" crossorigin="anonymous"></script>
      <script type="text/javascript" src="../js/app.minffaf.js?v=1.4"></script>

      <!-- <script type="text/javascript" src="../js/watch.mind134.js?v=3.4"></script> -->
      <script type="module" src="../js/search.js" async="async"></script>
      <script type="module" src="../js/random.js" async="async"></script>
      <script type="module" src="../js/recommend.js" async="async"></script>
      <script type="module" src="../js/watch-page.js" async="async"></script>
    </div>
  </body>
</html>
"""

    # Create the filename and path for the HTML file
    html_file_name = f"{page_name}.html"
    html_file_path = os.path.join(output_dir, html_file_name)

    # Write the HTML template to each file
    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        # html_file.write(html_page_code)
        html_file.write(html_watchpage_code)

    print(f"Created: {html_file_path}")

print("All HTML files have been created successfully.")
