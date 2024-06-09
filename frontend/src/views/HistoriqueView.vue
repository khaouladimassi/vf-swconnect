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
      <title>Historique</title>
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
        <navbarEntreprise v-if="userType === 'entreprise'" />
        <navbarEtudiant v-if="userType === 'etudiant'" />
        <navbarAdmin v-if= "userType === 'admin'" />
    <main class="main-2" style="margin-top: 0px;">
      <div class="nav-2" style="border-right: 1px solid #dee2e6">
        <nav v-if="userType === 'entreprise'" class="nav-main-menu-2">
          <ul class="main-menu-2">
            <li>
              <router-link :to="'/EntOverview/' + entreprise.id">
                <img src="../assets/imgs/template/icons/stack.svg" alt="jobBox" />
                <span class="name">Overview</span>
              </router-link>
            </li>
            <li>
              <router-link to="/BookGeneration"  class="dashboard2" >
                <img src="../assets/imgs/template/icons/file-person.svg" alt="jobBox" />
                <span class="name">Générer Pfe Book</span>
              </router-link>
            </li>
            <li>
              <router-link to="/PostView" class="dashboard2">
                <img src="../assets/imgs/template/icons/plus-circle.svg" alt="jobBox" />
                <span class="name">Publier Un Offre</span>
              </router-link>
            </li>
            <li>
              <a class="active dashboard2" :href="'/MesOffres/' + entreprise.id">
                <img src="../assets/imgs/template/icons/briefcase2.svg" alt="jobBox" />
                <span class="name">Mes Offres</span>
              </a>
            </li>
            <li>
              <a class="dashboard2" :href="'/EtudDrive/' + entreprise.id">
                <img src="../assets/imgs/template/icons/folder.svg" alt="jobBox" />
                <span class="name">Mon Drive</span>
              </a>
            </li>
          </ul>
        </nav>
        <nav v-if="userType === 'etudiant'" class="nav-main-menu-2">
          <ul class="main-menu-2">
            <li>
              <router-link :to="'/EtudOverview/' + etudiant.id">
                <img src="../assets/imgs/template/icons/stack.svg" alt="jobBox" />
                <span class="name">Overview</span>
              </router-link>
            </li>
            <li>
              <router-link :to="'/GenerationPortfolio/' + etudiant.id">
                <img src="../assets/imgs/template/icons/file-person.svg" alt="jobBox" />
                <span class="name">Générer Portfolio</span>
              </router-link>
            </li>
            <li>
              <router-link to="/Demandes">
                <img src="../assets/imgs/template/icons/briefcase2.svg" alt="jobBox" />
                <span class="name">Mes Demades</span>
              </router-link>
            </li>
            <li>
              <router-link :to="'/EtudDrive/' + etudiant.id">
                <img src="../assets/imgs/template/icons/folder.svg" alt="jobBox" />
                <span class="name">Mon Drive</span>
              </router-link>
            </li>
          </ul>
        </nav>
        <nav v-if="userType === 'admin'" class="nav-main-menu-2">
          <ul class="main-menu-2">
            <li>
                <router-link to="/AdminOverview" class="dashboard2 active" 
                ><img
                  src="/template/assetss/imgs/template/icons/stack.svg"
                  alt="jobBox"
                /><span class="name">Overview</span></router-link
              >
            </li>
            <li>
              <router-link to="/EtuTable" class="dashboard2"
                ><img
                  src="/template/assetss/imgs/template/icons/file-person.svg"
                  alt="jobBox"
                /><span class="name">Tous Les Etudiants</span></router-link
              >
            </li>
            <li>
              <router-link to="/EntTable" class="dashboard2" exact
                ><img
                  src="/template/assetss/imgs/template/icons/building-fill-gear.svg"
                  alt="jobBox"
                /><span class="name">Toutes Les Entreprises</span></router-link
              >
            </li>
            <li>
              <router-link to="/OffreTable" class="dashboard2 " 
                ><img
                  src="/template/assetss/imgs/template/icons/briefcase2.svg"
                  alt="jobBox"
                /><span class="name">Toutes Les Offres</span></router-link
              >
            </li>
          </ul>
        </nav>
        <div class="border-bottom mb-20 mt-20"></div>
      </div>
  
      <span style="font-size: 25px;font-weight: 660;color:rgb(133, 133, 133);position: relative;top: 25px;left: 57px;">Historique</span>
      <div class="mobile-search mobile-header-border mb-30" style="position: relative;width: 30%; top:63px;left: -2%;">
  <form @submit.prevent style="position: relative;left: -40px;">
    <input type="text" v-model="searchKeyword" @keyup.enter="searchByKeyword" placeholder="Rechercher historique">
    <i class="fi-rr-search" ></i>
  </form>
<div style="    max-height: 400px;position: relative;
overflow-y: auto; overflow-x: hidden;width:750px;top: 40px;left: -35px">
  <table style="position: relative;max-height: 400px; overflow-y: auto;overflow-x: hidden;">
    <tbody>
      <!-- Vérifiez si searchKeyword est vide -->
      <template v-if="!searchKeyword">
        <!-- Boucle sur les groupes d'actions regroupées par date et heure -->
        <template v-for="(group, dateTime) in groupedActions" :key="`group-${dateTime}`">
          <!-- Ligne pour chaque groupe de date et heure -->
          <tr>
            <!-- Cellule pour afficher la date et l'heure -->
            <td colspan="2" scope="row">
              <h2 class="invoice-num" style="color: #313131; font-size: 15px; line-height: 1;">{{ formatDate(dateTime) }}</h2>
            </td>
          </tr>
          <!-- Boucle sur les actions dans ce groupe -->
          <tr v-for="action in group" :key="action.id">
            <td scope="row">
              <!-- Affichez chaque action -->
              <span class="fs-18" style="color: #6C6B6B; font-size: 14px; line-height: 1;">{{ action.action_message }}</span><br>
            </td>
            <td style="position: relative;">  
              <!-- Affichez l'heure de chaque action -->
              <span class="fs-18" style="color: #818181; font-size: 16px;padding: 7px;">{{ formatTime(action.timestamp) }}</span>

            </td>
          </tr>
        </template>
      </template>
      <!-- Si searchKeyword n'est pas vide, affichez uniquement les actions filtrées -->
      <template v-else>
  <tr v-for="action in filteredActions" :key="action.id">
    <td colspan="2" scope="row">
      <!-- Affichez la date et l'heure -->
      <h2 class="invoice-num" style="color: #313131; font-size: 15px; line-height: 1;">{{ formatDate(action.timestamp) }}</h2>
    </td>
    <td scope="row">
      <!-- Affichez chaque action filtrée -->
      <span class="fs-18" style="color: #6C6B6B; font-size: 13px; line-height: 1;">{{ action.action_message }}</span><br>
    </td>
    <td>  
      <!-- Affichez l'heure de chaque action filtrée -->
      <span class="fs-18" style="color: #818181; font-size: 16px;padding: 7px;">{{ formatTime(action.timestamp) }}</span>
    </td>
  </tr>
</template>

    </tbody>
  </table>
</div>
</div>


        






    </main>
    <div class="footer-2 mt-20">
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
  import axios from 'axios';
  import navbarEntreprise from "@/components/navbarEntreprise.vue";
import navbarEtudiant from "@/components/navbarEtudiant.vue";  
import navbarAdmin from "@/components/navbarAdmin.vue";  

  export default {
    components: { navbarEntreprise, navbarEtudiant,navbarAdmin },
  
    data() {
      return {
        uploadedFileName: '',
        isDropdownOpen1: false,
        isDropdownOpen2: false,
        actions: [],
        groupedActions: {}, // Définir groupedActions dans les données du composant
        searchKeyword: '',
        filteredActions: [],
        userType: null,
        entreprise: {},
        etudiant: {},

      };
    },
    created() {
  const userId = localStorage.getItem("user_id");
  if (!userId) {
    alert("You have to log in");
    this.$router.push("/ConnexionView");
    return;
  }

  const userType = localStorage.getItem("user_type");
  this.userType = userType;

  if (userType === 'etudiant') {
        this.etudiant = { id: userId };
  } else if (userType === 'entreprise') {
        this.entreprise = { id: userId };
  } else if (userType === 'admin'){
        this.admin = {id: userId}
  }
  },

    mounted() {
      // Appeler la méthode pour récupérer toutes les actions une fois que le composant est monté
      this.getAllActions();
    },
    methods: {
      getAllActions() {
        const userId = localStorage.getItem("user_id");
        if (!userId) {
          alert("You must be logged in.");
          return;
        }
        axios.get(`http://127.0.0.1:8000/get-all-actions/${userId}/`)
          .then(response => {
            // Mise à jour de groupedActions dans les données du composant avec les données récupérées
            this.groupedActions = this.groupActionsByDateTime(response.data);
            console.log('Grouped actions:', this.groupedActions);
          })
          .catch(error => {
            console.error('Error fetching actions:', error);
            // Gérer l'erreur ici
          });
      },
      groupActionsByDateTime(actions) {
        // Create an object to store grouped actions
        const groupedActions = {};
        // Loop through each action
        actions.forEach(action => {
          // Extract date and time from timestamp
          const date = this.formatDate(action.timestamp);
          // Check if the date exists in groupedActions
          if (!groupedActions[date]) {
            // If not, initialize an array for this date
            groupedActions[date] = [];
          }
          // Push the action to the corresponding date array
          groupedActions[date].push(action);
        });
        return groupedActions;
      },
      stopPropagation(event) {
        event.stopPropagation();
      },
      toggleDropdown1() {
        this.isDropdownOpen1 = !this.isDropdownOpen1;
        if (this.isDropdownOpen1 && this.isDropdownOpen2) {
          this.isDropdownOpen2 = false; // Ferme le dropdown 2 si ouvert
        }
      },
      toggleDropdown2() {
        this.isDropdownOpen2 = !this.isDropdownOpen2;
        if (this.isDropdownOpen2 && this.isDropdownOpen1) {
          this.isDropdownOpen1 = false; // Ferme le dropdown 1 si ouvert
        }
      },
      formatDate(timestamp) {
        // Extraire la date de la chaîne de timestamp
        const date = new Date(timestamp);
        // Formater la date en utilisant les méthodes de l'objet Date
        const formattedDate = date.toISOString().split('T')[0];
        // Retourner la date formatée
        return formattedDate;
      },
      formatTime(timestamp) {
        // Extraire l'heure de la chaîne de timestamp
        const time = new Date(timestamp);
        // Formater l'heure en utilisant les méthodes de l'objet Date
        const formattedTime = time.toISOString().split('T')[1].split('.')[0];
        // Retourner l'heure formatée
        return formattedTime;
      },
      searchByKeyword(event) {
        // Empêcher le comportement par défaut du formulaire
        event.preventDefault();
  
        if (this.searchKeyword) {
          // Effectuer une requête GET vers votre API pour rechercher les actions correspondant au mot-clé saisi
          axios.get(`http://127.0.0.1:8000/search_by_mc/${this.searchKeyword.trim()}/`)
            .then(response => {
              // Mettre à jour les actions filtrées avec les résultats de la recherche
              this.filteredActions = response.data; // Assurez-vous que la structure de réponse est correcte
              console.log(this.searchKeyword);
              console.log(this.searchKeyword);
  
            })
            .catch(error => {
  
              console.error('Erreur lors de la recherche par mot-clé :', error);
            });
        } else {
          console.error('Veuillez entrer un mot-clé de recherche.');
        }
      },
    }
  };
  </script>
  
  <style scoped>
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
/* Styles pour la croix */
 
  </style>
  