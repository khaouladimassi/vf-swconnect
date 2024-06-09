<template>
   
   <header class="header sticky-bar">
        <div class="container container-cus">
          <div class="main-header">
            <div class="header-left" style="margin-left:20px">
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
                    <router-link to="/">Accueil</router-link>
                  </li>
                  <li :class="{ 'active': isRouteActive('/OffreTable') }">
                <router-link to="/OffreTable">Offres</router-link>
              </li>
              <li :class="{ 'active': isRouteActive('/EntTable') }">
                <router-link to="/EntTable">Entreprises</router-link>
              </li>
              <li :class="{ 'active': isRouteActive('/EtuTable') }">
                <router-link to="/EtuTable">Etudiants</router-link>
              </li>
              <li :class="{ 'active': isRouteActive('/Dashboard') }">
                    <router-link to="/Dashboard" >Tableau de bord</router-link>
                  </li>
                  <li :class="{ 'active': isRouteActive('/Aide') }">
                    <router-link to="/Aide" >Aide & Support</router-link>
                  </li>
                </ul>
              </nav>
             
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
            <router-link to="chatView" class="icon-container hover-up">
              <img
                style="width: 28px; fill: #447ab8"
                src="../assets/imgs/template/icons/envelope-arrow-up.svg"
              />
            </router-link>
       
            <div class="icon-container hover-up" style="">
      <img  class="icon-fb" alt="profile-fb" src="/template/assets/default/admin.png" @click="toggleDropdown" />
      <div class="dropdown-menu dropdown-menu-left" v-if="showDropdown"  >
        <router-link to="/AdminDetails"   class="dropdown-item" ><img
                src="../assets/imgs/template/icons/person-circle.svg"
                alt="jobBox"
              /><span>Profil</span></router-link> 
            
        
              <a class="dropdown-item" :href="`/HistoriqueView/` + admin.id">
              <img src="../assets/imgs/template/icons/clock-history.svg" alt="jobBox" />
              <span>Historique</span>
          </a>
          <router-link to="/ProfilAdView" class="dropdown-item">
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
            //userType: 'etudiant',
    
    showDropdown: false,

    etudiantUrl:null,
    isDropdownsOpen1: {
        notification: false,
      },

    notifications :[],
    notificationCount :0,
    userType: null,

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

  if (userType === 'admin') {
        this.admin = { id: userId };
  } 
  },
mounted(){
  this.getAllnotifs();

},
  methods: {
    
    toggleDropdown() {
      this.showDropdown = !this.showDropdown;
      console.log(this.showDropdown);
    },
    logout() {
         // localStorage.removeItem('user_id');
          this.$router.push('/ConnexionView');
          console.log('Logout successful');
    },
    isRouteActive(route) {
      return this.$route.path === route;
    },

  getAllnotifs() {

  axios.get(`http://127.0.0.1:8000/notificationsAdmin/`)
  .then(response => { // Accès à la réponse de la requête
      this.notifications = response.data; // Utilisation de response.data pour obtenir les données de la réponse
      this.notificationCount = this.notifications.length;
    })
    .catch(error => {
      console.error('Erreur lors de la récupération des notifications :', error);
    });
},
handleBellClick() {
    this.toggleDropdown1('notification');
    this.getAllnotifs();

  },
  toggleDropdown1(notification) {
  console.log('Toggle dropdown 1');
  this.isDropdownsOpen1[notification] = !this.isDropdownsOpen1[notification];
  console.log('Dropdown 1 state:', this.isDropdownsOpen1[notification]);
  this.getAllnotifs();

},
formatDate(dateTime) {
      const dateObj = new Date(dateTime);
      const date = dateObj.toLocaleDateString(); // Obtenez la date sous forme de chaîne de caractères (ex: "dd/mm/yyyy")
      const time = dateObj.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }); // Obtenez l'heure sans les secondes
      return `${date} ${time}`; // Retourne la date et l'heure avec un espace entre les deux parties
    },
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
.icon-fb{
  width:50px;
  height:45px;
}

.show-dropdown .dropdown-menu {
  display: block;
}
.icon-container{
position: relative; cursor: pointer; width: 50px; height: 50px; margin-top: 0px; z-index: 1;
margin-left:5px !important;
display:flex;
}
.container-cus{
  margin-left: 5px !important;
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