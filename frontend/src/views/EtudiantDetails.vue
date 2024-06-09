<template>
  <router-view></router-view>
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, maximum-scale=1"
    />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <meta name="msapplication-TileColor" content="#0E0E0E" />
    <meta name="template-color" content="#0E0E0E" />
    <meta name="msapplication-config" content="browserconfig.html" />
    <meta name="description" content="Index page" />
    <meta name="keywords" content="index, page" />
    <meta name="author" content="" />
    <title>Etudiant</title>
    <link
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
      rel="stylesheet"
    />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
    />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css"
      rel="stylesheet"
    />
    <link
      href="https://cdn.tiny.cloud/1/YOUR_API_KEY/tinymce/5/tinymce.min.js"
      referrerpolicy="origin"
    />
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="/template/assets/imgs/template/favicon.svg"
    />

    <link
      href="/template/assets/css/plugins/animate.min.css"
      rel="stylesheet"
    />
    <link
      href="/template/assets/css/plugins/magnific-popup.css"
      rel="stylesheet"
    />
    <link
      href="/template/assets/css/plugins/perfect-scrollbar.css"
      rel="stylesheet"
    />
    <link
      href="/template/assets/css/plugins/select2.min.css"
      rel="stylesheet"
    />
    <link
      href="/template/assets/css/plugins/swiper-bundle.min.css"
      rel="stylesheet"
    />

    <link href="/template/assets/css/stylecd4ee.css" rel="stylesheet" />

    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
    />
  </head>
  <body>
    <navbarEntreprise v-if="userType === 'entreprise' " />
 <navbarEtudiant v-if="userType==='etudiant'" />
 <navbarAdmin v-if="userType==='admin'" />
    <main class="main">
      <div class="banner-hero banner-image-single" style="margin-left:5px; "><img :src="this.etudiant.profile_cover" alt="jobbox" style="height:348px;"></div>
      <div class="box-company-profile" style="width:100px">
            <div class="image-compay" style="width:100px; margin-left:-596px;"><img :src="this.etudiant.profile_photo" alt="jobbox">
            </div>

                    
      </div>
      <section class="section-box-2">
        <div class="container" style="margin-bottom:0px;">
          <div class="row mt-10">
            <div class="col-lg-8 col-md-12">
              <div class="inline-content">
                <h3 style="display: inline">
                  {{ etudiant.first_name }} {{ etudiant.last_name }}
                </h3>
              </div>
              <p class="company-name" href="#">{{etudiant.role}}</p>
            </div>
            <div  v-if="userType === 'entreprise'"  class="col-lg-4 col-md-12 text-lg-end">
              <div class="btn-group" role="group" aria-label="Button group">
                <div class="icon-container-2 hover-up" style="cursor: pointer">
                  <i v-if="!isEtudiantInFavorites" class="bi bi-bookmark custom-icon-3"   @click="addFavoriteEtudiant(etudiant.id)"></i>
                  <i v-if="isEtudiantInFavorites"  class="bi bi-bookmark-fill custom-icon-3" @click="deleteFavoriteEtudiant(favoriteEtudiantId)"></i>
                </div>
                <router-link :to="'/chatView/'+ etudiant.username"
                  class="btn btn-apply btn-apply-big hover-up"
             
                  style="border-radius: 8px"
                >
                  Contacter <i class="bi bi-chat-text custom-icon-4"></i>
              </router-link>
              </div>
            </div>
          </div>
          <div class="border-bottom pt-10 pb-10"></div>
        </div>
      </section>
      <section class="section-box mt-50">
        <div class="container">
          <div class="row">
            <div class="col-lg-8 col-md-12 col-sm-12 col-12">
              <div class="content-single">
                <h5>Biographie</h5>
                <p>{{ etudiant.bio }}</p>
                <h5 v-if="etudiant.lettre_motivation">Lettre de motivation</h5>
                <p v-if="etudiant.lettre_motivation">{{ etudiant.lettre_motivation }}</p>
              </div>
              <div class="author-single">
                <span>{{ etudiant.first_name }} {{ etudiant.last_name }}</span>
              </div>
              <div class="single-apply-jobs">
                <div class="row align-items-center">
                  <div  class="col-md-5" style="width: 380px">
                    <a  v-if="userType === 'entreprise'"  class="btn btn-default mr-15" :href="'/chatView/'+ etudiant.username">Contacter</a
                    ><a  v-if="userType === 'entreprise'  && !isEtudiantInFavorites"  class="btn btn-border" href="#">Ajouter aux favoris</a>
                  </div>
                  <div
                    class="text-lg-end social-share"
                    style="width: 500px; margin-right: 0px;"
                  >
                    <h6
                      class="color-text-paragraph-2 d-inline-block d-baseline mr-10"
                    >
                      Suivre sur
                    </h6>
                    <a v-if="etudiant.fb_lien"  class="mr-5 d-inline-block d-middle" :href="etudiant.fb_lien" target="_blank"
                      ><img v-if="etudiant.fb_lien"
                        alt="jobBox"
                        src="/template/assets/imgs/template/icons/facebook-colored.svg" /></a
                    >
                    <a v-if="etudiant.link_lien"
                      class="mr-5 d-inline-block d-middle"
                      :href="etudiant.link_lien"
                      target="_blank"
                      ><img v-if="etudiant.link_lien"
                        alt="jobBox"
                        src="/template/assets/imgs/template/icons/linkedin-colored.svg" /></a
                    >
                    <a v-if="etudiant.in_lien" class="mr-5 d-inline-block d-middle"  :href="etudiant.in_lien"
                      target="_blank"
                      ><img  v-if="etudiant.in_lien"
                        alt="jobBox"
                        src="/template/assets/imgs/template/icons/instagram-colored.svg" /></a
                    ><a  v-if="etudiant.git_lien" class="d-inline-block d-middle"  :href="etudiant.git_lien"
                      target="_blank"
                      ><img v-if="etudiant.git_lien"
                        alt="jobBox"
                        src="/template/assets/imgs/template/icons/github-colored.svg"
                    /></a>
                  </div>
                </div>
              </div>
            </div>
            <div
              class="col-lg-4 col-md-12 col-sm-12 col-12 pl-40 pl-lg-15 mt-lg-30"
            >
              <div class="sidebar-border">
                <div class="sidebar-heading">
                  <h5 class=" ">Coordonnées</h5>
                  <div class="avatar-sidebar">
                    <div class="sidebar-info"></div>
                  </div>
                </div>
                <div class="sidebar-list-job">
                  <ul>
                    <li>
                      <i class="bi bi-geo-alt custom-iconss"></i
                      >{{ etudiant.location }}
                    </li>
                    <li>
                      <i class="bi bi-telephone custom-iconss"></i
                      >{{ etudiant.telephone }}
                    </li>
                    <li>
                      <i class="bi bi-envelope custom-iconss"></i
                      >{{ etudiant.email }}
                    </li>
                  </ul>
                </div>
              </div>
              <div class="job-overview">
                <h5 class="border-bottom pb-15 mb-30">Informations</h5>
                <div class="row">
                  <div class="col-md-6">
                    <div class="sidebar-icon-item">
                      <img
                        src="../assets/imgs/page/job-single/industry.svg"
                        alt="jobBox"
                      />
                    </div>
                    <div class="sidebar-text-info ml-10">
                      <span class="text-description industry-icon mb-10"
                        >Domaine</span
                      >
                      <strong class="small-heading">{{
                        etudiant.domain
                      }}</strong>
                    </div>
                  </div>
                  <div class="col-md-6 mt-sm-15">
                    <div class="sidebar-icon-item">
                      <img
                        src="../assets/imgs/page/job-single/job-level.svg"
                        alt="jobBox"
                      />
                    </div>
                    <div class="sidebar-text-info ml-10">
                      <span class="text-description joblevel-icon mb-10"
                        >Role</span
                      >
                      <strong class="small-heading">{{ etudiant.role }}</strong>
                    </div>
                  </div>
                </div>
                <div class="row mt-25">
                  <div class="col-md-6">
                    <div class="sidebar-icon-item">
                      <img
                        src="../assets/imgs/page/job-single/experience.svg"
                        alt="jobBox"
                      />
                    </div>
                    <div class="sidebar-text-info ml-10">
                      <span class="text-description experience-icon mb-10"
                        >Education</span
                      ><strong class="small-heading">{{
                        etudiant.education
                      }}</strong>
                    </div>
                  </div>
                  <div class="col-md-6 mt-sm-15">
                    <div class="sidebar-icon-item">
                      <img
                        src="/template/assets/imgs/page/job-single/gender.svg"
                        alt="jobBox"
                      />
                    </div>
                    <div class="sidebar-text-info ml-10">
                      <span class="text-description salary-icon mb-10"
                        >Sexe</span
                      ><strong class="small-heading">{{
                        etudiant.sexe
                      }}</strong>
                    </div>
                  </div>
                </div>
                <div class="row mt-25">
                  <div class="col-md-6 mt-sm-15">
                    <div class="sidebar-icon-item">
                      <img
                        src="/template/assets/imgs/page/job-single/calendar-heart.svg"
                        alt="jobBox"
                      />
                    </div>
                    <div class="sidebar-text-info ml-10">
                      <span class="text-description jobtype-icon mb-10"
                        >Date de naissance</span
                      ><strong class="small-heading">{{
                        etudiant.date_naissance
                      }}</strong>
                    </div>
                  </div>
                </div>
              </div>
              <div class="sidebar-border">
                <h5 class="border-bottom pb-15 mb-30">Compétences</h5>
                <div class="comp-bar">
                  <div
                    v-for="(skill, index) in etudiant.skills"
                    :key="index"
                    class="container-competences"
                  >
                    {{ skill }}
                  </div>
                </div>
              </div>
              <div v-if="etudiant.cv" class="sidebar-border">
                <div class="sidebar-heading">
                  <div class="row">
                    <div class="col-md-6">
                      <div class="avatar-sidebar">
                        <figure>
                          <img
                            alt="jobBox"
                            src="\template\assets\imgs\page\job-single\file-earmark-person.svg"
                          />
                        </figure>
                        <div class="sidebar-info">
                          <span class="sidebar-company">CV</span
                          ><span>PDF</span>
                        </div>
                      </div>
                    </div>
                    <div class="col-md-6 mt-sm-15">
                      <div class="sidebar-text-info ml-10">
                        <span
                          class="btn btn-border comp-bar mb-10 mt-60 container-competences custom-file"
                          style="
                            padding-bottom: 26px;
                            border: none;
                            font-size: 14px;
                            font-weight: normal;
                          "
                          @click="openCV"
                        >
                          Voir CV</span
                        >
               
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div v-if="etudiant.certificats" class="sidebar-border">
                <div class="sidebar-heading">
                  <div class="row">
                    <div class="col-md-6">
                      <div class="avatar-sidebar">
                        <figure>
                          <img
                            alt="jobBox"
                            src="\template\assets\imgs\page\job-single\journal-bookmark.svg"
                          />
                        </figure>
                        <div class="sidebar-info">
                          <span class="sidebar-company">Certificats</span
                          ><span>PDF</span>
                        </div>
                      </div>
                    </div>
                    <div class="col-md-6 mt-sm-15">
                      <div class="sidebar-text-info ml-10">
                        <a>
                          <span
                            class="btn btn-border comp-bar mt-60 container-competences custom-file"
                            style="
                              padding-bottom: 26px;
                              border: none;
                              font-size: 14px;
                              font-weight: normal;
                            "
                          >
                            Voir Certificats</span
                          ></a
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="sidebar-border">
                <div class="sidebar-heading">
                  <div class="row">
                    <div class="col-md-6">
                      <div class="avatar-sidebar">
                        <figure>
                          <img
                            alt="jobBox"
                            src="\template\assets\imgs\page\job-single\filetype-ai.svg"
                          />
                        </figure>
                        <div class="sidebar-info">
                          <span class="sidebar-company">Portfolio</span
                          ><span>AI</span>
                        </div>
                      </div>
                    </div>
                    <div class="col-md-6 mt-sm-15">
                      <div class="sidebar-text-info ml-10">
                        <span
                          class="btn btn-border comp-bar mt-60 container-competences custom-file"
                          style="
                            padding-bottom: 26px;
                            border: none;
                            font-size: 14px;
                            font-weight: normal;
                          "
                            @click="voirportfolio"

                        >
                          Voir Portfolio</span
                        >
                      </div>
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
          <div class="text-left">
            <h2
              class="section-title mb-10 wow animate__animated animate__fadeInUp"
            >
              Offres Disponibles
            </h2>
            <p
              class="font-lg color-text-paragraph-2 wow animate__animated animate__fadeInUp"
            >
              Get the latest news, updates and tips
            </p>
          </div>
          <div class="mt-50">
            <div class="box-swiper style-nav-top">
              <div class="swiper-container swiper-group-4 swiper">
                <div class="swiper-wrapper pb-10 pt-5">
                  <div class="swiper-slide">
                    <div class="card-grid-2 hover-up">
                      <div class="card-grid-2-image-left">
                        <span class="flash"></span>
                        <div class="image-box">
                          <img
                            src="../assets/imgs/brands/brand-6.png"
                            alt="jobBox"
                          />
                        </div>
                        <div class="right-info">
                          <a class="name-job" href="company-details.html"
                            >Quora JSC</a
                          ><span class="location-small">New York, US</span>
                        </div>
                      </div>
                      <div class="card-block-info">
                        <h6>
                          <a href="job-details.html">Senior System Engineer</a>
                        </h6>
                        <div class="mt-5">
                          <span class="card-briefcase">Part time</span
                          ><span class="card-time"
                            >5<span> minutes ago</span></span
                          >
                        </div>
                        <p class="font-sm color-text-paragraph mt-15">
                          Lorem ipsum dolor sit amet, consectetur adipisicing
                          elit. Recusandae architecto eveniet, dolor quo
                          repellendus pariatur.
                        </p>
                        <div class="mt-30">
                          <a
                            class="btn btn-grey-small mr-5"
                            href="job-details.html"
                            >PHP</a
                          ><a
                            class="btn btn-grey-small mr-5"
                            href="job-details.html"
                            >Android
                          </a>
                        </div>
                        <div class="card-2-bottom mt-30">
                          <div class="row">
                            <div class="col-lg-7 col-7">
                              <span class="card-text-price">$800</span
                              ><span class="text-muted">/Hour</span>
                            </div>
                            <div class="col-lg-5 col-5 text-end">
                              <div
                                class="btn btn-apply-now"
                                data-bs-toggle="modal"
                                data-bs-target="#ModalApplyJobForm"
                              >
                                Apply now
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="swiper-slide">
                    <div class="card-grid-2 hover-up">
                      <div class="card-grid-2-image-left">
                        <span class="flash"></span>
                        <div class="image-box">
                          <img
                            src="../assets/imgs/brands/brand-4.png"
                            alt="jobBox"
                          />
                        </div>
                        <div class="right-info">
                          <a class="name-job" href="company-details.html"
                            >Dailymotion</a
                          ><span class="location-small">New York, US</span>
                        </div>
                      </div>
                      <div class="card-block-info">
                        <h6>
                          <a href="job-details.html">Frontend Developer</a>
                        </h6>
                        <div class="mt-5">
                          <span class="card-briefcase">Full time</span
                          ><span class="card-time"
                            >6<span> minutes ago</span></span
                          >
                        </div>
                        <p class="font-sm color-text-paragraph mt-15">
                          Lorem ipsum dolor sit amet, consectetur adipisicing
                          elit. Recusandae architecto eveniet, dolor quo
                          repellendus pariatur.
                        </p>
                        <div class="mt-30">
                          <a
                            class="btn btn-grey-small mr-5"
                            href="jobs-grid.html"
                            >Typescript</a
                          ><a
                            class="btn btn-grey-small mr-5"
                            href="jobs-grid.html"
                            >Java</a
                          >
                        </div>
                        <div class="card-2-bottom mt-30">
                          <div class="row">
                            <div class="col-lg-7 col-7">
                              <span class="card-text-price">$250</span
                              ><span class="text-muted">/Hour</span>
                            </div>
                            <div class="col-lg-5 col-5 text-end">
                              <div
                                class="btn btn-apply-now"
                                data-bs-toggle="modal"
                                data-bs-target="#ModalApplyJobForm"
                              >
                                Apply now
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="swiper-slide">
                    <div class="card-grid-2 hover-up">
                      <div class="card-grid-2-image-left">
                        <span class="flash"></span>
                        <div class="image-box">
                          <img
                            src="../assets/imgs/brands/brand-8.png"
                            alt="jobBox"
                          />
                        </div>
                        <div class="right-info">
                          <a class="name-job" href="company-details.html"
                            >Periscope</a
                          ><span class="location-small">New York, US</span>
                        </div>
                      </div>
                      <div class="card-block-info">
                        <h6>
                          <a href="job-details.html">Lead Quality Control QA</a>
                        </h6>
                        <div class="mt-5">
                          <span class="card-briefcase">Full time</span
                          ><span class="card-time"
                            >6<span> minutes ago</span></span
                          >
                        </div>
                        <p class="font-sm color-text-paragraph mt-15">
                          Lorem ipsum dolor sit amet, consectetur adipisicing
                          elit. Recusandae architecto eveniet, dolor quo
                          repellendus pariatur.
                        </p>
                        <div class="mt-30">
                          <a
                            class="btn btn-grey-small mr-5"
                            href="job-details.html"
                            >iOS</a
                          ><a
                            class="btn btn-grey-small mr-5"
                            href="job-details.html"
                            >Laravel</a
                          ><a
                            class="btn btn-grey-small mr-5"
                            href="job-details.html"
                            >Golang</a
                          >
                        </div>
                        <div class="card-2-bottom mt-30">
                          <div class="row">
                            <div class="col-lg-7 col-7">
                              <span class="card-text-price">$250</span
                              ><span class="text-muted">/Hour</span>
                            </div>
                            <div class="col-lg-5 col-5 text-end">
                              <div
                                class="btn btn-apply-now"
                                data-bs-toggle="modal"
                                data-bs-target="#ModalApplyJobForm"
                              >
                                Apply now
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="swiper-slide">
                    <div class="card-grid-2 hover-up">
                      <div class="card-grid-2-image-left">
                        <span class="flash"></span>
                        <div class="image-box">
                          <img
                            src="../assets/imgs/brands/brand-4.png"
                            alt="jobBox"
                          />
                        </div>
                        <div class="right-info">
                          <a class="name-job" href="company-details.html"
                            >Dailymotion</a
                          ><span class="location-small">New York, US</span>
                        </div>
                      </div>
                      <div class="card-block-info">
                        <h6>
                          <a href="job-details.html">Frontend Developer</a>
                        </h6>
                        <div class="mt-5">
                          <span class="card-briefcase">Full time</span
                          ><span class="card-time"
                            >6<span> minutes ago</span></span
                          >
                        </div>
                        <p class="font-sm color-text-paragraph mt-15">
                          Lorem ipsum dolor sit amet, consectetur adipisicing
                          elit. Recusandae architecto eveniet, dolor quo
                          repellendus pariatur.
                        </p>
                        <div class="mt-30">
                          <a
                            class="btn btn-grey-small mr-5"
                            href="jobs-grid.html"
                            >Typescript</a
                          ><a
                            class="btn btn-grey-small mr-5"
                            href="jobs-grid.html"
                            >Java</a
                          >
                        </div>
                        <div class="card-2-bottom mt-30">
                          <div class="row">
                            <div class="col-lg-7 col-7">
                              <span class="card-text-price">$250</span
                              ><span class="text-muted">/Hour</span>
                            </div>
                            <div class="col-lg-5 col-5 text-end">
                              <div
                                class="btn btn-apply-now"
                                data-bs-toggle="modal"
                                data-bs-target="#ModalApplyJobForm"
                              >
                                Apply now
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="swiper-button-next swiper-button-next-4"></div>
              <div class="swiper-button-prev swiper-button-prev-4"></div>
            </div>
            <div class="text-center">
              <a class="btn btn-grey" href="#">Load more posts</a>
            </div>
          </div>
        </div>
      </section>-->
    </main>
    <footer class="footer mt-50">
      <div class="container">
        <div class="row">
          <div class="footer-col-1 col-md-3 col-sm-12">
            <a href="index.html"
              ><img
                class="img-footer"
                alt="jobBox"
                src="../assets/imgs/logo/logo-blanc.png"
            /></a>
            <ul class="menu-footer">
              <li><a href="#">Téléphone : +216 27 351 589</a></li>
              <li><a href="#">Email : SWConnect@gmail.com</a></li>
              <li><a href="#">Addresse : Bouhjar, Monastir</a></li>
            </ul>
            <div class="footer-social">
              <a class="icon-socials icon-facebook" href="#"></a
              ><a class="icon-socials icon-twitter" href="#"></a
              ><a class="icon-socials icon-linkedin" href="#"></a>
            </div>
          </div>
          <div class="footer-col-2 col-md-2 col-xs-6">
            <h6 class="mb-20 footer-h6">Etudiant</h6>
            <ul class="menu-footer">
              <li><a href="#">Génération de portfolio</a></li>
              <li><a href="#">Consultation des offres</a></li>
              <li><a href="#">Filtrage des offres</a></li>
              <li><a href="#">Contacter entreprise</a></li>
            </ul>
          </div>
          <div class="footer-col-3 col-md-2 col-xs-6">
            <h6 class="mb-20 footer-h6">Entreprise</h6>
            <ul class="menu-footer">
              <li><a href="#">Génération de PFE book</a></li>
              <li><a href="#">Pulication des offres</a></li>
              <li><a href="#">Filtrage des stagiaires</a></li>
              <li><a href="#">Contacter Etudiant</a></li>
            </ul>
          </div>
          <div class="footer-col-4 col-md-2 col-xs-6">
            <h6 class="mb-20 footer-h6">Liens Rapides</h6>
            <ul class="menu-footer">
              <li><a href="#">Accueil</a></li>
              <li><a href="#">A propos</a></li>
              <li><a href="#">Equipe</a></li>
              <li><a href="#">Contact</a></li>
            </ul>
          </div>
          <div class="footer-col-5 col-md-2 col-xs-6">
            <h6 class="mb-20 footer-h6">Support</h6>
            <ul class="menu-footer">
              <li><a href="#">FAQ</a></li>
              <li><a href="#">Aide</a></li>
              <li><a href="#">Conditions générales</a></li>
              <li><a href="#">Politique de confidentialité</a></li>
            </ul>
          </div>
        </div>
        <div class="footer-bottom mt-50">
          <div class="row">
            <div class="col-md-6">
              <span class="font-xs color-text-paragraph-2-2"
                >Copyright &copy; 2022. JobBox all right reserved</span
              >
            </div>
            <div class="col-md-6 text-md-end text-start">
              <div class="footer-social">
                <a class="font-xs color-text-paragraph-2-2" href="#"
                  >Privacy Policy</a
                ><a
                  class="font-xs color-text-paragraph-2-2 mr-30 ml-30"
                  href="#"
                  >Terms &amp; Conditions</a
                ><a class="font-xs color-text-paragraph-2-2" href="#"
                  >Security</a
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </footer>
  </body>
</template>
<script>
import axios from "axios";
import navbarEtudiant from '@/components/navbarEtudiant.vue';
import navbarEntreprise from '@/components/navbarEntreprise.vue';
import navbarAdmin from "@/components/navbarAdmin.vue";
export default {
  name: "EtudiantDetails",
  components:{navbarEtudiant,navbarEntreprise,navbarAdmin},
  data() {
    return {
      showDropdown: false,
      etudiant: {},
      entrepriseUrl: null,
      etudiantUrl: null,
      baseUrl: "http://127.0.0.1:8000/",
      entreprise: {},
      userType:'',
      favoriteEtudiants:[],
      favoriteEtudiantId:null,
    };
  },
  mounted() {
    // Fetch offer details data from your API
    // Assuming you have a method to fetch offer details by ID
    const etudiantId = this.$route.params.id; // Assuming you pass the offer ID through route params
    this.fetchEudiantDetails(etudiantId);
    this.fetchFavoriteEtudiants();
    console.log(etudiantId, "details");
  },
  created() {
    const userId = localStorage.getItem("user_id");
    
    if (!userId) {
      // User ID not found in local storage, redirect to error interface
      alert("you have to log in");
      this.$router.push("/ConnexionView");
      return;
    }
     const userType = localStorage.getItem('user_type');
      this.userType = userType;

 

  },
  methods: {
    addFavoriteEtudiant(etudiantId) {
  const userId = localStorage.getItem("user_id");
  axios
    .post(`http://127.0.0.1:8000/api/entreprise/${userId}/addFavoriss/${etudiantId}/`)
    .then((response) => {
      // Handle successful response if needed
      console.log("Etudiant added to favorites:", response.data);
      this.fetchFavoriteEtudiants();
      this.ajouterAction();

      // You can update the UI to reflect that the offer is now favorited
    })
    .catch((error) => {
      console.error("Error adding etudiant to favorites:", error);
      // Handle error response if needed
    });
},

    openCV() {
      // Check if etudiant has a CV
      if (this.etudiant && this.etudiant.cv) {
        // Open a new window or tab to display the CV content
        window.open(this.etudiant.cv, '_blank');
      } 
    },
    downloadCV() {
  // Check if etudiant has a CV
  if (this.etudiant && this.etudiant.cv) {
    // Create a temporary link element
    const link = document.createElement('a');
    link.href = this.etudiant.cv;
    link.setAttribute('download', 'CV.pdf'); // Set the filename for download

    // Append the link to the body and trigger the download
    document.body.appendChild(link);
    link.click();

    // Clean up
    document.body.removeChild(link);
  }
},

    toggleDropdown() {
      this.showDropdown = !this.showDropdown;
    },
    logout() {
      localStorage.removeItem("user_id");
      this.$router.push("/ConnexionView");
      console.log("Logout successful");
    },
    fetchEudiantDetails(etudiantId) {
      // Make an API request to fetch offer details by ID
      axios
        .get(`http://127.0.0.1:8000/api/etudiant/${etudiantId}/`)
        .then((response) => {
          // Assign the fetched offer data to the 'offer' property
          this.etudiant = response.data;
          if (this.etudiant.profile_photo) {
          this.etudiantUrl = this.baseUrl + this.etudiant.profile_photo;
          console.log(this.etudiantUrl);
        }
        })
        .catch((error) => {
          console.error("Error fetching etudiant details:", error);
        });
    },

async deleteFavoriteEtudiant(favoriteEtudiantId) {
  if (!favoriteEtudiantId) {
    console.error("Favorite etudiant ID is null or undefined", favoriteEtudiantId);
    return;
  }
  try{
      await axios
        .delete(`http://127.0.0.1:8000/api/entreprise/deleteFavoriss/${favoriteEtudiantId}/`)
        .then(() => {
          // Handle successful response if needed
          console.log("Etudiant removed from favorites");
          // You can update the UI to reflect that the offer is now removed from favorites
          this.fetchFavoriteEtudiants(); // Fetch the student's favorite offers again after removing a favorite
        })
      }catch(error) {
          console.error("Error removing etudiant from favorites:", error);
          // Handle error response if needed
        }
    },
fetchFavoriteEtudiants() {
  const userId = localStorage.getItem("user_id");
      axios
        .get(`http://127.0.0.1:8000/api/entreprise/${userId}/getFavoriss/`)
        .then((response) => {
          // Store the fetched favorite offers in the data property
          this.favoriteEtudiants = response.data;
          this.updateFavoriteEtudiantId();
          console.log("Fetched favorite etudiants", this.favoriteEtudiants);
        })
        .catch((error) => {
          console.error("Error fetching favorite Etudiants:", error);
          // Handle error response if needed
        });
    },
    updateFavoriteEtudiantId() {
      const favorite = this.favoriteEtudiants.find((favoriteEtudiant) => favoriteEtudiant.etudiant=== this.etudiant.id);
      this.favoriteEtudiantId = favorite ? favorite.id : null;
    },
    ajouterAction() {
      const userId = localStorage.getItem("user_id");
  if (!userId) {
    alert("Vous devez être connecté.");
    return;
  }
  axios.post(`http://127.0.0.1:8000/creer-action/${userId}/`, {
    action_message: 'Ajout étudiant à la liste des favoris',
      })
  .then(() => {
    // Traiter la réponse si nécessaire
    console.log('Action ajoutée avec succès !');
  })
  .catch(error => {
    console.error('Erreur lors de l\'ajout de l\'action :', error);
    alert('Une erreur est survenue lors de l\'ajout de l\'action.');
  });
},
voirportfolio() {
  const userId = localStorage.getItem("user_id");
  if (!userId) {
    alert("Vous devez être connecté.");
    return;
  }
  axios.get(`http://127.0.0.1:8000/get-all-templates/${userId}/`)
    .then(response => {
      const templates = response.data;
      
      // Vérifier s'il y a des templates
      if (templates.length === 0) {
        console.log("Aucun template n'a été trouvé.");
        return;
      }
      
      // Sélectionner la dernière template
      const latestTemplate = templates[templates.length - 1];
      
      // Rediriger vers le template correspondant
      if (latestTemplate.nomtemplate === "template1") {
        this.$router.push({ name: 'PortfolioTemplate1', params: { id: this.etudiant.id } });
      } else if (latestTemplate.nomtemplate === "template2") {
        this.$router.push({ name: 'PortfolioTemplate2', params: { id: this.etudiant.id } });
      } else if (latestTemplate.nomtemplate === "template3") {
        this.$router.push({ name: 'PortfolioTemplate3', params: { id: this.etudiant.id } });
      }
      else {
        console.log("Aucun template valide n'a été trouvé.");
      }
    })
    .catch(error => {
      console.error('Erreur lors de la récupération des templates : ', error);
    });
},
  },
  computed: {
    isEtudiantInFavorites() {
      console.log("this etudiantId",this.etudiant.id);
    
      // Check if the current offer is in the student's favorite offers
      return this.favoriteEtudiants.some((favoriteEtudiant) => favoriteEtudiant.etudiant === this.etudiant.id);
      
    }
  },
  watch: {
    favoriteEtudiants() {
      this.updateFavoriteEtudiantId();
    }
  }
};
</script>
<style scoped>
.custom-file {
  padding-bottom: 0px;
  width: 126px;
  text-align: center;
  justify-content: center;
}
.custom-iconss {
  font-size: 1.5rem;
  margin-right: 20px;
  color: #05264e;
}
.custom-icon-4 {
  color: #fff;
  font-size: 1.5rem;
  margin-left: 8px;
}
.dropdown-menu {
  display: block;
  left: auto !important;
  right: 0;
  min-width: 13rem;
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
  margin-left: 20px;
  width: 25px;
}
.dropdown-menu {
  z-index: 9999; /* Set a high z-index value */
}

.show-dropdown .dropdown-menu {
  display: block;
}
</style>
