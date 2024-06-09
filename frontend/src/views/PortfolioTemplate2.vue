<template>
  <router-view></router-view>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="msapplication-TileColor" content="#0E0E0E">
    <meta name="template-color" content="#0E0E0E">
    <meta name="msapplication-config" content="browserconfig.html">
    <meta name="description" content="Index page">
    <meta name="keywords" content="index, page">
    <meta name="author" content="">
    <title>Portfolio 2 </title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css" rel="stylesheet">
    <link href="https://cdn.tiny.cloud/1/YOUR_API_KEY/tinymce/5/tinymce.min.js" referrerpolicy="origin">
    <link rel="shortcut icon" type="image/x-icon" href="/template/assets/imgs/template/favicon.svg">

    <link href="/template/assets/css/plugins/animate.min.css" rel="stylesheet">
    <link href="/template/assets/css/plugins/magnific-popup.css" rel="stylesheet">
    <link href="/template/assets/css/plugins/perfect-scrollbar.css" rel="stylesheet">
    <link href="/template/assets/css/plugins/select2.min.css" rel="stylesheet">
    <link href="/template/assets/css/plugins/swiper-bundle.min.css" rel="stylesheet">
    
    <link href="/template/assets/css/stylecd4e.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  </head>
  <body>

  <nav  style="background-color: #394856; height:60px;">
    <div class="navbar-icons">
    <!--<button class="scroll-top-button" style="display: flex; justify-content: center; align-items: center;position: relative;top: 10px;left: 15px;">
      <router-link :to="'/GenePortfo2/' + this.etudiant.id" >
  <svg xmlns="http://www.w3.org/2000/svg" width="25" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M19 12H6M12 5l-7 7 7 7"></path>
  </svg>
</router-link>
</button>-->

<!--<button class="copy-button" style="display: flex; justify-content: center; align-items: center; position: relative; left: 1280px; bottom: 35px;">
    <i class="fas fa-copy"></i>
</button>-->
    <!--<button class="download-button" style="display: flex; justify-content: center; align-items: center;position: relative;left: 1220px;bottom: 79px"><i class="fas fa-download"></i> </button>-->
  </div>

</nav>
  
    <main >


  
      <!--
        - #SIDEBAR
      -->
  
      <aside class="sidebar" data-sidebar>
  
        <div class="sidebar-info">
  
          <figure class="avatar-box">
            <img :src="imageUrl" alt="Richard hanrick" width="80">
            
          </figure>
  
          <div class="info-content" >
            <p> <span style="font-size: 34px;font-weight: bolder; margin: 6px;">{{ nom }}</span></p>         

            <p><span style="font-size: 34px;font-weight: bolder; margin: 6px;">{{ prenom }}</span></p>

             <!--<p class="title">Développeuse Web</p>-->
          </div>
  
          <button class="info_more-btn" data-sidebar-btn>
            <span>Contacts</span>
  
            <!--<ion-icon name="chevron-down"></ion-icon>-->
          </button>
  
        </div>
  
        <div class="sidebar-info_more">
  
          <div class="separator"></div>
  
          <ul class="contacts-list">
            <div class="contact-info" style="width: 289px;">
                <p class="contact-title" style="font-size: 20px;font-weight: 700;color: #05264E;">Profil</p>
                <p style="font-size: 18px;font-weight: 500"> {{profil}}</p>
              </div>
         
              
              
              <div class="contact-info">
                <p class="contact-title" style="font-size: 20px;font-weight: 700;color: #05264E;">E-mail</p>
                <a href="mailto:richard@example.com" class="contact-link" style="font-size: 18px;font-weight: 500"> {{email}}</a>
              </div>
  
  
   
  
              <div class="contact-info">
                <p class="contact-title" style="font-size: 20px;font-weight: 700;color: #05264E;">TÉLEPHONE</p>
  
                <a href="tel:+12133522795" class="contact-link" style="font-size: 18px;font-weight: 500">{{telephone}}</a>
              </div>
  
  
            <li class="contact-item">
  
              <div class="icon-box">
                <!--<ion-icon name="calendar-outline"></ion-icon>-->
              </div>
  
              <!--<div class="contact-info">
                <p class="contact-title">Date de Naissance</p>
  
                <time datetime="1982-06-23">Septemper 18, 2002</time>
              </div>-->
  
            </li>
  
            <li class="contact-item">
  
              <div class="icon-box">
                <!--<ion-icon name="location-outline"></ion-icon>-->
              </div>
  
              <!--<div class="contact-info">
                <p class="contact-title">Adresse</p>
  
                <address>Monastir, Bouhjar 5015</address>
              </div>-->
  
            </li>
  
          </ul>
  
          <div class="separator"></div>
  
          <ul class="social-list">
  
            <li class="social-item">
              <a :href="skype" class="social-link" target="_blank">
                <i class="fab fa-skype fa-3x" style="color: #05264E;" ></i>
              </a>
            </li>
  
    <li class="social-item">
          <a :href="linkedin"  class="social-link" target="_blank">
            <i class="fab fa-linkedin fa-3x" style="color: #05264E;"></i>
        </a>
    </li>
  
            <li class="social-item">
              <a :href="github" class="social-link" target="_blank" >
                <i class="fab fa-github fa-3x" style="color: #05264E;"></i>
              </a>
            </li>
  
          </ul>
  
        </div>
  
      </aside>
  
  
  
  
  
      <!--
        - #main-content
      -->
  
      <div class="main-content">
  
        <!--
          - #NAVBAR
        -->
  
        <nav class="navbar">
  
          <ul class="navbar-list">
  
            <li class="navbar-item">
              <button class="navbar-link  active" data-nav-link>Formation</button>
            </li>
  
            <li class="navbar-item">
              <button class="navbar-link "  data-nav-link>Compétences</button>
            </li>
  
            <li class="navbar-item">
              <button  class="navbar-link " data-nav-link>Expérienes </button>
            </li>
  
            <li class="navbar-item">
              <button class="navbar-link " data-nav-link>Projets</button>
            </li>
  
            <li class="navbar-item">
              <button class="navbar-link " data-nav-link>Autres</button>
            </li>
  
          </ul>
  
        </nav>
  
  
  
  
  
        <!--
          - #ABOUT
        -->
  
        <article class="about  active" data-page="about">
  
          <header>
            <h2 class="h2 article-title" style="position: relative;top: 20px;"> Formation </h2>
          </header>
  
          <!--education start -->
<section id="formation" class="service">
  
  <div class="container">
    <div class="education-vertical-timeline">
        <div class="row">
            <div class="col-md-12">
                <div class="timeline">
                    <div class="timeline-content" v-for="formation in formations" :key="formation.nomformation">
                        <div class="timeline-header">
                            <h2 class="timeline-title" style="color: white;font-size: 22px;">{{ formation.nomformation }}</h2>
                            <p class="timeline-duration">{{ formation.debutformation }} - {{ formation.finformation }}</p>
                        </div>
                        <div class="timeline-body">
                            <p>{{ formation.etablissement }}</p>
                        </div>
                    </div>
                    <!-- Répétez cette structure pour chaque formation -->
                </div>
            </div>
        </div>
    </div>
</div>

</section>

<!--/.education-->
  
          <!--
            - service
        
  
          <section class="service">
  
            <h3 class="h3 service-title">Qu'est-ce que je fais</h3>
  
            <ul class="service-list">
  
              <li class="service-item">
  
                <div class="service-icon-box">
                  <img src="Template2/assets/images/icon-design.svg
                  " alt="design icon" width="40">
                </div>
  
                <div class="service-content-box">
                  <h4 class="h4 service-item-title">Conception</h4>
  
                  <p class="service-item-text">
                    
                    Maîtrise professionnelle de la conception avec des modèles modernes.
                  </p>
                </div>
  
              </li>
  
              <li class="service-item">
  
                <div class="service-icon-box">
                  <img src="Template2/assets/images/icon-dev.svg" alt="Web development icon" width="40">
                </div>
  
                <div class="service-content-box">
                  <h4 class="h4 service-item-title">Développement Web</h4>
  
                  <p class="service-item-text">
                    Création de sites web très performants et professionnels.
                  </p>
                </div>
  
              </li>
  
              <li class="service-item">
  
                <div class="service-icon-box">
                  <img src="Template2/assets/images/icon-app.svg" alt="mobile app icon" width="40">
                </div>
  
                <div class="service-content-box">
                  <h4 class="h4 service-item-title">Développement Mobile</h4>
  
                  <p class="service-item-text">
                    Développement professionnel d'applications pour iOS et Android.
                  </p>
                </div>
  
              </li>
      
            </ul>
  
          </section>  -->
  
  
          <!--
            - testimonials
          -->
  
          <!--<section class="testimonials">
  
            <h3 class="h3 testimonials-title">Références</h3>
  
            <ul class="testimonials-list has-scrollbar">
  
            
  
              <li class="testimonials-item">
                <div class="content-card" data-testimonials-item>
  
                  <figure class="testimonials-avatar-box">
                    <img src="Template2/assets/images/avatar-2.png" alt="Jessica miller" width="60" data-testimonials-avatar />
                  </figure>
  
                  <h4 class="h4 testimonials-item-title" data-testimonials-title>HENI Jihene</h4>
  
                  <div class="testimonials-text" data-testimonials-text>
                    <p>
                      Développeuse en  PHP/Laravel 
                    </p>
                    <p>
                      Téléphone: 52 371 100<br>
                      Adresse : La société SW  Consulting
                    </p>
                     
                  </div>
  
                  
              </div>
              </li>
  
                       <div data-modal-text></div>
  
             
  
            </ul>
  
          </section>-->
  
      <!--
            - testimonials modal
        
  
          <div class="modal-container" data-modal-container>
  
            <div class="overlay" data-overlay></div>
  
            <section class="testimonials-modal">
  
              <button class="modal-close-btn" data-modal-close-btn>
               <ion-icon name="close-outline"></ion-icon>
              </button>
  
              <div class="modal-img-wrapper">
                <figure class="modal-avatar-box">
                  <img src="Template2/assets/images/avatar-1.png" alt="Daniel lewis" width="80" data-modal-img />
                </figure>
  
                <img src="Template2/assets/images/icon-quote.svg" alt="quote icon">
              </div>
  
              <div class="modal-content">
  
                <h4 class="h3 modal-title" data-modal-title>HENI Jihen</h4>
               <p>
                
          Khaoula  s'est adaptée aisément à l'environnement professionnel, 
          démontrant ainsi une capacité d'adaptation notable. 
          Son habitude de poser des questions témoigne d'un professionnalisme exemplaire 
          et d'une volonté d'apprentissage remarquable.
         </p>
                
  
              </div>
  
            </section> 
  
          </div>
  
  
        
            - clients
        
  
          <section class="clients">
  
            <h3 class="h3 clients-title">Clients</h3>
  
            <ul class="clients-list has-scrollbar">
  
              <li class="clients-item">
                <a href="#">
                  <img src="./assets/images/logo-1-color.png" alt="client logo">
                </a>
              </li>
  
              <li class="clients-item">
                <a href="#">
                  <img src="./assets/images/logo-2-color.png" alt="client logo">
                </a>
              </li>
  
              <li class="clients-item">
                <a href="#">
                  <img src="./assets/images/logo-3-color.png" alt="client logo">
                </a>
              </li>
  
              <li class="clients-item">
                <a href="#">
                  <img src="./assets/images/logo-4-color.png" alt="client logo">
                </a>
              </li>
  
              <li class="clients-item">
                <a href="#">
                  <img src="./assets/images/logo-5-color.png" alt="client logo">
                </a>
              </li>
  
              <li class="clients-item">
                <a href="#">
                  <img src="./assets/images/logo-6-color.png" alt="client logo">
                </a>
              </li>
  
            </ul>
  
          </section>
        -->
        </article>
  
  
  
  
  
        <!--
          - #CV
        -->
  
        <article class="CV"  data-page="CV">
  
          <header>
            <h2 class="h2 article-title" style="position: relative;top: 20px;">Compétences</h2>
          </header>
          <section id="competences" class="profiles">
			<div class="profiles-details">
        <div class="title-box text-center">
  
        
        </div>
				<div class="container" >
					<div class="profiles-content">
						<div class="row">
							<div class="col-sm-3" v-for="(competence, index) in competences" :key="index">
								<div class="single-profile">
									<div class="profile-txt">
										<a href=""><i class="flaticon-themeforest"></i></a>
										<div class="profile-icon-name" style="font-size: 20px;font-weight:700;">{{competence.categorie}} : </div>
                    <div class="profile-icon-name"> {{competence.competence}} </div>

									</div>
						
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
     
  

        </article>
  
  
  
  
  
        <!--
          - #PORTFOLIO
        -->
  
        <article class="portfolio" data-page="portfolio">
  
          <header>
            <h2 class="h2 article-title" style="position: relative;top: 20px;"> Expériences professionnelles</h2>
          </header>
  
          <section id="experiences" class="experience">

    <div class="container" style="width: 1140px;">
        <div class="experience-content">
            <div class="main-timeline">
                <ul>
                    <li v-for="experience in experiences" :key="experience.id">
                        <div class="single-timeline-box fix">
                            <div class="row exp">
                                <div class="col-md-5" style="width: 41.6666666667%; left: -160px; position: relative;">
                                    <div class="experience-time text-right">
                                        <h2 style="position: relative;color: white;font-size: 18px;top:25px;padding: 10px;right: 11px;">{{ experience.debutexperience }} - {{ experience.finexperience }}</h2>
                                        <h3 style="color: white;font-size: 18px;font-weight: 700;">{{ experience.titre }}</h3>
                                    </div><!--/.experience-time-->
                                </div><!--/.col-->
                                <div class="col-md-offset-1 col-md-5">
                                    <div class="timeline">
                                        <div class="timeline-content" style="position: relative;right: 120px;">
                                            <h4 class="title" style="color: white;font-size: 18px;">
                                                {{ experience.entreprise }}
                                            </h4>
                                            <p class="description">
                                                {{ experience.description }}
                                            </p>
                                        </div><!--/.timeline-content-->
                                    </div><!--/.timeline-->
                                </div><!--/.col-->
                            </div>
                        </div><!--/.single-timeline-box-->
                    </li>
                    <!-- Ajoutez ici une condition pour gérer le cas où experiences est vide -->
              
                </ul>
            </div><!--.main-timeline-->
        </div><!--.experience-content-->
    </div>
</section>
  
        </article>
  
  
  
  
  
        <!--
          - #BLOG
        -->
  
        <article class="blog" data-page="blog">
  
          <header>
            <h2 class="h2 article-title" style="position: relative;top: 20px;">Projets</h2>
          </header>
  
          <section id="formation" class="service">
  
  <div class="container">
    <div class="education-vertical-timeline">
        <div class="row">
            <div class="col-md-12">
                <div class="timeline">
                    <div class="timeline-content" v-for="(projet, index) in projets" :key="index">
                        <div class="timeline-header">
                            <h2 class="timeline-title" style="color: white;font-size: 18px;font-weight: 500;">   
                               {{projet.titreprojet}}</h2>
                            <p class="timeline-duration">{{ projet.descriptionprojet }}</p>
                        </div>
               
                    </div>
                    <!-- Répétez cette structure pour chaque formation -->
                </div>
            </div>
        </div>
    </div>
</div>


</section>
  
        </article>
  
  
  
  
  
        <!--
          - #CONTACT
        -->
        <article class="contact" data-page="contact">
  
    <h3 class="h3 form-title" style="position: relative;top: 70px;font-weight: 700;color: rgb(5, 38, 78);">Centre d'intérêt</h3>

    <section id="competences" class="profiles">
			<div class="profiles-details">
        <div class="title-box text-center">
  
        
        </div>
				<div class="container" >
					<div class="profiles-content">
						<div class="row">
							<div class="col-sm-3" v-for="(interet, index) in interets" :key="index">
								<div class="single-profile">
									<div class="profile-txt">
										<a href=""><i class="flaticon-themeforest"></i></a>
										<div class="profile-icon-name" style="position: relative;font-size: 20px;font-weight:700;bottom: 15px">{{interet.titreInteret}}</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>



    <section id="competences" class="profiles">
      <h3 class="h3 form-title" style="position: relative;bottom:155px;font-weight: 700; color: rgb(5, 38, 78);">Langues</h3>

			<div class="profiles-details">
        <div class="title-box text-center">
  
        
        </div>
				<div class="container" >
					<div class="profiles-content">
						<div class="row">
							<div class="col-sm-3" v-for="(langue, index) in langues" :key="index">
								<div class="single-profile" style="position: relative;bottom: 160px;">
									<div class="profile-txt" >
										<a href=""><i class="flaticon-themeforest"></i></a>
										<div class="profile-icon-name" style="position: relative;font-size: 20px;font-weight:700">{{langue.langue}} : </div>
                    <div class="profile-icon-name" style="position: relative;font-size: 20px;font-weight:400">{{langue.niveau}}</div>

									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>



    <section id="competences" class="profiles">
      <h3 class="h3 form-title" style="position: relative;bottom:300px;font-weight: 700;color: rgb(5, 38, 78);">Soft_skills</h3>

			<div class="profiles-details">
        <div class="title-box text-center">
  
        
        </div>
				<div class="container" >
					<div class="profiles-content">
						<div class="row">
							<div class="col-sm-3" v-for="(skills, index) in softskills" :key="index">
								<div class="single-profile" style="position: relative;bottom: 300px;">
									<div class="profile-txt" >
										<a href=""><i class="flaticon-themeforest"></i></a>
										<div class="profile-icon-name" style="position: relative;font-size: 20px;font-weight:500">{{skills.titreskills}} </div>

									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>

    <section class="contact-form">
    <h3 class="h3 form-title" style="position: relative;bottom:400px;font-weight:700;color: rgb(5, 38, 78);">Références</h3>

    <section id="competences" class="profiles">
			<div class="profiles-details">
        <div class="title-box text-center">
  
        
        </div>
				<div class="container" >
					<div class="profiles-content">
						<div class="row">
							<div class="col-sm-3" v-for="reference in references" :key="reference.id">
								<div class="single-profile" style="position: relative;bottom: 500px;width: 300px;">
									<div class="profile-txt" >
										<a href=""><i class="flaticon-themeforest"></i></a>
										<div class="profile-icon-name" style="position: relative;font-size: 20px;font-weight:500">{{reference.titreref }} </div>
                    <div class="profile-icon-name" style="position: relative;font-size: 20px;font-weight:500">{{reference.poste }} </div>
                    <div class="profile-icon-name" style="position: relative;font-size: 20px;font-weight:500">{{reference.emailref }} </div>


									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>






  
    
  
  </section>


  <section class="contact-form">
    <h3 class="h3 form-title" style="position: relative;bottom:450px;font-weight: 700;color: rgb(5, 38, 78);;">Clubs</h3>

    <section id="competences" class="profiles">
			<div class="profiles-details">
        <div class="title-box text-center">
  
        
        </div>
				<div class="container" >
					<div class="profiles-content">
						<div class="row">
							<div class="col-sm-3" v-for="club in clubs" :key="club.id">
								<div class="single-profile" style="position: relative;bottom: 130px;">
									<div class="profile-txt" >
										<a href=""><i class="flaticon-themeforest"></i></a>
										<div class="profile-icon-name" style="position: relative;font-size: 20px;font-weight:500">{{club.nomclub }} </div>
                    <div class="profile-icon-name" style="position: relative;font-size: 20px;font-weight:500">{{club.role }} </div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>


    <h3 class="h3 form-title" style="position: relative;top: 70px;font-weight: 800;">Référence</h3>




  
    
  
  </section>
  
  </article>
        
  
      </div>
  
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
        clubs:[],
        etudiant: {
            id: null
        },





       
      };
    },
      mounted() {
        'use strict';
        this.fetchImageUrl();
        this.recupererDonnees();
  
        // Sélectionnez tous les boutons de navigation
        const navLinks = document.querySelectorAll('[data-nav-link]');
        // Sélectionnez tous les articles de page correspondants
        const articles = document.querySelectorAll('[data-page]');
  
        // Ajoutez un gestionnaire d'événement pour chaque bouton de navigation
        navLinks.forEach((link, index) => {
          link.addEventListener('click', () => {
            // Retirez la classe 'active' de tous les boutons
            navLinks.forEach((item) => item.classList.remove('active'));
            // Ajoutez la classe 'active' au bouton actuellement cliqué
            link.classList.add('active');
            // Masquez tous les articles de page
            articles.forEach((article) => article.classList.remove('active'));
            // Affichez uniquement l'article de page correspondant à l'index du bouton cliqué
            articles[index].classList.add('active');
          });
        });
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
  
  
  <style scoped>
  
  /*-----------------------------------*\
  #style.css
\*-----------------------------------*/


/**
 * copyright 2022 @codewithsadee
 */





/*-----------------------------------*\
  #CUSTOM PROPERTY
\*-----------------------------------*/

:root {

/**
 * colors
 */

/* gradient */

--bg-gradient-onyx: linear-gradient(
  to bottom right, 
  hsl(240, 1%, 25%) 3%, 
  hsl(0, 0%, 19%) 97%
);
--bg-gradient-jet: linear-gradient(
  to bottom right, 
  hsla(240, 1%, 18%, 0.251) 0%, 
  hsla(240, 2%, 11%, 0) 100%
), hsl(240, 2%, 13%);
--bg-gradient-yellow-1: linear-gradient(
  to bottom right, 
  hsl(45, 100%, 71%) 0%, 
  hsla(36, 100%, 69%, 0) 50%
);
--bg-gradient-yellow-2: linear-gradient(
  135deg, 
  hsla(45, 100%, 71%, 0.251) 0%, 
  hsla(35, 100%, 68%, 0) 59.86%
), hsl(240, 2%, 13%);
--border-gradient-onyx: linear-gradient(
  to bottom right, 
  hsl(0, 0%, 25%) 0%, 
  hsla(0, 0%, 25%, 0) 50%
);
--text-gradient-yellow: linear-gradient(
  to right, 
  hsl(45, 100%, 72%), 
  hsl(35, 100%, 68%)
);

/* solid */

--jet: hsl(0, 0%, 22%);
--onyx: hsl(240, 1%, 17%);
--eerie-black-1: hsla(0, 2%, 13%, 0.852);
--eerie-black-2: hsla(0, 2%, 13%, 0.852);
--smoky-black: hsl(0, 3%, 13%);
--white-1: hsl(0, 0%, 100%);
--white-2: hsl(0, 0%, 98%);
--orange-yellow-crayola: hsl(45, 100%, 72%);
--vegas-gold: hsl(45, 54%, 58%);
--light-gray: hsl(0, 0%, 84%);
--light-gray-70: hsla(0, 0%, 84%, 0.7);
--bittersweet-shimmer: hsl(0, 43%, 51%);

/**
 * typography
 */

/* font-family */
--ff-poppins: 'Poppins', sans-serif;

/* font-size */
--fs-1: 24px;
--fs-2: 18px;
--fs-3: 17px;
--fs-4: 16px;
--fs-5: 15px;
--fs-6: 14px;
--fs-7: 13px;
--fs-8: 11px;

/* font-weight */
--fw-300: 300;
--fw-400: 400;
--fw-500: 500;
--fw-600: 600;

/**
 * shadow
 */

--shadow-1: -4px 8px 24px hsla(0, 0%, 0%, 0.25);
--shadow-2: 0 16px 30px hsla(0, 0%, 0%, 0.25);
--shadow-3: 0 16px 40px hsla(0, 0%, 0%, 0.25);
--shadow-4: 0 25px 50px hsla(0, 0%, 0%, 0.15);
--shadow-5: 0 24px 80px hsla(0, 0%, 0%, 0.25);

/**
 * transition
 */

--transition-1: 0.25s ease;
--transition-2: 0.5s ease-in-out;

}





/*-----------------------------------*\
#RESET
\*-----------------------------------*/

*, *::before, *::after {
margin: 0;
padding: 0;
box-sizing: border-box;
}

a { text-decoration: none; }


img, ion-icon, a, button, time, span { display: block; }

button {
font: inherit;
background: none;
border: none;
text-align: left;
cursor: pointer;
}

input, textarea {
display: block;
width: 100%;
background: none;
font: inherit;
}









/*-----------------------------------*\
#REUSED STYLE
\*-----------------------------------*/

.sidebar,
article {
background: var(--eerie-black-2);
border: 1px solid var(--jet);
border-radius: 20px;
padding: 10px;
box-shadow: var(--shadow-1);
z-index: 1;
}

.separator {
width: 100%;
height: 1px;
background: var(--jet);
margin: 16px 0;
}

.icon-box {
position: relative;
background: var(--border-gradient-onyx);
width: 30px;
height: 30px;
border-radius: 8px;
display: flex;
justify-content: center;
align-items: center;
font-size: 16px;
color: var(--orange-yellow-crayola);
box-shadow: var(--shadow-1);
z-index: 1;
}

.icon-box::before {
content: "";
position: absolute;
inset: 1px;
background: var(--eerie-black-1);
border-radius: inherit;
z-index: -1;
}

.icon-box ion-icon { --ionicon-stroke-width: 35px; }

article { display: none; }

article.active {
display: block;
animation: fade 0.5s ease backwards;
}

@keyframes fade {
0% { opacity: 0; }
100% { opacity: 1; }
}

.h2,
.h3,
.h4,
.h5 {
color:white;
text-transform: capitalize;
}

.h2 { font-size: var(--fs-1); }

.h3 { font-size: 20px }

p{
  color: #ffffff;
}

.h4 { font-size: var(--fs-4); }

.h5 {
font-size: var(--fs-7);
font-weight: var(--fw-500);
}

.article-title {
position: relative;
padding-bottom: 7px;
}

.article-title::after {
content: "";
position: absolute;
bottom: 0;
left: 0;
width: 30px;
height: 3px;
background: var(--text-gradient-yellow);
border-radius: 3px;
}

.has-scrollbar::-webkit-scrollbar {
width: 5px; /* for vertical scrollbar */
height: 5px; /* for horizontal scrollbar */
}

.has-scrollbar::-webkit-scrollbar-track {
background: var(--onyx);
border-radius: 5px;
}

.has-scrollbar::-webkit-scrollbar-thumb {
background: var(--orange-yellow-crayola);
border-radius: 5px;
}

.has-scrollbar::-webkit-scrollbar-button { width: 20px; }

.content-card {
position: relative;
background: var(--border-gradient-onyx);
padding: 15px;
padding-top: 45px;
border-radius: 14px;
box-shadow: var(--shadow-2);
cursor: pointer;
z-index: 1;
}

.content-card::before {
content: "";
position: absolute;
inset: 1px;
background: var(--bg-gradient-jet);
border-radius: inherit;
z-index: -1;
}





/*-----------------------------------*\
#MAIN
\*-----------------------------------*/

main {
margin: 15px 12px;
margin-bottom: 75px;
min-width: 259px;
}





/*-----------------------------------*\
#SIDEBAR
\*-----------------------------------*/

.sidebar {
margin-bottom: 15px;
max-height: 112px;
overflow: hidden;
transition: var(--transition-2);
background-color: #AEC0D1;
}

.sidebar.active { max-height: 405px; }

.sidebar-info {
position: relative;
display: flex;
justify-content: flex-start;
align-items: center;
gap: 15px;
}

.avatar-box {
background: var(--bg-gradient-onyx);
border-radius: 20px;
}

.info-content .name {
color: var(--white-2);
font-size: var(--fs-3);
font-weight: var(--fw-500);
letter-spacing: -0.25px;
margin-bottom: 10px;
}

.info-content .title {
color: var(--white-1);
background: var(--onyx);
font-size: var(--fs-8);
font-weight: var(--fw-300);
width: max-content;
padding: 3px 12px;
border-radius: 8px;
}

.info_more-btn {
position: absolute;
top: -15px;
right: -15px;
border-radius: 0 15px;
font-size: 13px;
color: var(--orange-yellow-crayola);
background: var(--border-gradient-onyx);
padding: 10px;
box-shadow: var(--shadow-2);
transition: var(--transition-1);
z-index: 1;
}

.info_more-btn::before {
content: "";
position: absolute;
inset: 1px;
border-radius: inherit;
background: var(--bg-gradient-jet);
transition: var(--transition-1);
z-index: -1;
}

.info_more-btn:hover,
.info_more-btn:focus { background: var(--bg-gradient-yellow-1); }

.info_more-btn:hover::before,
.info_more-btn:focus::before { background: var(--bg-gradient-yellow-2); }

.info_more-btn span { display: none; }

.sidebar-info_more {
opacity: 0;
visibility: hidden;
transition: var(--transition-2);
}

.sidebar.active .sidebar-info_more {
opacity: 1;
visibility: visible;
}

.contacts-list {
display: grid;
grid-template-columns: 1fr;
gap: 16px;
}

.contact-item {
min-width: 100%;
display: flex;
align-items: center;
gap: 16px;
}

.contact-info {
max-width: calc(100% - 46px);
width: calc(100% - 46px);
}

.contact-title {
color: white;
font-size: var(--fs-8);
text-transform: uppercase;
margin-bottom: 2px;
}

.contact-info :is(.contact-link, time, address) {
color: white;
font-size: var(--fs-7);
}

.contact-info address { font-style: normal; }

.social-list {
display: flex;
justify-content: flex-start;
align-items: center;
gap: 15px;
padding-bottom: 4px;
padding-left: 7px;
}

.social-item .social-link {
color: var(--light-gray-70);
font-size: 18px;
}


.social-item .social-link:hover { color: var(--light-gray); }





/*-----------------------------------*\
#NAVBAR
\*-----------------------------------*/

.navbar {
position: fixed;
bottom: 0;
right:180px;
width: 150%;
background-color: white;
backdrop-filter: blur(10px);
border: 1px solid var(--jet);
border-radius: 12px 12px 0 0;
box-shadow: var(--shadow-2);
z-index: 5;
}

.navbar-list {
display: flex;
flex-wrap: wrap;
justify-content: center;
align-items: center;
padding: 0 10px;
}

.navbar-link {
color: #AEC0D1;
font-size: 20px;
font-weight: 700;
padding: 20px 7px;
}

.navbar-link:hover,
.navbar-link:focus { color: var(--light-gray-70); }

.navbar-link.active { color: #394856; }





/*-----------------------------------*\
#ABOUT
\*-----------------------------------*/

.about .article-title { margin-top: 35px; }

.about-text {
color: white;
font-size: var(--fs-6);
font-weight: var(--fw-300);
line-height: 1.6;
}

.about-text p { margin-bottom: 15px; 
  color: #ffffff;
}



/**
* #service 
*/

.service { margin-bottom: 35px; }

.service-title { 
  margin-bottom: 20px; 
  color: #ffffff;
}

.service-list {
display: grid;
grid-template-columns: 1fr;
gap: 20px;
}

.service-item {
position: relative;
background: var(--border-gradient-onyx);
padding: 25px;
border-radius: 14px;
box-shadow: var(--shadow-2);
z-index: 1;
}

.service-item::before {
content: "";
position: absolute;
inset: 1px;
background: #593b1fb3;
border-radius: inherit;
z-index: -1;
}

.service-icon-box { margin-bottom: 10px; }

.service-icon-box img { margin: auto; }

.service-content-box { text-align: center; }

.service-item-title { margin-bottom: 7px; }

.service-item-text {
color: white;
font-size: var(--fs-6);
font-weight: var(--fw-3);
line-height: 1.6;
}


/**
* #testimonials 
*/

.testimonials { margin-bottom: 30px; }

.testimonials-title { margin-bottom: 20px; }

.testimonials-list {
display: flex;
justify-content: flex-start;
align-items: flex-start;
gap: 15px;
margin: 0 -15px;
padding: 15px 15px;
padding-bottom: 35px;
overflow-x: auto;
scroll-behavior: smooth;
overscroll-behavior-inline: contain;
scroll-snap-type: inline mandatory;
}

.testimonials-item {
min-width: 100%;
scroll-snap-align: center;
}

.testimonials-avatar-box {
position: absolute;
top: 0;
left: 0;
transform: translate(15px, -25px);
background: var(--bg-gradient-onyx);
border-radius: 10px;
box-shadow: var(--shadow-1);
}

.testimonials-item-title { margin-bottom: 7px; }

.testimonials-text {
color: white;
font-size: var(--fs-6);
font-weight: var(--fw-300);
line-height: 1.6;
display: -webkit-box;
line-clamp: 4;
-webkit-line-clamp: 4;
-webkit-box-orient: vertical;
}


/**
* #testimonials-modal
*/

.modal-container {
position: fixed;
top: 0;
left: 0;
width: 100%;
height: 100%;
display: flex;
justify-content: center;
align-items: center;
overflow-y: auto;
overscroll-behavior: contain;
z-index: 20;
pointer-events: none;
visibility: hidden;
}

.modal-container::-webkit-scrollbar { display: none; }

.modal-container.active {
pointer-events: all;
visibility: visible;
}

.overlay {
position: fixed;
top: 0;
left: 0;
width: 100%;
height: 100vh;
background: hsl(0, 0%, 5%);
opacity: 0;
visibility: hidden;
pointer-events: none;
z-index: 1;
transition: var(--transition-1);
}

.overlay.active {
opacity: 0.8;
visibility: visible;
pointer-events: all;
}

.testimonials-modal {
background: var(--eerie-black-1);
position: relative;
padding: 15px;
margin: 15px 12px;
border: 1px solid var(--jet);
border-radius: 14px;
box-shadow: var(--shadow-5);
transform: scale(1.2);
opacity: 0;
transition: var(--transition-1);
z-index: 2;
}

.modal-container.active .testimonials-modal {
transform: scale(1);
opacity: 1;
}

.modal-close-btn {
position: absolute;
top: 15px;
right: 15px;
background: var(--onyx);
border-radius: 8px;
width: 32px;
height: 32px;
display: flex;
justify-content: center;
align-items: center;
color: white;
font-size: 18px;
opacity: 0.7;
}

.modal-close-btn:hover,
.modal-close-btn:focus { opacity: 1; }

.modal-close-btn ion-icon { --ionicon-stroke-width: 50px; }

.modal-avatar-box {
background: var(--bg-gradient-onyx);
width: max-content;
border-radius: 14px;
margin-bottom: 15px;
box-shadow: var(--shadow-2);
}

.modal-img-wrapper > img { display: none; }

.modal-title { margin-bottom: 4px; }

.modal-content time {
font-size: var(--fs-6);
font-weight: var(--fw-300);
margin-bottom: 10px;
}

.modal-content p {
color: white;
font-size: var(--fs-6);
font-weight: var(--fw-300);
line-height: 1.6;
}


/**
* #clients 
*/

.clients { margin-bottom: 15px; }

.clients-list {
display: flex;
justify-content: flex-start;
align-items: flex-start;
gap: 15px;
margin: 0 -15px;
padding: 25px;
padding-bottom: 25px;
overflow-x: auto;
scroll-behavior: smooth;
overscroll-behavior-inline: contain;
scroll-snap-type: inline mandatory;
scroll-padding-inline: 25px;
}

.clients-item {
min-width: 50%;
scroll-snap-align: start;
}

.clients-item img {
width: 100%;
filter: grayscale(1);
transition: var(--transition-1);
}

.clients-item img:hover { filter: grayscale(0); }





/*-----------------------------------*\
#CV
\*-----------------------------------*/

.article-title { margin-top: 30px; }


/**
* education and experience 
*/

.timeline { margin-bottom: 30px; }

.timeline .title-wrapper {
display: flex;
align-items: center;
gap: 15px;
margin-bottom: 25px;
}

.timeline-list {
font-size: var(--fs-6);
margin-left: 45px;
}

.timeline-item { position: relative; }

.timeline-item:not(:last-child) { margin-bottom: 20px; }

.timeline-item-title {
font-size: var(--fs-6);
line-height: 1.3;
margin-bottom: 7px;
}

.timeline-list span {
color: white;
font-weight: var(--fw-400);
line-height: 1.6;
}

.timeline-item:not(:last-child)::before {
content: "";
position: absolute;
top: -25px;
left: -30px;
width: 1px;
height: calc(100% + 50px);
background: var(--jet);
}

.timeline-item::after {
content: "";
position: absolute;
top: 5px;
left: -33px;
height: 6px;
width: 6px;
background: var(--text-gradient-yellow);
border-radius: 50%;
box-shadow: 0 0 0 4px var(--jet);
}

.timeline-text {
color: white;
font-weight: var(--fw-300);
line-height: 1.6;
}


/**
* skills 
*/

.skills-title { margin-bottom: 20px; }

.skills-list { padding: 20px; }


.skills-item:not(:last-child) { margin-bottom: 15px; }

.skill .title-wrapper {
display: flex;
align-items: center;
gap: 5px;
margin-bottom: 8px;
}

.skill .title-wrapper data {
color: white;
font-size: var(--fs-7);
font-weight: var(--fw-300);
}

.skill-progress-bg {
background: var(--jet);
width: 100%;
height: 8px;
border-radius: 10px;
}

.skill-progress-fill {
background: var(--text-gradient-yellow);
height: 100%;
border-radius: inherit;
}





/*-----------------------------------*\
#PORTFOLIO
\*-----------------------------------*/

.filter-list { display: none; }

.filter-select-box {
position: relative;
margin-bottom: 25px;
}

.filter-select {
background: var(--eerie-black-2);
color:white;
display: flex;
justify-content: space-between;
align-items: center;
width: 100%;
padding: 12px 16px;
border: 1px solid var(--jet);
border-radius: 14px;
font-size: var(--fs-6);
font-weight: var(--fw-300);
}

.filter-select.active .select-icon { transform: rotate(0.5turn); }

.select-list {
background: var(--eerie-black-2);
position: absolute;
top: calc(100% + 6px);
width: 100%;
padding: 6px;
border: 1px solid var(--jet);
border-radius: 14px;
z-index: 2;
opacity: 0;
visibility: hidden;
pointer-events: none;
transition: 0.15s ease-in-out;
}

.filter-select.active + .select-list {
opacity: 1;
visibility: visible;
pointer-events: all;
}

.select-item button {
background: var(--eerie-black-2);
color: white;
font-size: var(--fs-6);
font-weight: var(--fw-300);
text-transform: capitalize;
width: 100%;
padding: 8px 10px;
border-radius: 8px;
}

.select-item button:hover { --eerie-black-2: hsl(240, 2%, 20%); }

.project-list {
display: grid;
grid-template-columns: 1fr;
gap: 30px;
margin-bottom: 10px;
}

.project-item { display: none; }

.project-item.active {
display: block;
animation: scaleUp 0.25s ease forwards;
}

@keyframes scaleUp {
0% { transform: scale(0.5); }
100% { transform: scale(1); }
}

.project-item > a { width: 100%; }

.project-img {
position: relative;
width: 100%;
height: 200px;
border-radius: 16px;
overflow: hidden;
margin-bottom: 15px;
}

.project-img::before {
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background: transparent;
z-index: 1;
transition: var(--transition-1);
}

.project-item > a:hover .project-img::before { background: hsla(0, 0%, 0%, 0.5); }

.project-item-icon-box {
--scale: 0.8;

background: var(--jet);
color: var(--orange-yellow-crayola);
position: absolute;
top: 50%;
left: 50%;
transform: translate(-50%, -50%) scale(var(--scale));
font-size: 20px;
padding: 18px;
border-radius: 12px;
opacity: 0;
z-index: 1;
transition: var(--transition-1);
}

.project-item > a:hover .project-item-icon-box {
--scale: 1;
opacity: 1;
}

.project-item-icon-box ion-icon { --ionicon-stroke-width: 50px; }

.project-img img {
width: 100%;
height: 100%;
object-fit: cover;
transition: var(--transition-1);
}

.project-item > a:hover img { transform: scale(1.1); }

.project-title,
.project-category { margin-left: 10px; }

.project-title {
color:white;
font-size: var(--fs-5);
font-weight: var(--fw-400);
text-transform: capitalize;
line-height: 1.3;
}

.project-category {
color: white;
font-size: var(--fs-6);
font-weight: var(--fw-300);
}





/*-----------------------------------*\
#BLOG
\*-----------------------------------*/

.blog-posts { margin-bottom: 10px; }

.blog-posts-list {
display: grid;
grid-template-columns: 1fr;
gap: 20px;
}

.blog-post-item > a {
position: relative;
background: var(--border-gradient-onyx);
height: 100%;
box-shadow: var(--shadow-4);
border-radius: 16px;
z-index: 1;
}

.blog-post-item > a::before {
content: "";
position: absolute;
inset: 1px;
border-radius: inherit;
background: var(--eerie-black-1);
z-index: -1;
}

.blog-banner-box {
width: 100%;
height: 200px;
border-radius: 12px;
overflow: hidden;
}

.blog-banner-box img {
width: 100%;
height: 100%;
object-fit: cover;
transition: var(--transition-1);
}

.blog-post-item > a:hover .blog-banner-box img { transform: scale(1.1); }

.blog-content { padding: 15px; }

.blog-meta {
display: flex;
justify-content: flex-start;
align-items: center;
gap: 7px;
margin-bottom: 10px;
}

.blog-meta :is(.blog-category, time) {
color: white;
font-size: var(--fs-6);
font-weight: var(--fw-300);
}

.blog-meta .dot {
background: var(--light-gray-70);
width: 4px;
height: 4px;
border-radius: 4px;
}

.blog-item-title {
margin-bottom: 10px;
line-height: 1.3;
transition: var(--transition-1);
}

.blog-post-item > a:hover .blog-item-title { color: var(--orange-yellow-crayola); }

.blog-text {
color: white;
font-size: var(--fs-6);
font-weight: var(--fw-300);
line-height: 1.6;
}





/*-----------------------------------*\
#CONTACT
\*-----------------------------------*/

.mapbox {
position: relative;
height: 250px;
width: 100%;
border-radius: 16px;
margin-bottom: 30px;
border: 1px solid var(--jet);
overflow: hidden;
}

.mapbox figure { height: 100%; }

.mapbox iframe {
width: 100%;
height: 100%;
border: none;
filter: grayscale(1) invert(1);
}

.contact-form { margin-bottom: 10px; }

.form-title { margin-bottom: 20px; }

.input-wrapper {
display: grid;
grid-template-columns: 1fr;
gap: 25px;
margin-bottom: 25px;
}

.form-input {
color: var(--white-2);
font-size: var(--fs-6);
font-weight: var(--fw-400);
padding: 13px 20px;
border: 1px solid var(--jet);
border-radius: 14px;
outline: none;
}

.form-input::placeholder { font-weight: var(--fw-500); }

.form-input:focus { border-color: var(--orange-yellow-crayola); }

textarea.form-input {
min-height: 100px;
height: 120px;
max-height: 200px;
resize: vertical;
margin-bottom: 25px;
}

textarea.form-input::-webkit-resizer { display: none; }

.form-input:focus:invalid { border-color: var(--bittersweet-shimmer); }

.form-btn {
position: relative;
width: 100%;
background: var(--border-gradient-onyx);
color: var(--orange-yellow-crayola);
display: flex;
justify-content: center;
align-items: center;
gap: 10px;
padding: 13px 20px;
border-radius: 14px;
font-size: var(--fs-6);
text-transform: capitalize;
box-shadow: var(--shadow-3);
z-index: 1;
transition: var(--transition-1);
}

.form-btn::before {
content: "";
position: absolute;
inset: 1px;
background: var(--bg-gradient-jet);
border-radius: inherit;
z-index: -1;
transition: var(--transition-1);
}

.form-btn ion-icon { font-size: 16px; }

.form-btn:hover { background: var(--bg-gradient-yellow-1); }

.form-btn:hover::before { background: var(--bg-gradient-yellow-2); }

.form-btn:disabled {
opacity: 0.7;
cursor: not-allowed;
}

.form-btn:disabled:hover { background: var(--border-gradient-onyx); }

.form-btn:disabled:hover::before { background: var(--bg-gradient-jet); }





/*-----------------------------------*\
#RESPONSIVE
\*-----------------------------------*/

/**
* responsive larger than 450px screen
*/

@media (min-width: 450px) {

/**
 * client
 */

.clients-item { min-width: calc(33.33% - 10px); }



/**
 * #PORTFOLIO, BLOG 
 */

.project-img,
.blog-banner-box { height: auto; }

}





/**
* responsive larger than 580px screen
*/

@media (min-width: 580px) {

/**
 * CUSTOM PROPERTY
 */

:root {

  /**
   * typography
   */

  --fs-1: 32px;
  --fs-2: 24px;
  --fs-3: 26px;
  --fs-4: 18px;
  --fs-6: 15px;
  --fs-7: 15px;
  --fs-8: 12px;

}



/**
 * #REUSED STYLE
 */

.sidebar, article {
  width: 520px;
  margin-inline: auto;
  padding: 30px;
}

.article-title {

  padding-bottom: 15px;
  color: #ffffff;
  font-weight: bolder;
  font-size: 30px;
}

.article-title::after {
  width: 40px;
  height: 5px;
}

.icon-box {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  font-size: 18px;
}



/**
 * #MAIN
 */

main {
  margin-top: 100px;
  margin-bottom: 100px;
}



/**
 * #SIDEBAR
 */

.sidebar {
  max-height: 200px;
  margin-bottom: 30px;
}

.sidebar.active { max-height: 584px; width: 50px; }

.sidebar-info { gap: 25px; }

.avatar-box { border-radius: 30px; }

.avatar-box img { width: 120px;border-radius: 30px;  }

.info-content .name { margin-bottom: 15px; }

.info-content .title { padding: 5px 18px; }

.info_more-btn {
  top: -30px;
  right: -30px;
  padding: 10px 15px;
}

.info_more-btn span {
  display: block;
  font-size: var(--fs-8);
}

.info_more-btn ion-icon { display: none; }

.separator { margin: 32px 0; }

.contacts-list { gap: 20px; }

.contact-info {
  max-width: calc(100% - 64px);
  width: calc(100% - 64px);
}



/**
 * #NAVBAR
 */

.navbar { border-radius: 20px 20px 0 0; }

.navbar-list { gap: 20px; }




/**
 * #ABOUT
 */

.about .article-title { margin-bottom: 20px; }

.about-text { margin-bottom: 40px; }

/* service */

.service-item {
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  gap: 18px;
  padding: 30px;
}

.service-icon-box {
  margin-bottom: 0;
  margin-top: 5px;
}

.service-content-box { text-align: left; }

/* testimonials */

.testimonials-title { margin-bottom: 25px; }

.testimonials-list {
  gap: 30px;
  margin: 0 -30px;
  padding: 30px;
  padding-bottom: 35px;
}

.content-card {
  padding: 30px;
  padding-top: 25px;
}

.testimonials-avatar-box {
  transform: translate(30px, -30px);
  border-radius: 20px;
}

.testimonials-avatar-box img { width: 80px; }

.testimonials-item-title {
  margin-bottom: 10px;
  margin-left: 95px;
}

.testimonials-text {
  line-clamp: 3;
  -webkit-line-clamp: 2;
}

/* testimonials modal */

.modal-container { padding: 10px; }

.testimonials-modal {
  display: flex;
  justify-content:center;
  align-items: stretch;
  gap: 25px;
  padding: 40px;
  border-radius: 20px;
}

.modal-img-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.modal-avatar-box {
  border-radius: 18px;
  margin-bottom: 0;
}

.modal-avatar-box img { width: 65px; }

.modal-img-wrapper > img {
  display: block;
  flex-grow: 1;
  width: 35px;
}

/* clients */

.clients-list {
  gap: 50px;
  margin: 0 -30px;
  padding: 45px;
  scroll-padding-inline: 45px;
}

.clients-item { min-width: calc(33.33% - 35px); }



/**
 * #CV
 */

.timeline-list { margin-left: 65px; }

.timeline-item:not(:last-child)::before { left: -40px; }

.timeline-item::after {
  height: 8px;
  width: 8px;
  left: -43px;
}

.skills-item:not(:last-child) { margin-bottom: 25px; }



/**
 * #PORTFOLIO, BLOG
 */

.project-img, .blog-banner-box { border-radius: 16px; }

.blog-posts-list { gap: 30px; }

.blog-content { padding: 25px; }



/**
 * #CONTACT
 */

.mapbox {
  height: 500px;
  border-radius: 5px;
}

.input-wrapper {
  gap: 30px;
  margin-bottom: 30px;
}

.form-input { padding: 15px 20px; }

textarea.form-input { margin-bottom: 30px; }

.form-btn {
  --fs-6: 16px;
  padding: 16px 20px;
}

.form-btn ion-icon { font-size: 18px; }

}





/**
* responsive larger than 768px screen
*/

@media (min-width: 768px) {

/**
 * REUSED STYLE
 */

.sidebar, article { width: 700px; }

.has-scrollbar::-webkit-scrollbar-button { width: 100px; }



/**
 * SIDEBAR
 */

.contacts-list {
  grid-template-columns: 1fr 1fr;
  gap: 30px 15px;
}



/**
 * NAVBAR
 */

.navbar-link { --fs-8: 15px; }



/**
 * ABOUT
 */

/* testimonials modal */

.testimonials-modal {
  gap: 35px;
  max-width: 680px;
}

.modal-avatar-box img { width: 80px; }



/**
 * PORTFOLIO
 */

.article-title { padding-bottom: 20px; }

.filter-select-box { display: none; }

.filter-list {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  gap: 25px;
  padding-left: 5px;
  margin-bottom: 30px;
}

.filter-item button {
  color: var(--light-gray);
  font-size: var(--fs-5);
  transition: var(--transition-1);
}

.filter-item button:hover { color: var(--light-gray-70); }

.filter-item button.active { color: var(--orange-yellow-crayola); }

/* portfolio and blog grid */

.project-list, .blog-posts-list { grid-template-columns: 1fr 1fr; }



/**
 * CONTACT
 */

.input-wrapper { grid-template-columns: 1fr 1fr; }

.form-btn {
  width: max-content;
  margin-left: auto;
}

}





/**
* responsive larger than 1024px screen
*/

@media (min-width: 1024px) {

/**
 * CUSTOM PROPERTY
 */

:root {

  /**
  * shadow
  */

  --shadow-1: -4px 8px 24px hsla(0, 0%, 0%, 0.125);
  --shadow-2: 0 16px 30px hsla(0, 0%, 0%, 0.125);
  --shadow-3: 0 16px 40px hsla(0, 0%, 0%, 0.125);

}



/**
 * REUSED STYLE
 */

.sidebar, article {
  width: 950px;
  box-shadow: var(--shadow-5);
}



/**
 * MAIN 
 */

main { margin-bottom: 60px; }

.main-content {
  position: relative;
  width: max-content;
  margin: auto;
  background-color: #AEC0D1;
}



/**
 * NAVBAR
 */

.navbar {
  position: absolute;
  bottom: auto;
  top: 0;
  left: auto;
  right: 0;
  width: max-content;
  border-radius: 0 20px;
  padding: 0 20px;
  box-shadow: none;
}

.navbar-list {
  gap: 30px;
  padding: 0 20px;
}




/**
 * ABOUT
 */

/* service */

.service-list {
  grid-template-columns: 1fr 1fr;
  gap: 20px 25px;
}

/* testimonials */

.testimonials-item { min-width: calc(50% - 15px); }

/* clients */

.clients-item { min-width: calc(25% - 38px); }



/**
 * PORTFOLIO
 */

.project-list { grid-template-columns: repeat(3, 1fr); }



/**
 * BLOG
 */

.blog-banner-box { height: 230px; }

}





/**
* responsive larger than 1250px screen
*/

@media (min-width: 1250px) {

/**
 * RESET
 */

body::-webkit-scrollbar { width: 20px; }

body::-webkit-scrollbar-track { background: var(--smoky-black); }

body::-webkit-scrollbar-thumb {
  border: 5px solid var(--smoky-black);
  background: hsla(0, 0%, 100%, 0.1);
  border-radius: 20px;
  box-shadow: inset 1px 1px 0 hsla(0, 0%, 100%, 0.11),
              inset -1px -1px 0 hsla(0, 0%, 100%, 0.11);
}

body::-webkit-scrollbar-thumb:hover { background: hsla(0, 0%, 100%, 0.15); }

body::-webkit-scrollbar-button { height: 60px; }



/**
 * REUSED STYLE
 */

.sidebar, article { width: auto; }

article { min-height: 100%; }



/**
 * MAIN
 */

main {
  max-width: 1200px;
  margin-inline: auto;
  display: flex;
  justify-content: center;
  align-items: stretch;
  gap: 25px;
}

.main-content {
  min-width: 75%;
  width: 75%;
  margin: 0;
  border-radius: 20px;
}



/**
 * SIDEBAR
 */

.sidebar {
  position: sticky;
  top: 60px;
  max-height: max-content;
  height: 100%;
  margin-bottom: 0;
  padding-top: 60px;
  z-index: 1;
}

.sidebar-info { flex-direction: column; }

.avatar-box img { width: 150px; }

.info-content .name {
  white-space: nowrap;
  text-align: center;
}

.info-content .title { margin: auto; }

.info_more-btn { display: none; }

.sidebar-info_more {
  opacity: 1;
  visibility: visible;
}

.contacts-list { grid-template-columns: 1fr; }

.contact-info :is(.contact-link) {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.contact-info :is(.contact-link, time, address) {
  --fs-7: 14px;
  font-weight: var(--fw-300);
}

.separator:last-of-type {
  margin: 15px 0;
  opacity: 0;
}

.social-list { justify-content: center; }



/**
 * CV
 */

.timeline-text { max-width: 700px; }

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
/* Style pour les titres des formations */
.timeline-title {
    color: #333; /* Couleur du texte */
    font-size: 22px; /* Taille de police */
    font-weight: bold; /* Gras */
    margin-bottom: 10px; /* Marge en bas */
}

/* Style pour la durée de la formation */
.timeline-duration {
    color: #05264e63; /* Couleur du texte */
    font-size: 16px; /* Taille de police */
    margin-bottom: 20px; /* Marge en bas */
}

/* Style pour le corps de la formation */
.timeline-body p {
    color: #05264E; /* Couleur du texte */
    font-size: 18px; /* Taille de police */
    line-height: 1.6; /* Hauteur de ligne */
    margin-bottom: 0; /* Marge en bas */
}

/* Style pour la timeline */
.timeline {
    position: relative;
    padding: 20px 0;
}

/* Style pour le contenu de la timeline */
.timeline-content {
    position: relative;
    padding: 30px;
    background-color: #ffffff1c; /* Couleur de fond */
    box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Ombre */
    border-radius: 5px; /* Bord arrondi */
    margin-bottom: 30px; /* Marge en bas */
    transition: all 0.3s ease; /* Animation de transition */
}

/* Style pour le contenu de la timeline au survol */
.timeline-content:hover {
    box-shadow: 0 4px 8px rgba(0,0,0,0.2); /* Ombre au survol */
    transform: translateY(-5px); /* Décalage vers le haut au survol */
}
/* Style pour la section de compétences */
#competences.profiles {
    padding: 80px 0; /* Espacement intérieur */
}

/* Style pour les profils */
.single-profile {
    position: relative;
    overflow: hidden;
    margin-bottom: 30px; /* Marge en bas */
}

/* Style pour le texte du profil */
.profile-txt {
    background-color: #ffffff00; /* Couleur de fond */
    padding: 32px; /* Espacement intérieur */
    text-align: center; /* Alignement du texte */
    transition: all 0.3s ease; /* Animation de transition */
}

/* Style pour le texte du profil au survol */
.single-profile:hover .profile-txt {
    transform: translateY(-20px); /* Décalage vers le haut au survol */
}

/* Style pour l'icône du profil */
.profile-txt i {
    font-size: 36px; /* Taille de l'icône */
    color: #333; /* Couleur de l'icône */
    margin-bottom: 10px; /* Marge en bas */
    display: block; /* Affichage en bloc */
}

/* Style pour le nom du profil */
.profile-icon-name {
    font-size: 18px; /* Taille du texte */
    color: #ffffff; /* Couleur du texte */
}

/* Style pour le survol de l'icône */
.single-profile-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0); /* Couleur de fond semi-transparente */
    opacity: 0; /* Opacité initiale */
    transition: all 0.3s ease; /* Animation de transition */
}

/* Style pour le survol de l'icône au survol */
.single-profile:hover .single-profile-overlay {
    opacity: 1; /* Opacité maximale au survol */
}
/* Style pour la section des projets */
#projets.portfolio-mf {
    padding: 80px 0; /* Espacement intérieur */
    background-color: #f8f9fa00; /* Couleur de fond */
}

/* Style pour la boîte de travail */
.work-box {
    position: relative;
    overflow: hidden;
    margin-bottom: 30px; /* Marge en bas */
    background-color: #ffffff00; /* Couleur de fond */
    border-radius: 5px; /* Bord arrondi */
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1); /* Ombre */
    transition: all 0.3s ease; /* Animation de transition */
    height: 120px;
}

/* Style pour le contenu du travail */
.work-content {
    padding: 20px; /* Espacement intérieur */
}

/* Style pour le titre du projet */
.work-content h2 {
    font-size: 20px; /* Taille de police */
    color: #333; /* Couleur du texte */
    margin-bottom: 10px; /* Marge en bas */
}

/* Style pour la description du projet */
.work-content .w-more {
    font-size: 16px; /* Taille de police */
    color: #666; /* Couleur du texte */
}

/* Style pour l'icône "plus" */
.work-content .w-like a {
    color: #333; /* Couleur de l'icône */
    font-size: 24px; /* Taille de l'icône */
}

.work-content .w-like a:hover {
    color: #007bff; /* Couleur de l'icône au survol */
}


  </style>