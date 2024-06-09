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
    <title>Mes demandes</title>
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
      <navbarEntreprise/>

  <main class="main-2" style="margin-top: 0px">
    <div class="nav-2" style="border-right: 1px solid #dee2e6">
      <nav class="nav-main-menu-2">
          <ul class="main-menu-2">
          <li>
       <router-link :to="'/EntOverview/'+userId"   class="dashboard2">
              ><img
                src="../assets/imgs/template/icons/stack.svg"
                alt="jobBox"
              /><span class="name">Overview</span></router-link
            >
          </li>
          <li>
            <router-link to="/BookGeneration" class="dashboard2" 
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
            <a class=" dashboard2" :href="'/MesOffres' "
              ><img
                src="../assets/imgs/template/icons/briefcase2.svg"
                alt="jobBox"
              /><span class="name">Mes Offres</span></a
            >
          </li>
          <li>
            <a class="dashboard2" :href="'/EtudDrive/' +userId"
              ><img
                src="../assets/imgs/template/icons/folder.svg"
                alt="jobBox"
              /><span class="name">Mon Drive</span></a
            >
          </li>
        </ul>
        </nav>
      <div class="border-bottom mb-20 mt-20"></div>
    </div>

    <div class="form-section-2" style="background-color: #ffffff">
     
      <div class="tab-content" >
        <div class="box-heading-2 " >
          <div class="box-title-2" style="width:100%; display:flex;">
            <h3 class="mb-35">Mes Demandes</h3>
       
          </div>
        
        </div>
        <div class="row-2">
          <div class="col-lg-1222">
            <div class="section-box-2">
              <div class="container-22">
                <div class="panel-white-2 mb-30">
                  <div class="box-padding-2 bg-postjob-2">
                    <div class="row mt-30">
                      <div class="col-lg-9">
                          <table class="table">
<thead>
  <tr>
      <th scope="col">Etudiant</th>
    <th scope="col">Prénom</th>
    <th scope="col">Nom</th>
    <th scope="col">Date de postulation</th>
    <th scope="col">Status</th>
    <th scope="col">Actions</th>
  </tr>
</thead>
<tbody>
  <tr v-for="demande in demandes" :key="demande.id">
    <th scope="row" ><div class="image-box"><img  :src="demande.profile_photo" alt="jobBox" style="width: 30px;;"></div></th>
    <td class="cus-td "><a :href="'/EtudiantDetails/' + demande.etudiant_id ">{{demande.prenom}}</a></td>
   <td class="cus-td "><a :href="'/EtudiantDetails/' + demande.etudiant_id ">{{demande.nom}}</a></td>
   <td class="cus-td "><span class="card-time">{{demande.created_at.slice(0,10)}}</span></td>
    <td class="cus-td"><template v-if="demande.status==='en attente'">
      <img src="/template/assets/imgs/page/candidates/pended.png" alt="verified" style="height:20px;">
    </template>
    <template v-if="demande.status==='accepted'">
      <img src="/template/assets/imgs/page/candidates/accepted.png" alt="verified" style="height:20px;">
    </template>
    <template v-if="demande.status==='refused'">
      <img src="/template/assets/imgs/page/candidates/refused.png" alt="verified" style="height:20px;">
    </template>
  </td>
  <td class="cus-td">
      <span v-if="demande.status==='en attente'"  @click="accept(demande.id)"><img src="/template/assets/imgs/template/icons/check-square-fill.svg" alt="sw-connect" style="cursor: pointer;"></span>
        <span v-if="demande.status==='en attente'" @click="refuse(demande.id)"><img src="/template/assets/imgs/template/icons/ban-fill.svg" alt="sw-connect" style="cursor: pointer;"></span>
        <span v-if="demande.status==='accepted'" @click="refuse(demande.id)"><img src="/template/assets/imgs/template/icons/ban-fill.svg" alt="sw-connect" style="cursor: pointer;"></span>
        <span v-if="demande.status==='refused'"  @click="accept(demande.id)"><img src="/template/assets/imgs/template/icons/check-square-fill.svg" alt="sw-connect" style="cursor: pointer;"></span>
  </td>
  </tr>

 
</tbody>
</table>







                          </div>
                 
              
                
               
               
                
              
                     
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
     
        <div class="footer-2 mt-20">
          <div class="container">
            <div class="box-footer-2">
              <div class="row">
                <div class="col-md-6 col-sm-12 mb-25 text-center text-md-start">
                  <p class="font-lg color-text-paragraph-made-by">
                    © 2024 - Made By SwConnect
                  </p>
                </div>
                <div class="col-md-6 col-sm-12 text-center text-md-end mb-25">
                  <ul class="menu-footer-2">
                    <li><a href="#">About</a></li>
                    <li><a href="#">Careers</a></li>
                    <li><a href="#">Policy</a></li>
                    <li><a href="#">Contact</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
    </div>
  </main>
</body>
  
</template>
<script>
import axios from "axios";
import navbarEntreprise from '@/components/navbarEntreprise.vue';
export default {
  name: "MesDemandes",
  components:{navbarEntreprise},
  data() {
    return {
      baseUrl: "http://localhost:8000",

      userType:'',


      demandes: [],
      showDropdown: false,
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

},
mounted() { 
  // Call a method to fetch all offers from the backend API
  
  const offerId = this.$route.params.id; 
  this.fetchDemandes(offerId);

},

  methods: {
    logout() {
          localStorage.removeItem('user_id');
          this.$router.push('/ConnexionView');
          console.log('Logout successful');
    },
    fetchDemandes(offerId) {
    axios
      .get(`http://127.0.0.1:8000/api/demande/offer/${offerId}/`)
      .then((response) => {
        // Store the fetched favorite offers in the data property
        this.demandes = response.data;
        console.log("Fetched demandes", this.demandes);
      })
      .catch((error) => {
        console.error("Error fetching demandes:", error);
        // Handle error response if needed
      });
  },
  accept(id) {
  axios.put(`http://localhost:8000/api/demande/${id}/setAccepted/`)
    .then(response => {
      // Update the verified status in the frontend
      const demandeIndex = this.demandes.findIndex(demande => demande.id === id);
      if (demandeIndex !== -1) {
        this.demandes[demandeIndex].status = 'accepted';
        console.log(response.data);
        
        // Assuming response.data includes the accepted demandes with offer_title
        const acceptedDemande = response.data.demandes[0];
        this.demandes[demandeIndex].offer_title = acceptedDemande.offer_title;
        
        this.ajouterAction('Demande acceptée');
        const message = `La demande dans l'offre ${acceptedDemande.offer_title} a été acceptée.`;
        if (acceptedDemande.id) {  // Assurez-vous que demandeId est présent
        this.ajouterNotification(acceptedDemande.id, message);
      } else {
        console.error('Demande ID is not provided.');
      }
      }
      alert('Demande accepted successfully.');
      //window.location.reload();
    })
    .catch(error => {
      console.error('There was an error accepting demande:', error);
      alert('Error accepting demande.');
    });
},
refuse(id) {
try {
  axios.put(`http://localhost:8000/api/demande/${id}/setRefused/`)
    .then(response => {
      // Update the verified status in the frontend
      const demandeIndex = this.demandes.findIndex(demande => demande.id === id);
      if (demandeIndex !== -1) {
        this.demandes[demandeIndex].status = 'refused';
        console.log(response);

        const refusedDemande = response.data.demandes[0];
        this.demandes[demandeIndex].offer_title = refusedDemande.offer_title;

        this.ajouterAction('Demande refusée');
        const message = `La demande dans l'offre ${refusedDemande.offer_title} a été refusée.`;
        console.log(this.demandes[demandeIndex])
        if (this.demandes[demandeIndex].id) { // Assurez-vous que demandeId est présent
          this.ajouterNotification(refusedDemande.id, message);
        } else {
          console.error('Demande ID is not provided.');
        }

      }
      alert('Demande refused successfully.');
      //window.location.reload();
    })
    .catch(error => {
      console.error('There was an error refusing demande:', error);
      alert('Error refusing demande.');
    });
} catch (error) {
  console.error('There was an error refusing demande:', error);
  alert('Error refusing demande.');
}
},
ajouterAction(message) {
const userId = localStorage.getItem("user_id");
if (!userId) {
  alert("Vous devez être connecté.");
  return;
}
axios.post(`http://127.0.0.1:8000/creer-action/${userId}/`, {
  action_message: message,
})
.then(() => {
  // Traiter la réponse si nécessaire
  console.log('Action ajoutée avec succès !');
})
.catch(error => {
  console.error('Erreur lors de l\'ajout de l\'action :', error);
  alert('Une erreur est survenue lors de l\'ajout de l\'action.');
});
},
ajouterNotification(demandeId, message) {

try {
  if (!demandeId) {
    console.error('Demande ID is not provided.');
    return;
  }

  // Envoyer la notification au serveur
  axios.post(`http://localhost:8000/creer-notif/${demandeId}/`, {
    message: message,
  })
  .then(response => {
    console.log('Notification added successfully:', response.data);
  })
  .catch(error => {
    console.error('Error adding notification:', error);
  });
} catch (error) {
  console.error('Error adding notification:', error);
}
}


  },

};
</script>
<style scoped>
.form-section-2{
  width:100%;
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
margin: 5% auto;
padding: 20px;
border: 1px solid #888;
width: 90%;
max-width: 900px;
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
.btn-grey-small{
  margin-bottom: 5px;
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
  min-height: 1490px;
  height: auto;
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
  height:85px;
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
  transform: translateY(18px);
}
/* Styles for the tab content */
.tab-content {
  padding: 30px;
  border: 1px solid #dee2e6;
  border-top: none;
  border-right: none;
  background-color: #f2f4fa;
  border-radius: 9px;
  padding-top:50px;
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

.card-grid-2:hover .btn-apply-now {
  background-color: #447AB8 !important;
  color: #E0E6F7 !important;
}
.cus-td{
  padding-top: 15px;
  font-size:16px;
  padding-bottom: 15px;
}
.cus-td img{
  margin-right: 10px;
}
.cus-td a:hover{
  color:#447AB8;
  font-size:17px;
}
thead{
  background-color: #f2f4fa;
}
.icon-people{
margin-right:5px;
font-size:1.2rem;
}
th{
  font-size:17px;
}
</style>
