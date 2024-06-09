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
    <title>Portfolio 1</title>
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

    <link href="/template/assets/css/stylecd4e.css" rel="stylesheet" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
    />
  </head>
  <body>
    <!-- ======= Header ======= -->
    <header
      id="header"
      class="fixed-top"
      style="background: #4e505a; height: 80px"
    >
      <div class="container d-flex align-items-center justify-content-between">
        <!-- Uncomment below if you prefer to use an image logo -->
        <!-- <a href="index.html" class="logo"><img src="assets/img/logo.png" alt="" class="img-fluid"></a>-->

        <nav id="navbar" class="navbar" style="height: 31px">
          <div class="navbar-icons">
            <!--<button class="scroll-top-button">
        <router-link to="/GenePortfo2" >
    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M19 12H6M12 5l-7 7 7 7"></path>
    </svg>
  </router-link>
  </button>-->

            
          </div>
          <ul>
            <li v-for="section in sections" :key="section.id">
              <span
                v-if="section.id === currentSectionId"
                class="section-name"
                >{{ section.name }}</span
              >
            </li>
          </ul>
        </nav>
        <!-- .navbar -->
      </div>
    </header>
    <!-- End Header -->

    <!-- ======= Hero Section ======= -->
    <div
      id="hero"
      class="hero route bg-image"
      style="background-image: url(DevFolio/assets/img/Template1BG.png)"
    >
      <div class="hero-content display-table">
        <div class="table-cell">
          <div class="container" style="padding-bottom: -35px">
            <!--<p class="display-6 color-d">Hello, world!</p>-->
            <!-- <p class="pt-3"><a class="btn btn-primary btn js-scroll px-4" href="#about" role="button">Learn More</a></p> -->
          </div>
        </div>
      </div>
    </div>
    <!-- End Hero Section -->

    <main id="main">
      <!-- ======= About Section ======= -->
      <section id="profil" class="about-mf sect-pt4 route">
        <div class="container">
          <div class="row">
            <div class="col-sm-12">
              <div class="boxprofil">
                <div class="row">
                  <div class="col-md-6">
                    <div class="row profil">
                      <div class="col-sm-6 col-md-5">
                        <div class="about-img">
                          <!-- Utilisez la liaison de données pour définir dynamiquement la source de l'image -->
                          <img :src="imageUrl" class="imageprofil" alt="" />
                        </div>
                      </div>
                      <div class="col-sm-6 col-md-7">
                        <div
                          class="info"
                          style="position: relative; top: 20px; left: 430px"
                        >
                          <p>
                            <span
                              style="
                                font-size: 65px;
                                font-weight: bold;
                                color: #5e5f62d4;
                              "
                              >{{ prenom }}&nbsp;{{ nom }}</span
                            >
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div
                      class="about-me pt-4 pt-md-0"
                      style="position: relative; top: 120px; left: 100px"
                    >
                      <div class="title-box-2">
                        <h5 class="title-left">A propos de moi</h5>
                      </div>
                      <p class="lead">
                        <textarea
                          v-model="profil"
                          placeholder="Écrivez plus sur vous ..."
                          style="
                            border: none;
                            outline: none;
                            background: none;
                            width: calc(100% + 17px);
                            font-size: 1.25rem;
                            font-weight: 300;
                            color: #4f5e64;
                            resize: vertical;
                            position: relative;
                            left: -17px;
                          "
                        ></textarea>
                      </p>
                    </div>
                  </div>
                  <div style="position: relative; left: 305px; top: -40px">
                    <ul class="social-list">
                      <li
                        class="social-item"
                        style="position: relative; left: 80px"
                      >
                        <a :href="skype" class="social-link" target="_blank">
                          <i
                            class="fab fa-skype fa-3x"
                            style="color: rgb(78, 80, 90)"
                          ></i>
                        </a>
                      </li>

                      <li
                        class="social-item"
                        style="position: relative; left: 140px; top: -45px"
                      >
                        <a :href="linkedin" class="social-link" target="_blank">
                          <i
                            class="fab fa-linkedin fa-3x"
                            style="color: rgb(78, 80, 90)"
                          ></i>
                        </a>
                      </li>

                      <li
                        class="social-item"
                        style="position: relative; left: 200px; top: -87px"
                      >
                        <a :href="github" class="social-link" target="_blank">
                          <i
                            class="fab fa-github fa-3x"
                            style="color: rgb(78, 80, 90)"
                          ></i>
                        </a>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <span
            style="
              position: relative;
              color: #e7efff;
              font-size: 130px;
              left: 90%;
              top: 40px;
            "
            >✦</span
          >
          <span
            style="
              position: relative;
              color: #d7d9e5;
              font-size: 50px;
              left: 82%;
              top: 40px;
            "
            >✦</span
          >
          <span
            style="
              position: relative;
              color: #d7d9e5;
              font-size: 50px;
              left: 80%;
              top: 60px;
            "
            >✦</span
          >
        </div>
      </section>
      <!-- End About Section -->

      <!--education start -->
      <section
        id="formation"
        class="education"
        style="position: relative; top: 100px"
      >
        <div
          class="title-box-2"
          style="position: relative; left: 35%; top: 50%"
        >
          <h5 class="title-left">Mon parcours académique</h5>
        </div>
        <div class="container" style="width: 1000px; height: 500px">
          <div class="education-horizontal-timeline">
            <div class="row">
              <!-- Afficher les formations existantes -->
              <div
                class="col-sm-4"
                v-for="(formation, index) in formations"
                :key="index"
              >
                <div class="single-horizontal-timeline">
                  <div class="experience-time">
                    <h2>
                      <input
                        type="text"
                        v-model="formation.debutformation"
                        placeholder="Début"
                        style="
                          border: none;
                          outline: none;
                          background: none;
                          width: 40%;
                        "
                      />
                      ~
                      <input
                        type="text"
                        v-model="formation.finformation"
                        placeholder="Fin"
                        style="
                          border: none;
                          outline: none;
                          background: none;
                          width: 35%;
                        "
                      />
                    </h2>
                    <h3>
                      <input
                        type="text"
                        v-model="formation.nomformation"
                        placeholder="Formation"
                        style="
                          border: none;
                          outline: none;
                          background: none;
                          width: 90%;
                          font-size: 16px;
                          font-weight: 300;
                          color: #636a82;
                          margin-top: 1px;
                          text-transform: uppercase;
                        "
                      />
                    </h3>
                  </div>
                  <div class="timeline-horizontal-border" style="padding: 7px">
                    <i class="fa fa-circle" aria-hidden="true"></i>
                    <span class="single-timeline-horizontal"></span>
                  </div>
                  <div class="timeline">
                    <div class="timeline-content">
                      <h4 class="title">
                        <input
                          type="text"
                          v-model="formation.etablissement"
                          placeholder="Etablissement"
                          style="
                            border: none;
                            outline: none;
                            background: none;
                            width: 80%;
                            font-size: 16px;
                            font-weight: 400;
                            text-transform: uppercase;
                            color: #43485c;
                          "
                        />
                      </h4>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-sm-4">
                <div class="single-horizontal-timeline">
                  <div class="experience-time">
                    <h2>
                      <input
                        type="text"
                        v-model="debutformation"
                        placeholder="Début"
                        style="
                          border: none;
                          outline: none;
                          background: none;
                          width: 40%;
                        "
                      />
                      ~
                      <input
                        type="text"
                        v-model="finformation"
                        placeholder="Fin"
                        style="
                          border: none;
                          outline: none;
                          background: none;
                          width: 35%;
                        "
                      />
                    </h2>
                    <h3>
                      <input
                        type="text"
                        v-model="nomformation"
                        placeholder="Formation"
                        style="
                          border: none;
                          outline: none;
                          background: none;
                          width: 90%;
                          font-size: 16px;
                          font-weight: 300;
                          color: #636a82;
                          margin-top: 1px;
                          text-transform: uppercase;
                        "
                      />
                    </h3>
                  </div>
                  <div class="timeline-horizontal-border" style="padding: 7px">
                    <i class="fa fa-circle" aria-hidden="true"></i>
                    <span class="single-timeline-horizontal"></span>
                  </div>
                  <div class="timeline">
                    <div class="timeline-content">
                      <h4 class="title">
                        <input
                          type="text"
                          v-model="etablissement"
                          placeholder="Etablissement"
                          style="
                            border: none;
                            outline: none;
                            background: none;
                            width: 80%;
                            font-size: 16px;
                            font-weight: 400;
                            text-transform: uppercase;
                            color: #43485c;
                          "
                        />
                      </h4>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!--experience start -->
      <section id="experiences" class="experience">
        <div
          class="title-box-2"
          style="position: relative; left: 40%; top: 40%"
        >
          <h5 class="title-left">Mon expérience professionnelle</h5>
        </div>
        <div class="container" style="width: 1140px">
          <div class="experience-content">
            <div class="main-timeline">
              <ul>
                <li v-for="experience in experiences" :key="experience.id">
                  <div class="single-timeline-box fix">
                    <div class="row exp">
                      <div
                        class="col-md-5"
                        style="
                          width: 41.6666666667%;
                          left: 50px;
                          position: relative;
                        "
                      >
                        <div class="experience-time text-right">
                          <h2>
                            <input
                              type="text"
                              v-model="experience.debutexperience"
                              placeholder="Début"
                              style="
                                border: none;
                                outline: none;
                                background: none;
                                width: 40%;
                              "
                            />
                            ~
                            <input
                              type="text"
                              v-model="experience.finexperience"
                              placeholder="Fin"
                              style="
                                border: none;
                                outline: none;
                                background: none;
                                width: 35%;
                              "
                            />
                          </h2>
                          <h3>
                            <input
                              type="text"
                              v-model="experience.titre"
                              placeholder="Titre"
                              style="
                                border: none;
                                outline: none;
                                background: none;
                                width: 90%;
                                font-size: 16px;
                                font-weight: 300;
                                color: #636a82;
                                margin-top: 1px;
                                text-transform: uppercase;
                              "
                            />
                          </h3>
                        </div>
                        <!--/.experience-time-->
                      </div>
                      <!--/.col-->
                      <div class="col-md-offset-1 col-md-5">
                        <div class="timeline">
                          <div class="timeline-content">
                            <h4 class="title">
                              <span
                                ><i
                                  class="fa fa-circle"
                                  aria-hidden="true"
                                  style="
                                    color: #03045e;
                                    position: relative;
                                    left: -11px;
                                    top: 5px;
                                  "
                                ></i
                              ></span>
                              <input
                                type="text"
                                v-model="experience.entreprise"
                                placeholder="Entreprise"
                                style="
                                  border: none;
                                  outline: none;
                                  background: none;
                                  width: 90%;
                                  font-size: 16px;
                                  font-weight: 300;
                                  color: #636a82;
                                  margin-top: 1px;
                                  text-transform: uppercase;
                                "
                              />
                            </h4>
                            <p class="description">
                              <textarea
                                v-model="experience.description"
                                placeholder="Écrivez plus sur vos expériences ..."
                                style="
                                  border: none;
                                  outline: none;
                                  background: none;
                                  width: calc(100% + 17px);
                                  font-size: 1.25rem;
                                  font-weight: 300;
                                  color: #4f5e64;
                                  resize: vertical;
                                  position: relative;
                                  left: -17px;
                                "
                              ></textarea>
                            </p>
                          </div>
                          <!--/.timeline-content-->
                        </div>
                        <!--/.timeline-->
                      </div>
                      <!--/.col-->
                    </div>
                  </div>
                  <!--/.single-timeline-box-->
                </li>
                <li>
                  <div class="single-timeline-box fix">
                    <div class="row exp">
                      <div
                        class="col-md-5"
                        style="
                          width: 41.6666666667%;
                          left: 50px;
                          position: relative;
                        "
                      >
                        <div class="experience-time text-right">
                          <h2>
                            <input
                              type="text"
                              v-model="debutexperience"
                              placeholder="Début"
                              style="
                                border: none;
                                outline: none;
                                background: none;
                                width: 40%;
                              "
                            />
                            ~
                            <input
                              type="text"
                              v-model="finexperience"
                              placeholder="Fin"
                              style="
                                border: none;
                                outline: none;
                                background: none;
                                width: 35%;
                              "
                            />
                          </h2>
                          <h3>
                            <input
                              type="text"
                              v-model="titreexperience"
                              placeholder="Formation"
                              style="
                                border: none;
                                outline: none;
                                background: none;
                                width: 90%;
                                font-size: 16px;
                                font-weight: 300;
                                color: #636a82;
                                margin-top: 1px;
                                text-transform: uppercase;
                              "
                            />
                          </h3>
                        </div>
                        <!--/.experience-time-->
                      </div>
                      <!--/.col-->
                      <div class="col-md-offset-1 col-md-5">
                        <div class="timeline">
                          <div class="timeline-content">
                            <h4 class="title">
                              <span
                                ><i
                                  class="fa fa-circle"
                                  aria-hidden="true"
                                  style="
                                    color: #03045e;
                                    position: relative;
                                    left: -11px;
                                    top: 5px;
                                  "
                                ></i
                              ></span>
                              <input
                                type="text"
                                v-model="entreprisexperience"
                                placeholder="Formation"
                                style="
                                  border: none;
                                  outline: none;
                                  background: none;
                                  width: 90%;
                                  font-size: 16px;
                                  font-weight: 300;
                                  color: #636a82;
                                  margin-top: 1px;
                                  text-transform: uppercase;
                                "
                              />
                            </h4>
                            <p class="description">
                              <textarea
                                v-model="descriptionexperience"
                                placeholder="Écrivez plus sur vos expériences ..."
                                style="
                                  border: none;
                                  outline: none;
                                  background: none;
                                  width: calc(100% + 17px);
                                  font-size: 1.25rem;
                                  font-weight: 300;
                                  color: #4f5e64;
                                  resize: vertical;
                                  position: relative;
                                  left: -17px;
                                "
                              ></textarea>
                            </p>
                          </div>
                          <!--/.timeline-content-->
                        </div>
                        <!--/.timeline-->
                      </div>
                      <!--/.col-->
                    </div>
                  </div>
                  <!--/.single-timeline-box-->
                </li>
              </ul>
            </div>
            <!--.main-timeline-->
          </div>
          <!--.experience-content-->
        </div>
      </section>
      <!--/.experience-->
      <!--experience end -->
      <!--profiles start -->
      <section id="competences" class="profiles">
        <div class="profiles-details">
          <div class="title-box text-center">
            <div
              class="title-box-2"
              style="position: relative; left: 3%; top: 50%"
            >
              <h5 class="title-left">Mes compétences et expertises</h5>
            </div>
          </div>
          <div class="container">
            <div class="profiles-content">
              <div class="row">
                <div
                  class="col-sm-3"
                  v-for="(competence, index) in competences"
                  :key="index"
                >
                  <div class="single-profile">
                    <div class="profile-txt">
                      <a href=""><i class="flaticon-themeforest"></i></a>
                      <div class="profile-icon-name">
                        <textarea
                          v-model="competence.categorie"
                          placeholder="Categorie"
                          style="
                            border: none;
                            outline: none;
                            background: none;
                            color: #43485c;
                            font-size: 18px;
                            resize: none;
                            position: relative;
                            top: 185px;
                            font-weight: 600;
                          "
                          maxlength="45"
                        ></textarea>
                        <textarea
                          v-model="competence.competence"
                          placeholder="Compétences"
                          style="
                            border: none;
                            outline: none;
                            background: none;
                            color: #43485c;
                            font-size: 18px;
                            resize: none;
                            font-weight: 400;
                          "
                          maxlength="45"
                        ></textarea>
                      </div>
                    </div>
                    <div class="single-profile-overlay">
                      <div class="profile-txt">
                        <a href=""><i class="flaticon-themeforest"></i></a>
                        <div class="profile-icon-name">
                          <textarea
                            v-model="competence.categorie"
                            placeholder="Categorie"
                            style="
                              border: none;
                              outline: none;
                              background: none;
                              color: white;
                              font-size: 18px;
                              resize: none;
                              position: relative;
                              top: 185px;
                              font-weight: 600;
                            "
                            maxlength="85"
                          ></textarea>
                          <textarea
                            v-model="competence.competence"
                            placeholder="Compétences"
                            style="
                              border: none;
                              outline: none;
                              background: none;
                              color: #43485c;
                              font-size: 18px;
                              resize: none;
                              font-weight: 400;
                              position: relative;
                              top: 5px;
                            "
                            maxlength="45"
                          ></textarea>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-sm-3">
                  <div class="single-profile">
                    <div class="profile-txt">
                      <a href=""><i class="flaticon-themeforest"></i></a>
                      <div class="profile-icon-name">
                        <textarea
                          v-model="categorie"
                          placeholder="Categorie"
                          style="
                            border: none;
                            outline: none;
                            background: none;
                            color: #43485c;
                            font-size: 18px;
                            resize: none;
                            position: relative;
                            top: 185px;
                            font-weight: 600;
                          "
                          maxlength="45"
                        ></textarea>
                        <textarea
                          v-model="competence"
                          placeholder="Compétences"
                          style="
                            border: none;
                            outline: none;
                            background: none;
                            color: #43485c;
                            font-size: 18px;
                            resize: none;
                            font-weight: 400;
                          "
                          maxlength="45"
                        ></textarea>
                      </div>
                    </div>
                    <div class="single-profile-overlay">
                      <div class="profile-txt">
                        <a href=""><i class="flaticon-themeforest"></i></a>
                        <div class="profile-icon-name">
                          <textarea
                            v-model="categorie"
                            placeholder="Categorie"
                            style="
                              border: none;
                              outline: none;
                              background: none;
                              color: white;
                              font-size: 18px;
                              resize: none;
                              position: relative;
                              top: 185px;
                              font-weight: 600;
                            "
                            maxlength="75"
                          ></textarea>
                          <textarea
                            v-model="competence"
                            placeholder="Compétences"
                            style="
                              border: none;
                              outline: none;
                              background: none;
                              color: #43485c;
                              font-size: 18px;
                              resize: none;
                              font-weight: 400;
                              position: relative;
                              top: 5px;
                            "
                            maxlength="45"
                          ></textarea>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!--/.profiles-->
      <!--profiles end -->

      <!-- ======= projets Section ======= -->
      <section id="projets" class="portfolio-mf sect-pt4 route">
        <div class="container">
          <div class="row">
            <div class="col-sm-12">
              <div class="title-box text-center">
                <div
                  class="title-box-2"
                  style="position: relative; left: 3%; top: 50%"
                >
                  <h5 class="title-left">
                    Mes réalisations sur différents projets.
                  </h5>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div
              class="col-md-4"
              v-for="(projet, index) in projets"
              :key="index"
            >
              <img
                src="template\assetss\imgs\icons\trombone.png"
                style="width: 35%; position: relative; top: 80px; left: 290px"
              />

              <div class="work-box">
                <div class="work-content">
                  <div class="row">
                    <div class="col-sm-8">
                      <h2 class="w-title">
                        <textarea
                          type="text"
                          v-model="projet.titreprojet"
                          placeholder="Titre du projet"
                          style="
                            border: none;
                            outline: none;
                            background: none;
                            width: 100%;
                            font-size: 18px;
                            font-weight: 550;
                            color: #636a82;
                            margin-top: 1px;
                            text-transform: uppercase;
                          "
                        ></textarea>
                      </h2>
                      <div class="w-more">
                        <span class="w-ctegory">
                          <textarea
                            v-model="projet.descriptionprojet"
                            placeholder="Description"
                            style="
                              border: none;
                              outline: none;
                              background: none;
                              width: calc(100% + 155px);
                              font-size: 17px;
                              font-weight: 400;
                              color: #43485c;
                              resize: vertical;
                              position: relative;
                              left: -17px;
                              text-transform: capitalize;
                            "
                          ></textarea>
                        </span>
                      </div>
                    </div>
                    <div class="col-sm-4"></div>
                  </div>
                </div>
              </div>
            </div>

            <div
              class="col-md-4"
              style="position: relative; top: 155px"
              v-show="!showProjet"
            >
              <div class="work-box">
                <div class="work-content" style="height: 450px">
                  <h2 class="w-title">Ajouter un nouveau projet</h2>
                  <form @submit.prevent="ajouterProjet">
                    <div class="form-group">
                      <label for="titreProjet">Titre du projet:</label>
                      <input
                        type="text"
                        class="form-control"
                        id="titreProjet"
                        v-model="nomnewprojet"
                        name="nomnewprojet"
                      />
                    </div>
                    <div class="form-group">
                      <label for="descriptionProjet"
                        >Description du projet:</label
                      >
                      <textarea
                        class="form-control"
                        id="descriptionProjet"
                        v-model="descriptionnewprojet"
                        name="descriptionnewprojet"
                      ></textarea>
                    </div>

                    <!--<div class="upload-container" >
        <label for="imageUpload" class="upload-label">
            <i class="fas fa-cloud-download-alt fa-3x" style="position: relative;color: #828282; opacity: 0.2; left:120px;padding: 10px;bottom: 12px;" ></i>
            <p class="upload-info" style="position: relative;left: 32px;bottom: 25px;font-weight: 700;">Uploader votre projet  ".Zip"</p>
        </label>
        <input type="file" id="imageUpload" name="fichier_zip" accept=".zip" style="display: none;" @change="displayFileName">
    </div>-->
                    <button
                      type="submit"
                      class="btn"
                      style="
                        position: relative;
                        left: 85%;
                        background-color: #43485c;
                        width: 30px;
                        height: 40px;
                        top: 30px;
                      "
                      @click="basculerAffichage()"
                    >
                      <i
                        class="fas fa-plus fa-2x"
                        style="
                          color: white;
                          position: relative;
                          left: -10px;
                          top: -8px;
                        "
                      ></i>
                    </button>
                  </form>
                </div>
              </div>
            </div>

            <div class="col-md-4" v-show="showProjet">
              <img
                src="template\assetss\imgs\icons\trombone.png"
                style="width: 35%; position: relative; top: 80px; left: 290px"
              />

              <div class="work-box">
                <div class="work-content">
                  <div class="row">
                    <div class="col-sm-8">
                      <h2 class="w-title">
                        <input
                          type="text"
                          v-model="nomnewprojet"
                          placeholder="Titre du projet"
                          style="
                            border: none;
                            outline: none;
                            background: none;
                            width: 80%;
                            font-size: 18px;
                            font-weight: 550;
                            color: #636a82;
                            margin-top: 1px;
                            text-transform: uppercase;
                          "
                        />
                      </h2>
                      <div class="w-more">
                        <span class="w-ctegory">
                          <textarea
                            v-model="descriptionnewprojet"
                            placeholder="Description"
                            style="
                              border: none;
                              outline: none;
                              background: none;
                              width: calc(100% + 155px);
                              font-size: 17px;
                              font-weight: 400;
                              color: #43485c;
                              resize: vertical;
                              position: relative;
                              left: -17px;
                              text-transform: capitalize;
                              resize: none;
                            "
                          ></textarea>
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!-- End Projet Section -->

      <!-- ======= soft skills Section ======= -->
      <section id="skills" class="blog-mf sect-pt4 route">
        <div
          class="container"
          style="padding-bottom: 150px; bottom: 20px; padding-top: 120px"
        >
          <div class="row">
            <div class="col-sm-12">
              <div class="title-box text-center">
                <div
                  class="title-box-2"
                  style="position: relative; left: 3%; top: 50%"
                >
                  <h5 class="title-left">Mes compétences relationnelles</h5>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <!-- Boucle sur les compétences récupérées de la base de données -->
            <div
              class="col-md-4"
              v-for="(skills, index) in softskills"
              :key="index"
            >
              <div class="box-shadow-full" :class="'skills-box-color-' + index">
                <div class="skill">
                  <h4 class="skill-title">
                    <input
                      type="text"
                      v-model="skills.titreskills"
                      placeholder="+ Soft Skills"
                      style="
                        border: none;
                        outline: none;
                        background: none;
                        width: 100%;
                        font-size: 20px;
                        font-weight: 550;
                        color: #43485c;
                        margin-top: 1px;
                        text-transform: uppercase;
                      "
                    />
                  </h4>
                </div>
              </div>
            </div>
            <div
              class="box-shadow-full"
              style="
                position: relative;
                left: 550px;
                top: 88px;
                background-color: #d7d9e5;
                height: 80px;
              "
            >
              <div class="skill">
                <h4 class="skill-title">
                  <input
                    type="text"
                    v-model="titreskills"
                    placeholder="+ Soft Skills"
                    style="
                      border: none;
                      outline: none;
                      background: none;
                      width: 90%;
                      font-size: 20px;
                      font-weight: 550;
                      color: #43485c;
                      margin-top: 1px;
                      text-transform: uppercase;
                    "
                  />
                </h4>
              </div>
            </div>
          </div>
        </div>

        <span
          style="
            position: relative;
            color: #4e505a;
            font-size: 70px;
            left: 92%;
            bottom: 300px;
          "
          >✦</span
        >
        <span
          style="
            position: relative;
            color: #4e505a;
            font-size: 33px;
            left: 92%;
            bottom: 300px;
          "
          >✦</span
        >
      </section>
      <!-- End soft skills Section -->

      <!-- ======= Centres d'interet Section ======= -->
      <section id="interet" class="blog-mf sect-pt4 route">
        <div class="container" style="padding-bottom: 150px">
          <div class="row">
            <div class="col-sm-12">
              <div class="title-box text-center">
                <div
                  class="title-box-2"
                  style="position: relative; left: 3%; top: 50%"
                >
                  <h5 class="title-left">Mes passions en dehors du travail</h5>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div
              class="col-md-4"
              v-for="(interet, index) in interets"
              :key="index"
            >
              <div
                class="box-shadow-full"
                :class="'interet-box-color-' + index"
              >
                <div class="skill">
                  <h4 class="skill-title">
                    <input
                      type="text"
                      v-model="interet.titreInteret"
                      placeholder="+ Centres d'interet"
                      style="
                        border: none;
                        outline: none;
                        background: none;
                        width: 90%;
                        font-size: 20px;
                        font-weight: 550;
                        color: #43485c;
                        margin-top: 1px;
                        text-transform: uppercase;
                      "
                    />
                  </h4>
                </div>
              </div>
            </div>
            <div
              class="box-shadow-full"
              style="
                position: relative;
                left: 570px;
                top: 77px;
                background-color: #e7efff;
                height: 80px;
              "
            >
              <div class="skill">
                <h4 class="skill-title">
                  <input
                    type="text"
                    v-model="titreInteret"
                    placeholder="+ Centres d'interet"
                    style="
                      border: none;
                      outline: none;
                      background: none;
                      width: 90%;
                      font-size: 20px;
                      font-weight: 550;
                      color: #43485c;
                      margin-top: 1px;
                      text-transform: uppercase;
                    "
                  />
                </h4>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!-- End Centres d'interet Section -->

      <!-- ======= langues Section ======= -->
      <section id="langue" class="blog-mf sect-pt4 route">
        <div class="container" style="padding-bottom: 300px">
          <div class="row">
            <div class="col-sm-12">
              <div class="title-box text-center">
                <div
                  class="title-box-2"
                  style="position: relative; left: 3%; top: 50%"
                >
                  <h5 class="title-left">Ma maîtrise des langues</h5>
                </div>
              </div>
            </div>
          </div>

          <div class="row">
            <div
              class="col-md-4"
              v-for="(langue, index) in langues"
              :key="index"
            >
              <div class="box-shadow-full" :class="'box-color-' + index">
                <div class="skill">
                  <h4 class="skill-title">
                    <input
                      type="text"
                      v-model="langue.langue"
                      placeholder="Langue"
                      style="
                        border: none;
                        outline: none;
                        background: none;
                        max-width: 200px;
                        width: 44%;
                        font-size: 20px;
                        font-weight: 550;
                        color: #43485c;
                        position: relative;
                        left: -75px;
                        word-wrap: break-word;
                      "
                    />
                    <span style="position: relative; left: -75px">:</span>
                  </h4>
                  <h4 class="skill-title">
                    <textarea
                      v-model="langue.niveau"
                      placeholder="Niveau"
                      style="
                        border: none;
                        outline: none;
                        background: none;
                        color: #43485c;
                        font-size: 18px;
                        resize: none;
                        position: relative;
                        top: -30px;
                        left: 100px;
                        font-weight: 600;
                        padding-top: 10px;
                      "
                      maxlength="25"
                    ></textarea>
                  </h4>
                </div>
              </div>
            </div>

            <div
              class="box-shadow-full"
              style="
                position: relative;
                left: 550px;
                top: 255px;
                background-color: #e7efff;
                height: 80px;
              "
            >
              <div class="skill">
                <h4 class="skill-title">
                  <input
                    type="text"
                    v-model="langue"
                    placeholder="Langue"
                    style="
                      border: none;
                      outline: none;
                      background: none;
                      width: 44%;
                      font-size: 20px;
                      font-weight: 550;
                      color: #43485c;
                      position: relative;
                      left: -45px;
                    "
                  /><span style="position: relative; left: -45px">:</span>
                  <input
                    type="text"
                    v-model="niveau"
                    placeholder="Niveau"
                    style="
                      border: none;
                      outline: none;
                      background: none;
                      width: 35;
                      font-size: 20px;
                      font-weight: 550;
                      color: #43485c;
                      position: relative;
                      left: 125px;
                      top: -48px;
                    "
                  />
                </h4>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!-- End langues Section -->

      <!-- ======= References Section ======= -->
      <section id="reference" class="blog-mf sect-pt4 route">
        <div class="container" style="padding-bottom: 150px">
          <div class="row">
            <div class="col-sm-12">
              <div class="title-box text-center">
                <div
                  class="title-box-2"
                  style="position: relative; left: 3%; top: 50%"
                >
                  <h5 class="title-left">Mes références</h5>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <!-- Loop through existing references -->
            <div
              class="col-md-4"
              v-for="reference in references"
              :key="reference"
            >
              <div
                class="box-shadow-full"
                style="
                  position: relative;
                  left: 300px;
                  top: 20px;
                  background-color: #e7efff;
                  height: 90px;
                  width: 350px;
                "
              >
                <div class="skill">
                  <h4 class="skill-title">
                    <input
                      type="text"
                      v-model="reference.titreref"
                      placeholder="Nom"
                      style="
                        border: none;
                        outline: none;
                        background: none;
                        width: 350px;
                        font-size: 17px;
                        font-weight: 550;
                        color: #43485c;
                        position: relative;
                        left: -25px;
                        top: -25px;
                      "
                    />
                  </h4>
                  <h4 class="skill-title">
                    <input
                      type="text"
                      v-model="reference.poste"
                      placeholder="Poste"
                      style="
                        border: none;
                        outline: none;
                        background: none;
                        height: 20px;
                        width: 350px;
                        font-size: 17px;
                        font-weight: 550;
                        color: #43485c;
                        position: relative;
                        left: -25px;
                        top: -24px;
                      "
                    />
                  </h4>
                  <h4 class="skill-title">
                    <input
                      type="text"
                      v-model="reference.emailref"
                      placeholder="Email"
                      style="
                        border: none;
                        outline: none;
                        background: none;
                        width: 350px;
                        font-size: 17px;
                        font-weight: 550;
                        color: #43485c;
                        position: relative;
                        left: -25px;
                        top: -32px;
                      "
                    />
                  </h4>
                </div>
              </div>
            </div>
          </div>
          <!-- Section for adding a new reference -->
          <div class="col-md-4">
            <div
              class="box-shadow-full"
              style="
                position: relative;
                left: 300px;
                top: 20px;
                background-color: #e7efff;
                height: 90px;
                width: 350px;
              "
            >
              <div class="skill">
                <h4 class="skill-title">
                  <input
                    type="text"
                    v-model="titreref"
                    placeholder="Nom"
                    class="textarea-limit-lines"
                    style="
                      border: none;
                      outline: none;
                      background: none;
                      width: 350px;
                      font-size: 17px;
                      font-weight: 550;
                      color: #43485c;
                      position: relative;
                      left: -25px;
                      top: -32px;
                    "
                  />
                </h4>
                <h4 class="skill-title">
                  <input
                    type="text"
                    v-model="poste"
                    placeholder="Poste"
                    class="textarea-limit-lines"
                    style="
                      border: none;
                      outline: none;
                      background: none;
                      height: 17px;
                      width: 350px;
                      font-size: 17px;
                      font-weight: 550;
                      color: #43485c;
                      position: relative;
                      left: -25px;
                      top: -30px;
                    "
                  />
                </h4>
                <h4 class="skill-title">
                  <input
                    type="text"
                    v-model="emailref"
                    placeholder="Email"
                    class="textarea-limit-lines"
                    style="
                      border: none;
                      outline: none;
                      background: none;
                      width: 350px;
                      font-size: 17px;
                      font-weight: 550;
                      color: #43485c;
                      position: relative;
                      left: -25px;
                      top: -27px;
                    "
                  />
                </h4>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- End References Section -->

      <!-- ======= clubs Section ======= -->
      <section id="clubs" class="blog-mf sect-pt4 route">
        <div class="container" style="padding-bottom: 150px">
          <div class="row">
            <div class="col-sm-12">
              <div class="title-box text-center">
                <div
                  class="title-box-2"
                  style="position: relative; left: 3%; top: 50%"
                >
                  <h5 class="title-left">Ma vie associative</h5>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-4" v-for="club in clubs" :key="club.id">
              <div
                class="box-shadow-full"
                style="
                  position: relative;
                  left: 300px;
                  top: 20px;
                  background-color: #e7efff;
                  height: 90px;
                  width: 350px;
                "
              >
                <div class="skill">
                  <h4 class="skill-title">
                    <input
                      type="text"
                      v-model="club.nomclub"
                      placeholder="Club"
                      style="
                        border: none;
                        outline: none;
                        background: none;
                        width: 350px;
                        font-size: 20px;
                        font-weight: 550;
                        color: #43485c;
                        position: relative;
                        left: -25px;
                        top: -20px;
                      "
                    />
                  </h4>
                  <h4 class="skill-title">
                    <input
                      type="text"
                      v-model="club.role"
                      placeholder="Nom"
                      class="textarea-limit-lines"
                      style="
                        border: none;
                        outline: none;
                        background: none;
                        width: 350px;
                        font-size: 17px;
                        font-weight: 550;
                        color: #43485c;
                        position: relative;
                        left: -25px;
                        top: -20px;
                      "
                    />
                  </h4>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div
              class="box-shadow-full"
              style="
                position: relative;
                left: 300px;
                top: 20px;
                background-color: #e7efff;
                height: 90px;
                width: 350px;
              "
            >
              <div class="skill">
                <h4 class="skill-title">
                  <input
                    type="text"
                    v-model="nomclub"
                    placeholder="Club"
                    class="textarea-limit-lines"
                    style="
                      border: none;
                      outline: none;
                      background: none;
                      width: 350px;
                      font-size: 17px;
                      font-weight: 550;
                      color: #43485c;
                      position: relative;
                      left: -25px;
                      top: -20px;
                    "
                  />
                </h4>
                <h4 class="skill-title">
                  <input
                    type="text"
                    v-model="role"
                    placeholder="Role"
                    class="textarea-limit-lines"
                    style="
                      border: none;
                      outline: none;
                      background: none;
                      width: 350px;
                      font-size: 17px;
                      font-weight: 550;
                      color: #43485c;
                      position: relative;
                      left: -25px;
                      top: -20px;
                    "
                  />
                </h4>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- End clubs Section -->

      <!-- ======= fin Section ======= -->
      <section class="blog-mf sect-pt4 route">
        <div class="container" style="padding-bottom: 100px">
          <div class="row">
            <div class="col-sm-12">
              <div class="title-box text-center">
                <div
                  class="title-box-2"
                  style="position: relative; left: 3%; top: 50%"
                >
                  <h5 class="title-left">MERCI !</h5>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-md-4">
              <div
                class="box-shadow-full"
                style="
                  position: relative;
                  left: 60px;
                  top: 20px;
                  background-color: rgb(78, 80, 90);
                  height: 100%;
                  width: 1200px;
                "
              >
                <div class="skill">
                  <h4
                    class="skill"
                    style="
                      color: white;
                      font-size: 30px;
                      font-weight: 100;
                      align-content: center;
                    "
                  >
                    Merci de visiter mon portfolio. J'espère que mon travail
                    vous a inspiré et vous a donné un aperçu de qui je suis en
                    tant que professionnel. Je suis enthousiaste à l'idée de
                    nouvelles opportunités de collaboration et de croissance.
                  </h4>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <!-- End fin Section -->
      <div>
        <button
          class="btn"
          style="
            background-color: rgb(67, 72, 92);
            opacity: 0.5;
            position: relative;
            top: -23px;
            left: 1180px;
          "
          @click.prevent="Enregistrerdonnestemplate"
        >
          <span style="color: white; font-weight: 800; font-size: 20px"
            >Enregistrer
          </span>
        </button>
      </div>
    </main>
    <!-- End #main -->

    <a
      href="#"
      class="back-to-top d-flex align-items-center justify-content-center"
      ><i class="bi bi-arrow-up-short"></i
    ></a>
  </body>
</template>

<script>
import axios from "axios";

export default {
  name: "PortTemplate1Choi",

  data() {
    return {
      sections: [
        { id: "profil", name: "Profil" },
        { id: "formation", name: "Formation" },
        { id: "experiences", name: "Experiences professionnelles" },
        { id: "competences", name: "Comptétences Techniques" },
        { id: "projets", name: "Projets" },
        { id: "skills", name: "Soft Skills" },
        { id: "interet", name: "Centres d'intérêt" },
        { id: "langue", name: "Langues" },
        { id: "reference", name: "References" },
        { id: "clubs", name: "Clubs" },
      ],
      currentSectionId: "",
      imageUrl: "",
      nom: "",
      prenom: "",
      profil: "",
      nomnewprojet: "",
      descriptionnewprojet: "",
      references: [],
      langues: [],
      interets: [],
      softskills: [],
      projets: [],
      competences: [],
      experiences: [],
      formations: [],
      clubs: [],
      showProjet: false,
      user: {},
      nouveauTexte: "",
      details: "",
      nomref: "",
      comp: "",
      cat: "",
      nouveauForma: "",
      etudiant: {
        id: null,
      },
      debutexperience: "",
      finexperience: "",
      titreexperience: "",
      entreprisexperience: "",
      descriptionexperience: "",
      debutformation: "",
      finformation: "",
      formation: "",
      etablissement: "",
      competence: "",
      categorie: "",
      titreskills: "",
      titreInteret: "",
      langue: "",
      niveau: "",
      titreref: "",
      emailref: "",
      poste: "",
      nomformation: "",
      nomclub: "",
      role: "",

      linkedin: "",
      github: "",
      skype: "",
    };
  },

  mounted() {
    window.addEventListener("scroll", this.handleScroll);
    this.fetchImageUrl();
    this.recupererDonnees();
    this.$nextTick(() => {});
  },

  beforeUnmount() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  created() {
    const userId = localStorage.getItem("user_id");
    if (!userId) {
      alert("Vous devez vous connecter.");
      this.$router.push("/ConnexionView");
    } else {
      // Stockez l'ID de l'utilisateur dans this.etudiant.id
      this.etudiant.id = userId;
    }
  },

  methods: {
    handleScroll() {
      const scrollPosition = window.scrollY + window.innerHeight / 2;
      for (let i = 0; i < this.sections.length; i++) {
        const section = this.sections[i];
        const sectionElement = document.getElementById(section.id);
        if (
          sectionElement.offsetTop <= scrollPosition &&
          sectionElement.offsetTop + sectionElement.offsetHeight >
            scrollPosition
        ) {
          this.currentSectionId = section.id;
          return;
        }
      }
      this.currentSectionId = "";
    },

    fetchImageUrl() {
      const userId = localStorage.getItem("user_id");
      if (!userId) {
        alert("Vous devez être connecté.");
        return;
      }

      axios
        .get(`http://127.0.0.1:8000/get-last-image/${userId}/`, {
          responseType: "blob",
        })
        .then((response) => {
          const imageUrl = URL.createObjectURL(response.data);
          this.imageUrl = imageUrl;
        })
        .catch((error) => {
          console.error(
            "Erreur lors de la récupération de l'URL de l'image:",
            error
          );
        });
    },

    recupererDonnees() {
      const userId = localStorage.getItem("user_id");
      if (!userId) {
        alert("Vous devez être connecté.");
        return;
      }
      axios
        .get(`http://127.0.0.1:8000/get-last-info/${userId}`)
        .then((response) => {
          this.nom = response.data.nom || "";
          this.prenom = response.data.prenom || "";
          this.profil = response.data.profil || "";
          this.formations = Array.isArray(response.data.formations)
            ? response.data.formations
            : [];
          this.experiences = Array.isArray(response.data.experiences)
            ? response.data.experiences
            : [];
          this.references = Array.isArray(response.data.references)
            ? response.data.references
            : [];
          this.langues = Array.isArray(response.data.langues)
            ? response.data.langues
            : [];
          this.interets = Array.isArray(response.data.interets)
            ? response.data.interets
            : [];
          this.competences = Array.isArray(response.data.competences)
            ? response.data.competences
            : [];
          this.softskills = Array.isArray(response.data.softskills)
            ? response.data.softskills
            : [];
          this.projets = Array.isArray(response.data.projets)
            ? response.data.projets
            : [];
          this.clubs = Array.isArray(response.data.clubs)
            ? response.data.clubs
            : [];
        })
        .catch((error) => {
          console.error("Erreur lors de la récupération des données:", error);
        });
    },

    onFileChange(event) {
      const selectedFile = event.target.files[0];
      this.fichiernewprojet = selectedFile;
    },

    shareLink() {
      // Vérifie si l'API Web Share est disponible dans le navigateur
      if (navigator.share) {
        // Utilisez l'API Web Share pour partager le lien
        navigator
          .share({
            title: "Votre titre", // Titre que vous voulez partager
            text: "Description de votre contenu", // Description de votre contenu
            url: "http://localhost:8080/PortfolioTemplate1", // Lien que vous souhaitez partager
          })
          .then(() => console.log("Lien partagé avec succès"))
          .catch((error) => console.error("Erreur lors du partage :", error));
      } else {
        // Si l'API Web Share n'est pas disponible, affichez un message d'avertissement ou une alternative
        alert(
          "La fonction de partage n'est pas prise en charge par votre navigateur."
        );
      }
    },

    basculerAffichage() {
      // Basculer entre l'affichage du formulaire et l'affichage du projet
      this.showProjet = !this.showProjet;
    },

    saveInfos() {
      const userId = localStorage.getItem("user_id");
      if (!userId) {
        alert("Vous devez être connecté.");
        return;
      }

      // Créez un tableau pour stocker les données des formations
      const formationsData = [];

      // Ajoutez les données des formations existantes
      this.formations.forEach((formation) => {
        formationsData.push({
          debutformation: formation.debutformation,
          finformation: formation.finformation,
          nomformation: formation.nomformation,
          etablissement: formation.etablissement,
        });
      });

      // Vérifiez si les données de la nouvelle formation sont remplies et ajoutez-les si oui
      if (
        this.debutformation ||
        this.finformation ||
        this.nomformation ||
        this.etablissement
      ) {
        formationsData.push({
          debutformation: this.debutformation,
          finformation: this.finformation,
          nomformation: this.nomformation,
          etablissement: this.etablissement,
        });
      }

      // Créez un tableau pour stocker les données des expériences professionnelles
      const experiencesData = [];

      // Ajoutez les données des expériences professionnelles existantes
      this.experiences.forEach((experience) => {
        experiencesData.push({
          debutexperience: experience.debutexperience,
          finexperience: experience.finexperience,
          titre: experience.titre,
          entreprise: experience.entreprise,
          description: experience.description,
        });
      });

      // Vérifiez si les données de la nouvelle expérience professionnelle sont remplies et ajoutez-les si oui
      if (
        this.debutexperience ||
        this.finexperience ||
        this.titreexperience ||
        this.entreprisexperience ||
        this.descriptionexperience
      ) {
        experiencesData.push({
          debutexperience: this.debutexperience,
          finexperience: this.finexperience,
          titre: this.titreexperience,
          entreprise: this.entreprisexperience,
          description: this.descriptionexperience,
        });
      }

      const competencesData = [];

      // Ajoutez les données des competences existantes
      this.competences.forEach((competence) => {
        competencesData.push({
          categorie: competence.categorie,
          competence: competence.competence,
        });
      });

      // Vérifiez si les données de la nouvelle competence sont remplies et ajoutez-les si oui
      if (this.categorie || this.competence) {
        competencesData.push({
          categorie: this.categorie,
          competence: this.competence,
        });
      }

      const softskillsData = [];

      this.softskills.forEach((skills) => {
        softskillsData.push({
          titreskills: skills.titreskills,
        });
      });

      if (this.titreskills) {
        softskillsData.push({
          titreskills: this.titreskills,
        });
      }

      const centreinteretsData = [];
      this.interets.forEach((interet) => {
        centreinteretsData.push({
          titreInteret: interet.titreInteret,
        });
      });

      if (this.titreInteret) {
        centreinteretsData.push({
          titreInteret: this.titreInteret,
        });
      }

      const languesData = [];
      this.langues.forEach((langue) => {
        languesData.push({
          langue: langue.langue,
          niveau: langue.niveau,
        });
      });

      if (this.langue || this.niveau) {
        languesData.push({
          langue: this.langue,
          niveau: this.niveau,
        });
      }
      const referencesData = [];
      const referenceSet = new Set();

      // Ajouter les références existantes en évitant les doublons
      this.references.forEach((reference) => {
        const referenceKey = `${reference.titreref}-${reference.poste}-${reference.emailref}`;
        if (!referenceSet.has(referenceKey)) {
          referencesData.push({
            titreref: reference.titreref,
            poste: reference.poste,
            emailref: reference.emailref,
          });
          referenceSet.add(referenceKey);
        }
      });

      // Ajouter les nouvelles références
      if (this.titreref || this.poste || this.emailref) {
        const newReferenceKey = `${this.titreref}-${this.poste}-${this.emailref}`;
        if (!referenceSet.has(newReferenceKey)) {
          referencesData.push({
            titreref: this.titreref,
            poste: this.poste,
            emailref: this.emailref,
          });
          referenceSet.add(newReferenceKey);
        }
      }

      const clubsData = [];
      //crée un nouvel ensemble vide
      const clubSet = new Set();

      this.clubs.forEach((club) => {
        const clubKey = `${club.nomclub}-${club.role}`;
        if (!clubSet.has(clubKey)) {
          clubsData.push({
            nomclub: club.nomclub,
            role: club.role,
          });
          clubSet.add(clubKey);
        }
      });

      if (this.nomclub || this.role) {
        const newclubKey = `${this.nomclub}-${this.role}`;
        if (!clubSet.has(newclubKey)) {
          clubsData.push({
            nomclub: this.nomclub,
            role: this.role,
          });
          clubSet.add(newclubKey);
        }
      }

      // Supposons que this.uploadedFileName et this.fichier_zip sont définis ailleurs dans le code
      console.log("Nom du fichier téléchargé:", this.uploadedFileName);
      console.log("Contenu du fichier téléchargé:", this.fichier_zip);

      const projetsData = [];
      this.projets.forEach((projet) => {
        projetsData.push({
          titreprojet: projet.titreprojet,
          descriptionprojet: projet.descriptionprojet,
          //fichier_zip: projet.fichier_zip,
        });
      });

      // Vérification des informations du nouveau projet
      if (this.nomnewprojet || this.descriptionnewprojet || this.fichier_zip) {
        projetsData.push({
          titreprojet: this.nomnewprojet,
          descriptionprojet: this.descriptionnewprojet,
          //fichier_zip_nom: this.uploadedFileName,
          fichier_zip: this.fichier_zip,
        });
        console.log("Nouveau projet ajouté avec succès.");
      }

      axios
        .post(`http://127.0.0.1:8000/stock-informations/${userId}/`, {
          profil: this.profil,
          formations: formationsData,
          experiences: experiencesData,
          competences: competencesData,
          softskills: softskillsData,
          interets: centreinteretsData,
          langues: languesData,
          references: referencesData,
          clubs: clubsData,
          projets: projetsData,
        })
        .then(() => {
          // Gérer la réponse du serveur si nécessaire
          console.log("Infos professionnelles enregistrés avec succès !");

          // Vous pouvez également actualiser les données après avoir enregistré les informations
          this.recupererDonnees();
        })
        .catch((error) => {
          // Gérer les erreurs si la sauvegarde échoue
          console.error(
            "Erreur lors de l'enregistrement des informations : ",
            error
          );
        });
    },
    enregistrerTemplate() {
      const userId = localStorage.getItem("user_id");
      if (!userId) {
        alert("Vous devez être connecté.");
        return;
      }

      const nomTemplate = "template1";

      axios
        .post(`http://127.0.0.1:8000/stock-template/${userId}/`, {
          etudiant: userId,
          nomtemplate: nomTemplate,
        })
        .then(() => {
          console.log("Template enregistré avec succès !");
          this.recupererDonnees();
        })
        .catch((error) => {
          console.error(
            "Erreur lors de l'enregistrement du template : ",
            error
          );
        });
    },

    Enregistrerdonnestemplate() {
      const userId = localStorage.getItem("user_id");
      if (!userId) {
        alert("Vous devez être connecté.");
        return;
      }
      this.saveInfos();
      this.enregistrerTemplate();
      this.$router.push("/EtudiantDetails/" + this.etudiant.id);
    },
  },
};
</script>
<style scoped>
/**
  * Template Name: DevFolio
  * Template URL: https://bootstrapmade.com/devfolio-bootstrap-portfolio-html-template/
  * Updated: Mar 17 2024 with Bootstrap v5.3.3
  * Author: BootstrapMade.com
  * License: https://bootstrapmade.com/license/
  */

/*--------------------------------------------------------------
  # General
  --------------------------------------------------------------*/

h1,
h2,
h3,
h4,
h5,
h6 {
  color: #1e1e1e;
}
.imageprofil {
  position: relative;
  height: 450px;
  width: 450px;
  bottom: 35px;
  left: 150px;
}
a {
  color: #1e1e1e;
  text-decoration: none;
  transition: all 0.5s ease-in-out;
}
body {
  color: #05264e;
  font-family: "Plus Jakarta Sans", sans-serif;
  font-size: 14px;
  line-height: 24px;
  font-style: normal;
  font-weight: 400;
  overflow: hidden;
}

a:hover {
  color: #0078ff;
  text-decoration: none;
  transition: all 0.5s ease-in-out;
}

.p-r {
  position: relative;
}

.color-a {
  text-decoration: none;
  color: #0078ff;
}

.color-d {
  color: #f5f5f5;
}

.color-text-a {
  text-decoration: none;
  color: #4e4e4e;
}

.box-shadow,
.card-blog,
.work-box,
.service-box,
.paralax-mf {
  box-shadow: 0 13px 8px -10px rgba(0, 0, 0, 0.1);
}

.box-shadow-a,
.button:hover {
  text-decoration: none;
  box-shadow: 0 0 0 4px #cde1f8;
}

.display-5 {
  font-size: 2.5rem;
  font-weight: 300;
  line-height: 1.1;
}

.display-6 {
  font-size: 2rem;
  font-weight: 300;
  line-height: 1.1;
}

.avatar {
  width: 32px;
  height: 32px;
  margin-right: 4px;
  overflow: hidden;
}

.bg-image {
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  background-position: center center;
}

@media (max-width: 1024px) {
  .bg-image {
    background-attachment: scroll;
  }
}

.overlay-mf {
  background-color: #0078ff;
}

.overlay-mf {
  position: absolute;
  top: 0;
  left: 0px;
  padding: 0;
  height: 100%;
  width: 100%;
  opacity: 0.7;
}

.paralax-mf {
  position: relative;
  padding: 8rem 0;
}

.display-table {
  width: 100%;
  height: 100%;
  display: table;
}

.table-cell {
  display: table-cell;
  vertical-align: middle;
}

/*--/ Sections /--*/
.sect-4 {
  padding: 4rem 0;
}

.sect-pt4 {
  padding-top: 4rem;
}

.sect-mt4 {
  margin-top: 4rem;
}

/*--/ Title s /--*/
.title-s {
  font-weight: 600;
  color: #1e1e1e;
  font-size: 1.1rem;
}

/*--/ Title A /--*/
.title-box {
  margin-bottom: 4rem;
}

.title-a {
  text-decoration: none;
  font-size: 3rem;
  font-weight: bold;
  text-transform: uppercase;
}

.subtitle-a {
  text-decoration: none;
  color: #4e4e4e;
}

.line-mf {
  width: 40px;
  height: 5px;
  background-color: #0078ff;
  margin: 0 auto;
}

/*--/ Title Left /--*/
.title-box-2 {
  margin-bottom: 3rem;
}

.title-left {
  font-size: 2rem;
  position: relative;
}

.title-left:before {
  content: "";
  position: absolute;
  height: 3px;
  background-color: #5e5f62d4;
  width: 150px;
  bottom: -12px;
}

/*------/ Box /------*/
.box-pl2 {
  padding-left: 2rem;
}

.box-shadow-full {
  padding: 2rem;
  position: relative;
  background-color: #fff;
  margin-bottom: 1rem;
  z-index: 2;
  box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.2);
  border-radius: 30px;
  height: 0.7px;
  width: 280px;
  top: 10px;
}

@media (min-width: 768px) {
  .box-shadow-full {
    padding: 2rem;
  }
}

/*------/ Socials /------*/
.socials {
  padding: 1.5rem 0;
}

.socials ul li {
  display: inline-block;
}

.socials .ico-circle {
  height: 40px;
  width: 40px;
  font-size: 1.2rem;
  border-radius: 50%;
  line-height: 1.6;
  margin: 0 15px 0 0;
  box-shadow: 0 0 0 3px #0078ff;
  transition: all 500ms ease;
}

.socials .ico-circle:hover {
  background-color: #0078ff;
  color: #fff;
  box-shadow: 0 0 0 3px #cde1f8;
  transition: all 500ms ease;
}

/*------/ Ul resect /------*/
.ul-resect,
.widget-tags ul,
.widget-sidebar .list-sidebar,
.box-comments .list-comments,
.blog-wrapper .post-meta ul,
.list-ico,
.socials ul {
  list-style: none;
  padding-left: 0;
  margin-bottom: 0;
}

.list-ico {
  line-height: 2;
}

.list-ico span {
  color: #0078ff;
  margin-right: 10px;
}

/*------/ Ico Circle /------*/
.ico-circle {
  height: 100px;
  width: 100px;
  font-size: 2rem;
  border-radius: 50%;
  line-height: 1.55;
  margin: 0 auto;
  text-align: center;
  box-shadow: 0 0 0 10px #0078ff;
  display: block;
}

/*------/ Owl Carousel /------*/
.owl-theme .owl-dots {
  text-align: center;
  margin-top: 18px;
}

.owl-theme .owl-dots .owl-dot {
  display: inline-block;
}

.owl-theme .owl-dots .owl-dot span {
  width: 18px;
  height: 7px;
  margin: 5px 5px;
  background: #cde1f8;
  border: 0px solid #cde1f8;
  display: block;
  transition: all 0.6s ease-in-out;
  cursor: pointer;
}

.owl-theme .owl-dots .owl-dot:hover span {
  background-color: #cde1f8;
}

.owl-theme .owl-dots .owl-dot.active span {
  background-color: #1b1b1b;
  width: 25px;
}

/*--/ Scrolltop s /--*/
.scrolltop-mf {
  position: relative;
  display: none;
}

.scrolltop-mf span {
  z-index: 999;
  position: fixed;
  width: 42px;
  height: 42px;
  background-color: #0078ff;
  opacity: 0.7;
  font-size: 1.6rem;
  line-height: 1.5;
  text-align: center;
  color: #fff;
  top: auto;
  left: auto;
  right: 30px;
  bottom: 50px;
  cursor: pointer;
  border-radius: 50%;
}

/*--------------------------------------------------------------
  # Back to top button
  --------------------------------------------------------------*/
.back-to-top {
  position: fixed;
  visibility: hidden;
  opacity: 0;
  right: 15px;
  bottom: 15px;
  z-index: 996;
  background: #0078ff;
  width: 40px;
  height: 40px;
  border-radius: 50px;
  transition: all 0.4s;
}

.back-to-top i {
  font-size: 28px;
  color: #fff;
  line-height: 0;
}

.back-to-top:hover {
  background: #298eff;
  color: #fff;
}

.back-to-top.active {
  visibility: visible;
  opacity: 1;
}

/*------/ Prelaoder /------*/
#preloader {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 9999;
  overflow: hidden;
  background: #fff;
}

#preloader:before {
  content: "";
  position: fixed;
  top: calc(50% - 30px);
  left: calc(50% - 30px);
  border: 6px solid #f2f2f2;
  border-top: 6px solid #0078ff;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  animation: animate-preloader 1s linear infinite;
}

@keyframes animate-preloader {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

/*------/ Button /------*/
.button {
  display: inline-block;
  padding: 0.3rem 0.6rem;
  text-align: center;
  vertical-align: middle;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
  font-size: 1rem;
  border-radius: 0.3rem;
  border: 1px solid transparent;
  transition: all 500ms ease;
  cursor: pointer;
}

.button:focus {
  outline: 0;
}

.button:hover {
  background-color: #0062d3;
  color: #fff;
  transition: all 500ms ease;
}

.button-a {
  text-decoration: none;
  background-color: #0078ff;
  color: #fff;
  border-color: #cde1f8;
}

.button-big {
  padding: 0.9rem 2.3rem;
  font-size: 1.2rem;
}

.button-rouded {
  border-radius: 5rem;
}

.btn-lg {
  padding: 0.5rem 1rem;
  font-size: 1.25rem;
  line-height: 1.5;
  border-radius: 0.3rem;
}

/*--------------------------------------------------------------
  # Header
  --------------------------------------------------------------*/
#header {
  transition: all 0.5s;
  z-index: 997;
  padding: 20px 0;
}

#header .logo {
  font-size: 28px;
  margin: 0;
  padding: 0;
  font-weight: 600;
  letter-spacing: 1px;
}

#header .logo a {
  color: #fff;
}

#header .logo img {
  max-height: 40px;
}

#header.header-scrolled {
  background: rgba(0, 0, 0, 0.9);
  padding: 12px 0;
}

/*--------------------------------------------------------------
  # Navigation Menu
  --------------------------------------------------------------*/
/**
  * Desktop Navigation 
  */
.navbar {
  padding: 0;
}

.navbar ul {
  margin: 0;
  padding: 0;
  display: flex;
  list-style: none;
  align-items: center;
}

.navbar li {
  position: relative;
}

.navbar > ul > li {
  white-space: nowrap;
  padding: 5px;
}

.navbar a,
.navbar a:focus {
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: #fff;
  font-size: 16px;
  font-weight: 600;
  padding: 0;
  white-space: nowrap;
  transition: 0.3s;
  letter-spacing: 0.4px;
  position: relative;
  text-transform: uppercase;
}

.navbar a i,
.navbar a:focus i {
  font-size: 12px;
  line-height: 0;
  margin-left: 5px;
}

.navbar > ul > li > a:before {
  content: "";
  position: absolute;
  width: 100%;
  height: 2px;
  bottom: -6px;
  left: 0;
  width: 0;
  background-color: #fff;
  visibility: hidden;
  transition: all 0.3s ease-in-out 0s;
}

.navbar a:hover:before,
.navbar li:hover > a:before,
.navbar .active:before {
  visibility: visible;
  width: 80%;
}

.navbar a:hover,
.navbar .active,
.navbar .active:focus,
.navbar li:hover > a {
  color: #fff;
}

.navbar .dropdown ul {
  display: block;
  position: absolute;
  left: 30px;
  top: calc(100% + 30px);
  margin: 0;
  padding: 10px 0;
  z-index: 99;
  opacity: 0;
  visibility: hidden;
  background: #fff;
  box-shadow: 0px 0px 30px rgba(127, 137, 161, 0.25);
  transition: 0.3s;
}

.navbar .dropdown ul li {
  min-width: 200px;
}

.navbar .dropdown ul a {
  padding: 10px 20px;
  font-size: 14px;
  text-transform: none;
  color: #4e4e4e;
}

.navbar .dropdown ul a i {
  font-size: 12px;
}

.navbar .dropdown ul a:hover,
.navbar .dropdown ul .active:hover,
.navbar .dropdown ul li:hover > a {
  color: #0078ff;
}

.navbar .dropdown:hover > ul {
  opacity: 1;
  top: 100%;
  visibility: visible;
}

.navbar .dropdown .dropdown ul {
  top: 0;
  left: calc(100% - 30px);
  visibility: hidden;
}

.navbar .dropdown .dropdown:hover > ul {
  opacity: 1;
  top: 0;
  left: 100%;
  visibility: visible;
}

@media (max-width: 1366px) {
  .navbar .dropdown .dropdown ul {
    left: -90%;
  }

  .navbar .dropdown .dropdown:hover > ul {
    left: -100%;
  }
}

/**
  * Mobile Navigation 
  */
.mobile-nav-toggle {
  color: #fff;
  font-size: 28px;
  cursor: pointer;
  display: none;
  line-height: 0;
  transition: 0.5s;
}

@media (max-width: 991px) {
  .mobile-nav-toggle {
    display: block;
  }

  .navbar ul {
    display: none;
  }
}

.navbar-mobile {
  position: fixed;
  overflow: hidden;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  background: rgba(78, 78, 78, 0.9);
  transition: 0.3s;
  z-index: 999;
}

.navbar-mobile .mobile-nav-toggle {
  position: absolute;
  top: 15px;
  right: 15px;
}

.navbar-mobile ul {
  display: block;
  position: absolute;
  top: 55px;
  right: 15px;
  bottom: 15px;
  left: 15px;
  padding: 10px 0;
  background-color: #fff;
  overflow-y: auto;
  transition: 0.3s;
}

.navbar-mobile > ul > li {
  padding: 0;
}

.navbar-mobile a:hover:before,
.navbar-mobile li:hover > a:before,
.navbar-mobile .active:before {
  visibility: hidden;
}

.navbar-mobile a,
.navbar-mobile a:focus {
  padding: 10px 20px;
  font-size: 15px;
  color: #4e4e4e;
}

.navbar-mobile a:hover,
.navbar-mobile .active,
.navbar-mobile li:hover > a {
  color: #0078ff;
}

.navbar-mobile .getstarted,
.navbar-mobile .getstarted:focus {
  margin: 15px;
}

.navbar-mobile .dropdown ul {
  position: static;
  display: none;
  margin: 10px 20px;
  padding: 10px 0;
  z-index: 99;
  opacity: 1;
  visibility: visible;
  background: #fff;
  box-shadow: 0px 0px 30px rgba(127, 137, 161, 0.25);
}

.navbar-mobile .dropdown ul li {
  min-width: 200px;
}

.navbar-mobile .dropdown ul a {
  padding: 10px 20px;
}

.navbar-mobile .dropdown ul a i {
  font-size: 12px;
}

.navbar-mobile .dropdown ul a:hover,
.navbar-mobile .dropdown ul .active:hover,
.navbar-mobile .dropdown ul li:hover > a {
  color: #0078ff;
}

.navbar-mobile .dropdown > .dropdown-active {
  display: block;
}

/*--------------------------------------------------------------
  # Hero Section
  --------------------------------------------------------------*/
.hero {
  height: 100vh;
  position: relative;
  color: #eb4343;
}

.hero .hero-content {
  text-align: center;
  position: absolute;
}

.hero .overlay-itro {
  background-color: rgba(0, 0, 0, 0.01);
  position: absolute;
  top: 0;
  left: 0px;
  padding: 0;
  height: 100%;
  width: 100%;
  opacity: 0.9;
}

@media (min-width: 768px) {
  .hero .hero-title {
    font-size: 4.5rem;
  }
}

.hero .hero-subtitle {
  font-size: 1.5rem;
  font-weight: 600;
}

@media (min-width: 768px) {
  .hero .hero-subtitle {
    font-size: 2.5rem;
  }
}

.hero .text-slider-items {
  display: none;
}

.hero-single {
  height: 350px;
}

.hero-single .hero-content {
  margin-top: 30px;
}

.hero-single .hero-title {
  text-transform: uppercase;
  font-size: 3rem;
}

@media (min-width: 768px) {
  .hero-single .hero-title {
    font-size: 3.5rem;
  }
}

.hero-single .breadcrumb {
  background-color: transparent;
  color: #0078ff;
}

.hero-single .breadcrumb .breadcrumb-item:before {
  color: #cde1f8;
}

.hero-single .breadcrumb .breadcrumb-item.active {
  color: #cde1f8;
}

.hero-single .breadcrumb a {
  color: #fff;
}

/*--------------------------------------------------------------
  # About
  --------------------------------------------------------------*/
.about-mf .box-shadow-full {
  padding-top: 10rem;
  padding-bottom: 9px;
}

.about-mf .about-img {
  margin-bottom: 2rem;
}

.about-mf .about-img img {
  margin-left: 10px;
}

@media (min-width: 767px) {
  .about-mf .box-pl2 {
    margin-top: 3rem;
    padding-left: 0rem;
  }
}

.skill-mf span {
  color: #4e4e4e;
}

.skill-mf .progress {
  background-color: #cde1f8;
  margin: 0.5rem 0 1.2rem 0;
  border-radius: 0;
  height: 0.7rem;
}

.skill-mf .progress .progress-bar {
  height: 0.7rem;
  background-color: #0078ff;
}

/*--------------------------------------------------------------
  # Services
  --------------------------------------------------------------*/
.service-box {
  background-color: #fff;
  padding: 2.5rem 1.3rem;
  border-radius: 1rem;
  margin-bottom: 3rem;
  text-align: center;
}

.service-box:hover .ico-circle {
  transition: all 500ms ease;
  color: #fff;
  background-color: #0078ff;
  box-shadow: 0 0 0 10px #cde1f8;
}

.service-box .service-ico {
  margin-bottom: 1rem;
  color: #1e1e1e;
}

.service-box .ico-circle {
  transition: all 500ms ease;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.service-box .ico-circle i {
  line-height: 0;
  font-size: 40px;
}

.service-box .s-title {
  font-size: 1.4rem;
  text-transform: uppercase;
  text-align: center;
  padding: 0.4rem 0;
}

.service-box .s-description {
  color: #4e4e4e;
}

/*--------------------------------------------------------------
  # Counter
  --------------------------------------------------------------*/
.counter-box {
  color: #fff;
  text-align: center;
}

@media (min-width: 577px) {
  .counter-box {
    margin-bottom: 1.8rem;
  }
}

.counter-ico {
  margin-bottom: 1rem;
}

.counter-ico .ico-circle {
  height: 60px;
  width: 60px;
  line-height: 1.5;
  box-shadow: 0 0 0 10px #cde1f8;
}

.counter-num .counter {
  font-size: 2rem;
  margin-bottom: 0;
}

/*--------------------------------------------------------------
  # Portfolio
  --------------------------------------------------------------*/
.work-box {
  margin-bottom: 3rem;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  background-color: rgba(78, 80, 90, 0.057);
}

.work-box:hover img {
  transform: scale(1.3);
}

.work-img {
  display: block;
  overflow: hidden;
}

.work-img img {
  transition: all 1s;
}

.work-content {
  padding: 2rem 3% 1rem 4%;
}

.work-content .w-more {
  color: #4e4e4e;
  font-size: 0.8rem;
}

.work-content .w-more .w-ctegory {
  color: #0078ff;
}

.work-content .w-like {
  font-size: 2.5rem;
  color: #0078ff;
  float: right;
}

.work-content .w-like a {
  color: #0078ff;
}

.work-content .w-like .num-like {
  font-size: 0.7rem;
}

.w-title {
  font-size: 1.2rem;
  width: 350px;
}

/*--------------------------------------------------------------
  # Portfolio Details
  --------------------------------------------------------------*/
.portfolio-details {
  padding-top: 40px;
}

.portfolio-details .portfolio-details-slider img {
  width: 100%;
}

.portfolio-details .portfolio-details-slider .swiper-pagination {
  margin-top: 20px;
  position: relative;
}

.portfolio-details
  .portfolio-details-slider
  .swiper-pagination
  .swiper-pagination-bullet {
  width: 12px;
  height: 12px;
  background-color: #fff;
  opacity: 1;
  border: 1px solid #0078ff;
}

.portfolio-details
  .portfolio-details-slider
  .swiper-pagination
  .swiper-pagination-bullet-active {
  background-color: #0078ff;
}

.portfolio-details .portfolio-info {
  padding: 30px;
  box-shadow: 0px 0 30px rgba(78, 78, 78, 0.08);
}

.portfolio-details .portfolio-info h3 {
  font-size: 22px;
  font-weight: 700;
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 1px solid #eee;
}

.portfolio-details .portfolio-info ul {
  list-style: none;
  padding: 0;
  font-size: 15px;
}

.portfolio-details .portfolio-info ul li + li {
  margin-top: 10px;
}

.portfolio-details .portfolio-description {
  padding-top: 30px;
}

.portfolio-details .portfolio-description h2 {
  font-size: 26px;
  font-weight: 700;
  margin-bottom: 20px;
}

.portfolio-details .portfolio-description p {
  padding: 0;
}

/*--------------------------------------------------------------
  # Testimonials
  --------------------------------------------------------------*/
.testimonial-box {
  color: #fff;
  text-align: center;
}

.testimonial-box .author-test {
  margin-top: 1rem;
}

.testimonial-box .author-test img {
  margin: 0 auto;
}

.testimonial-box .author {
  color: #fff;
  text-transform: uppercase;
  font-weight: 600;
  margin: 1rem 0;
  display: block;
  font-size: 1.4rem;
}

.testimonial-box .comit {
  font-size: 2rem;
  color: #0078ff;
  background-color: #fff;
  width: 52px;
  height: 52px;
  display: block;
  margin: 0 auto;
  border-radius: 50%;
  line-height: 1.6;
}

@media (min-width: 768px) {
  .testimonial-box .description {
    padding: 0 5rem;
  }
}

@media (min-width: 992px) {
  .testimonial-box .description {
    padding: 0 8rem;
  }
}

@media (min-width: 1200px) {
  .testimonial-box .description {
    padding: 0 13rem;
  }
}

.swiper-pagination {
  margin-top: 20px;
  position: relative;
}

.swiper-pagination .swiper-pagination-bullet {
  width: 12px;
  height: 12px;
  background-color: rgba(255, 255, 255, 0.4);
  opacity: 1;
}

.swiper-pagination .swiper-pagination-bullet-active {
  background-color: #fff;
}

/*--------------------------------------------------------------
  # Contact
  --------------------------------------------------------------*/
.footer-paralax {
  padding: 4rem 0 0 0;
}

.contact-mf {
  margin-top: 4rem;
}

@media (min-width: 767px) {
  .contact-mf .box-pl2 {
    margin-top: 3rem;
    padding-left: 0rem;
  }
}

.php-email-form .error-message {
  display: none;
  color: #fff;
  background: #ed3c0d;
  text-align: center;
  padding: 15px;
  font-weight: 600;
}

.php-email-form .sent-message {
  display: none;
  color: #fff;
  background: #18d26e;
  text-align: center;
  padding: 15px;
  font-weight: 600;
}

.php-email-form .loading {
  display: none;
  background: #fff;
  text-align: center;
  padding: 15px;
}

.php-email-form .loading:before {
  content: "";
  display: inline-block;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  margin: 0 10px -6px 0;
  border: 3px solid #18d26e;
  border-top-color: #eee;
  animation: animate-loading 1s linear infinite;
}

.php-email-form input,
.php-email-form textarea {
  border-radius: 0;
  box-shadow: none;
  font-size: 14px;
}

.php-email-form input:focus,
.php-email-form textarea:focus {
  border-color: #0078ff;
}

.php-email-form input {
  padding: 10px 15px;
}

.php-email-form textarea {
  padding: 12px 15px;
  margin-bottom: 0;
}

.php-email-form button[type="submit"] {
  background: #0078ff;
  border: 0;
  padding: 10px 24px;
  color: #fff;
  transition: 0.4s;
}

.php-email-form button[type="submit"]:hover {
  background: #3393ff;
}

@keyframes animate-loading {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

/*--------------------------------------------------------------
  # Blog
  --------------------------------------------------------------*/
@media (min-width: 767px) {
  .card-blog {
    margin-bottom: 3rem;
  }
}

.card-blog .card-body {
  position: relative;
}

.card-blog .card-category-box {
  position: absolute;
  text-align: center;
  top: -16px;
  left: 15px;
  right: 15px;
  line-height: 25px;
  overflow: hidden;
}

.card-blog .card-category {
  display: inline-block;
  color: #fff;
  padding: 0 15px 5px;
  overflow: hidden;
  background-color: #0078ff;
  border-radius: 4px;
}

.card-blog .card-category .category {
  color: #fff;
  display: inline-block;
  text-transform: uppercase;
  font-size: 0.7rem;
  letter-spacing: 0.1px;
  margin-bottom: 0;
}

.card-blog .card-title {
  font-size: 1.3rem;
  margin-top: 0.6rem;
}

.card-blog .card-description {
  color: #4e4e4e;
}

.card-blog .post-author {
  display: inline-block;
}

.card-blog .post-date {
  color: #4e4e4e;
  display: inline-block;
}

/*--------------------------------------------------------------
  # Blog Single
  --------------------------------------------------------------*/
.post-box,
.form-comments,
.box-comments,
.widget-sidebar {
  padding: 2rem;
  background-color: #fff;
  margin-bottom: 3rem;
}

@media (min-width: 768px) {
  .post-box,
  .form-comments,
  .box-comments,
  .widget-sidebar {
    padding: 3rem;
  }
}

.blog-wrapper .article-title {
  font-size: 1.5rem;
}

@media (min-width: 768px) {
  .blog-wrapper .article-title {
    font-size: 1.9rem;
  }
}

.blog-wrapper .post-meta {
  margin: 1rem 0;
}

.blog-wrapper .post-meta ul {
  border-left: 4px solid #0078ff;
  margin-top: 1rem;
}

.blog-wrapper .post-meta ul li {
  display: inline-block;
  margin-left: 15px;
}

.blog-wrapper .post-meta ul a {
  color: #0078ff;
}

.blog-wrapper .post-meta ul span {
  color: #1e1e1e;
}

.blog-wrapper .blockquote {
  border-left: 4px solid #0078ff;
  padding: 18px;
  font-style: italic;
}

/*------/ Comments /------*/
.box-comments .list-comments li {
  padding-bottom: 40px;
}

.box-comments .list-comments .comment-avatar {
  display: table-cell;
  vertical-align: top;
}

.box-comments .list-comments .comment-avatar img {
  width: 80px;
  height: 80px;
}

.box-comments .list-comments .comment-author {
  font-size: 1.3rem;
}

@media (min-width: 768px) {
  .box-comments .list-comments .comment-author {
    font-size: 1.5rem;
  }
}

.box-comments .list-comments .comment-details {
  display: table-cell;
  vertical-align: top;
  padding-left: 25px;
}

.box-comments .list-comments a {
  color: #0078ff;
}

.box-comments .list-comments span {
  color: #1e1e1e;
  font-style: italic;
}

.box-comments .comment-children {
  margin-left: 40px;
}

/*------/ Sidebar /------*/
.widget-sidebar .sidebar-title {
  font-size: 1.6rem;
  font-weight: 600;
  border-left: 5px solid #0078ff;
  padding-left: 15px;
  text-transform: uppercase;
  margin-bottom: 1.5rem;
}

.widget-sidebar .list-sidebar li {
  position: relative;
  padding: 6px 0 6px 24px;
}

.widget-sidebar .list-sidebar li:before {
  position: absolute;
  content: "";
  width: 10px;
  height: 1px;
  left: 0;
  background-color: #0078ff;
  top: 20px;
}

.sidebar-search input {
  background-color: #fff;
  border-radius: 0;
  transition: all 0.5s ease-in-out;
}

.sidebar-search .btn-search {
  background-color: #0078ff;
  border-color: #0078ff;
  border-radius: 0;
  padding-left: 20px;
  padding-right: 20px;
}

.widget-tags ul li {
  display: inline-block;
  background-color: #0078ff;
  padding: 0.2rem 0.6rem;
  margin-bottom: 0.5rem;
  border-radius: 15px;
}

.widget-tags ul li a {
  color: #fff;
}

/*--------------------------------------------------------------
  # Footer
  --------------------------------------------------------------*/
footer {
  text-align: center;
  color: #fff;
  padding: 25px 0;
  background: #0062d3;
}

footer .copyright {
  margin-bottom: 0.3rem;
}

footer .credits {
  margin-bottom: 0;
}

footer .credits a {
  color: #fff;
}
.navbar ul li span {
  font-size: 35px;
  font-weight: bold; /* Par exemple, applique une police en gras */
  color: #ffffff; /* Par exemple, définissez la couleur du texte */
  /* Ajoutez d'autres règles de style selon vos besoins */
}
span.single-timeline-horizontal {
  display: inline-block;
  background: #b2c1ce;
  height: 1px;
  width: 380px;
}
.section-heading h2 {
  font-size: 24px;
  font-weight: 600;
  text-transform: uppercase;
  padding-bottom: 50px;
  border-bottom: 1px solid #e5ebf2;
}
h1,
h2,
h3,
h4,
h5,
h6 {
  margin: 0;
  color: #43485c;
  font-size: 16px;
  font-family: "Poppins", sans-serif;
  text-transform: capitalize;
}

.timeline-horizontal-border i {
  font-size: 10px;
  color: #020c62c2;
  margin-right: 5px;
}
.timeline-horizontal-border {
  display: flex;
  align-items: center;
  padding: 26px 0 30px;
}

.single-timeline-box {
  margin-bottom: 75px;
}

.fix {
  position: relative;
  clear: both;
}
.section-heading h2 {
  font-size: 24px;
  font-weight: 600;
  text-transform: uppercase;
  padding-bottom: 50px;
  border-bottom: 1px solid #e5ebf2;
}
.single-timeline-box {
  margin-bottom: 75px;
}
.row {
  margin-right: 20px;
  margin-left: -15px;
}
.exp {
  margin-right: 20px;
  margin-left: 200px;
}
/*-------------------------------------
          7. Experience
  -------------------------------------*/
.experience {
  padding: 50px 0 100px;
  border-top: 1px solid #e5ebf2;
}
.experience-content {
  padding-top: 100px;
}
.single-timeline-box {
  margin-bottom: 75px;
}

/*experience-time*/
.experience-time {
  position: relative;
  left: -75px;
}
.experience-time h2 {
  font-weight: 400;
}
.experience-time h3 {
  font-size: 16px;
  font-weight: 300;
  color: #636a82;
  margin-top: 14px;
  text-transform: uppercase;
}
/*experience-time*/

/*main-timeline*/
.main-timeline {
  position: relative;
}
.main-timeline:before {
  content: "";
  width: 2px;
  height: 75%;
  background: #b2c1ce;
  position: absolute;
  top: 1.5%;
  left: 45.8%;
  z-index: -1;
}
.main-timeline .timeline {
  position: relative;
}

.timeline-content span > i,
.experience-time span > i {
  color: #66f92c;
  position: absolute;
  font-size: 15px;
  left: 15.5%;
  z-index: 1;
}
.timeline-content h4.title {
  font-size: 16px;
  font-weight: 400;
  text-transform: uppercase;
}
.timeline-content h5 {
  color: #636a82;
  font-size: 14px;
  font-weight: 300;
  margin: 18px 0 20px;
}
.main-timeline .description {
  font-size: 14px;
  color: #999fb3;
}
.main-timeline .timeline-content.right {
  float: right;
  text-align: left;
}
.timeline-single-before:before {
  content: "";
  top: 57px;
  left: -3px;
  position: absolute;
  width: 100%;
  height: 400px;
  border-left: 15px solid #fff;
}
/*-------------------------------------
          8. Profiles
  --------------------------------------*/
.profiles {
  padding: 50px 0 100px;
  border: 1px solid #e5ebf2;
}

.profiles-content {
  padding-top: 100px;
}
.profiles-content .col-sm-3 {
  padding: 0;
}
.profile-txt {
  display: flex;
  align-items: center;
  flex-direction: column;
}
.single-profile {
  position: relative;
  height: 150px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-right: 1px solid #b2c1ce;
  overflow: hidden;
  -webkit-transition: background 0.5s linear;
  -moz-transition: background 0.5s linear;
  -ms-transition: background 0.5s linear;
  -o-transition: background 0.5s linear;
  transition: background 0.5s linear;
}
.profile-icon-name {
  text-transform: capitalize;
  color: #636a82;
  font-size: 18px;
  font-weight: 600;
  padding: 15px;
}
.single-profile.profile-no-border {
  border-right: transparent;
}
.profile-border {
  border-bottom: 1px solid #b2c1ce;
}
.single-profile-overlay {
  display: flex;
  align-items: center;
  text-transform: capitalize;
  justify-content: center;
  position: absolute;
  top: 0;
  left: 0;
  content: " ";
  width: 100%;
  height: 100%;
  background: #a1aace;
  background: -moz-linear-gradient(left, #a1aace 0%, #a1aace 100%);
  background: -webkit-linear-gradient(left, #a1aace 0%, #a1aace 100%);
  background: linear-gradient(to right, #a1aace 0%, #4e505a 100%);
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#d92cf9', endColorstr='#b636ff',GradientType=1 );
  -webkit-transform: scale(0);
  -moz-transform: scale(0);
  -ms-transform: scale(0);
  -o-transform: scale(0);
  transform: scale(0);
  -webkit-transition: 0.5s;
  -moz-transition: 0.5s;
  -ms-transition: 0.5s;
  -o-transition: 0.5s;
  transition: 0.5s;
}
.single-profile:hover .single-profile-overlay {
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transform: scale(1);
  top: 0;
}
.single-profile:hover .profile-icon-name,
.single-profile:hover .profile-txt a > i {
  color: #fff;
}
.single-profile:hover .profile-border {
  border: transparent;
}

.skill-title {
  margin: -15px;
  color: #43485c;
  font-size: 20px;
  font-family: "Poppins", sans-serif;
  text-transform: capitalize;
  text-align: center;
}
.box-color-0 {
  position: relative;
  background-color: #e7efff;
  left: 707px;
  top: 140px;
  height: 80px;
}
.box-color-1 {
  position: relative;
  left: 100px;
  top: 25px;
  background-color: #d7d9e5;
  height: 80px;
}
.box-color-2 {
  position: relative;
  left: -450px;
  top: 230px;
  background-color: #d7d9e5;
  height: 80px;
}
.box-color-3 {
  position: relative;
  left: -45px;
  top: 300px;
  background-color: #e7efff;
  height: 80px;
}
.interet-box-color-0 {
  position: relative;
  left: 175px;
  top: 10px;
  background-color: #e7efff;
  height: 80px;
}
.interet-box-color-1 {
  position: relative;
  left: 120px;
  top: 60px;
  background-color: #d7d9e5;
  height: 80px;
}
.interet-box-color-2 {
  position: relative;
  left: 52px;
  top: 5px;
  background-color: #e7efff;
  height: 80px;
}

.skills-box-color-0 {
  position: relative;
  left: 170px;
  bottom: 15px;
  background-color: #d7d9e5;
  height: 80px;
}
.skills-box-color-1 {
  position: relative;
  left: 100px;
  top: 80px;
  background-color: #e7efff;
  height: 80px;
}
.skills-box-color-2 {
  position: relative;
  left: 15px;
  bottom: 15px;
  background-color: #d7d9e5;
  height: 80px;
}
.skills-box-color-3 {
  position: relative;
  left: 50px;
  bottom: 15px;
  background-color: #e7efff;
  height: 80px;
}
.skills-box-color-4 {
  position: relative;
  top: 85px;
  left: 320px;
  background-color: #d7d9e5;
  height: 80px;
}
.navbar-icons button {
  border: none;
  border-radius: 50%; /* Rend les boutons sous forme de cercle */
  width: 40px; /* Ajustez la taille selon vos besoins */
  height: 40px;
  font-size: 18px;
  background-color: #cccccc65;
  color: #fff;
  cursor: pointer;
  margin-bottom: 4px;
}
.bold-arrow {
  font-weight: bolder !important;
  font-size: large;
}
.upload-container {
  position: relative;
  border: 2px dashed #ccc;
  width: 80%;
  height: 90px;
  top: -2px;
  padding: 20px;
  padding-bottom: 20px;
  left: 35px;
}
</style>
