<template>
    <RouterView></RouterView>
    
      <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
  
          <meta name="description" content="">
          <meta name="author" content="TemplateMo">
  
          <title>Portfolio 3</title>
  
          <!-- CSS FILES -->
          <link rel="preconnect" href="https://fonts.googleapis.com">
          
          <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
          
          <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
  
          <link href="/Exemple3/css/bootstrap.min.css" rel="stylesheet">
  
          <link href="/Exemple3/css/bootstrap-icons.css" rel="stylesheet">
  
          <link href="/Exemple3/css/magnific-popup.css" rel="stylesheet">
  
          <link href="/Exemple3/css/templatemo-first-portfolio-style.css" rel="stylesheet">
  
          
  <!--
  
  TemplateMo 578 First Portfolio
  
  https://templatemo.com/tm-578-first-portfolio
  
  -->
      </head>
      
      <body>
         
          
  
  
          <main>
              
              <nav class="navbar navbar-expand-lg " >
              <div class="container ">
  
                
  
                  <!--<a href="index.html" class="navbar-brand mx-auto mx-lg-0">First</a>-->
  
                  
  
                  <div class="collapse navbar-collapse " id="navbarNav" >
                      <ul class="navbar-nav ms-lg-5 ">
                          <div class="navbar-icons">
  
                          <!--<button class="scroll-top-button" style="display: flex; justify-content: center; align-items: center;position: relative;top: 10px;left: -85px;">
    <router-link :to="'/GenePortfo2/' + this.etudiant.id" >
    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M19 12H6M12 5l-7 7 7 7"></path>
    </svg>
  </router-link>
  </button>-->
  <!--<button class="copy-button" style="display: flex; justify-content: center; align-items: center; position: relative; left: 1170px; bottom: 35px;">
                        <i class="fas fa-copy"></i>
                         </button>-->
  
      <!--<button class="download-button" style="display: flex; justify-content: center; align-items: center;position: relative;left: 1220px;bottom: 79px"><i class="fas fa-download"></i> </button>-->
          </div>                
          <li class="nav-item">
                              <a class="nav-link click-scroll" href="#section_1">Home</a>
                          </li>
  
                          <li class="nav-item">
                              <a class="nav-link click-scroll" href="#section_2">A propos</a>
                          </li>
  
                          <li class="nav-item">
                              <a class="nav-link click-scroll" href="#section_3">Formations</a>
                          </li>
  
                          <li class="nav-item">
                              <a class="nav-link click-scroll" href="#section_4">Compétences</a>
                          </li>
  
                          <li class="nav-item">
                              <a class="nav-link click-scroll" href="#section_5">Experiences</a>
                          </li>
  
                          <li class="nav-item">
                              <a class="nav-link click-scroll" href="#section_6">Projets</a>
                          </li>
  
                          <li class="nav-item">
                              <a class="nav-link click-scroll" href="#section_7">Autres</a>
                          </li>
      
                         
   
                      </ul>
  
                      <!--<div class="d-lg-flex align-items-center d-none ms-auto">
                          <i class="navbar-icon bi-telephone-plus me-3"></i>
                          <a class="custom-btn btn" href="#section_5">
                              120-240-9600
                          </a>
                      </div>-->
                  </div>
  
              </div>
          </nav>
              
  
  
              <section class="hero d-flex justify-content-center align-items-center" id="section_1">
                 
                  <div class="container">
                      <div class="row">
  
                          <div class="col-lg-7 col-12">
                              <div class="hero-text">
                                  <div class="hero-title-wrap d-flex align-items-center mb-4">
                                      
  
                                      <h1 class="hero-title ms-3 mb-0">Bonjour!</h1>
                                  </div>
  
                                  <h2 class="mb-4" style="font-weight: 600;font-size:56px;">Je suis  {{ prenom  }} &nbsp; {{ nom }}</h2>
                                  <p class="mb-4"><a class="custom-btn btn custom-link" href="#section_2">Bienvenu à mon portfolio</a></p>
                              </div>
                          </div>
  
                          <div class="col-lg-5 col-12 position-relative">
                          <div class="hero-image-wrap">
                              <img :src="imageUrl" alt=""  style="width: 390px;height: 390px;border-radius: 200px;position: relative;left:9px;top: -5px;">
                          </div>
                          </div>
  
                      </div>
                  </div>
  
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="#535da1" fill-opacity="1" d="M0,160L24,160C48,160,96,160,144,138.7C192,117,240,75,288,64C336,53,384,75,432,106.7C480,139,528,181,576,208C624,235,672,245,720,240C768,235,816,213,864,186.7C912,160,960,128,1008,133.3C1056,139,1104,181,1152,202.7C1200,224,1248,224,1296,197.3C1344,171,1392,117,1416,90.7L1440,64L1440,0L1416,0C1392,0,1344,0,1296,0C1248,0,1200,0,1152,0C1104,0,1056,0,1008,0C960,0,912,0,864,0C816,0,768,0,720,0C672,0,624,0,576,0C528,0,480,0,432,0C384,0,336,0,288,0C240,0,192,0,144,0C96,0,48,0,24,0L0,0Z"></path></svg>
              </section>
  
  
              <section class="about section-padding" id="section_2">
                  <div class="container">
                      <div class="row">
  
                          <div class="col-lg-6 col-12">
                              <img src="/Exemple3/images/profil.png" class="about-image img-fluid mouvement" alt="" style="width:400px;position: relative;left: 95px;">
                          </div>
  
                          <div class="col-lg-6 col-12 mt-5 mt-lg-0">
                              <div class="about-thumb">
  
                                  <div class="section-title-wrap d-flex justify-content-end align-items-center mb-4">
                                      <h2 class="text-white me-4 mb-0" style="position: relative;right: 190px;">A propos de moi</h2>
  
                                  </div>
  
                                  <p> {{ profil }}</p>
  
                              </div>
                          </div>
  
                      </div>
                  </div>
              </section>
  
              <section class="featured section-padding">
                  <div class="container">
                      <div class="row">
  
                          <div class="col-lg-6 col-12" style="position: relative;left: 350px;">
      <div class="profile-thumb">
          <div class="profile-title">
              <h4 class="mb-0">Information Personnelle</h4>
          </div>
          <div class="profile-body">
              <p v-if="telephone">
                  <span class="profile-small-title">Téléphone</span> 
                  <span>{{telephone}}</span>
              </p>
              <p v-if="email">
                  <span class="profile-small-title">Email</span> 
                  <span><a :href="'mailto:' + email">{{ email }}</a></span>
              </p>
              <p v-if="linkedin">
                  <span class="profile-small-title">Linkedin</span> 
                  <span><a :href="linkedin">{{linkedin}}</a></span>
              </p>
              <p v-if="github">
                  <span class="profile-small-title">Github</span> 
                  <span><a :href="github">{{github}}</a></span>
              </p>
              <p v-if="skype">
                  <span class="profile-small-title">Skype</span> 
                  <span><a :href="'skype:' + skype">{{skype}}</a></span>
              </p>
          </div>
      </div>
  </div>
  
  
                         <!-- <div class="col-lg-6 col-12 mt-5 mt-lg-0">
                              <div class="about-thumb">
                                  <div class="row">
                                      <div class="col-lg-6 col-6 featured-border-bottom py-2">
                                          <strong class="featured-numbers">20+</strong>
  
                                          <p class="featured-text">Years of Experiences</p>
                                      </div>
  
                                      <div class="col-lg-6 col-6 featured-border-start featured-border-bottom ps-5 py-2">
                                          <strong class="featured-numbers">245</strong>
  
                                          <p class="featured-text">Happy Customers</p>
                                      </div>
  
                                      <div class="col-lg-6 col-6 pt-4">
                                          <strong class="featured-numbers">640</strong>
  
                                          <p class="featured-text">Project Finished</p>
                                      </div>
  
                                      <div class="col-lg-6 col-6 featured-border-start ps-5 pt-4">
                                          <strong class="featured-numbers">72+</strong>
  
                                          <p class="featured-text">Digital Awards</p>
                                      </div>
                                  </div>
                              </div>
                          </div>-->
  
                      </div>
                  </div>
              </section>
  
  
              <!--<section class="clients section-padding">
                  <div class="container">
                      <div class="row align-items-center">
  
                          <div class="col-lg-12 col-12">
                              <h3 class="text-center mb-5">Companies I've had worked</h3>
                          </div>
  
                          <div class="col-lg-2 col-4 ms-auto clients-item-height">
                              <img src="Exemple3/images/clients/cachet.svg" class="clients-image img-fluid" alt="">
                          </div>
  
                          <div class="col-lg-2 col-4 clients-item-height">
                              <img src="Exemple3/images/clients/guitar-center.svg" class="clients-image img-fluid" alt="">
                          </div>
  
                          <div class="col-lg-2 col-4 clients-item-height">
                              <img src="Exemple3/images/clients/tokico.svg" class="clients-image img-fluid" alt="">
                          </div>
  
                          <div class="col-lg-2 col-4 clients-item-height">
                              <img src="Exemple3/images/clients/shopify.svg" class="clients-image img-fluid" alt="">
                          </div>
  
                          <div class="col-lg-2 col-4 me-auto clients-item-height">
                              <img src="Exemple3/images/clients/profil-rejser.svg" class="clients-image img-fluid" alt="">
                          </div>
  
                      </div>
                  </div>
              </section>-->
  
              <section class="services section-padding" id="section_3">
      <div class="container">
          <div class="row">
              <div class="col-lg-10 col-12 mx-auto">
                  <div class="section-title-wrap d-flex justify-content-center align-items-center mb-5">
                      <h2 class="text-white ms-4 mb-0">Formations</h2>
                  </div>
                  <div class="row pt-lg-5">
                      <div class="col-lg-6 col-12" v-for="formation in formations" :key="formation.nomformation">
                          <div class="services-thumb">
                              <div class="d-flex flex-wrap align-items-center border-bottom mb-4 pb-3">
                                  <h3 class="mb-0">{{ formation.nomformation }}</h3>
                                  <div class="services-price-wrap ms-auto">
                                      <p class="services-price-text mb-0">{{ formation.debutformation }} - {{ formation.finformation }}</p>
                                      <div class="services-price-overlay"></div>
                                  </div>
                              </div>
                              <p>{{ formation.etablissement }}</p>
                              <div class="services-icon-wrap d-flex justify-content-center align-items-center">
                                  <i class="fas fa-book-open services-icon"></i>
                              </div>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </section>
  
  <section class="services section-padding" id="section_4">
    <div class="container">
      <div class="row">
        <div class="col-lg-10 col-12 mx-auto">
  
          <div class="section-title-wrap d-flex justify-content-center align-items-center mb-5">
            <h2 class="text-white ms-4 mb-0">Compétences</h2>
          </div>
  
          <div class="col-lg-6 col-12 mt-5 mt-lg-0">
            <form action="#" method="get" class="custom-form contact-form" role="form" >
              <div class="row">
                <div class="col-lg-3 col-md-6 col-6" v-for="(competence, index) in competences" :key="index">
                  <div class="form-check form-check-inline" >
                      <input :name="competence.nom" type="checkbox" class="form-check-input" :id="'inlineCheckbox' + index" :value="competence.id" style="margin-right: 150px;">
                    <label class="form-check-label" :for="'inlineCheckbox' + index  " >
                      <span class="form-check-label-text">{{ competence.competence }}</span>
                    </label>
                  </div>
                </div>
              </div>
            </form>
          </div>
  
        </div>
      </div>
    </div>
  </section>
  
  <section class="services section-padding" id="section_5">
      <div class="container">
          <div class="row">
              <div class="col-lg-10 col-12 mx-auto">
                  <div class="section-title-wrap d-flex justify-content-center align-items-center mb-5">
                      <h2 class="text-white ms-4 mb-0">Experiences</h2>
                  </div>
                  <div class="row pt-lg-5">
                      <div class="col-lg-6 col-12" v-for="experience in experiences" :key="experience.id">
                          <div class="services-thumb">
                              <div class="d-flex flex-wrap align-items-center border-bottom mb-4 pb-3">
                                  <h3 class="mb-0">{{ experience.titre }}</h3>
                                  <div class="services-price-wrap ms-auto">
                                      <p class="services-price-text mb-0">{{ experience.debutexperience }} - {{ experience.finexperience }}</p>
                                      <div class="services-price-overlay"></div>
                                  </div>
                              </div>
                              <p>{{ experience.entreprise }}</p>
                              <p>{{ experience.description }}</p>
  
                              <div class="services-icon-wrap d-flex justify-content-center align-items-center" style="height: 30%;">
                                  <i class="bi bi-lightbulb services-icon"></i>
  
                              </div>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </section>
  
           <section class="projects section-padding" id="section_6">
                  <div class="container">
                      <div class="row"> 
                          <div class="col-lg-10 col-12 mx-auto">
                  <div class="section-title-wrap d-flex justify-content-center align-items-center mb-5">
                      <h2 class="text-white ms-4 mb-0">Projets</h2>
                  </div>
  </div>
                          <div class="clearfix"></div>
  
                          <div class="col-lg-4 col-md-6 col-12" v-for="(projet, index) in projets" :key="index">
                              <div class="projects-thumb">
                                  <div class="projects-info">
                                      <h6 class="projects-title" style="font-weight: 400;"> {{projet.titreprojet}}</h6>
  
                                      <h3 class="projects-title">{{ projet.descriptionprojet }}</h3>
                                  </div>
  
                                  <a href="" class="popup-image">
                                      <img src="/Exemple3/images/projects/projet.png" class="projects-image img-fluid" alt="" >
                                  </a>
                              </div>
                          </div>
  
                      
                      </div>
                  </div>
              </section>
              <section class="contact section-padding" id="section_7">
                      <div class="container">
                          <div class="row">
  
                           
  
                              <div class="clearfix"></div>
  
                              <div class="col-lg-3 col-md-6 col-12 pe-lg-0" v-if="softskills.length > 0">
      <div class="contact-info contact-info-border-start d-flex flex-column">
          <h3 class="site-footer-title d-block mb-3" style="font-size: 20px;">Soft Skills</h3>
  
          <ul class="footer-menu" v-for="(skills, index) in softskills" :key="index">
              <li class="footer-menu-item"><a class="footer-menu-link">{{skills.titreskills}}</a></li>
          </ul>
      </div>
  </div>
  
  
  <div class="col-lg-3 col-md-6 col-12 pe-lg-0" v-if="langues.length > 0">
      <div class="contact-info contact-info-border-start d-flex flex-column">
          <h3 class="site-footer-title d-block mb-3" style="font-size: 20px;">Langues</h3>
  
          <ul class="footer-menu" v-for="(langue, index) in langues" :key="index">
              <li class="footer-menu-item"><a class="footer-menu-link">{{langue.langue}} : {{langue.niveau}}</a></li>
          </ul>
      </div>
  </div>
  
  <div class="col-lg-3 col-md-6 col-12 pe-lg-0" v-if="interets.length > 0">
      <div class="contact-info contact-info-border-start d-flex flex-column">
          <h3 class="site-footer-title d-block mb-3" style="font-size: 20px;">Centre d'intérêt</h3>
  
          <ul class="footer-menu" v-for="(interet, index) in interets" :key="index">
              <li class="footer-menu-item"><a class="footer-menu-link">{{interet.titreInteret}}</a></li>
          </ul>
      </div>
  </div>
  
                              <div class="col-lg-3 col-md-6 col-12 pe-lg-0" v-if="clubs.length > 0">
      <div class="contact-info contact-info-border-start d-flex flex-column">
          <h3 class="site-footer-title d-block mb-3" style="font-size: 20px;">Club</h3>
  
          <ul class="footer-menu" v-for="club in clubs" :key="club.id">
              <li class="footer-menu-item"><a class="footer-menu-link">{{club.nomclub}} : {{club.role}}</a></li>
          </ul>
      </div>
  </div>
  
                              <div class=" col-lg-3 col-md-6 col-12 pe-lg-0" v-if="references.length > 0">
      <div class="contact-info contact-info-border-start d-flex flex-column">
          <h3 class="site-footer-title d-block mb-3" style="font-size: 20px;">Référence</h3>
  
          <ul class="footer-menu" v-for="reference in references" :key="reference.id">
              <li class="footer-menu-item"><a class="footer-menu-link">{{reference.titreref}}</a></li><br>
              <li class="footer-menu-item"><a class="footer-menu-link">{{reference.poste}}</a></li><br>
              <li class="footer-menu-item"><a class="footer-menu-link">{{reference.emailref}}</a></li>
          </ul>
      </div>
  </div>
  
  
  
                           
                          </div>
                      </div>
              </section>
  
          </main>
  
          
  
  
  
      </body>
  
  </template>
  <script>
    import axios from 'axios';
      export default {
        name: 'PortfolioTemplate2',
        data() {
        return {
          imageUrl: '', 
          nom: '',
          prenom: '',
          profil:'',
          email:'',
          telephone:'',
          linkedin:'',
          github:'',
          skype:'',
          formations: [],
          competences: [],
          experiences: [],
          projets: [],
          langues: [],
          interets: [],
          softskills: [],
          references: [],
          clubs: [],
          isNavbarVisible: false,
          etudiant: {
            id: null
        },
  
  
  
  
  
  
         
        };
      },
        mounted() {
          'use strict';
          this.fetchImageUrl();
          this.recupererDonnees();
    
    
    
  
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
            fetchImageUrl() {
    const userId = localStorage.getItem("user_id");
    if (!userId) {
        alert("Vous devez être connecté.");
        return;
    }
    
    axios.get(`http://127.0.0.1:8000/get-last-image/${userId}/`, { responseType: 'blob' })
        .then(response => {
            const imageUrl = URL.createObjectURL(response.data);
            this.imageUrl = imageUrl;
        })
        .catch(error => {
            console.error('Erreur lors de la récupération de l\'URL de l\'image:', error);
        });
},
recupererDonnees() {
      const userId = localStorage.getItem("user_id");
    if (!userId) {
        alert("Vous devez être connecté.");
        return;
    }
    axios.get(`http://127.0.0.1:8000/get-last-info/${userId}`)
        .then(response => {
          this.nom = response.data.nom || '';
          this.prenom = response.data.prenom || '';
          this.profil = response.data.profil || '';
          this.github = response.data.github || '';
          this.skype = response.data.skype || '';
          this.email = response.data.email || '';
          this.linkedin = response.data.linkedin || '';
          this.telephone = response.data.telephone || '';

          this.formations = Array.isArray(response.data.formations) ? response.data.formations : [];
          this.experiences = Array.isArray(response.data.experiences) ? response.data.experiences : [];
          this.references = Array.isArray(response.data.references) ? response.data.references : [];
          this.langues = Array.isArray(response.data.langues) ? response.data.langues : [];
          this.interets = Array.isArray(response.data.interets) ? response.data.interets : [];
          this.competences = Array.isArray(response.data.competences) ? response.data.competences : [];
          this.softskills = Array.isArray(response.data.softskills) ? response.data.softskills : [];
          this.projets = Array.isArray(response.data.projets) ? response.data.projets : [];
          this.clubs = Array.isArray(response.data.clubs) ? response.data.clubs : [];

        })
        .catch(error => {
          console.error('Erreur lors de la récupération des données:', error);
        });
    },
      },
      }
    </script>
  
  <style >
  
  .mouvement {
    animation: bougerImage 2s infinite;
  }
  
  @keyframes bougerImage {
    0% {
      transform: translateX(0);
    }
    50% {
      transform: translateX(20px);
    }
    100% {
      transform: translateX(0);
    }
  }
  .navbar-icons button {
    border: none;
    border-radius: 50%; 
    width : 40px; 
    height : 40px; 
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
  </style>
  