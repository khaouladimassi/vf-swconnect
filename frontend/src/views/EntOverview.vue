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
      <NavbarEntreprise/>


    <main class="main-2" style="margin-top: 10px;overflow: hidden; height: 1000px;">
        <div class="nav-2" style="border-right: 1px solid #dee2e6">
        <nav class="nav-main-menu-2">
          <ul class="main-menu-2">
            <li>
              <a class=" active dashboard2" :href="'/EntOverview/' + entreprise.id"
                ><img
                  src="../assets/imgs/template/icons/stack.svg"
                  alt="jobBox"
                /><span class="name">Overview</span></a
              >
            </li>
            <li>
              <router-link to="/BookGeneration"  class="dashboard2" href="candidates.html"
                ><img
                  src="../assets/imgs/template/icons/file-person.svg"
                  alt="jobBox"
                /><span class="name">Générer Pfe Book</span></router-link
              >
            </li>
            <li>
              <router-link to="/PostView" class="dashboard2" 
                ><img
                  src="../assets/imgs/template/icons/plus-circle.svg"
                  alt="jobBox"
                /><span class="name">Publier Un Offre</span></router-link
              >
            </li>
            <li>
              <a class=" dashboard2" href="/MesOffres"
                ><img
                  src="../assets/imgs/template/icons/briefcase2.svg"
                  alt="jobBox"
                /><span class="name">Mes Offres</span></a
              >
            </li>
            <li>
              <router-link :to="'/EtudDrive/' + this.entreprise.id"
                ><img
                  src="../assets/imgs/template/icons/folder.svg"
                  alt="jobBox"
                /><span class="name">Mon Drive</span></router-link>
            </li>
          </ul>
        </nav>
        <div class="border-bottom mb-20 mt-20"></div>
      </div>

      <div class="content-body" style="width: 900px;position: relative;left: 30px;">

<div class="intro">
  <span style="font-size: 24px; color: #333; font-family: Arial, sans-serif;">Bonjour,</span><br>
  <span style="font-size: 18px; color: #666; font-family: Arial, sans-serif;">Voici vos candidats et demandes quotidiennes</span>
</div>

<div class="row invoice-card-row" >
                  <div class="col-xl-3 col-xxl-3 col-sm-6">
                      <div class="card  invoice-card"  style="position: relative;background-color: #E7F0FA; left:5px;width: 250px;">
                          <div class="card-body d-flex">
                              <div class="icon me-3">
                                  <img src="/template/assets/imgs/template/icons/offresDash.png" style="width: 60px;height: 60px;position: relative;left: 150px;border-radius: 10px;">
                                  
                              </div>
                              <div style="position: relative;right: 50px;">
                                  <h2 class="invoice-num" style="color: #313131;" >{{OfferCount}}</h2>
                                  <span class=" fs-18" style="color: #6C6B6B;">Offres de stage</span>
                              </div>
                          </div>
                      </div>
                  </div>
                  <div class="col-xl-3 col-xxl-3 col-sm-6">
                      <div class="card  invoice-card" style="position: relative;background-color: #FCE0E0; left:50px;width: 250px;">
                          <div class="card-body d-flex" >
                              <div class="icon me-3">
                                  <img src="/template/assets/imgs/template/icons/demands.png" style="width: 60px;height: 60px;position: relative;left: 150px;border-radius: 10px;">
                                  
                              </div>
                              <div style="position: relative;right: 50px;">
                                  <h2 class=" invoice-num" style="color: #313131;">{{DemandsCount}}</h2>
                                  <span class=" fs-18" style="color: #6C6B6B;">Demandes</span>
                              </div>
                          </div>
                      </div>
                  </div>
              
                  
              </div>

<div class="offrepublie" style="padding-bottom: 25px;">
<div style="font-size: 18px; color: #666; font-family: Arial, sans-serif;position: relative;left: 5px;top:47px;">
  Offres Publiées Récemment
</div>
<table class="table" style="position: relative;top: 55px;">
  <thead style="background-color: #E5E8F3;" >
    <tr>
      <th scope="col">Offres</th>
      <th scope="col">Demandes</th>
      <th scope="col">Accepté</th>
      <th scope="col">Refusé</th>
      <th scope="col" >En attente</th>
    </tr>
  </thead>
  <tbody>
   
    <tr v-for="offer in offerData" :key="offer.title">
<td scope="row">
<h2 class="invoice-num" style="color: #313131; font-size: 15px; line-height: 1;">{{ offer.title }}</h2>
</td>   
<td>  <i class="fas fa-user" style="font-size: 20px;color:  #818181;"></i>
  <span class="fs-18" style="color: #818181; font-size: 16px;padding: 7px;">{{ offer.total_demandes }}</span>

</td>     
<td>  
        <i class="fas fa-check-circle" style="color: #1BA836; font-size: 18px;">
        </i>
        <span class="fs-18" style="color: #1BA836; font-size: 16px;padding:3px;font-weight: 600;">{{offer.demandes_acceptees}}</span>

     </td>
  

     <td>
  <!--<button type="button" class="btn btn-sm">Voir Demandes</button>-->
  <i class="fas fa-times-circle" style="color: red; font-size: 18px;">
        </i>
        <span class="fs-18" style="color: red; font-size: 16px;padding:3px;font-weight: 600;">{{  offer.demandes_refusees}}</span>
</td>
<td>

  <i class="fas fa-clock" style="color: #FFC107; font-size: 18px;"></i>
      
        <span class="fs-18" style="color: #FFC107; font-size: 16px;padding:3px;font-weight: 600;">{{  offer.demandes_en_attente}}</span>
</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="card" style="height: 285px;width:490px;position: relative;left:5px;top:50px;">
                          
                          <div class="card-body tab-content p-0"  >
                              <h2 class="section-title" style="position: relative;color: #05004E;font-size: 20px;padding: 3px;left: 15px;">Top Offres Visitées </h2>

                              <div class="tab-pane active show fade"  role="tabpanel">

                                  <div class="table2" style="position: relative;bottom: 36px;left: 15px;height: 220px;">
                                      <table class="table2 table-responsive-md card-table transactions-table">
                                          <tbody>
                                              <tr style="position: relative;top: 35px;">
                                                  <th >
                                                      <span style="color: #B8BFCC; ">#</span>

                                                  </th>
                                                  <th >
                                                      <span class="fs-14" style="color: #B8BFCC;position: relative;left:40px">Titre</span>
                                                  </th>
                                                  <th >
                                                      <span class="fs-14" style="color: #B8BFCC;position: relative;left: 80px;">Popularité</span>

                                          </th >
                                                  <th><span class="fs-14" style="color: #B8BFCC;position: relative;left:100px;">Demandes</span></th>
                                              </tr>
                                          
                                              <tr v-for="(offer, index) in top_offers" :key="offer.title">
                                                  <td style="position: relative;left: 7px;top: 47px;">
                                                      <span >{{ (index + 1).toString().padStart(2, '0') }}</span>

                                                  </td>
                                                  <td style="position: relative;left:40px;top: 47px;width:70px">
                                                      <span class="fs-14">{{offer.title}}</span>
                                                  </td>
                                                  <td style="position: relative;left: 80px;top: 47px;">
                                                      <div class="progress mt-4" style="height:10px; width:115px;background-color: #E7F0FA;">
                                                  <div class="progress-bar  progress-animated" :style="{ width: (offer.total_demandes / this.top_offers.reduce((acc, offer) => acc + offer.total_demandes, 0) * 100) + '% ', height: '10px', backgroundColor: '#447AB8', opacity: 0.55 }" role="progressbar">
                                                  </div>
                                              </div>
                                                  </td >
                                                  <td style="position: relative;left:130px;top: 47px;color: #447AB8;"><span style="font-size: 17px;font-weight: 700;">{{offer.total_demandes}}</span></td>
                                              </tr>
                                          
                                        

                     
                                              
                                  
                                          </tbody>
                                      </table>
                                  </div>
                              </div>
                              
                              
                          
                          </div>
            </div>

<div class="card" style="height: 285px;width:520px;position: relative;left:56.2%;top:   -234px;">
      <h2 class="section-title" style="color: #05004E;font-size: 20px;position: relative;left:20px">Offres Publiées</h2>

      
      <canvas id="offersChart" width="400" height="180"></canvas>


   
 
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
import NavbarEntreprise from '@/components/navbarEntreprise.vue';
import axios from "axios";
import Chart from 'chart.js/auto';

  
  export default {
    components:{ NavbarEntreprise},
    data() {
      return {
        isDropdownOpen: false,
        entreprise: {
            id: null
        },
        OfferCount:0,
        DemandsCount:0,
        offerData:[],
        top_offers: [],
        offersData: [],

     





        
      };
    },
    created() {
    const userId = localStorage.getItem("user_id");
    if (!userId) {
        alert("Vous devez vous connecter.");
        this.$router.push("/ConnexionView");
    } else {
        // Stockez l'ID de l'utilisateur dans this.etudiant.id
        this.entreprise.id = userId;
    }
},
mounted(){
    this.getAllOfferByEntreprise();
    this. getAllDemandsByEntreprise();
    this. getAllStatusDemandsByOffer();
    this.getTopOffers();
    this.getOffersPerMonth();

},
    methods: {
    
       
  stopPropagation(event) {
          event.stopPropagation();
        },
        toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen;
    },
    getAllOfferByEntreprise(){
        axios.get(`http://127.0.0.1:8000/entreprise/${this.entreprise.id}/total_offers/`)
        .then(response => {
           console.log('Données de réponse :', response.data);
           this.OfferCount = response.data.total_offers;
         })
         .catch(error => {
           console.error('Erreur lors de la récupération des favoris :', error);
         });
     },
     getAllDemandsByEntreprise(){
        axios.get(`http://127.0.0.1:8000/entreprise/${this.entreprise.id}/total_demands/`)
        .then(response => {
           console.log('Données de réponse :', response.data);
           this.DemandsCount = response.data.total_demandes;
         })
         .catch(error => {
           console.error('Erreur lors de la récupération des favoris :', error);
         });
     },
     getAllStatusDemandsByOffer() {
  axios.get(`http://127.0.0.1:8000/entreprise/${this.entreprise.id}/recent_offers/`)
    .then(response => {
      console.log('Données de réponse :', response.data);
      // Assurez-vous que response.data.recent_offers est une liste
      if (response.data.recent_offers && response.data.recent_offers.length > 0) {
        // Réinitialiser les variables
        this.offerData = response.data.recent_offers.map(offer => {
          return {
            title: offer.title,
            total_demandes: offer.total_demandes,
            demandes_acceptees: offer.demandes_acceptees,
            demandes_refusees: offer.demandes_refusees,
            demandes_en_attente: offer.demandes_en_attente
          };
        });
      } else {
        console.error('Aucune offre récente trouvée.');
      }
    })
    .catch(error => {
      console.error('Erreur lors de la récupération des offres récentes :', error);
    });
},
getTopOffers() {
  axios.get(`http://127.0.0.1:8000/entreprise/${this.entreprise.id}/top_offers/`)
    .then(response => {
      console.log('Données de réponse :', response.data);
      // Assurez-vous que response.data.top_offers est une liste
      if (response.data.top_offers && response.data.top_offers.length > 0) {
        // Réinitialiser les variables
        this.top_offers = response.data.top_offers.map(offer => {
          return {
            title: offer.title,
            total_demandes: offer.total_demandes,
          };
        });
      } else {
        console.error('Aucune offre récente trouvée.');
      }
    })
    .catch(error => {
      console.error('Erreur lors de la récupération des meilleures offres :', error);
    });
},
getOffersPerMonth() {
  axios.get(`http://127.0.0.1:8000/entreprise/${this.entreprise.id}/offers_per_month/`)
    .then(response => {
      if (response.data.offers_per_month && response.data.offers_per_month.length > 0) {
        // Créer un objet pour stocker le nombre d'offres par mois
        const offersCountByMonth = {};

        // Initialiser le nombre d'offres à zéro pour chaque mois de l'année
        for (let month = 1; month <= 12; month++) {
          offersCountByMonth[month] = 0;
        }

        // Remplir l'objet avec le nombre d'offres réel par mois
        response.data.offers_per_month.forEach(item => {
          offersCountByMonth[item.month_number] = item.offers_count;
        });

        // Créer des listes séparées pour les mois et le nombre d'offres
        const monthNames = [
  "Jan", "Feb", "Mar", "Apr", "May", "Jun",
  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
];

// Extraction des mois et formatage en noms abrégés
        const months = Object.keys(offersCountByMonth).map(month => monthNames[parseInt(month) - 1]);
        const offersCount = Object.values(offersCountByMonth);

        // Créer le graphique avec Chart.js
        const ctx = document.getElementById('offersChart').getContext('2d');
        new Chart(ctx, {
          type: 'line',
          data: {
            labels: months,
            datasets: [{
              label: 'Offres par mois',
              data: offersCount,
              backgroundColor: 'rgba(54, 162, 235, 0.2)',
              borderColor: 'rgba(54, 162, 235, 1)',
              borderWidth: 1
            }]
          },
          options: {
            scales: {
              y: {
                beginAtZero: true
              }
            }
          }
        });
      } else {
        console.error('Aucune donnée sur le nombre d\'offres publiées par mois.');
      }
    })
    .catch(error => {
      console.error('Erreur lors de la récupération des données sur le nombre d\'offres publiées par mois :', error);
    });
}

      }
    
  
  
  
    
  };
  </script>
  <style scoped>
  .circle-chart {
  position: relative;
  width: 200px;
  height: 200px;
  border-radius: 50%;
  border: 5px solid #ffffff; /* bordure grise */
  overflow: hidden; /* pour masquer le contenu en dehors du cercle */
}

.circle-section {
  position: absolute;
  width: 100%;
  height: 100%;
  clip: rect(0, 100px, 200px, 0); /* pour diviser le cercle en demi-cercles */
  border-radius: 50%;
}

.section-1 {
  background-color: #F78080; /* première couleur */
  transform: rotate(0deg);
}

.section-2 {
  background-color: #FBDCBE; /* deuxième couleur */
  transform: rotate(120deg);
}

.section-3 {
  background-color: #B2F0C0; /* troisième couleur */
  transform: rotate(240deg);
}

.circle-chart::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100px;
  height: 100px;
  border-radius: 50%;
  border: 5px solid #ffffff; /* bordure grise */
  background-color: white;
}
.chart-container {
	position: relative;
  width: 800px;

  bottom: 76px;
  left: 25px;
}
.chart-container-act{
  position: relative;
  width: 840px;

  bottom: 46px;
  left: 100px;
}
.container-fluid{
height: 950px;
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
    /*border: 1px solid #dee2e6;*/
    border-top: none;
    border-right: none;
    /*background-color: #f2f4fa;*/
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
 .dropdown-button{
    border: none;
    background: none;
    padding: 0;
    font-size: 24px;
    line-height: 1;
  }
  .dropdown-toggle:hover {
    cursor: pointer;
  }
  </style>
  