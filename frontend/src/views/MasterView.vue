<template>
  <router>
    <!DOCTYPE html>

    <meta http-equiv="content-type" content="text/html;charset=UTF-8" />
    <head>
      <meta charset="UTF-8" />
      <meta
        name="viewport"
        content="width=device-width, initial-scale=1, maximum-scale=1"
      />
      <meta http-equiv="X-UA-Compatible" content="ie=edge" />
      <meta name="msapplication-TileColor" content="#0E0E0E" />
      <meta name="template-color" content="#0E0E0E" />
      <link rel="manifest" href="manifest.html" crossorigin />
      <meta name="msapplication-config" content="browserconfig.html" />
      <meta name="description" content="Index page" />
      <meta name="keywords" content="index, page" />
      <meta name="author" content="" />
      <title>Accueil</title>
      <link
        rel="shortcut icon"
        type="image/x-icon"
        href="assets/imgs/template/favicon.svg"
      />
      <link
        href="./template/assets/css/stylecd4e.css?version=4.1"
        rel="stylesheet"
      />
      <title>SW Connect</title>
    </head>
    <body>
      <div class="containerMaster">
        <router-view></router-view>
        <header class="header sticky-bar">
          <div class="container">
            <div class="main-header">
              <div class="header-nav">
                <nav class="nav-main-menu">
                  <ul class="main-menu">
                    <li class="has-children">
                      <router-link to="/">Accueil</router-link>
                    </li>
                    <li class="has-children">
                      <router-link to="/PageRegisterEtudiant"
                        >S'inscrire</router-link
                      >
                    </li>
                    <li class="has-children">
                      <router-link to="/ConnexionView"
                        >Se Connecter</router-link
                      >
                    </li>
                    <li class="has-children">
                      <router-link to="/OffreGrid">Etudiant</router-link>
                    </li>
                    <li class="has-children">
                      <router-link to="/OffreGrid">Entreprise</router-link>
                    </li>
                  </ul>
                </nav>

                <!-- <div class="burger-icon burger-icon-white"><span class="burger-icon-top"></span><span class="burger-icon-mid"></span><span class="burger-icon-bottom"></span></div>-->
              </div>

              <!--<div class="block-signin"><a class='text-link-bd-btom hover-up' href='page-register.html'>Register</a><a class='btn btn-default btn-shadow ml-40 hover-up' href='page-signin.html'>Sign in</a></div>-->
            </div>
          </div>
        </header>

        <main class="main">
          <section class="section-box mb-70">
            <div class="banner-hero hero-1 banner-homepage5">
              <div class="banner-inner">
                <div class="row">
                  <div class="col-xl-7 col-lg-12">
                    <div class="box-logos-485">
                      <img
                        class="logo-image"
                        src="template/assets/imgs/page/homepage5/SW-logo.png"
                        alt="SW Connect Logo"
                      />
                      <h1
                        class="banner-description mt-10 wow animate__animated animate__fadeInUp"
                      >
                        Générez votre portfolio, trouvez vos opportunités.
                      </h1>
                    </div>
                  </div>

                  <div>
                    <div class="banner-imgs">
                      <div class="banner-1 shape-1">
                        <img
                          class="img-responsive"
                          src="template/assets/imgs/page/homepage5/image.png"
                        />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
          <!--Statistique-->
          <section class="section-box overflow-visible mt-50 mb-50">
            <div class="container">
              <div class="row">
                <div class="col-12">
                  <div class="image-container">
                    <img
                      src="template/assets/imgs/page/homepage5/img1.png"
                      class="image1"
                    />
                  </div>
                </div>
              </div>

              <div class="column">
                <div class="col-xl-3 col-lg-3 col-md-6 col-sm-6 col-12">
                  <div class="text-start">
                    <div class="list-tabs list-tabs-2 mt-30">
                      <ul class="nav nav-tabs-stat" role="tablist">
                        <li class="offres">
                          <a
                            class="active"
                            data-bs-toggle="tab"
                            role="tab"
                            aria-controls="tab-job-1"
                            aria-selected="true"
                          >
                            <img
                              src="template/assets/imgs/template/icons/briefcase.png"
                              alt="jobBox"
                            />
                            <h1 class="color-brand-2">
                              <span class="count">1450</span>
                            </h1>
                            offres de stage</a
                          >
                        </li>
                        <li class="etud">
                          <a
                            class="active"
                            data-bs-toggle="tab"
                            role="tab"
                            aria-controls="tab-job-1"
                            aria-selected="true"
                            ><img
                              src="template/assets/imgs/template/icons/etud.png"
                              alt="jobBox"
                            />
                            <h1 class="color-brand-2">
                              <span class="count">380</span>
                            </h1>
                            Etudiants</a
                          >
                        </li>
                        <li class="ent">
                          <a
                            class="active"
                            data-bs-toggle="tab"
                            role="tab"
                            aria-controls="tab-job-1"
                            aria-selected="true"
                            ><img
                              src="template/assets/imgs/template/icons/ent.png"
                              alt="jobBox"
                            />
                            <h1 class="color-brand-2">
                              <span class="count">2500</span>
                            </h1>
                            Entreprises</a
                          >
                        </li>
                        <li class="dom">
                          <a
                            class="active"
                            data-bs-toggle="tab"
                            role="tab"
                            aria-controls="tab-job-1"
                            aria-selected="true"
                            ><img
                              src="template/assets/imgs/template/icons/Stack.png"
                              alt="jobBox"
                            />
                            <h1 class="color-brand-2">
                              <span class="count">59</span>
                            </h1>
                            Domaines</a
                          >
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>

          <!--Découvrez   SW Connect ...-->
          <section class="section-box mt-50 mb-30 bg-brand-2 pt-60 pb-60">
            <div class="container">
              <div class="row">
                <div class="col-xl-5">
                  <div class="pt-70">
                    <h2 class="color-white mb-20">Découvrez SW Connect ...</h2>
                  </div>
                </div>

                <div class="col-xl-7">
                  <div class="box-swiper mt-50 layout-brand-1">
                    <div
                      class="swiper-container swiper-group-3-explore mh-none swiper"
                    >
                      <div class="swiper-wrapper pb-70 pt-5">
                        <div class="swiper-slide hover-up">
                          <div
                            class="card-grid-5 card-category hover-up"
                            style="background-color: white"
                          >
                            <!--<a href='jobs-grid.html'>-->
                            <div class="box-cover-img">
                              <img
                                src="template/assets/imgs/template/icons/Icon-tele.png"
                                alt="Description de l'image"
                              />
                              <div class="content-bottom">
                                <h6 class="mb-5">Génération d’un portfolio</h6>
                              </div>
                            </div>
                          </div>
                        </div>

                        <div class="swiper-slide hover-up">
                          <div
                            class="card-grid-5 card-category hover-up"
                            style="background-color: white"
                          >
                            <!--<a href='jobs-grid.html'>-->
                            <div class="box-cover-img">
                              <img
                                src="template/assets/imgs/template/icons/Icon.rech.png"
                                alt="Description de l'image"
                              />
                              <div class="content-bottom">
                                <h6 class="mb-5">
                                  Filtrage des offres selon vos besoins
                                </h6>
                              </div>
                            </div>
                          </div>
                        </div>

                        <div class="swiper-slide hover-up">
                          <div
                            class="card-grid-5 card-category hover-up"
                            style="background-color: white"
                          >
                            <!--<a href='jobs-grid.html'>-->
                            <div class="box-cover-img">
                              <img
                                src="template/assets/imgs/template/icons/Icon-com.png"
                                alt="Description de l'image"
                              />
                              <div class="content-bottom">
                                <h6 class="mb-5">
                                  Communication avec les entreprises
                                </h6>
                              </div>
                            </div>
                          </div>
                        </div>

                        <div class="swiper-slide hover-up">
                          <div
                            class="card-grid-5 card-category hover-up"
                            style="background-color: white"
                          >
                            <!--<a href='jobs-grid.html'>-->
                            <div class="box-cover-img">
                              <img
                                src="template/assets/imgs/template/icons/Icon-tele.png"
                                alt="Description de l'image"
                              />
                              <div class="content-bottom">
                                <h6 class="mb-5">
                                  Publication des offres de stage
                                </h6>
                              </div>
                            </div>
                          </div>
                        </div>

                        <div class="swiper-slide hover-up">
                          <div
                            class="card-grid-5 card-category hover-up"
                            style="background-color: white"
                          >
                            <!--<a href='jobs-grid.html'>-->
                            <div class="box-cover-img">
                              <img
                                src="template/assets/imgs/template/icons/Icon.rech.png"
                                alt="Description de l'image"
                              />
                              <div class="content-bottom">
                                <h6 class="mb-5">Filtrage des stagiaires</h6>
                              </div>
                            </div>
                          </div>
                        </div>

                        <div class="swiper-slide hover-up">
                          <div
                            class="card-grid-5 card-category hover-up"
                            style="background-color: white"
                          >
                            <!--<a href='jobs-grid.html'>-->
                            <div class="box-cover-img">
                              <img
                                src="template/assets/imgs/template/icons/Icon-com.png"
                                alt="Description de l'image"
                              />
                              <div class="content-bottom">
                                <h6 class="mb-5">
                                  Communication avec les candidatures
                                </h6>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="swiper-button-next swiper-button-next-1"></div>
                    <div class="swiper-button-prev swiper-button-prev-1"></div>
                  </div>
                </div>
              </div>
            </div>
          </section>

          <!--Domaines-->
          <section class="section-box mt-50">
            <div class="section-box wow animate__animated animate__fadeIn">
              <div class="container">
                <div class="text-start">
                  <h2
                    class="section-title mb-10 wow animate__animated animate__fadeInUp"
                    style="color: #447ab8"
                  >
                    Différents domaines
                  </h2>
                  <div class="list-tabs list-tabs-2 mt-30">
                    <ul class="nav nav-tabs" role="tablist">
                      <li class="row">
                        <p
                          class="active"
                          id="nav-tab-job-1"
                          data-bs-toggle="tab"
                          role="tab"
                          aria-controls="tab-job-1"
                        >
                          <img
                            src="template/assets/imgs/template/icons/Icon-inf.png"
                            alt="jobBox"
                          />
                          <span
                            style="
                              position: relative;
                              padding: 5px;
                              bottom: 10px;
                            "
                            >Informatique</span
                          ><br />
                          <span
                            style="
                              position: relative;
                              font-weight: 100;
                              padding: 60px;
                              bottom: 7px;
                            "
                            >15 sociétés</span
                          >
                        </p>
                        <p
                          id="nav-tab-job-2"
                          data-bs-toggle="tab"
                          role="tab"
                          aria-controls="tab-job-2"
                        >
                          <img
                            src="template/assets/imgs/template/icons/Icon-design.png"
                            alt="jobBox"
                          />
                          <span
                            style="
                              position: relative;
                              padding: 5px;
                              bottom: 10px;
                            "
                            >Design graphique et multimédia</span
                          ><br />
                          <span
                            style="
                              position: relative;
                              font-weight: 100;
                              padding: 60px;
                              bottom: 7px;
                            "
                            >25 sociétés</span
                          >
                        </p>
                        <p
                          id="nav-tab-job-3"
                          data-bs-toggle="tab"
                          role="tab"
                          aria-controls="tab-job-3"
                        >
                          <img
                            src="template/assets/imgs/template/icons/Icon-mark.png"
                            alt="jobBox"
                          />
                          <span
                            style="
                              position: relative;
                              padding: 5px;
                              bottom: 10px;
                            "
                            >Marketing</span
                          ><br />
                          <span
                            style="
                              position: relative;
                              font-weight: 100;
                              padding: 60px;
                              bottom: 7px;
                            "
                            >5 sociétés</span
                          >
                        </p>
                        <p
                          id="nav-tab-job-4"
                          data-bs-toggle="tab"
                          role="tab"
                          aria-controls="tab-job-4"
                        >
                          <img
                            src="template/assets/imgs/template/icons/Icon-tou.png"
                            alt="jobBox"
                          />
                          <span
                            style="
                              position: relative;
                              padding: 5px;
                              bottom: 10px;
                            "
                            >Tourisme</span
                          ><br />
                          <span
                            style="
                              position: relative;
                              font-weight: 100;
                              padding: 60px;
                              bottom: 7px;
                            "
                            >9 sociétés</span
                          >
                        </p>
                      </li>
                      <li class="row">
                        <p
                          id="nav-tab-job-5"
                          data-bs-toggle="tab"
                          role="tab"
                          aria-controls="tab-job-5"
                        >
                          <img
                            src="template/assets/imgs/template/icons/Icon-geni.png"
                            alt="jobBox"
                          />
                          <span
                            style="
                              position: relative;
                              padding: 5px;
                              bottom: 10px;
                            "
                            >Génie Civil</span
                          ><br />
                          <span
                            style="
                              position: relative;
                              font-weight: 100;
                              padding: 60px;
                              bottom: 7px;
                            "
                            >16 sociétés</span
                          >
                        </p>
                        <p
                          id="nav-tab-job-6"
                          data-bs-toggle="tab"
                          role="tab"
                          aria-controls="tab-job-6"
                        >
                          <img
                            src="template/assets/imgs/template/icons/Icon-finan.png"
                            alt="jobBox"
                          />
                          <span
                            style="
                              position: relative;
                              padding: 5px;
                              bottom: 10px;
                            "
                            >Finance et comptabilité</span
                          ><br />
                          <span
                            style="
                              position: relative;
                              font-weight: 100;
                              padding: 60px;
                              bottom: 7px;
                            "
                            >22 sociétés</span
                          >
                        </p>
                        <p
                          id="nav-tab-job-7"
                          data-bs-toggle="tab"
                          role="tab"
                          aria-controls="tab-job-7"
                        >
                          <img
                            src="template/assets/imgs/template/icons/Icon-med.png"
                            alt="jobBox"
                          />
                          <span
                            style="
                              position: relative;
                              padding: 5px;
                              bottom: 10px;
                            "
                            >Médecine et soins de santé</span
                          ><br />
                          <span
                            style="
                              position: relative;
                              font-weight: 100;
                              padding: 60px;
                              bottom: 7px;
                            "
                            >15 sociétés</span
                          >
                        </p>
                        <p
                          id="nav-tab-job-8"
                          data-bs-toggle="tab"
                          role="tab"
                          aria-controls="tab-job-8"
                        >
                          <img
                            src="template/assets/imgs/template/icons/Icon-sc.png"
                            alt="jobBox"
                          />
                          <span
                            style="
                              position: relative;
                              padding: 5px;
                              bottom: 10px;
                            "
                            >Science des données</span
                          ><br />
                          <span
                            style="
                              position: relative;
                              font-weight: 100;
                              padding: 60px;
                              bottom: 7px;
                            "
                            >4 sociétés</span
                          >
                        </p>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </section>

          <!--Chatbot-->
          <div>
            <section class="section-box mt-50 mb-30 bg-border-3 pt-100 pb-100">
              <div class="container">
                <div class="row">
                  <div class="col-lg-6">
                    <div class="pl-30">
                      <h2 class="color-brand-1 mt-0 mb-15">
                        Obtenez des réponses bien filtrées à vos questions sur SW
                        Connect...
                      </h2>
                      <p class="font-lg color-text-paragraph-2">
                        Offres, entreprises ou étudiants.
                      </p>
                    </div>
                  </div>
                  <div class="col-lg-6">
                    <img
                      class="bdrd-10 move-animation"
                      src="template/assets/imgs/page/homepage5/Chatbot.png"
                      alt="Chatbot"
                    />
                  </div>
                </div>
              </div>
            </section>
          </div>

          <!--Entreprises-->
          <section class="section-box-ent">
            <div class="mt-50">
              <h2
                class="section-title mb-10 wow animate__animated animate__fadeInUp"
                style="color: #447ab8; padding: 50px"
              >
                Différentes Offres
              </h2>

              <div class="tab-content" id="myTabContent-1">
                <div
                  class="tab-pane fade show active"
                  id="tab-job-1"
                  role="tabpanel"
                  aria-labelledby="tab-job-1"
                >
                  <div class="row">
                    <div
                      class="col-xl-4 col-lg-4 col-md-6 col-sm-12 col-12"
                      style="position: relative; padding: 21px"
                    >
                      <div class="card-grid-2 grid-bd-16 hover-up">
                        <div class="card-grid-2-image">
                          <div class="image-box">
                            <figure>
                              <img
                                src="template/assets/imgs/page/homepage2/img1.png"
                                alt="jobBox"
                              />
                            </figure>
                          </div>
                        </div>

                        <div class="card-block-info">
                          <h5>
                            <a href="job-details.html"
                              >React Native Web Developer</a
                            >
                          </h5>
                          <div class="mt-5">
                            <span class="card-location mr-15"
                              >New York, US</span
                            >
                          </div>
                          <div class="card-2-bottom mt-20">
                            <div class="row">
                              <div class="col-xl-7 col-md-7 mb-2">
                                <!--<a class="btn btn-tags-sm mr-5" href="#"
                                  >Voir Détails</a
                                >-->
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    <div
                      class="col-xl-4 col-lg-4 col-md-6 col-sm-12 col-12"
                      style="position: relative; padding: 21px"
                    >
                      <div class="card-grid-2 grid-bd-16 hover-up">
                        <div class="card-grid-2-image">
                          <div class="image-box">
                            <figure>
                              <img
                                src="template/assets/imgs/page/homepage2/img2.png"
                                alt="jobBox"
                              />
                            </figure>
                          </div>
                        </div>

                        <div class="card-block-info">
                          <h5>
                            <a href="job-details.html"
                              >Digital Marketing Manager</a
                            >
                          </h5>
                          <div class="mt-5">
                             <!--<span class="card-location mr-15">Chicago, US</span>-->
                          </div>
                          <div class="card-2-bottom mt-20">
                            <div class="row">
                              <div class="col-xl-7 col-md-7 mb-2">
                                    <!--<a class="btn btn-tags-sm mr-5" href="#"
                                  >Voir Détails</a
                                >-->
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    <div
                      class="col-xl-4 col-lg-4 col-md-6 col-sm-12 col-12"
                      style="position: relative; padding: 21px"
                    >
                      <div class="card-grid-2 grid-bd-16 hover-up">
                        <div class="card-grid-2-image">
                          <div class="image-box">
                            <figure>
                              <img
                                src="template/assets/imgs/page/homepage2/img3.png"
                                alt="jobBox"
                              />
                            </figure>
                          </div>
                        </div>

                        <div class="card-block-info">
                          <h5>
                            <a href="job-details.html"
                              >Web Designer/Developer</a
                            >
                          </h5>
                          <div class="mt-5">
                           <!--<span class="card-location mr-15">Chicago, US</span>-->
                          </div>
                          <div class="card-2-bottom mt-20">
                            <div class="row">
                              <div class="col-xl-7 col-md-7 mb-2">
                                    <!--<a class="btn btn-tags-sm mr-5" href="#"
                                  >Voir Détails</a
                                >-->
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    <div
                      class="col-xl-4 col-lg-4 col-md-6 col-sm-12 col-12"
                      style="position: relative; padding: 21px"
                    >
                      <div class="card-grid-2 grid-bd-16 hover-up">
                        <div class="card-grid-2-image">
                          <div class="image-box">
                            <figure>
                              <img
                                src="template/assets/imgs/page/homepage2/img4.png"
                                alt="jobBox"
                              />
                            </figure>
                          </div>
                        </div>

                        <div class="card-block-info">
                          <h5>
                            <a href="job-details.html">Full Stack Engineer</a>
                          </h5>
                          <div class="mt-5">
                             <!--<span class="card-location mr-15">Chicago, US</span>-->
                          </div>
                          <div class="card-2-bottom mt-20">
                            <div class="row">
                              <div class="col-xl-7 col-md-7 mb-2">
                                 <!--<a class="btn btn-tags-sm mr-5" href="#"
                                  >Voir Détails</a
                                >-->
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    <div
                      class="col-xl-4 col-lg-4 col-md-6 col-sm-12 col-12"
                      style="position: relative; padding: 21px"
                    >
                      <div class="card-grid-2 grid-bd-16 hover-up">
                        <div class="card-grid-2-image">
                          <div class="image-box">
                            <figure>
                              <img
                                src="template/assets/imgs/page/homepage2/img5.png"
                                alt="jobBox"
                              />
                            </figure>
                          </div>
                        </div>

                        <div class="card-block-info">
                          <h5>
                            <a href="job-details.html"
                              >Frontend Developer Full time</a
                            >
                          </h5>
                          <div class="mt-5">
                            <!--<span class="card-location mr-15">Chicago, US</span>-->
                          </div>
                          <div class="card-2-bottom mt-20">
                            <div class="row">
                              <div class="col-xl-7 col-md-7 mb-2">
                             <!--<a class="btn btn-tags-sm mr-5" href="#"
                                  >Voir Détails</a
                                >-->
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    <div
                      class="col-xl-4 col-lg-4 col-md-6 col-sm-12 col-12"
                      style="position: relative; padding: 21px"
                    >
                      <div class="card-grid-2 grid-bd-16 hover-up">
                        <div class="card-grid-2-image">
                          <div class="image-box">
                            <figure>
                              <img
                                src="template/assets/imgs/page/homepage2/img6.png"
                                alt="jobBox"
                              />
                            </figure>
                          </div>
                        </div>

                        <div class="card-block-info">
                          <h5>
                            <a href="job-details.html"
                              >React Native Mobile Developer</a
                            >
                          </h5>
                          <div class="mt-5">
                            <!--<span class="card-location mr-15">Chicago, US</span>-->
                          </div>
                          <div class="card-2-bottom mt-20">
                            <div class="row">
                              <div class="col-xl-7 col-md-7 mb-2">
                                    <!--<a class="btn btn-tags-sm mr-5" href="#"
                                  >Voir Détails</a
                                >-->
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    <a
                      href="#"
                      style="
                        position: absolute;
                        color: #646464c5;
                        font-size: 18px;
                        font-weight: 600;
                        left: 90%;
                      "
                      > <i class="fas fa-chevron-right"></i
                    ></a>
                  </div>
                </div>
              </div>
            </div>
          </section>
          <section class="section-box mt-50" style="background-color:#447AB8">
            <div class="section-box wow animate__animated animate__fadeIn">
              <div class="container">
                <div class="text-start">
                  <h2
                    class="section-title mb-10 wow animate__animated animate__fadeInUp"
                    style="color: #fff"
                  >
                    Différentes Entreprises
                  </h2>
                  <div class="list-tabs list-tabs-2 mt-30">
                    <ul class="nav nav-tabs" role="tablist">
                      <li class="row">
                        <p
                          class="active"
                          id="nav-tab-job-1"
                          data-bs-toggle="tab"
                          role="tab"
                          aria-controls="tab-job-1"
                        >
                          <img
                            src="template/assets/imgs/template/icons/Icon-inf.png"
                            alt="jobBox"
                          />
                          <span
                            style="
                              position: relative;
                              padding: 5px;
                              bottom: 10px;
                            "
                            >Proxym</span
                          ><br />
                          <span
                            style="
                              position: relative;
                              font-weight: 100;
                              padding: 60px;
                              bottom: 7px;
                            "
                            ></span
                          >
                        </p>
                        <p
                          id="nav-tab-job-2"
                          data-bs-toggle="tab"
                          role="tab"
                          aria-controls="tab-job-2"
                        >
                          <img
                            src="template/assets/imgs/template/icons/Icon-design.png"
                            alt="jobBox"
                          />
                          <span
                            style="
                              position: relative;
                              padding: 5px;
                              bottom: 10px;
                            "
                            >Design Print</span
                          ><br />
                          <span
                            style="
                              position: relative;
                              font-weight: 100;
                              padding: 60px;
                              bottom: 7px;
                            "
                            ></span
                          >
                        </p>
                        <p
                          id="nav-tab-job-3"
                          data-bs-toggle="tab"
                          role="tab"
                          aria-controls="tab-job-3"
                        >
                          <img
                            src="template/assets/imgs/template/icons/Icon-mark.png"
                            alt="jobBox"
                          />
                          <span
                            style="
                              position: relative;
                              padding: 5px;
                              bottom: 10px;
                            "
                            >MindShare Tunisie</span
                          ><br />
                          <span
                            style="
                              position: relative;
                              font-weight: 100;
                              padding: 60px;
                              bottom: 7px;
                            "
                            ></span
                          >
                        </p>
                        <p
                          id="nav-tab-job-4"
                          data-bs-toggle="tab"
                          role="tab"
                          aria-controls="tab-job-4"
                        >
                          <img
                            src="template/assets/imgs/template/icons/Icon-tou.png"
                            alt="jobBox"
                          />
                          <span
                            style="
                              position: relative;
                              padding: 5px;
                              bottom: 10px;
                            "
                            >Travel To Do</span
                          ><br />
                          <span
                            style="
                              position: relative;
                              font-weight: 100;
                              padding: 60px;
                              bottom: 7px;
                            "
                            ></span
                          >
                        </p>
                      </li>
                      <li class="row">
                        <p
                          id="nav-tab-job-6"
                          data-bs-toggle="tab"
                          role="tab"
                          aria-controls="tab-job-6"
                        >
                          <img
                            src="template/assets/imgs/template/icons/Icon-finan.png"
                            alt="jobBox"
                          />
                          <span
                            style="
                              position: relative;
                              padding: 5px;
                              bottom: 10px;
                            "
                            >BIAT</span
                          ><br />
                          <span
                            style="
                              position: relative;
                              font-weight: 100;
                              padding: 60px;
                              bottom: 7px;
                            "
                            ></span
                          >
                        </p>
                        <p
                          id="nav-tab-job-7"
                          data-bs-toggle="tab"
                          role="tab"
                          aria-controls="tab-job-7"
                        >
                          <img
                            src="template/assets/imgs/template/icons/Icon-med.png"
                            alt="jobBox"
                          />
                          <span
                            style="
                              position: relative;
                              padding: 5px;
                              bottom: 10px;
                            "
                            >Clinique Hannibal</span
                          ><br />
                          <span
                            style="
                              position: relative;
                              font-weight: 100;
                              padding: 60px;
                              bottom: 7px;
                            "
                            ></span
                          >
                        </p>
                        <p
                          id="nav-tab-job-8"
                          data-bs-toggle="tab"
                          role="tab"
                          aria-controls="tab-job-8"
                        >
                          <img
                            src="template/assets/imgs/template/icons/Icon-sc.png"
                            alt="jobBox"
                          />
                          <span
                            style="
                              position: relative;
                              padding: 5px;
                              bottom: 10px;
                            "
                            >Datavora</span
                          ><br />
                          <span
                            style="
                              position: relative;
                              font-weight: 100;
                              padding: 60px;
                              bottom: 7px;
                            "
                            ></span
                          >
                        </p>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </section>
          <section class="section-box mt-50">
            <div class="container">
              <div class="row">
                <div class="col-lg-6 col-md-12 mb-15 mb-lg-0">
                  <div class="box-radius-8 bg-urgent hover-up">
                    <div class="text-info">
                      <h3 style="color: #447ab8">Pour les étudiants</h3>
                      <p
                        class="font-sm color-text-paragraph-2"
                        style="
                          color: #447ab8;
                          font-size: 15px;
                          font-weight: 100;
                        "
                      >
                        Personnalisez votre portfolio pour mettre en valeur<br />
                        vos réalisations. Trouvez facilement le stage idéal<br />
                        en filtrant les offres selon vos critères.
                      </p>
                      <div class="mt-15">
                     <a class="btn btn-arrow-right" href="/PageRegisterEtudiant">
                          >s'inscrire maintenant</a
                        >
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-lg-6 col-md-12">
                  <div class="box-radius-8 bg-9 hover-up">
                    <div class="text-info">
                      <h3 style="color: #ffffff">Pour les entreprises</h3>
                      <p
                        class="font-sm color-text-paragraph-2"
                        style="
                          color: #ffffff;
                          font-size: 15px;
                          font-weight: 100;
                        "
                      >
                        Publiez vos offres de stage et sélectionnez les
                        meilleurs<br />
                        stagiaires pour votre équipe. Créez également <br />un
                        PFE BOOK pour présenter vos projets et attirer les
                        talents<br />
                        les plus prometteurs.
                      </p>
                      <div class="mt-15">
                     <a class="btn btn-arrow-right" href="/PageRegisterEtudiant">
                          >s'inscrire maintenant</a
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </main>
        <footer class="footer mt-50">
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
              <!--<div class="col-md-6 text-md-end text-start">
                  <div class="footer-social"><a class="font-xs color-text-paragraph" href="#">Privacy Policy</a><a class="font-xs color-text-paragraph mr-30 ml-30" href="#">Terms &amp; Conditions</a><a class="font-xs color-text-paragraph" href="#">Security</a></div>
                </div>-->
            </div>
          </div>
        </footer>
      </div>
    </body>
  </router>
</template>

<script>
export default {
  name: "MasterView",
};
</script>
<style></style>
