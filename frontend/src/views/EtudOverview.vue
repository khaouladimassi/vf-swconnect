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
      <title>Overview</title>
      <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css" rel="stylesheet">
      <link href="https://cdn.tiny.cloud/1/YOUR_API_KEY/tinymce/5/tinymce.min.js" referrerpolicy="origin">
      <link rel="shortcut icon" type="image/x-icon" href="./template/assets/imgs/template/favicon.svg">
  
      <link href="/template/assets/css/plugins/animate.min.css" rel="stylesheet">
      <link href="/template/assets/css/plugins/magnific-popup.css" rel="stylesheet">
      <link href="/template/assets/css/plugins/perfect-scrollbar.css" rel="stylesheet">
      <link href="/template/assets/css/plugins/select2.min.css" rel="stylesheet">
      <link href="/template/assets/css/plugins/swiper-bundle.min.css" rel="stylesheet">
      
      <link href="/template/assets/css/stylecd4ee.css" rel="stylesheet">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    </head>
    <body>
      <NavbarEtudiant/>


    <main class="main-2" style="margin-top: 0px;overflow: hidden; height: 1500px;">
      <div class="nav-2" style="border-right: 1px solid #dee2e6;position: relative;top: 27px;">
        <nav class="nav-main-menu-2" >
          <ul class="main-menu-2">
            <li>
              <router-link :to="'/EtudOverview/' + this.etudiant.id"  class="active dashboard2" exact
                ><img
                  src="../assets/imgs/template/icons/stack.svg"
                  alt="jobBox"
                /><span class="name">Overview</span></router-link
              >
            </li>
            <li>
              <router-link :to="'/GenerationPortfolio/' + this.etudiant.id"
                ><img
                  src="../assets/imgs/template/icons/file-person.svg"
                  alt="jobBox"
                /><span class="name">Générer Portfolio</span></router-link>
              
            </li>
           
            <li>
              <router-link to="/Demandes"
                ><img
                  src="../assets/imgs/template/icons/briefcase2.svg"
                  alt="jobBox"
                /><span class="name">Mes Demades</span></router-link>
            </li>
            <li>
              <router-link :to="'/EtudDrive/' + this.etudiant.id"
                ><img
                  src="../assets/imgs/template/icons/folder.svg"
                  alt="jobBox"
                /><span class="name">Mon Drive</span></router-link>
            </li>
          </ul>
        </nav>
        <div class="border-bottom mb-20 mt-20"></div>
      </div>

            <!-- row -->
			<div class="container-fluid" style="position: relative;top: 17px;">
				<div class="row invoice-card-row"  >
					<div class="col-xl-3 col-xxl-3 col-sm-6" >
						<div class="card  invoice-card"  style="position: relative;background-color: #E7F0FA; left:-5px;width: 260px;">
							<div class="card-body d-flex">
								<div class="icon me-3">
									<img src="/template/assets/imgs/template/icons/offresDash.png" style="width: 70px;height: 70px;position: relative;left: 140px;top:-5px;border-radius: 10px;">
									
								</div>
								<div style="position: relative;left: -73px;width: 150px;">
									<h2 class="invoice-num" style="color: #313131;" >{{ OffresCount }}</h2>
									<span class=" fs-18" style="color: #6C6B6B;">Offres de stage</span>
								</div>
							</div>
						</div>
					</div>
					<div class="col-xl-3 col-xxl-3 col-sm-6">
						<div class="card  invoice-card" style="position: relative;background-color: #FCE0E0; left: -5px;width: 260px;">
							<div class="card-body d-flex" >
								<div class="icon me-3">
									<img src="/template/assets/imgs/template/icons/favorisDash.png" style="width: 70px;height: 70px;position: relative;left: 150px;border-radius: 10px;">
									
								</div>
								<div style="position: relative;left: -50px;">
									<h2 class=" invoice-num" style="color: #313131;">{{FavorisCount}}</h2>
									<span class=" fs-18" style="color: #6C6B6B;">Favoris</span>
								</div>
							</div>
						</div>
					</div>
					<div class="col-xl-3 col-xxl-3 col-sm-6">
						<div class="card  invoice-card" style="position: relative;background-color: #E7FAEB; left:-5px;width: 260px;">
							<div class="card-body d-flex">
								<div class="icon me-3">
									<img src="/template/assets/imgs/template/icons/notifDash.png" style="width: 70px;height: 70px;position: relative;left: 150px;border-radius: 10px;">

									
								</div>
								<div style="position: relative;left: -70px;">
									<h2 class=" invoice-num" style="color: #313131;">{{NotifsCount}}</h2>
									<span class=" fs-18" style="color: #6C6B6B;">Notifications</span>
								</div>
							</div>
						</div>
					</div>
					<div class="col-xl-3 col-xxl-3 col-sm-6">
						<div class="card  invoice-card" style="position: relative; background-color: #FFEED6; left:-5px;width: 260px;">
							<div class="card-body d-flex">
								<div class="icon me-3">
									<img src="/template/assets/imgs/template/icons/appliqueDash.png" style="width: 70px;height: 70px;position: relative;left: 150px;border-radius: 10px;">

								
								</div>
								<div style="position: relative;left: -80px;">
									<h2 class=" invoice-num" style="color: #313131;">{{DemandeCount}}</h2>
									<span class=" fs-18" style="color: #6C6B6B;">Offres appliqués</span>
								</div>
							</div>
						</div>
					</div>
				</div>

				<div class="row" style="position: relative; left:60px">

					<!--<div class="col-xl-9 col-xxl-12">
  <div class="card" style="background-color: #828282; opacity: 25%; height: 100%; padding-bottom: 30px;left: -65px;width: 101%;">
    <div class="card-body" style="height: 50px; position: relative; left:100px;">
      <div class="row align-items-center">
        <div class="col-xl-6">
          <i class="far fa-user-circle fa-4x" style="position: relative;left: -100px;top: -11px;color:#313131;"></i>
          <h4 class="card-title mb-2" style="position: relative;color: white;bottom: 60px;">Votre édition de profil n'est pas complète</h4>
        </div>
        <button style="position: relative;width: 20%; background-color: #828282;bottom: 30px;left: 65px;font-weight: 600;">
          <span style="color: white;">Compléter votre profil</span>
        </button>
      </div>
    </div>
  </div>
</div>-->

 
<div class="col-xl-3 col-xxl-5">
      <div class="card" style="position: relative; top: 27px; height: 260px; left: -65px; width: 420px;">
        <div class="card-header pb-0 border-0" style="background-color: white;">
          <h2 class="section-title" style="color: #808080; font-size: 28px; text-align: center;">Etat</h2>
          <!--<div style="position: relative; top: 30px; left: 15px;">
            <i class="fas fa-circle" style="color: #FBDCBE;"></i>
            <span style="color: #808080; font-size: 18px; padding: 10px;">En attente</span>
            <span id="pending-count" style="color: #808080; font-size: 18px; padding: 10px;">{{ pendingCount }}</span>
          </div>-->
          <!--<div style="position: relative; top: 30px; left: 10px; padding: 5px;">
            <i class="fas fa-circle" style="color: #B2F0C0;"></i>
            <span style="color: #808080; font-size: 18px; padding: 10px;">Accepté</span>
            <span id="accepted-count" style="color: #808080; font-size: 18px; padding: 10px;">{{ acceptedCount }}</span>
          </div>-->
          <!--<div style="position: relative; top: 30px; left: 10px; padding: 5px;">
            <i class="fas fa-circle" style="color: #F78080;"></i>
            <span style="color: #808080; font-size: 18px; padding: 10px;">Refusé</span>
            <span id="refused-count" style="color: #808080; font-size: 18px; padding: 10px;">{{ refusedCount }}</span>
          </div>-->
          <div class="circle-chart">
            <canvas id="myChart"></canvas>

            <!--<div class="circle-section section-accepted" :style="acceptedStyle"></div>
            <div class="circle-section section-refused" :style="refusedStyle"></div>
            <div class="circle-section section-pending" :style="pendingStyle"></div>-->
          </div>
        </div>
      </div>e
    </div>


	<div class="col-xl-3 col-xxl-7" style="position: relative; top: -270px; height: 295px; left: 140px;width: 846px;">
						
  <div class="card" >
		<h2 class="section-title" style="color: #808080;font-size: 27px;text-align: center;">Fréquence d'apparition de votre profil</h2>
  
        <!--<div class="chart-container">
            <svg class="chart" viewBox="0 0 800 700" xmlns="http://www.w3.org/2000/svg">
				<line x1="50" y1="250" x2="530" y2="250" stroke="#464E5F" stroke-width="1" opacity="0.3" />
                <line x1="50" y1="250" x2="50" y2="90" stroke="#464E5F" stroke-width="1"  opacity="0.3" />
    <text x="50" y="280" font-size="12">Jan</text>
    <text x="90" y="280" font-size="12">Fev</text>
    <text x="130" y="280" font-size="12">Mar</text>
    <text x="170" y="280" font-size="12">Avr</text>
    <text x="210" y="280" font-size="12">Mai</text>
    <text x="250" y="280" font-size="12">Jun</text>
    <text x="290" y="280" font-size="12">Jui</text>
    <text x="330" y="280" font-size="12">Aou</text>
    <text x="370" y="280" font-size="12">Sept</text>
    <text x="410" y="280" font-size="12">Oct</text>
    <text x="450" y="280" font-size="12">Nov</text>
    <text x="490" y="280" font-size="12">Dec</text>

                <text x="10" y="250" font-size="12">Faible</text>
                <text x="9" y="200" font-size="12">Moyen</text>
                <text x="9" y="150" font-size="12">Élevé</text>

				<path d="M50,250 Q150,150 250,200 Q350,250 350,150 Q400,100 500,150" fill="none" stroke="#C6DDFF" stroke-width="2" stroke-linecap="round" />
            </svg>
        </div>-->
        <canvas id="apparitionChart" height="180" width="560"></canvas>
    </div>
</div>


<div class="col-xl-6 col-xxl-7"  >
	<div class="card" style="background-color: white;position: relative; top: -252px; height: 270px;left: -63px;width: 627px;background-color: white;">
		<h2 class="section-title" style="color: #808080;font-size: 27px;text-align: center;">Fréquence des candidatures soumises</h2>

        <!--<div class="chart-container">
            <svg class="chart" viewBox="0 0 800 700" xmlns="http://www.w3.org/2000/svg">
				<line x1="50" y1="250" x2="530" y2="250" stroke="#464E5F" stroke-width="1" opacity="0.3" />
                <line x1="50" y1="250" x2="50" y2="90" stroke="#464E5F" stroke-width="1"  opacity="0.3" />
    <text x="50" y="280" font-size="12">Jan</text>
    <text x="90" y="280" font-size="12">Fev</text>
    <text x="130" y="280" font-size="12">Mar</text>
    <text x="170" y="280" font-size="12">Avr</text>
    <text x="210" y="280" font-size="12">Mai</text>
    <text x="250" y="280" font-size="12">Jun</text>
    <text x="290" y="280" font-size="12">Jui</text>
    <text x="330" y="280" font-size="12">Aou</text>
    <text x="370" y="280" font-size="12">Sept</text>
    <text x="410" y="280" font-size="12">Oct</text>
    <text x="450" y="280" font-size="12">Nov</text>
    <text x="490" y="280" font-size="12">Dec</text>

                <text x="10" y="250" font-size="12">Faible</text>
                <text x="9" y="200" font-size="12">Moyen</text>
                <text x="9" y="150" font-size="12">Élevé</text>

				<path d="M50,250 Q150,150 250,200 Q350,250 350,150 Q400,100 500,150" fill="none" stroke="#F78080" stroke-width="2" stroke-linecap="round"  opacity="0.51" />
            </svg>
        </div>-->
        <canvas id="candidatureChart" height="180" width="560"></canvas>

    </div>
</div>

					<div class="col-xl-6 col-xxl-12">
						<div class="card" style="height: 257px;width:435px;position: relative;left: 580px;top: -523px;background-color: white;">
							
							<div class="card-body tab-content p-0" style="background-color: white;">
								<h2 class="section-title" style="color: #808080;font-size: 25px;text-align: center;">Top domaines</h2>

								<div class="tab-pane active show fade"  role="tabpanel">

									<div class="table" style="position: relative;bottom: 36px;">
										<table class="table table-responsive-md card-table transactions-table table-borderless" >
											<tbody>
												<tr>
													<th style="position: relative;left: 7px;top: 55px;">
														<span style="color: #B8BFCC;">#</span>

													</th>
													<th style="position: relative;left: 5px;top: 55px;">
														<span class="fs-14" style="color: #B8BFCC;">Titre</span>
													</th>
													<th style="position: relative;left: 10px;top: 55px;">
														<span class="fs-14" style="color: #B8BFCC;">Popularité</span>

											</th >
													<th style="position: relative;left:2px;top: 55px;color: #B8BFCC;"><span class="fs-16 font-w600">Applications</span></th>
												</tr>
											
												<tr  v-for="(domaine, index) in topdomaines" :key="domaine.offer__domain">
													<td style="position: relative;left: 7px;top:46px;top: 47px;">
														<span >{{ (index + 1).toString().padStart(2, '0') }}</span>

													</td>
													<td style="position: relative;left: 10px;top:46px">
														<span class="fs-14">{{domaine.domain}} </span>
													</td>
													<td style="position: relative;left: 10px;top:36px">
														<div class="progress mt-4" style="height:10px; width:115px;background-color: #C3FFC9;">
													<div class="progress-bar progress-animated" :style="{ width: (domaine.total_demandes / this.topentreprises.reduce((acc, domaine) => acc + domaine.total_demandes, 0) * 100) + '% ', height: '10px', backgroundColor: 'cadetblue', opacity: 0.65 }" role="progressbar">
													</div>
												</div>
													</td>
													<td style="position: relative;left:25px;top:51px;color: #27C445;"><span style="color: cadetblue;font-size: 17px;font-weight: 700;">{{domaine.total_demandes}}</span></td>
												</tr>
												
												
									
											</tbody>
										</table>
									</div>
								</div>
								
								
							
							</div>
						</div>
					</div>
					<div class="col-xl-6 col-xxl-12">
						<div class="row">
							<div class="card" style="height: 257px;width:435px;position: relative;left:-50px;top: -495px;background-color: white;">
    <div class="card-body  p-0" style="background-color: white;">
        <h2 class="section-title" style="color: #808080;font-size: 25px;text-align: center;">Top Entreprises </h2>

        <div class="tab-pane active show fade"  role="tabpanel">

            <div class="entre" style="position: relative;bottom: 36px;">
                <table class="table table-responsive-md card-table table-borderless"> <!-- Ajoutez la classe table-borderless pour supprimer les bordures -->
                    <tbody>
                        <tr>
                            <th style="position: relative;left: 7px;top: 55px;">
                                <span style="color: #B8BFCC;">#</span>
                            </th>
                            <th style="position: relative;left: 5px;top: 55px;">
                                <span class="fs-14" style="color: #B8BFCC;">Titre</span>
                            </th>
                            <th style="position: relative;left: 10px;top: 55px;">
                                <span class="fs-14" style="color: #B8BFCC;">Popularité</span>
                            </th>
                            <th style="position: relative;left:2px;top: 55px;color: #B8BFCC;"><span class="fs-16  font-w600">Applications</span></th>
                        </tr>
                        
                        <tr v-for="(entreprise, index) in topentreprises" :key="entreprise.offer__entreprise__id">
                            <td style="position: relative;left: 7px;top: 47px;">
                                <span>{{ (index + 1).toString().padStart(2, '0') }}</span>
                            </td>
                            <td style="position: relative;left: 5px;top: 47px;">
                                <span class="fs-14">{{entreprise.offer__entreprise__nom}}</span>
                            </td>
                            <td style="position: relative;left: 10px;top: 37px;">
                                <div class="progress mt-4" style="height:10px; width:115px;background-color: #E7F0FA;">
                                    <div class="progress-bar  progress-animated" :style="{ width: (entreprise.total_demandes / this.topentreprises.reduce((acc, entreprise) => acc + entreprise.total_demandes, 0) * 100) + '% ', height: '10px', backgroundColor: '#447AB8', opacity: 0.65 }" role="progressbar">
                                    </div>
                                </div>
                            </td>
                            <td style="position: relative;left:25px;top: 47px;color: #447AB8;">
                                <span style="font-size: 17px;font-weight: 700;">{{entreprise.total_demandes}}</span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>

<div class="col-xl-3 col-xxl-5">
    <div class="card" style="height: 256px; width: 630px; position: relative; top: -495px; left: -47px; color: white;">
        <h2 class="section-title " style="color: #808080; font-size: 25px; text-align: center;">Technologies les plus demandées</h2>
        <div class="card-header pb-0 border-0 skill" style="background-color: transparent; position: relative; bottom: 196px;left: -40px;">
    <!-- Créer un seul <svg> pour les 4 compétences -->
    <svg width="600" height="400" xmlns="http://www.w3.org/2000/svg">
        <!-- Axes -->

        <!-- Compétences -->
        <!-- Utiliser  pour itérer sur les 4 premières compétences -->
        <template v-for="(skill, index) in topskills.slice(0, 4)" :key="index" >
            <!-- Décaler horizontalement chaque compétence en fonction de son index -->
            <rect :x="100 + index * 150" y="240" width="50" height="120" rx="10" ry="10" :fill="getSkillColor(skill[0])"/>
            <text :x="125 + index * 162" y="380" text-anchor="middle" >{{ skill[0] }}</text>
        </template>
    </svg>
</div>




       <!-- <div class="skills-container">
    <div class="axis-x">
        <div v-for="(skill, index) in topskills.slice(0, 4)" :key="index" class="skill">
            <span class="skill-name">{{ skill[0] }}</span> 
        </div>
    </div>
    <div class="chart">
        <div v-for="(skill, index) in topskills.slice(0, 4)" :key="index" class="bar">
            <div class="bar-inner" :style="{ height: skill[1] * 20 + 'px' }"></div> // Utiliser la deuxième valeur de chaque compétence (probablement le niveau de compétence) pour définir la hauteur du rectangle//
        </div>
    </div>
</div>-->

    </div>
</div>


						
					<!--<div class="col-xl-3 col-xxl-7" style="position: relative; top:  -489px; left: -287px;">
						
						<div class="card" style="width: 1075px; height: 305px">
							<h2 class="section-title" style="color: #808080;font-size: 27px;text-align: center;">L'activité d'utilisation du site</h2>
					
							<div class="chart-container-act">
								<svg class="chart" viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
									<line x1="50" y1="250" x2="900" y2="250" stroke="#464E5F" stroke-width="1" opacity="0.3" />
									<line x1="50" y1="250" x2="50" y2="30" stroke="#464E5F" stroke-width="1"  opacity="0.3" />
<text x="30" y="280" font-size="12">Jan</text>
<text x="100" y="280" font-size="12">Fev</text>
<text x="170" y="280" font-size="12">Mar</text>
<text x="240" y="280" font-size="12">Avr</text>
<text x="310" y="280" font-size="12">Mai</text>
<text x="380" y="280" font-size="12">Jun</text>
<text x="450" y="280" font-size="12">Jui</text>
<text x="520" y="280" font-size="12">Aou</text>
<text x="590" y="280" font-size="12">Sept</text>
<text x="660" y="280" font-size="12">Oct</text>
<text x="720" y="280" font-size="12">Nov</text>
<text x="777" y="280" font-size="12">Dec</text>

					
									<text x="10" y="250" font-size="12">20%</text>
									<text x="9" y="200" font-size="12">40%</text>
									<text x="9" y="150" font-size="12">60%</text>
									<text x="9" y="100" font-size="12">80%</text>
									<text x="9" y="50" font-size="12">100%</text>


					
                  <path d="M50,250 Q150,250 250,200 Q350,250 450,100 Q550,150 650,150" fill="none" stroke="#C6DDFF" stroke-width="2" stroke-linecap="round" />

<circle cx="50" cy="250" r="3" fill="#C6DDFF" />
<circle cx="250" cy="200" r="3" fill="#C6DDFF" />
<circle cx="450" cy="100" r="3" fill="#C6DDFF" />
<circle cx="650" cy="150" r="3" fill="#C6DDFF" />
								</svg>
							</div>
						</div>
					</div>-->
						
							
							
						</div>
					</div>
				</div>
            </div>





    </main>
    <div class="footer-2 mt-20" style="height: 99px;">
          <div class="container">
            <div class="box-footer-2">
              <div class="row">
                <div class="col-md-6 col-sm-12 mb-25 text-center text-md-start" style="position: relative;left: 14px;">
                  <p class="font-lg color-text-paragraph-made-by">
                    © 2024 - Made By SwConnect
                  </p>
                </div>
                
              </div>
            </div>
          </div>
        </div>
  </body>
    
  </template>
 <script>
 import NavbarEtudiant from '@/components/navbarEtudiant.vue';
 import axios from "axios";
 import Chart from 'chart.js/auto'; // Ajout de l'importation de Chart.js
 import 'chartjs-adapter-date-fns';
 
 export default {
   components: { NavbarEtudiant },
   data() {
     return {
       etudiant: {
         id: null
       },
       OffresCount: 0,
       offers: [],
       FavorisCount: 0,
       favoris: [],
       NotifsCount: 0,
       notifs: [],
       DemandeCount: 0,
       demandes: [],
       acceptedCount: 0,
       refusedCount: 0,
       pendingCount: 0, // Ajouté pour les demandes en attente
       apparitions: [],
       candidatureData: [],
       topentreprises:[],
       topdomaines:[],
       topskills:[]
    
    };
  },
 
   created() {
     const userId = localStorage.getItem("user_id");
     if (!userId) {
       alert("Vous devez vous connecter.");
       this.$router.push("/ConnexionView");
     } else {
       this.etudiant.id = userId;
     }
   },
   mounted() {
     this.getAlloffers();
     this.getAllfavoris();
     this.getAllNotifs();
     this.getAllDemandes();
     this.getDemandeStats(); // Ajoutez cet appel pour récupérer les statistiques
     this.fetchApparitionProfilParSemaine();
     this.fetchCandidatureData();
     this.getTopEntreprises();
     this.getTopDomains();
     this.getSkillsTopDomains();
     this.getTopTopDomains();
     

   },
   methods: {
     stopPropagation(event) {
       event.stopPropagation();
     },
     getAlloffers() {
       axios.get(`http://127.0.0.1:8000/api/offers/`)
         .then(response => {
           console.log('Données de réponse :', response.data);
           this.offers = response.data;
           this.OffresCount = this.offers.length;
         })
         .catch(error => {
           console.error('Erreur lors de la récupération des offres :', error);
         });
     },
     getAllfavoris() {
       axios.get(`http://127.0.0.1:8000/api/etudiant/${this.etudiant.id}/getFavoris/`)
         .then(response => {
           console.log('Données de réponse :', response.data);
           this.favoris = response.data;
           this.FavorisCount = this.favoris.length;
         })
         .catch(error => {
           console.error('Erreur lors de la récupération des favoris :', error);
         });
     },
     getAllNotifs() {
       axios.get(`http://127.0.0.1:8000/notifications/${this.etudiant.id}/`)
         .then(response => {
           console.log('Données de réponse :', response.data);
           this.notifs = response.data;
           this.NotifsCount = this.notifs.length;
         })
         .catch(error => {
           console.error('Erreur lors de la récupération des notifications :', error);
         });
     },
     getAllDemandes() {
       axios.get(`http://127.0.0.1:8000/api/demande/etudiant/${this.etudiant.id}/`)
         .then(response => {
           console.log('Données de réponse :', response.data);
           this.demandes = response.data;
           this.DemandeCount = this.demandes.length;
         })
         .catch(error => {
           console.error('Erreur lors de la récupération des demandes :', error);
         });
     },
     getDemandeStats() {
       axios.get(`http://127.0.0.1:8000/demande/stats/${this.etudiant.id}/`)
         .then(response => {
           console.log('Statistiques des demandes :', response.data);
           this.acceptedCount = response.data.accepted_count;
           this.refusedCount = response.data.refused_count;
           this.pendingCount = response.data.pending_count;
 
           new Chart(document.getElementById('myChart').getContext('2d'), {
             type: 'doughnut',
             data: {
               labels: ['Accepté', 'Refusé', 'En attente'],
               datasets: [{
                 label: '# of Votes',
                 data: [this.acceptedCount, this.refusedCount, this.pendingCount],
                 backgroundColor: [
                   'rgba(75, 192, 192, 0.2)',
                   'rgba(255, 99, 132, 0.2)',
                   'rgba(255, 206, 86, 0.2)'
                 ],
                 borderColor: [
                   'rgba(75, 192, 192, 1)',
                   'rgba(255, 99, 132, 1)',
                   'rgba(255, 206, 86, 1)'
                 ],
                 borderWidth: 1
               }]
             },
             options: {
               responsive: true,
               maintainAspectRatio: false,
               plugins: {
                 legend: {
                   display: true,
                   position: 'right',
                   labels: {
                     font: {
                       size: 12
                     }
                   }
                 }
               }
             }
           });
         })
         .catch(error => {
           console.error('Erreur lors de la récupération des statistiques des demandes :', error);
         });
     },
    
     async fetchApparitionProfilParSemaine() {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/apparition_profil/semaine/${this.etudiant.id}/`);
        console.log('apparitions :', response.data);
        this.apparitions = response.data;
        this.renderChart();
      } catch (error) {
        console.error('Erreur lors de la récupération des données:', error);
      }
    },
    renderChart() {
      
      const labels = this.apparitions.map(item => item.date);
      const data = this.apparitions.map(item => item.nombre_apparitions);

      new Chart(document.getElementById('apparitionChart').getContext('2d'), {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: 'Apparitions de profil',
            data: data,
            borderColor: '#447AB8',
            borderWidth: 2,
            fill: false
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
              ticks: {
                callback: function(value) {
                  if (value < 3) return 'Faible';
                  if (value < 10) return 'Moyen';
                  return 'Élevé';
                }
              }
            },
            x: {
              type: 'time',
              time: {
                unit: 'day',
                tooltipFormat: 'yyyy-MM-dd'
              }
            }
          }
        }
      });
    },
    fetchCandidatureData() {
  const userId = localStorage.getItem("user_id");
  axios
    .get(`http://127.0.0.1:8000/api/candidature/frequency/${userId}/`)
    .then((response) => {
      // Vérifier si les données sont disponibles
      if (response.data && response.data.length > 0) {
        // Store the fetched candidature frequency data
        this.candidatureData = response.data;
        console.log("Fetched candidature data", this.candidatureData);
        // Render the chart
        this.renderChartCandidate();
      } else {
        console.error("No candidature data received");
      }
    })
    .catch((error) => {
      console.error("Error fetching candidature data:", error);
      // Handle error response if needed
    });
},

renderChartCandidate() {
  const ctx = document.getElementById("candidatureChart");
  if (!ctx) {
    console.error("Canvas element not found");
    return;
  }
  const chartContext = ctx.getContext("2d");
  
  // Vérifier si les données sont disponibles
  if (!this.candidatureData || this.candidatureData.length === 0) {
    console.error("No candidature data available to render chart");
    return;
  }

  const labels = this.candidatureData.map((item) => item.date);
  const data = this.candidatureData.map((item) => item.frequency);

  new Chart(chartContext, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Fréquence de candidature",
          data: data,
          borderColor: "#F78080",
          borderWidth: 2,
          fill: false,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
          ticks: {
            callback: function(value) {
              if (value < 3) return 'Faible';
              if (value < 10) return 'Moyen';
              return 'Élevé';
            }
          }
        },
        x: {
          type: "time",
          time: {
            unit: "day",
            tooltipFormat: 'yyyy-MM-dd',
          },
        },
      },
    },
  });
},
getTopEntreprises() {
  axios.get('http://127.0.0.1:8000/api/top-companies/')
    .then(response => {
      console.log('topentreprises :', response.data);
      this.topentreprises = response.data;
    })
    .catch(error => {
      console.error('Erreur lors de la récupération des offres :', error);
    });
},
getTopDomains() {
  axios.get('http://127.0.0.1:8000/api/top-domaines/')
    .then(response => {
      console.log('topdomaines :', response.data);
      this.topdomaines = response.data;
    })
    .catch(error => {
      console.error('Erreur lors de la récupération des offres :', error);
    });
},
// Méthode pour récupérer les noms des 3 meilleurs domaines
getTopTopDomains() {
  axios.get('http://127.0.0.1:8000/api/top-domaines/')
    .then(response => {
      console.log('Top domains:', response.data);
      this.topdomains = response.data;
      
      // Récupérer les compétences pour chaque domaine
      this.topdomains.forEach(domain => {
        this.getSkillsTopDomains(domain.domain); // Accédez à la propriété 'domain' au lieu de 'offer__domain'
      });
    })
    .catch(error => {
      console.error('Error fetching top domains:', error);
    });
},

// Méthode pour récupérer les compétences pour un domaine donné
getSkillsTopDomains(domain) {
  axios.get(`http://127.0.0.1:8000/top-skills/${domain}/`)
    .then(response => {
      console.log(`Skills for top domain ${domain}:`, response.data);
      // Ajoutez les compétences récupérées à une liste ou une structure de données appropriée au lieu de les écraser
      // Par exemple, si vous voulez stocker les compétences pour chaque domaine séparément
      // Vous pouvez utiliser un objet où la clé est le domaine et la valeur est la liste des compétences
      // this.topskills[domain] = response.data; // Utilisez cette approche si vous voulez stocker les compétences pour chaque domaine séparément
      // Ou si vous voulez simplement avoir une liste de toutes les compétences sans distinction de domaine
      // Vous pouvez concaténer les nouvelles compétences à la liste existante
      this.topskills.push(...response.data); // Utilisez cette approche si vous voulez une liste de toutes les compétences sans distinction de domaine
    })
    .catch(error => {
      console.error(`Error fetching skills for top domain ${domain}:`, error);
    });
},

getSkillColor() {
      // Logique pour déterminer la couleur
      // Par exemple, vous pouvez utiliser un mapping de couleur
      // Ici, nous utilisons simplement des couleurs aléatoires pour l'exemple
      const colors = ['rgb(252, 224, 224)', 'rgb(231, 240, 250)', 'rgb(255, 238, 214)', 'rgb(231, 250, 235)'];
      const index = Math.floor(Math.random() * colors.length);
      return colors[index];
    }








   }
 };
 </script>


 
  <style scoped>
.circle-chart {
  position: relative;
  width: 310px;
  height: 310px;
  left: 50px;
    top: -61px;
}


    .modal {
      display: block;
      position: fixed;
      z-index: 1;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.5);
    }
    
    .modal-content {
      background-color: #fefefe;
      margin: 15% auto;
      padding: 20px;
      border: 1px solid #888;
      width: 80%;
      max-width: 400px;
      text-align: center;
    }
    
    .close {
      position: relative;
      color: #aaa;
     left: 50%;
     bottom: 25px;
      font-size: 40px;
      font-weight: bold;
    }
    
    .close:hover,
    .close:focus {
      color: black;
      text-decoration: none;
      cursor: pointer;
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
    display: block;
    left: auto !important;
    right: 0;
    min-width: 13rem;
  }
  .icon-plus {
    padding: 8px;
  }
  .btn-modal {
    width: 100%;
    height: 49.5px;
    background-color: #f2f4fa;
    color: #313131;
    border: 1px solid #dee2e6;
    font-size: 18px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .custom-svg {
    width: 47px; /* Adjust width as needed */
    fill: #447ab8; /* Fill color */
    margin-right: 14px;
    margin-left: 10px;
  }
  .custom-png {
    width: 62px;
    height: 35px;
    margin-right: 10px;
    margin-top: 5px;
  }
  .input-group-prepend {
    display: flex;
    border-top: #dee2e6 solid 1px;
    border-bottom: #dee2e6 solid 1px;
    border-left: #dee2e6 solid 1px;
  }
  .input-group-prepend img {
    padding-left: 21px;
  }
  .btn-lien {
    width: 145px;
    padding-left: 0px;
    font-size: 18px;
    display: flex;
    align-items: center;
  }
  .btn-lien-1 {
    width: 135px;
    padding-left: 0px;
    font-size: 18px;
    display: flex;
    align-items: center;
  }
  .col-lg-1222 {
    flex: 0 0 auto;
    width: 100%;
  }
  .col-lg-9 {
    flex: 0 0 auto;
    width: 100%;
  }
  .panel-white-2 {
    height: 1440px;
  }
  .form-control {
    height: 50px;
  }
  .col-md-3-2 {
    flex: 0 0 auto;
    width: 35%;
  }
  .col-md-100 {
    flex: 0 0 auto;
    width: 100%;
    max-width: 2000px;
  }
  .btn-pre-1 {
    margin-left: 30px;
  }
  .btn-pre-2 {
    margin-left: 30px;
  }
  .drag-drop-area {
    background-color: #f0f0f0; /* Background color */
    border: 2px dashed #ccc; /* Border style */
    border-radius: 10px; /* Rounded corners */
    height: 200px; /* Height */
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    text-align: center;
  }
  .input-group {
    width: 100%;
    max-width: 2000px;
    margin: 0 auto;
    margin-right: 0px;
  }
  .wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    overflow-x: auto;
    padding: 10px;
    border-bottom: 2px solid #ccc;
    margin-bottom: 35px;
  }
  .tab-box {
    display: flex;
    flex-wrap: nowrap;
  }
  .tab {
    padding: 10px 20px;
    margin-right: 10px;
    cursor: pointer;
    background-color: #ffffff;
    color: #313131;
    font-family: "Plus Jakarta Sans", sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 16px;
  }
  .tab.active {
    color: #447ab8 !important;
    font-family: "Plus Jakarta Sans", sans-serif;
    font-style: normal;
    font-weight: 700;
    font-size: 17px;
    border-bottom: #447ab8 solid 3px;
  }
  /* Styles for the tab content */
  .tab-content {
    padding: 30px;
    border: 1px solid #dee2e6;
    border-top: none;
    border-right: none;
    background-color: #f2f4fa;
    border-radius: 9px;
  }
  .tab-content.active {
    display: block;
  }
  /* Styles for the draggable tab */
  .icon {
    cursor: pointer;
    margin: 0 10px;
  }
  .search-span {
    width: 49px;
    display: flex;
    justify-content: center;
  }
  .header .main-menu li a {
    font-family: "Plus Jakarta Sans", sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 20px;
    line-height: 18px;
    color: #FFFFFF;
    display: block;
    padding: 0px;
    text-decoration: none;
    position: relative;
}
.main-2{
  height: 550px;
}
.upload-container {
    position: relative;
    border: 2px dashed #ccc;
    width: 80%;
    height: 220px;
    top: 50px;
    padding: 10px;
    left: -45px;
  
}
.container2 {
    max-width: 1330px;
    width: 100%;
    margin: 0 auto;
    align-items: center;
    justify-content: space-between;
    position: relative;
    top: 15px;
}
.footer-2 .box-footer-2 {
    padding: 25px 0px 0px 0px;
    border-top: 1px solid #E0E6F6;
}
.main-2 .nav-2 {
    max-width: 280px;
    width: 100%;
    padding: 10px;
    background-color: #ffffff;
    position: relative;
    bottom: 0px;
    display: inline-block !important;
}


.skills-container {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}

.axis-x {
    display: flex;
    flex-direction: column;
}

.skill {
    margin-bottom: 10px;
}

.skill-name {
    font-weight: bold;
    color: #007bff;
}

.chart {
    display: flex;
    flex-direction: column;
}



  </style>
  