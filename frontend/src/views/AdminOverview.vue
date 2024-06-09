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
      <NavbarAdmin/>


    <main class="main-2" style="margin-top: 0px;overflow: hidden; height: 1500px;">
        <div class="nav-2" style="border-right: 1px solid #dee2e6 ;   max-width: 310px;">
        <nav class="nav-main-menu-2">
          <ul class="main-menu-2">
            <li>
                <router-link to="/AdminOverview" class="dashboard2 active" 
                ><img
                  src="template/assetss/imgs/template/icons/stack.svg"
                  alt="jobBox"
                /><span class="name">Overview</span></router-link
              >
            </li>
            <li>
              <router-link to="/EtuTable" class="dashboard2"
                ><img
                  src="template/assetss/imgs/template/icons/file-person.svg"
                  alt="jobBox"
                /><span class="name">Tous Les Etudiants</span></router-link
              >
            </li>
            <li>
              <router-link to="/EntTable" class="dashboard2" exact
                ><img
                  src="template/assetss/imgs/template/icons/building-fill-gear.svg"
                  alt="jobBox"
                /><span class="name">Toutes Les Entreprises</span></router-link
              >
            </li>
            <li>
              <router-link to="/OffreTable" class="dashboard2 " 
                ><img
                  src="template/assetss/imgs/template/icons/briefcase2.svg"
                  alt="jobBox"
                /><span class="name">Toutes Les Offres</span></router-link
              >
            </li>
          </ul>
        </nav>
        <div class="border-bottom mb-20 mt-20"></div>
      </div>

      <div class="row invoice-card-row" >
                  <div class="col-xl-3 col-xxl-3 col-sm-6">
                      <div class="card  invoice-card"  style="position: relative;background-color: #E7F0FA; left:250px;width: 280px;height: 100px;">
                          <div class="card-body d-flex">
                              <div class="icon me-3">
                                  <img src="/template/assets/imgs/template/icons/company.png" style="width: 60px;height: 60px;position: relative;left: 150px;border-radius: 10px;">
                                  
                              </div>
                              <div style="position: relative;right: 50px;">
                                  <h2 class="invoice-num" style="color: #6C6B6B;" >{{Companies}}</h2>
                                  <span  style="color: #6C6B6B;font-size: 20px;font-weight:700 ;">Entreprises</span>
                              </div>
                          </div>
                      </div>
                  </div>
                  <div class="col-xl-3 col-xxl-3 col-sm-6">
                      <div class="card  invoice-card" style="position: relative;background-color: #FCE0E0; left:440px;width: 280px;height: 100px;">
                          <div class="card-body d-flex" >
                              <div class="icon me-3">
                                  <img src="/template/assets/imgs/template/icons/etuds.png" style="width: 60px;height: 60px;position: relative;left: 150px;border-radius: 10px;">
                                  
                              </div>
                              <div style="position: relative;right: 50px;">
                                  <h2 class=" invoice-num" style="color: #6C6B6B;">{{students}}</h2>
                                  <span style="color: #6C6B6B; font-size: 20px;font-weight:700 ;">Etudiants</span>
                              </div>
                          </div>
                      </div>
                  </div>
                
                  
              </div>
              <div class="col-xl-3 col-xxl-3 col-sm-6">

 <div class="card" style="height: 285px;width:905px;position: relative;left:-300px;top:   140px;">
      <h2 class="section-title" style="color: #6C6B6B;font-size: 20px;position: relative;left:20px">Taux d'utilisateurs</h2>
      <canvas id="usersChart" width="400" height="100"></canvas>
  </div>
</div>

<div class="col-xl-3 col-xxl-3 col-sm-6">

    <div class="card"  style="height:350px;width:905px;position: relative;left:-650px;top:440px;">
      <h2 class="section-title" style="color: #6C6B6B;font-size: 20px;position: relative;left:20px">Statistiques des offres</h2>
      <canvas id="offersStatusChart" style="width: 50;height: 300px;"></canvas>
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
 import NavbarAdmin from '@/components/navbarAdmin.vue';
 import axios from "axios";
 import Chart from 'chart.js/auto';


 
 export default {
   components: { NavbarAdmin },
   data() {
     return {
       etudiant: {
         id: null
       },
       Companies:[],
       students:[],
       OffersTotal: 0,
      RecruitmentOffers: 0,
      SoonOffers: 0,
      ExpiredOffers: 0
      
    
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
   this.getAllCompanies();
   this.getAllStudents();
   this.   getUsersPerMonth();
   this.getOffersStatus();


     

   },
   methods: {
     stopPropagation(event) {
       event.stopPropagation();
     },
     getAllCompanies(){
        axios.get(`http://127.0.0.1:8000/totalentreprise/`)
        .then(response => {
           console.log('Données de réponse :', response.data);
           this.Companies = response.data.total_entreprises;
         })
         .catch(error => {
           console.error('Erreur lors de la récupération des favoris :', error);
         });
     },
     getAllStudents(){
        axios.get(`http://127.0.0.1:8000/totaletudiants/`)
        .then(response => {
           console.log('Données de réponse :', response.data);
           this.students = response.data.total_etudiants;
         })
         .catch(error => {
           console.error('Erreur lors de la récupération des favoris :', error);
         });
     },
     getUsersPerMonth() {
  axios.get('http://127.0.0.1:8000/api/users_per_month/')
    .then(response => {
      if (response.data && response.data.length > 0) {
        // Créer un objet pour stocker le nombre d'utilisateurs par mois
        const usersCountByMonth = {};

        // Initialiser le nombre d'utilisateurs à zéro pour chaque mois de l'année
        for (let month = 1; month <= 12; month++) {
          usersCountByMonth[month] = 0;
        }

        // Remplir l'objet avec le nombre d'utilisateurs réel par mois
        response.data.forEach(item => {
          // Extraire le numéro du mois à partir de la date
          const monthNumber = new Date(item.month).getMonth() + 1;
          usersCountByMonth[monthNumber] = item.count;
        });

        // Créer des listes séparées pour les mois et le nombre d'utilisateurs
        const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
        
        // Extraction des mois et formatage en noms abrégés
        const months = Object.keys(usersCountByMonth).map(month => monthNames[parseInt(month) - 1]);
        const usersCount = Object.values(usersCountByMonth);

        // Créer le graphique avec Chart.js
        const ctx = document.getElementById('usersChart').getContext('2d');
        new Chart(ctx, {
          type: 'line',
          data: {
            labels: months,
            datasets: [{
              label: 'Utilisateurs par mois',
              data: usersCount,
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
        console.error('Aucune donnée sur le nombre d\'utilisateurs inscrits par mois.');
      }
    })
    .catch(error => {
      console.error('Erreur lors de la récupération des données sur le nombre d\'utilisateurs inscrits par mois :', error);
    });
},
getOffersStatus() {
      axios.get('http://127.0.0.1:8000/api/offers_summary/')
        .then(response => {
          console.log('Données de réponse :', response.data);
          this.OffersTotal = response.data.total_offers;
          this.RecruitmentOffers = response.data.recruitment_offers;
          this.SoonOffers = response.data.soon_offers;
          this.ExpiredOffers = response.data.expired_offers;
          this.createChart();
        })
        .catch(error => {
          console.error('Erreur lors de la récupération des offres :', error);
        });
    },
    createChart() {
  const ctx = document.getElementById('offersStatusChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Offres Totales', 'En cours de recrutement', 'Soon', 'Expirées'],
      datasets: [{
        label: '',
        data: [this.OffersTotal, this.RecruitmentOffers, this.SoonOffers, this.ExpiredOffers],
        backgroundColor: ['#36A2EB', '#FFCE56', '#FF6384', '#4BC0C0']
      }]
    },
    options: {
      plugins: {
        legend: {
          display: false, // Masquer la légende
          position: 'top' // Positionner la légende en haut
        },
        title: {
          display: false // Masquer le titre
        }
      },
      responsive: true,
      scales: {
        x: {
          grid: {
            display: false // Masquer les lignes de la grille pour l'axe x
          }
        },
        y: {
          grid: {
            display: false // Masquer les lignes de la grille pour l'axe y
          },
          beginAtZero: true
        }
      }
    }
  });
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
.statistics {
  display: flex;
  justify-content: space-around;
  margin-top: 20px;
}

.stat {
  text-align: center;
  background: #f5f5f5;
  padding: 20px;
  border-radius: 10px;
  width: 20%;
}

.stat h3 {
  margin-bottom: 10px;
}

.stat p {
  font-size: 24px;
  font-weight: bold;
  margin: 0;
}


  </style>
  