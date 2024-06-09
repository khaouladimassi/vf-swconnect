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
          <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

  
          
  <!--
  
  TemplateMo 578 First Portfolio
  
  https://templatemo.com/tm-578-first-portfolio
  
  -->
      </head>
      
      <body style="overflow-x: hidden;">
         
          
  
  
          <main>
              
              <nav class="navbar navbar-expand-lg " >
              <div class="container ">
  
                
  
                  <!--<a href="index.html" class="navbar-brand mx-auto mx-lg-0">First</a>-->
  
                  
  
                  <div class="collapse navbar-collapse " id="navbarNav" >
                      <ul class="navbar-nav ms-lg-5 ">
                          <div class="navbar-icons">
  
                         <!-- <button class="scroll-top-button" style="display: flex; justify-content: center; align-items: center;position: relative;top: 10px;left: -85px;">
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
  
                                  <p> 
                                    <textarea 
                                    v-model="profil" 
                                    placeholder="Écrivez plus sur vous ..." 
                                    style="border: none; outline: none; background: none; width: calc(100% + 17px); font-size: 18px; font-weight: 500; color: var(--p-color);; resize: none;position: relative;left: -17px;height: 300px;overflow: hidden;"   
                                    maxlength="2000"
                                   >
                                </textarea>
                                </p>
  
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
                                  <h3 class="mb-0" >
                                    <input type="text" v-model="formation.nomformation" placeholder="Nom" style="border: none; outline: none; background: none; width: 950px;color: var(--dark-color);font-size: 29px;font-weight: bold;"/>                            
                                </h3>
                                  <div class="services-price-wrap ms-auto">
                                      <p class="services-price-text mb-0"><input type="text" v-model="formation.debutformation" placeholder="date de début" style="border: none; outline: none; background: none; width: 40px;color: white;"/> ~ <input type="text" v-model="formation.finformation" placeholder="date de fin" style="border: none; outline: none; background: none; width: 40px;color:white;"/></p>
                                      <div class="services-price-overlay"></div>
                                  </div>
                              </div>
                              <p><input type="text" v-model="formation.etablissement" placeholder="Etablissement" style="border: none; outline: none; background: none; width: 950px;color: #05264E;font-size: 18px;"/></p>
                              <div class="services-icon-wrap d-flex justify-content-center align-items-center">
                                  <i class="fas fa-book-open services-icon"></i>
                              </div>
                          </div>
                      </div>
                      <div class="col-lg-6 col-12" >
                          <div class="services-thumb">
                              <div class="d-flex flex-wrap align-items-center border-bottom mb-4 pb-3">
                                  <h3 class="mb-0" >
                                    <input type="text" v-model="nomformation" placeholder="Nom" style="border: none; outline: none; background: none; width: 950px;color: var(--dark-color);font-size: 29px;font-weight: bold;"/>                            
                                </h3>
                                  <div class="services-price-wrap ms-auto">
                                      <p class="services-price-text mb-0"><input type="text" v-model="debutformation" placeholder="Début" style="border: none; outline: none; background: none; width: 40px;color: white;"/> ~ <input type="text" v-model="finformation" placeholder="Fin" style="border: none; outline: none; background: none; width: 40px;color:white;"/></p>
                                      <div class="services-price-overlay"></div>
                                  </div>
                              </div>
                              <p><input type="text" v-model="etablissement" placeholder="Etablissement" style="border: none; outline: none; background: none; width: 950px;color: #05264E;font-size: 18px;"/></p>
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
                    <div class="form-check form-check-inline">
<input :name="competence.nom" type="checkbox" class="form-check-input" :id="'inlineCheckbox' + index" :value="competence.id" style="margin-right: 150px;">
<label class="form-check-label" :for="'inlineCheckbox' + index">
<span class="form-check-label-text">
<textarea 
v-model="competence.competence" 
placeholder="Compétences" 
style="border: none; outline: none; background: none; color: var(--p-color); font-size: 18px; resize: none;overflow: hidden;position: relative;left: 10px; width: 105px;"
maxlength="25"
></textarea> 
</span>
</label>
</div>
                </div>

                <div class="col-lg-3 col-md-6 col-6">
                    <div class="form-check form-check-inline">
<input :name="competence.nom" type="checkbox" class="form-check-input"  :value="competence.id" style="margin-right: 150px;">
<label class="form-check-label" >
<span class="form-check-label-text">
<textarea 
v-model="competence" 
placeholder="+ Compétence" 
style="border: none; outline: none; background: none; color: var(--p-color); font-size: 18px; resize: none;overflow: hidden;position: relative;left: 10px; width: 105px;"
maxlength="25"
></textarea> 
</span>
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
                                  <h3 class="mb-0">
                                    <textarea 
          v-model="experience.titre" 
          placeholder="Titre" 
          style="border: none; outline: none; background: none; color: var(--dark-color); font-size: 29px; resize: none;position: relative;top: 15px;font-weight: bold;"
          maxlength="120"
          
          
      ></textarea> 
                                  </h3>
                                  <div class="services-price-wrap ms-auto">
                                      <p class="services-price-text mb-0"><input type="text" v-model="experience.debutexperience" placeholder="Début" style="border: none; outline: none; background: none; width: 40px;color: white;"/> ~ <input type="text" v-model="experience.finexperience" placeholder="Fin" style="border: none; outline: none; background: none; width: 40px;color:white;"/></p>
                                      <div class="services-price-overlay"></div>
                                  </div>
                              </div>
                              <p> <textarea 
          v-model="experience.entreprise" 
          placeholder="Entreprise" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size: 18px; resize: none;"
          maxlength="120"
          
          
      ></textarea> </p>
                              <p> <textarea 
          v-model="experience.description" 
          placeholder="Description" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size: 18px; resize: none;overflow: hidden;width: 450px;height: 400px;"
          maxlength="950"
          
          
      ></textarea> </p>
  
                              <div class="services-icon-wrap d-flex justify-content-center align-items-center" style="height: 30%;">
                                  <i class="bi bi-lightbulb services-icon"></i>
  
                              </div>
                          </div>
                      </div>
                      <div class="col-lg-6 col-12">
                          <div class="services-thumb">
                              <div class="d-flex flex-wrap align-items-center border-bottom mb-4 pb-3">
                                  <h3 class="mb-0">
                                    <textarea 
          v-model="titre" 
          placeholder="Titre" 
          style="border: none; outline: none; background: none; color: var(--dark-color); font-size: 29px; resize: none;position: relative;top: 15px;font-weight: bold;"
          maxlength="120"
          
          
      ></textarea> 
                                  </h3>
                                  <div class="services-price-wrap ms-auto">
                                      <p class="services-price-text mb-0"><input type="text" v-model="debutexperience" placeholder="Début" style="border: none; outline: none; background: none; width: 40px;color: white;"/> ~ <input type="text" v-model="finexperience" placeholder="Fin" style="border: none; outline: none; background: none; width: 40px;color:white;"/></p>
                                      <div class="services-price-overlay"></div>
                                  </div>
                              </div>
                              <p> <textarea 
          v-model="entreprise" 
          placeholder="Entreprise" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size: 18px; resize: none;"
          maxlength="120"
          
          
      ></textarea> </p>
                              <p> <textarea 
          v-model="description" 
          placeholder="Description" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size: 18px; resize: none;overflow: hidden;width: 450px;height: 400px;"
          maxlength="950"
          
          
      ></textarea> </p>
  
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
  
           <section class="projects section-padding" id="section_6" >
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
                                      <h6 class="projects-title" style="font-weight: 400;">   
                                         <textarea 
          v-model="projet.titreprojet" 
          placeholder="Titre_Projet" 
          style="border: none; outline: none; background: none; color: var(--dark-color); font-size: 23px; resize: none;font-weight: 650;overflow: hidden;"
          maxlength="100"
          
          
      ></textarea></h6>
  
                                      <h3 class="projects-title"><textarea 
          v-model="projet.descriptionprojet" 
          placeholder="Description" 
          style="border: none; outline: none; background: none; color: var(--dark-color); font-size: 23px; resize: none;overflow: hidden;width: 350px;"
          maxlength="370"
          
          
      ></textarea></h3>
                                  </div>
  
                                  <a href="" class="popup-image">
                                      <img src="/Exemple3/images/projects/projet.png" class="projects-image img-fluid" alt="" >
                                  </a>
                              </div>
                          </div>
  
                      
                      </div>
                      <div class="projects-thumb"  v-show="!showProjet" style="width: 420px;height: 420px;position: relative;left: 500px;top: -50px;">
    <div class="work-box" style="position: relative;height: 450px; width:500px;">
        <div class="work-content" >
            <h2 class="w-title" style="font-size:30px;">Ajouter un nouveau projet</h2>
            <form  >
                <div class="form-group">
                    <label for="titreProjet">Titre du projet:</label>
                    <input type="text" class="form-control" id="titreProjet" v-model="nomnewprojet" name="nomnewprojet" style="background-color: transparent;width: 300px;position: relative;left: 20px;">
                </div>
                <div class="form-group">
                    <label for="descriptionProjet">Description du projet:</label>
                    <textarea class="form-control" id="descriptionProjet" v-model="descriptionnewprojet" name="descriptionnewprojet" style="background-color: transparent;width: 300px;position: relative;left: 20px;"></textarea>
                </div>
         
              
  <button type="button" class="btn " style="position: relative;left: 300px;background-color:var(--secondary-color);;width: 40px;height:40px;top: 30px;" @click="basculerAffichage()"><i class="fas fa-plus fa-2x" style="color: white;position: relative;left: -10px;top: -5px;"></i></button>
            </form>
        </div>
    </div>
</div>
<div class="col-lg-4 col-md-6 col-12" v-show="showProjet" style="position: relative;left: 470px;top: -630px;">
                              <div class="projects-thumb">
                                  <div class="projects-info">
                                      <h6 class="projects-title" style="font-weight: 400;">   
                                         <textarea 
          v-model="titreprojet" 
          placeholder="Titre_Projet" 
          style="border: none; outline: none; background: none; color: var(--dark-color); font-size: 23px; resize: none;font-weight: 650;overflow: hidden;"
          maxlength="100"
          
          
      ></textarea></h6>
  
                                      <h3 class="projects-title"><textarea 
          v-model="descriptionprojet" 
          placeholder="Description" 
          style="border: none; outline: none; background: none; color: var(--dark-color); font-size: 23px; resize: none;overflow: hidden;width: 350px;"
          maxlength="370"
          
          
      ></textarea></h3>
                                  </div>
  
                                  <a href="" class="popup-image">
                                      <img src="/Exemple3/images/projects/projet.png" class="projects-image img-fluid" alt="" >
                                  </a>
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
              <li class="footer-menu-item"><a class="footer-menu-link">
                <input 
          v-model="skills.titreskills" 
          placeholder="Soft-Skills" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 19px;"
          
          
      />

              </a></li>
          </ul>
          <ul class="footer-menu">
              <li class="footer-menu-item"><a class="footer-menu-link">
                <input 
          v-model="titreskills" 
          placeholder="+ Soft-Skills" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 19px;"
          
          
      />

              </a></li>
          </ul>
      </div>
  </div>
  
  
  <div class="col-lg-3 col-md-6 col-12 pe-lg-0" v-if="langues.length > 0">
      <div class="contact-info contact-info-border-start d-flex flex-column">
          <h3 class="site-footer-title d-block mb-3" style="font-size: 20px;">Langues</h3>
  
          <ul class="footer-menu" v-for="(langue, index) in langues" :key="index">
              <li class="footer-menu-item"><a class="footer-menu-link">
                <input 
          v-model="langue.langue" 
          placeholder="langue" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 19px;"
        
      /> <input 
          v-model="langue.niveau" 
          placeholder="niveau" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 20px;"
          
          
      /></a></li>
          </ul>
          <ul class="footer-menu" >
              <li class="footer-menu-item"><a class="footer-menu-link">
                <input 
          v-model="langue" 
          placeholder="+ langue" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 19px;"
        
      /> <input 
          v-model="niveau" 
          placeholder="+ niveau" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 20px;"
          
          
      /></a></li>
          </ul>
      </div>
  </div>
  
  <div class="col-lg-3 col-md-6 col-12 pe-lg-0" v-if="interets.length > 0">
      <div class="contact-info contact-info-border-start d-flex flex-column">
          <h3 class="site-footer-title d-block mb-3" style="font-size: 20px;">Centre d'intérêt</h3>
  
          <ul class="footer-menu" v-for="(interet, index) in interets" :key="index">
              <li class="footer-menu-item"><a class="footer-menu-link">
                <input 
          v-model="interet.titreInteret" 
          placeholder="Interet" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 19px;"
          
          
      />


              </a></li>
          </ul>
          <ul class="footer-menu" >
              <li class="footer-menu-item"><a class="footer-menu-link">
                <input 
          v-model="titreInteret" 
          placeholder="+ Interet" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 19px;"
          
          
      />


              </a></li>
          </ul>
      </div>
  </div>
  
                              <div class="col-lg-3 col-md-6 col-12 pe-lg-0" v-if="clubs.length > 0">
      <div class="contact-info contact-info-border-start d-flex flex-column">
          <h3 class="site-footer-title d-block mb-3" style="font-size: 20px;">Club</h3>
  
          <ul class="footer-menu" v-for="club in clubs" :key="club.id">
              <li class="footer-menu-item"><a class="footer-menu-link">
                <input 
          v-model="club.nomclub" 
          placeholder="club" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 19px;"
      />  <input 
          v-model="club.role" 
          placeholder="role" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 19px;"
          
          
      /></a></li>
          </ul>
          <ul class="footer-menu" >
              <li class="footer-menu-item"><a class="footer-menu-link">
                <input 
          v-model="nomclub" 
          placeholder="+ club" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 19px;"
      />  <input 
          v-model="role" 
          placeholder="+ role" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 19px;"
          
          
      /></a></li>
          </ul>
      </div>
  </div>
  
                              <div class=" col-lg-3 col-md-6 col-12 pe-lg-0" v-if="references.length > 0">
      <div class="contact-info contact-info-border-start d-flex flex-column">
          <h3 class="site-footer-title d-block mb-3" style="font-size: 20px;">Référence</h3>
  
          <ul class="footer-menu" v-for="reference in references" :key="reference.id">
              <li class="footer-menu-item"><a class="footer-menu-link">
                <input 
          v-model="reference.titreref" 
          placeholder="Titre" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 19px;"
          
          
      />
              </a></li><br>
              <li class="footer-menu-item"><a class="footer-menu-link">
                <input 
          v-model="reference.poste" 
          placeholder="poste" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 19px;"
          
          
      />
              </a></li><br>
              <li class="footer-menu-item"><a class="footer-menu-link">
                <input 
          v-model="reference.emailref" 
          placeholder="email" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 19px;"
          
          
      />
              </a></li>
          </ul>

          <ul class="footer-menu" >
              <li class="footer-menu-item"><a class="footer-menu-link">
                <input 
          v-model="titreref" 
          placeholder="+ reference" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 19px;"
          
          
      />
              </a></li><br>
              <li class="footer-menu-item"><a class="footer-menu-link">
                <input 
          v-model="poste" 
          placeholder="poste" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 19px;"
          
          
      />
              </a></li><br>
              <li class="footer-menu-item"><a class="footer-menu-link">
                <input 
          v-model="eamil" 
          placeholder="email" 
          style="border: none; outline: none; background: none; color: var(--p-color); font-size:17px; resize: none;font-weight:400;height: 19px;"
          
          
      />
              </a></li>
          </ul>
      </div>
  </div>
  
  
  
                           
                          </div>
                      </div>
              </section>
  
          </main>
          <div >
      
      <button class="btn" style="background-color: var(--secondary-color); ;position: relative;top: -40px;left: 1180px;height: 50px;width: 170px;margin-bottom: 150px;" @click.prevent="Enregistrerdonnestemplate" ><span style="color: white;font-weight: 800;font-size: 20px;text-align: center;">Enregistrer </span></button>
    </div>
          
  
  
  
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
        nomformation:'',
        debutformation:'',
        finformation:'',
        etablissement:'',
        categorie:'',
        competence:'',
        debutexperience:'',
        finexperience:'',
        nomclub:'',
        role:'',
        titreref:'',
        poste:'',
        langue:'',
        niveau:'',
        titreskills:'',
        titreInteret:'',
        titre:'',
        entreprise:'',
        description:'',
        emailref:'',
        showProjet: false,
        nomnewprojet:'',
        descriptionnewprojet:'',
        uploadedFileName: '',
        fichier_zip: null,
  
  
  
  
  
  
         
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
    basculerAffichage() {
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
this.formations.forEach(formation => {
  formationsData.push({
    debutformation: formation.debutformation,
    finformation: formation.finformation,
    nomformation: formation.nomformation,
    etablissement: formation.etablissement
  });
});

// Vérifiez si les données de la nouvelle formation sont remplies et ajoutez-les si oui
if (this.debutformation || this.finformation || this.nomformation || this.etablissement) {
  formationsData.push({
    debutformation: this.debutformation,
    finformation: this.finformation,
    nomformation: this.nomformation,
    etablissement: this.etablissement
  });
}

// Créez un tableau pour stocker les données des expériences professionnelles
const experiencesData = [];

// Ajoutez les données des expériences professionnelles existantes
this.experiences.forEach(experience => {
  experiencesData.push({
    debutexperience: experience.debutexperience,
    finexperience: experience.finexperience,
    titre: experience.titre,
    entreprise: experience.entreprise,
    description: experience.description
  });
});

// Vérifiez si les données de la nouvelle expérience professionnelle sont remplies et ajoutez-les si oui
if (this.debutexperience || this.finexperience || this.titreexperience || this.entreprisexperience || this.descriptionexperience) {
  experiencesData.push({
    debutexperience: this.debutexperience,
    finexperience: this.finexperience,
    titre: this.titreexperience,
    entreprise: this.entreprisexperience,
    description: this.descriptionexperience
  });
}


const competencesData = [];

  // Ajoutez les données des competences existantes
  this.competences.forEach(competence => {
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

this.softskills.forEach(skills => {
  softskillsData.push({
    titreskills: skills.titreskills,
  });
});

if (this.titreskills ) {
  softskillsData.push({
      titreskills: this.titreskills,

  });
}

const centreinteretsData = [];
this.interets.forEach(interet => {
  centreinteretsData.push({
    titreInteret: interet.titreInteret,
  });
});

if (this.titreInteret ) {
  centreinteretsData.push({
    titreInteret: this.titreInteret,

  });
}


const languesData = [];
this.langues.forEach(langue => {
  languesData.push({
    langue: langue.langue,
    niveau: langue.niveau
  });
});

if (this.langue || this.niveau ) {
  languesData.push({
    langue: this.langue,
    niveau: this.niveau

  });
}
const referencesData = [];
const referenceSet = new Set();

// Ajouter les références existantes en évitant les doublons
this.references.forEach(reference => {
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

this.clubs.forEach(club => {
  const clubKey = `${club.nomclub}-${club.role}`;
  if (!clubSet.has(clubKey)) {
    clubsData.push({
      nomclub: club.nomclub,
      role: club.role,
    });
    clubSet.add(clubKey);
  }
});

if (this.nomclub || this.role ) {
const newclubKey = `${this.nomclub}-${this.role}`;
if (!clubSet.has(newclubKey)) {
  clubsData.push({
    nomclub: this.nomclub,
    role: this.role,
  });
  clubSet.add(newclubKey);
}
}


const projetsData = [];
this.projets.forEach(projet => {
  projetsData.push({
    titreprojet: projet.titreprojet,
    descriptionprojet: projet.descriptionprojet,
  });
});

if (this.nomnewprojet ||  this.descriptionnewprojet  ||  this.uploadedFileName ) {
  projetsData.push({
    titreprojet: this.nomnewprojet,
    descriptionprojet: this.descriptionnewprojet,
    fichier_zip:this.uploadedFileName,
  });
}

axios.post(`http://127.0.0.1:8000/stock-informations/${userId}/`, {
  profil: this.profil,
  formations: formationsData,
  experiences: experiencesData,
  competences: competencesData,
  softskills :softskillsData,
  interets:centreinteretsData,
  langues:languesData,
  references:referencesData,
  clubs:clubsData,
  projets:projetsData,
})
.then(() => {
  // Gérer la réponse du serveur si nécessaire
  console.log('Infos professionnelles enregistrés avec succès !');
  
  // Vous pouvez également actualiser les données après avoir enregistré les informations
  this.recupererDonnees();

})
.catch(error => {
  // Gérer les erreurs si la sauvegarde échoue
  console.error('Erreur lors de l\'enregistrement des informations : ', error);
});
},
enregistrerTemplate() {
const userId = localStorage.getItem("user_id");
if (!userId) {
  alert("Vous devez être connecté.");
  return;
}

const nomTemplate = "template3";

axios.post(`http://127.0.0.1:8000/stock-template/${userId}/`, {
  etudiant: userId, 
  nomtemplate: nomTemplate 
})
.then(() => {
  console.log('Template enregistré avec succès !');
  this.recupererDonnees();
})
.catch(error => {
  console.error('Erreur lors de l\'enregistrement du template : ', error);
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
this.$router.push('/EtudiantDetails/' + this.etudiant.id);

}
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
  .upload-container {
  position: relative;
  border: 2px dashed #43434352;
  width: 60%;
  height: 90px;
  top: 15px;
  padding: 20px;
  padding-bottom: 20px;
  left: 20px;
  background-color: transparent;

}
  </style>
  