<template>
   
   <header class="header sticky-bar">
        <div class="container container-cus">
          <div class="main-header">
            <div class="header-left">
              <div class="header-logo">
                <a class="d-flex" href="index.html"
                  ><img alt="jobBox" src="../assets/imgs/logo/logo-blanc.png"
                /></a>
              </div>
            </div>
            <div class="header-nav">
              <nav class="nav-main-menu">
                <ul class="main-menu">
                  <li class="has-children">
                    <a  href="index.html">Accueil</a>
                  </li>
                  <li :class="{ 'active': isRouteActive('/EtuGrid') }">
                <router-link to="/EtuGrid">Trouver un candidat</router-link>
              </li>
              <li :class="{ 'active': isRouteActive('/Dashboard') }">
                    <router-link :to="'/EntOverview/' + this.entreprise.id" >Tableau de bord</router-link>
                  </li>
                  <li :class="{ 'active': isRouteActive('/MesOffres') }">
                    <a :href="'/MesOffres'">Mes Offres</a>
                  </li>
              
                  <li :class="{ 'active': isRouteActive('/Aide') }">
                    <router-link to="/Aide" >Aide & Support</router-link>
                  </li>
                </ul>
              </nav>
              <div class="burger-icon burger-icon-white">
                <span class="burger-icon-top"></span
                ><span class="burger-icon-mid"></span
                ><span class="burger-icon-bottom"></span>
              </div>
            </div>
          </div>
        </div>
      </header>
      <div class="header-2 sticky-bar2 d-flex" >
        <div class="container2">
          <div class="right-bar">
            <div class="icon-container hover-up" style="cursor: pointer">
              <img
                style="width: 28px; fill: #447ab8"
                src="../assets/imgs/template/icons/bell.svg"
                @click="handleBellClick"
              />
              <div style="position: relative;left: 4px;top:7px;">
              <span v-if="notificationCount > 0" class="notification-badge">{{ notificationCount }}</span>
            </div>
            </div>
            <div style="position: relative;top: 20px;right: 25px;">
              <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink1" v-if="isDropdownsOpen1.notification" 
       style="position: absolute; top: 32px; left: 0; z-index: 999 !important; height: auto;padding: 0px;">
    <!-- Contenu du dropdown -->
    <h6 class="dropdown-header" style="font-size: 23px; padding-bottom: 27px;background-color:#F2F6FD;padding-top: 10px;">Notifications</h6>
    <div >
      <div class="dropdown-item" v-for=" notification in notifications" :key="notification"
           style="z-index: 999; padding: 10px; position: relative; left: 0px; height: 90px;">
        <div class="notification-item">
          <!--<img :src="notification.profile_logo" alt="Logo entreprise" class="notification-image" style="width: 60px; height: 60px;">-->
          <div class="notification-details" style="position: relative; left: 40px;width: 600px;">
    <h6 class="notification-title" style="color: #4F5E64 ;width: 600px;">{{ notification.message }}</h6>
</div>

          <div style="position: relative; left: -559px; bottom: 25px;">
            <span>{{ formatDate(notification.created_at) }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
            <router-link to="/chatView"  class="icon-container hover-up">
              <img
                style="width: 28px; fill: #447ab8"
                src="../assets/imgs/template/icons/envelope-arrow-up.svg"
              />
            </router-link>
            <router-link
              to="/PostView"
              class="btn btn-default btn-shadow  postbutt" style="margin-right: 20px;"
              >Publier Offre</router-link
            >
            <div class="icon-container hover-up" >
      <img  class="icon-fb" alt="profile-fb" :src="this.entrepriseUrl" @click="toggleDropdown" />
      <div class="dropdown-menu dropdown-menu-left" v-if="showDropdown"  >
        <a class="dropdown-item" :href="'/EntrepriseDetails/' + entreprise.id"><img
                src="../assets/imgs/template/icons/person-circle.svg"
                alt="jobBox"
              /><span>Profil</span></a> 
              <router-link to="/EntrepriseFavoris" class="dropdown-item" >
              <img src="../assets/imgs/template/icons/bookmark.svg" alt="jobBox" />
              <span>Favoris</span>
              </router-link>
        
              <a class="dropdown-item" :href="'/HistoriqueView/' + entreprise.id">
                <img src="../assets/imgs/template/icons/clock-history.svg" alt="jobBox" />
              <span>Historique</span>
          </a>
          <router-link to="/profilEntView" class="dropdown-item">
              <img src="../assets/imgs/template/icons/gear.svg" alt="jobBox" />
              <span>Paramètres</span>
          </router-link>
          <a class="dropdown-item" href="#" @click="logout">
              <img src="../assets/imgs/template/icons/box-arrow-right.svg" alt="jobBox" />
              <span>Déconnexion</span>
          </a>
      </div>
  </div>
          </div>
        </div>
      </div>
  
</template>
<script>
import axios from "axios";
export default{
    data() {
        return{
            baseUrl: "http://127.0.0.1:8000/",
            userType: 'entreprise',
    
    showDropdown: false,
    isDropdownsOpen1: {
        notification: false,
      },

    offer: {},
    entrepriseUrl:null,
    notifications:[],
          notificationCount: 0,

        };
},
created() {
  const userId = localStorage.getItem("user_id");
    if (!userId) {
        // User ID not found in local storage, redirect to error interface
        alert("you have to log in");
        this.$router.push("/ConnexionView");
        return;
    }

    // Initialize entreprise object
    this.entreprise = {
        id: userId
    };
    console.log(this.entreprise.id);
    
    // Fetch entreprise data using the entreprise ID
    this.fetchEntrepriseData();
},
mounted() {
    this.getAllnotifs();
  },
  methods: {
    toggleDropdown1(notification) {
  console.log('Toggle dropdown 1');
  this.isDropdownsOpen1[notification] = !this.isDropdownsOpen1[notification];
  console.log('Dropdown 1 state:', this.isDropdownsOpen1[notification]);
  this.getAllnotifs();

},
    async fetchEntrepriseData() {
      try {

        const response = await axios.get(`http://127.0.0.1:8000/api/entreprises/get/${this.entreprise.id}/`);
        // Populate the etudiant object with data from the response
        this.entreprise = response.data;
        console.log(this.entreprise.profile_logo)
        if (this.entreprise.profile_logo) {
          this.entrepriseUrl = this.baseUrl + this.entreprise.profile_logo;
        }
      } catch (error) {
        console.error('Error fetching entreprise data:', error);
      }
    },
    toggleDropdown() {
      this.showDropdown = !this.showDropdown;
      console.log(this.showDropdown);
    },
    logout() {
          localStorage.removeItem('user_id');
          this.$router.push('/ConnexionView');
          console.log('Logout successful');
    },
    isRouteActive(route) {
      return this.$route.path === route;
    },
    formatDate(dateTime) {
      const dateObj = new Date(dateTime);
      const date = dateObj.toLocaleDateString(); // Obtenez la date sous forme de chaîne de caractères (ex: "dd/mm/yyyy")
      const time = dateObj.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }); // Obtenez l'heure sans les secondes
      return `${date} ${time}`; // Retourne la date et l'heure avec un espace entre les deux parties
    },
    getAllnotifs() {
  const userId = localStorage.getItem("user_id");
  if (!userId) {
    alert("Vous devez être connecté.");
    return;
  }
  axios.get(`http://127.0.0.1:8000/notificationsEntre/${userId}/`)
    .then(response => {
      console.log('ID de l\'utilisateur :', userId);
      console.log('Données de réponse :', response.data);
      // Supposons que 'this.notifications' est un tableau pour stocker les notifications
      this.notifications = response.data;
      this.notificationCount = this.notifications.length;



    })
    .catch(error => {
      console.error('Erreur lors de la récupération des notifications :', error);
    });
},
handleBellClick() {
    this.toggleDropdown1('notification');
    this.getAllnotifs();

  }
}}
</script>
<style>
.icon_fb{
height: 50px;
}
.dropdown-menu {
  display: block !important;
  left: auto !important;
  right: 0 !important;
  min-width: 13rem !important;
  position: absolute !important; 
  top: 100% !important; 

  z-index: 2 !important;
 margin-top:5px !important;
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
  font-weight: bold !important;
  font-size: 16px;
  line-height: 24px;
  color: #858585 !important;
  margin-bottom: 4px;
  display: flex !important;
  align-items: center;
  height: 40px;
}
.dropdown-item img {
  margin-right: 20px;

  width: 25px;
}


.show-dropdown .dropdown-menu {
  display: block;
}
.icon-container{
position: relative; cursor: pointer; width: 50px; height: 50px; margin-top: 0px; z-index: 1;
}
.container-cus{
  margin-left: 5px !important;
}
.header .main-menu li  {
    font-family: "Plus Jakarta Sans", sans-serif;
    font-style: normal;
    font-weight:900;
    font-size: 25px;
    line-height: 18px;
    color: #FFFFFF;
    display: block;
    padding: 5px;
    text-decoration: none;
    position: relative;
}
.notification-badge {
  position: absolute;
  top: 0px;
  right: 0px; /* Vous pouvez ajuster la position selon vos besoins */
  width: 16px; /* Vous pouvez ajuster la taille du cercle */
  height: 16px; /* Vous pouvez ajuster la taille du cercle */
  background-color:red !important;
  color: white;
  font-size:x-small !important;
  border-radius: 50%; /* Utilisez 50% pour obtenir un cercle */
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>