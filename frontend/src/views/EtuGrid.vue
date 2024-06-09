<template>
  <router>
      <!DOCTYPE html>

<meta http-equiv="content-type" content="text/html;charset=UTF-8" />
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <meta name="msapplication-TileColor" content="#0E0E0E">
  <meta name="template-color" content="#0E0E0E">
  <link rel="manifest" href="manifest.html" crossorigin>
  <meta name="msapplication-config" content="browserconfig.html">
  <meta name="description" content="Index page">
  <meta name="keywords" content="index, page">
  <meta name="author" content="">
  <link rel="shortcut icon" type="image/x-icon" href="assets/imgs/template/favicon.svg">
  <link href="./template/assets/css/stylecd4ee.css?version=4.1" rel="stylesheet">
  <title>SW Connect </title>
</head>
<body style="overflow-x: hidden;">
 <navbarEntreprise/>
  
  <main class="main">
    <section class="section-box-2">
<div class="container">
  <div class="banner-hero banner-single banner-single-bg">
    <div class="block-banner text-center">
      <h3 class="wow animate__animated animate__fadeInUp"><span class="color-brand-2">Étudiants</span> à la recherche de stages</h3>
      <div class="font-sm color-text-paragraph-2 mt-10 wow animate__animated animate__fadeInUp" data-wow-delay=".1s">Recherchez des étudiants qui recherchent des stages en saisissant un mot clé ou en filtrant les détails correspondant à vos critères <br class="d-none d-xl-block"></div>
      <div class="form-find text-start mt-40 wow animate__animated animate__fadeInUp" data-wow-delay=".2s">
        <form>
          <input id="input-keysearch" class="form-input input-keysearch mr-10" type="text" placeholder="Saisir un mot clé...">
          <button class="btn btn-default btn-find font-sm" @click.prevent="onSearchClick">Rechercher</button>
        </form>
      </div>
    </div>
  </div>
</div>
</section>
   
    <section class="section-box mt-30">
      <div class="container">
        <div class="row flex-row-reverse">
          <div class="col-lg-9 col-md-12 col-sm-12 col-12 float-right grid-row-offer">
            <div class="content-page">
              <div class="box-filters-job">
                <div class="row cus-row">
                  <!--<div class="col-xl-6 col-lg-5"><span class="text-small text-showing">Showing <strong>41-60 </strong>of <strong>944 </strong>jobs</span></div>-->
                  <div class="col-xl-6 col-lg-7 text-lg-end mt-sm-15">
                  
                  </div>
                </div>
              </div>
              <div class="row">
                <template v-if="searchClicked === false && FilterClick === false">

                <div v-for="etudiant in etudiants" :key="etudiant.id"  class="col-xl-4 col-lg-4 col-md-6 col-sm-12 col-12">
                       <div class="card-grid-2 hover-up">
                <div class="card-grid-2-image-left" >
                  <div class="card-grid-2-image-rd online"><a href='candidate-details.html'>
                      <figure><img alt="jobBox" :src="etudiant.profile_photo" style="width:50px;height:50px"></figure></a></div>
                  <div class="card-profile pt-10">
                      <h5><a href="#" @click="redirectToEtudiantDetails(etudiant.id)">{{etudiant.first_name}} {{etudiant.last_name}}</a></h5><span class="font-xs color-text-mutted">{{etudiant.role}}</span>
                  </div>
                </div>
                <div class="card-block-info">
                  <p class="font-xs color-text-paragraph-2">{{etudiant.bio.slice(0, 100)}}</p>
                  <div class="card-2-bottom card-2-bottom-candidate mt-30">
                    <div class="text-start">
                      <a v-for="(skill, index) in etudiant.skills" :key="index" class='btn btn-grey-small cus-mr mr-5' href='jobs-grid.html'>
                                  {{ skill }}
                              </a>
                    </div>
                  </div>
                  <div class="employers-info align-items-center justify-content-center mt-15">
                    <div class="row">
                      <div class="col-6"><span class="d-flex align-items-center"><i class="fi-rr-marker mr-5 ml-0"></i><span class="font-sm color-text-mutted">{{etudiant.location}}</span></span></div>
                    </div>
                  </div>
                </div>
              </div>
                </div>
              </template>
              <template v-if="searchClicked && filteredEtuds.length">

<div v-for="etudiant in filteredEtuds" :key="etudiant.id"  class="col-xl-4 col-lg-4 col-md-6 col-sm-12 col-12">
     <div class="card-grid-2 hover-up">
<div class="card-grid-2-image-left" >
<div class="card-grid-2-image-rd online"><a href='candidate-details.html'>
    <figure><img alt="jobBox" :src="this.baseUrl + etudiant.profile_photo" style="width:50px;height:50px"></figure></a></div>
<div class="card-profile pt-10">
    <h5><a href="#" @click="redirectToEtudiantDetails(etudiant.id)">{{etudiant.first_name}} {{etudiant.last_name}}</a></h5><span class="font-xs color-text-mutted">{{etudiant.role}}</span>
</div>
</div>
<div class="card-block-info">
<p class="font-xs color-text-paragraph-2">{{etudiant.bio.slice(0, 100)}}</p>
<div class="card-2-bottom card-2-bottom-candidate mt-30">
  <div class="text-start">
    <a v-for="(skill, index) in etudiant.skills" :key="index" class='btn btn-grey-small cus-mr mr-5' href='jobs-grid.html'>
                {{ skill }}
            </a>
  </div>
</div>
<div class="employers-info align-items-center justify-content-center mt-15">
  <div class="row">
    <div class="col-6"><span class="d-flex align-items-center"><i class="fi-rr-marker mr-5 ml-0"></i><span class="font-sm color-text-mutted">{{etudiant.location}}</span></span></div>
  </div>
</div>
</div>
</div>
</div>
</template>
<template v-if="FilterClick && filteredEtuds2.length">

<div v-for="etudiant in filteredEtuds2" :key="etudiant.id"  class="col-xl-4 col-lg-4 col-md-6 col-sm-12 col-12">
     <div class="card-grid-2 hover-up">
<div class="card-grid-2-image-left" >
<div class="card-grid-2-image-rd online"><a href='candidate-details.html'>
    <figure><img alt="jobBox" :src="this.baseUrl + etudiant.profile_photo" style="width:50px;height:50px"></figure></a></div>
<div class="card-profile pt-10">
    <h5><a href="#" @click="redirectToEtudiantDetails(etudiant.id)">{{etudiant.first_name}} {{etudiant.last_name}}</a></h5><span class="font-xs color-text-mutted">{{etudiant.role}}</span>
</div>
</div>
<div class="card-block-info">
<p class="font-xs color-text-paragraph-2">{{etudiant.bio.slice(0, 100)}}</p>
<div class="card-2-bottom card-2-bottom-candidate mt-30">
  <div class="text-start">
    <a v-for="(skill, index) in etudiant.skills" :key="index" class='btn btn-grey-small cus-mr mr-5' href='jobs-grid.html'>
                {{ skill }}
            </a>
  </div>
</div>
<div class="employers-info align-items-center justify-content-center mt-15">
  <div class="row">
    <div class="col-6"><span class="d-flex align-items-center"><i class="fi-rr-marker mr-5 ml-0"></i><span class="font-sm color-text-mutted">{{etudiant.location}}</span></span></div>
  </div>
</div>
</div>
</div>
</div>
</template>

              </div>
            </div>
            <!--<div class="paginations">
              <ul class="pager">
                <li><a class="pager-prev" href="#"></a></li>
                <li><a class="pager-number" href="#">1</a></li>
                <li><a class="pager-number" href="#">2</a></li>
                <li><a class="pager-number" href="#">3</a></li>
                <li><a class="pager-number" href="#">4</a></li>
                <li><a class="pager-number" href="#">5</a></li>
                <li><a class="pager-number active" href="#">6</a></li>
                <li><a class="pager-number" href="#">7</a></li>
                <li><a class="pager-next" href="#"></a></li>
              </ul>
            </div>-->
          </div>
          <div class="col-lg-3 col-md-12 col-sm-12 col-12" style="margin-top:-30px">
            <div class="sidebar-shadow none-shadow mb-30">
              <div class="sidebar-filters">
                <div class="filter-block head-border mb-30">
                  <h5>Filtrage Avancé</h5>
                </div>
        
                <div class="filter-block mb-20">
                  <h5 class="medium-heading mb-15">Domaines</h5>
                  <div class="form-group">
                      <ul class="list-checkbox">
                          <li>
                              <label class="cb-container">
                                  <input type="radio" name="domain" value="Agriculture" @change="toggleDomain('Agriculture')">
                                  <span class="text-small">Agriculture</span>
                                  <span class="checkmark"></span>
                              </label>
                          </li>
                          <li>
                              <label class="cb-container">
                                  <input type="radio" name="domain" value="Automotive" @change="toggleDomain('Automotive')">
                                  <span class="text-small">Automotive</span>
                                  <span class="checkmark"></span>
                              </label>
                          </li>
                          <li>
                              <label class="cb-container">
                                  <input type="radio" name="domain" value="Construction" @change="toggleDomain('Construction')">
                                  <span class="text-small">Construction</span>
                                  <span class="checkmark"></span>
                              </label>
                          </li>
                          <li>
                              <label class="cb-container">
                                  <input type="radio" name="domain" value="Consulting" @change="toggleDomain('Consulting')">
                                  <span class="text-small">Consulting</span>
                                  <span class="checkmark"></span>
                              </label>
                          </li>
                          <li>
                              <label class="cb-container">
                                  <input type="radio" name="domain" value="E-commerce" @change="toggleDomain('E-commerce')">
                                  <span class="text-small">E-commerce</span>
                                  <span class="checkmark"></span>
                              </label>
                          </li>
                          <li>
                              <label class="cb-container">
                                  <input type="radio" name="domain" value="Education" @change="toggleDomain('Education')">
                                  <span class="text-small">Education</span>
                                  <span class="checkmark"></span>
                              </label>
                          </li>
                          <li>
                              <label class="cb-container">
                                  <input type="radio" name="domain" value="Energy" @change="toggleDomain('Energy')">
                                  <span class="text-small">Energy</span>
                                  <span class="checkmark"></span>
                              </label>
                          </li>
                          <li>
                              <label class="cb-container">
                                  <input type="radio" name="domain" value="Finance" @change="toggleDomain('Finance')">
                                  <span class="text-small">Finance</span>
                                  <span class="checkmark"></span>
                              </label>
                          </li>
                          <li>
                              <label class="cb-container">
                                  <input type="radio" name="domain" value="Génie Civil" @change="toggleDomain('Génie Civil')">
                                  <span class="text-small">Génie Civil</span>
                                  <span class="checkmark"></span>
                              </label>
                          </li>
                          <li>
                              <label class="cb-container">
                                  <input type="radio" name="domain" value="Informatique" @change="toggleDomain('Informatique')">
                                  <span class="text-small">Informatique</span>
                                  <span class="checkmark"></span>
                              </label>
                          </li>
                          <li>
                              <label class="cb-container">
                                  <input type="radio" name="domain" value="Legal" @change="toggleDomain('Legal')">
                                  <span class="text-small">Legal</span>
                                  <span class="checkmark"></span>
                              </label>
                          </li>
                      </ul>
                  </div>
              </div>
              
                <!--<div class="list-checkbox pb-20" id="scrollable">
                  <h5 class="medium-heading mb-15" style="position:relative;top:-25px;">Payant ou non</h5>
                  <div class="row position-relative mt-10 mb-20">
                    <div class="col-sm-12 box-slider-range">
                      <div id="slider-range"></div>
                    </div>
                    <div class="box-input-money">
                      <input class="input-disabled form-control min-value-money" type="text" name="min-value-money" disabled="disabled" value="">
                      <input class="form-control min-value" type="hidden" name="min-value" value="">
                    </div>
                  </div>
                  <div class="box-number-money">
                    <div class="row mt-30">
                      <div class="col-sm-6 col-6"><span class="font-sm color-brand-1">0dt</span></div>
                      <div class="col-sm-6 col-6 text-end"><span class="font-sm color-brand-1">500dt</span></div>
                    </div>
                  </div>
                </div>-->
        
                <!--<div class="filter-block mb-30">
                  <div class="form-group">
                    <ul class="list-checkbox">
                      <li>
                        <label class="cb-container">
                          <input type="radio" name="stage" value="Bureau" checked="checked" @change="updateTypeStage('Bureau')">
                          <span class="text-small">Bureau</span>
                          <span class="checkmark"></span>
                        </label>
                      </li>
                      <li>
                        <label class="cb-container">
                          <input type="radio" name="stage" value="distance" @change="updateTypeStage('distance')">
                          <span class="text-small">Stage à distance</span>
                          <span class="checkmark"></span>
                        </label>
                      </li>
                    </ul>
                  </div>
                </div>-->
        
                <div class="filter-block mb-30">
                  <h5 class="medium-heading mb-10">Education</h5>
                  <div class="form-group">
                    <ul class="list-checkbox">
                      <li>
                        <label class="cb-container">
                          <input type="radio" name="education" value="Bac+2" @change="updateEduc('+2')">
                          <span class="text-small">Bac +2</span>
                          <span class="checkmark"></span>
                        </label>
                      </li>
                      <li>
                        <label class="cb-container">
                          <input type="radio" name="education" value="Bac+3" checked="checked" @change="updateEduc('+3')">
                          <span class="text-small">Bac +3</span>
                          <span class="checkmark"></span>
                        </label>
                      </li>
                      <li>
                        <label class="cb-container">
                          <input type="radio" name="education" value="Bac+5" checked="checked" @change="updateEduc('+5')">
                          <span class="text-small">Bac +5</span>
                          <span class="checkmark"></span>
                        </label>
                      </li>
                      <li>
                        <label class="cb-container">
                          <input type="radio" name="education" value="Bac+6" checked="checked" @change="updateEduc('+6')">
                          <span class="text-small">Bac +6</span>
                          <span class="checkmark"></span>
                        </label>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!--<section class="section-box mt-50 mb-50">
      <div class="container">
        <div class="text-start">
          <h2 class="section-title mb-10 wow animate__animated animate__fadeInUp">News and Blog</h2>
          <p class="font-lg color-text-paragraph-2 wow animate__animated animate__fadeInUp">Get the latest news, updates and tips</p>
        </div>
      </div>
      <div class="container">
        <div class="mt-50">
          <div class="box-swiper style-nav-top">
            <div class="swiper-container swiper-group-3 swiper">
              <div class="swiper-wrapper pb-70 pt-5">
                <div class="swiper-slide">
                  <div class="card-grid-3 hover-up wow animate__animated animate__fadeIn">
                    <div class="text-center card-grid-3-image"><a href="#">
                        <figure><img alt="jobBox" src="../assets/imgs/page/homepage1/img-news1.png"></figure></a></div>
                    <div class="card-block-info">
                      <div class="tags mb-15"><a class='btn btn-tag' href='blog-grid.html'>News</a></div>
                      <h5><a href='blog-details.html'>21 Job Interview Tips: How To Make a Great Impression</a></h5>
                      <p class="mt-10 color-text-paragraph font-sm">Our mission is to create the world&amp;rsquo;s most sustainable healthcare company by creating high-quality healthcare products in iconic, sustainable packaging.</p>
                      <div class="card-2-bottom mt-20">
                        <div class="row">
                          <div class="col-lg-6 col-6">
                            <div class="d-flex"><img class="img-rounded" src="../assets/imgs/page/homepage1/user1.png" alt="jobBox">
                              <div class="info-right-img"><span class="font-sm font-bold color-brand-1 op-70">Sarah Harding</span><br><span class="font-xs color-text-paragraph-2">06 September</span></div>
                            </div>
                          </div>
                          <div class="col-lg-6 text-end col-6 pt-15"><span class="color-text-paragraph-2 font-xs">8 mins to read</span></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="swiper-slide">
                  <div class="card-grid-3 hover-up wow animate__animated animate__fadeIn">
                    <div class="text-center card-grid-3-image"><a href="#">
                        <figure><img alt="jobBox" src="../assets/imgs/page/homepage1/img-news2.png"></figure></a></div>
                    <div class="card-block-info">
                      <div class="tags mb-15"><a class='btn btn-tag' href='blog-grid.html'>Events</a></div>
                      <h5><a href='blog-details.html'>39 Strengths and Weaknesses To Discuss in a Job Interview</a></h5>
                      <p class="mt-10 color-text-paragraph font-sm">Our mission is to create the world&amp;rsquo;s most sustainable healthcare company by creating high-quality healthcare products in iconic, sustainable packaging.</p>
                      <div class="card-2-bottom mt-20">
                        <div class="row">
                          <div class="col-lg-6 col-6">
                            <div class="d-flex"><img class="img-rounded" src="../assets/imgs/page/homepage1/user2.png" alt="jobBox">
                              <div class="info-right-img"><span class="font-sm font-bold color-brand-1 op-70">Steven Jobs</span><br><span class="font-xs color-text-paragraph-2">06 September</span></div>
                            </div>
                          </div>
                          <div class="col-lg-6 text-end col-6 pt-15"><span class="color-text-paragraph-2 font-xs">6 mins to read</span></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="swiper-slide">
                  <div class="card-grid-3 hover-up wow animate__animated animate__fadeIn">
                    <div class="text-center card-grid-3-image"><a href="#">
                        <figure><img alt="jobBox" src="../assets/imgs/page/homepage1/img-news3.png"></figure></a></div>
                    <div class="card-block-info">
                      <div class="tags mb-15"><a class='btn btn-tag' href='blog-grid.html'>News</a></div>
                      <h5><a href='blog-details.html'>Interview Question: Why Dont You Have a Degree?</a></h5>
                      <p class="mt-10 color-text-paragraph font-sm">Learn how to respond if an interviewer asks you why you dont have a degree, and read example answers that can help you craft</p>
                      <div class="card-2-bottom mt-20">
                        <div class="row">
                          <div class="col-lg-6 col-6">
                            <div class="d-flex"><img class="img-rounded" src="../assets/imgs/page/homepage1/user3.png" alt="jobBox">
                              <div class="info-right-img"><span class="font-sm font-bold color-brand-1 op-70">Wiliam Kend</span><br><span class="font-xs color-text-paragraph-2">06 September</span></div>
                            </div>
                          </div>
                          <div class="col-lg-6 text-end col-6 pt-15"><span class="color-text-paragraph-2 font-xs">9 mins to read</span></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="swiper-button-next"></div>
            <div class="swiper-button-prev"></div>
          </div>
          <div class="text-center"><a class='btn btn-brand-1 btn-icon-load mt--30 hover-up' href='blog-grid.html'>Load More Posts</a></div>
        </div>
      </div>
    </section>-->
   <!--<section class="section-box mt-50 mb-20">
      <div class="container">
        <div class="box-newsletter">
          <div class="row">
            <div class="col-xl-3 col-12 text-center d-none d-xl-block"><img src="/template/assets/imgs/template/newsletter-left.png" alt="joxBox"></div>
            <div class="col-lg-12 col-xl-6 col-12">
              <h2 class="text-md-newsletter text-center">New Things Will Always<br> Update Regularly</h2>
              <div class="box-form-newsletter mt-40">
                <form class="form-newsletter">
                  <input class="input-newsletter" type="text" value="" placeholder="Enter your email here">
                  <button class="btn btn-default font-heading icon-send-letter">Subscribe</button>
                </form>
              </div>
            </div>
            <div class="col-xl-3 col-12 text-center d-none d-xl-block"><img src="/template/assets/imgs/template/newsletter-right.png" alt="joxBox"></div>
          </div>

        </div>
      </div>

    </section>--> 
    <button class="btn btn-default btn-find font-sm" style="position: relative; left: 230px; width: 90px; top: -150px;" @click.prevent="onFilterClick"><span style="font-weight: 900;font-size: 30;">Filtrer</span></button>

  </main>
  <footer class="footer-cnx">
        <p>@ 2024 SW Connect - Tous droits réservés</p>
      </footer>
  <!--<footer class="footer mt-50">
          <div class="container-footer">
            <div class="row">
              <div class="footer-col-1 col-md-3 col-sm-12">
                <a href="index-5.html">
                  <img
                    alt="jobBox"
                    src="template/assets/imgs/page/homepage5/SW-logo.png"
                  />
                </a>
                <div
                  class="mt-20 mb-20 color-text-paragraph-2"
                  style="
                    position: relative;
                    left: 25px;
                    font-size: 16px;
                    bottom: 125px;
                  "
                >
                  Téléphone : (216) 27 351 589
                </div>
                <div
                  class="mt-20 mb-20 color-text-paragraph-2"
                  style="
                    position: relative;
                    left: 25px;
                    font-size: 16px;
                    bottom: 125px;
                  "
                >
                  Email: SWConnect@gmail.com
                </div>
                <div
                  class="mt-20 mb-20 color-text-paragraph-2"
                  style="
                    position: relative;
                    left: 25px;
                    font-size: 16px;
                    bottom: 125px;
                  "
                >
                  Adresse : Bouhjar, MONASTIR
                </div>

                <div class="footer-social">
                  <a class="icon-socials icon-facebook" href="#"></a>
                  <a class="icon-socials icon-twitter" href="#"></a>
                  <a class="icon-socials icon-linkedin" href="#"></a>
                </div>
              </div>
              <div class="footer-col-2 col-md-2 col-xs-6">
                <h6 class="mb-20">Liens rapides</h6>
                <ul class="menu-footer">
                  <li><a href="#">Accueil</a></li>
                  <li><a href="#">Contact</a></li>
                  <li><a href="#">À propos</a></li>
                </ul>
              </div>
              <div class="footer-col-3 col-md-2 col-xs-6">
                <h6 class="mb-20">Etudiant</h6>
                <ul class="menu-footer">
                  <li><a href="#">Génération d’un portfolio</a></li>
                  <li><a href="#">Consultation des offres</a></li>
                  <li><a href="#">Filtrage des opportunités</a></li>
                  <li><a href="#">Communication avec les entreprises</a></li>
                </ul>
              </div>
              <div class="footer-col-4 col-md-2 col-xs-6">
                <h6 class="mb-20">Entreprise</h6>
                <ul class="menu-footer">
                  <li><a href="#">Publication des offres</a></li>
                  <li><a href="#">Génération de PFE Book</a></li>
                  <li><a href="#">Sélection des stagiaires</a></li>
                  <li><a href="#">Communication avec les candidats</a></li>
                </ul>
              </div>
              <div class="footer-col-5 col-md-2 col-xs-6">
                <h6 class="mb-20">Support</h6>
                <ul class="menu-footer">
                  <li><a href="#">FAQ</a></li>
                  <li><a href="#">Conditions générales</a></li>
                  <li><a href="#">Politique de confidentialité</a></li>
                </ul>
              </div>
              <div class="footer-col-6 col-md-3 col-sm-12 image-container1">
                <img src="template/assets/imgs/page/homepage5/footer-img.png" />
              </div>
            </div>
          </div>
          <div class="footer-bottom mt-50">
            <div class="row">
              <div class="col-md-6">
                <span
                  class="font-xs color-text-paragraph"
                  style="position: relative; bottom: 10px; left: 15px"
                >
                  @ 2024 SW Connect - Tous droits réservés &copy;</span
                >
              </div>
              <div class="col-md-6 text-md-end text-start">
                  <div class="footer-social"><a class="font-xs color-text-paragraph" href="#">Privacy Policy</a><a class="font-xs color-text-paragraph mr-30 ml-30" href="#">Terms &amp; Conditions</a><a class="font-xs color-text-paragraph" href="#">Security</a></div>
                </div>
            </div>
          </div>
        </footer>-->

</body>


  </router>
</template>
<script>
import axios from "axios";
import navbarEntreprise from "@/components/navbarEntreprise.vue";
export default {
components:{navbarEntreprise},
name: "EtuGrid",
data() {
  return {
    etudiants:[],
    entrepriseUrl: null,
    etudiantUrl: null,
    baseUrl: "http://127.0.0.1:8000/",
    entreprise: {},
        //dropdownmenu
    showDropdown: false,
    filteredEtuds: [],
    searchClicked: false,
    FilterClick:false,
    filteredEtuds2:[],
    selectedEduc: 'non',
    apparitionprofil:0,




}},
mounted() {
  // Call a method to fetch all offers from the backend API
  this.fetchAllEtudiants();
  
},
created() {
  const userId = localStorage.getItem("user_id");
if (!userId) {
  // User ID not found in local storage, redirect to error interface
  alert("you have to log in");
  this.$router.push("/ConnexionView");
  return;
}

this.entreprise.id = userId;
console.log(this.entreprise.id);
// Fetch entreprise data using the entreprise ID
this.fetchEntrepriseData();
},
methods:{
fetchAllEtudiants() {
    // Make an API request to fetch all offers from the backend
    // Assuming you have a method named getAllOffers in your API service
    // Replace 'apiService' with your actual API service
    axios.get('http://127.0.0.1:8000/api/etudiant/')
      .then(response => {
        // Assign the fetched offers to the offers array
        this.etudiants = response.data;
        console.log(this.etudiant);
      
      })
      .catch(error => {
        console.error('Error fetching etudiants:', error);
      });
    },
async fetchEntrepriseData() {
    try {

      const response = await axios.get(`http://127.0.0.1:8000/api/entreprises/get/${this.entreprise.id}/`);
      // Populate the etudiant object with data from the response
      this.entreprise = response.data;
      console.log(this.entreprise.profile_logo)
      if (this.entreprise.profile_logo) {
        this.entrepriseUrl = this.baseUrl + this.entreprise.profile_logo;
      }
    } catch (error) {
      console.error('Error fetching entreprise data:', error);
    }
  },
  toggleDropdown() {  
    this.showDropdown = !this.showDropdown;
  },
  redirectToEtudiantDetails(etudiantId) {
     this.EnregistreApparitionProfil(etudiantId);

      // Navigate to the offer details view using the offer ID
      this.$router.push({ name: 'EtudiantDetails', params: { id: etudiantId } });
      console.log(etudiantId,'grids');


  },
  logout() {
        localStorage.removeItem('user_id');
        this.$router.push('/ConnexionView');
        console.log('Logout successful');
  },
  onSearchClick() {
  const keyword = document.getElementById('input-keysearch').value;
  this.rechercherEtud(keyword);
  this.searchClicked = true;
},
rechercherEtud(keyword) {
  if (keyword.trim() !== '') {
    // Requête GET à l'API pour récupérer les offres
    axios.get('http://localhost:8000/api/Etudbymc/', {
      params: {
        q: keyword
      }
    })
    .then(response => {
      const etudiants = response.data;
      // Mettre à jour la liste filteredOffers avec les résultats
      this.updateFilteredEtuds(etudiants);
    })
    .catch(error => {
      console.error('Une erreur s\'est produite lors de la récupération des offres!', error);
    });
  }
},
updateFilteredEtuds(etudiants) {
  this.filteredEtuds = etudiants;
},
onFilterClick() {
  const domain = document.querySelector('input[name="domain"]:checked').value;
  const education = document.querySelector('input[name="education"]:checked').value;
  //const role = document.querySelector('input[name="role"]:checked').value;
  //const skills = document.querySelector('input[name="skills"]:checked').value;
  //const location = document.querySelector('input[name="location"]:checked').value;

  this.FilterClick =true;

  this.filterEtuds(domain,education);
},
filterEtuds(domain,education) {
  const url = `http://localhost:8000/api/etuds/filter/${domain}/${education}/`;
  axios.get(url)
    .then(response => {
      const filteredEtuds2 = response.data;
      console.log('etudiants filtrées reçues :', filteredEtuds2);
      this.updateFilteredEtuds2(filteredEtuds2);
    })
    .catch(error => {
      console.error('Une erreur s\'est produite lors du filtrage des offres!', error);
    });
},
 // Méthode pour mettre à jour la liste filteredOffers avec les offres filtrées
 updateFilteredEtuds2(etudiants) {
  this.filteredEtuds2 = etudiants;
},
toggleDomain(domain) {
console.log('Domaine sélectionné :', domain);
this.selectedDomain = domain;
},
updateEduc(binome) {
console.log('Domaine sélectionné :', binome);
this.selectedEduc = binome;
},
async EnregistreApparitionProfil(etudiantId) {
    try {
      const response = await axios.post(`http://127.0.0.1:8000/apparition_profil/${etudiantId}/`, {});
      console.log('Apparition enregistrée:', response.data);
    } catch (error) {
      console.error('Erreur lors de l\'enregistrement de l\'apparition:', error.response ? error.response.data : error.message);
    }
  }
  }
  }
</script>
<style scoped>
.header{
height:85px;
}
.cus-mr{
  margin:5px;
}
.btn-apply-now {
  background-color: #E0E6F7;
  color: #447AB8;
  padding: 12px 10px;
  min-width: 95px;
  border-radius: 4px;
  font-size: 12px;
  text-transform: capitalize;
}
.card-grid-2 .card-block-info .card-text-price {
  color: #447AB8;
}
.card-grid-2:hover .btn-apply-now {
  color: #ffffff;
  background-color: #447AB8;
}
.color-text-paragraph{
  color: #05264E;
}
.btn.btn-default {
color: #447AB8;
background-color: #ffffff;
line-height: 26px;
padding: 10px 25px;
}
.btn.btn-default:hover {
background-color: #ffffff;
transform: translateY(-2px);
transition: 0.2s;
}
.postbutt{
border : 1px solid #447AB8;
margin-left: 10px;
width:162px;
}
.icon-fb{
  height: 50px;
  width: 50px;
}
.nav-li-cus{
  font-size: 16px;
}
.header-left-cus{
  margin-right: 275px;
}
.header-right-cus{
  min-width: 335px;
}
.header-logo-cus{
  height:50px;
}
.cus-mr{
  margin:5px;
}
.header-cus{
  margin-bottom: 92px;
  height:100px;

  background-color: #fff;
  border-bottom: 1px solid #E0E6F7;
}
.grid-row-offer{
  padding-right: 32px;
}
.logo-site{
  height: 49px; 
  width: 199px;
}
.cus-row{
  margin-right:0px;
}
.header .main-menu li a:hover, .header .main-menu li a.active{
  color:#fff;
}
.dropdown-menu a:hover span {
color: #447ab8 !important;

}

.dropdown-menu a:hover img {
filter: brightness(0) saturate(100%) invert(45%) sepia(30%) saturate(995%)
  hue-rotate(172deg) brightness(93%) contrast(87%);
}
.dropdown-menu a:hover {
background-color: #e7f0fa !important;
color: #447ab8 !important;
border-left: 4px solid #447ab8;
}
.dropdown-item {
font-family: "Plus Jakarta Sans", sans-serif;
font-style: normal;
font-weight: bold;
font-size: 16px;
line-height: 24px;
color: #858585;
margin-bottom: 4px;
display: flex;
align-items: center;
height: 40px;

}
.dropdown-item img {
margin-right: 20px;
width: 25px;
}
.dropdown-menu {
display: block;
left: auto !important;
right: 0;
min-width: 13rem;
}

.color-text-paragraph-2 {
color:#05264E;
}
.color-brand-1{
color:#05264E;
}
.card-grid-2 .card-grid-2-image-rd{
width: 30%;
  min-width: 70px !important;
  max-width: 70px !important;
}
.footer-cnx {
  position: relative;
  background-color: transparent;
  height: 20px;
  width: 150%;
  overflow-x: hidden;
}
</style>