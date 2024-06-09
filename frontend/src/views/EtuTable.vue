<template>
    <router>
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
    <title>Etudiants</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css" rel="stylesheet">
    <link href="https://cdn.tiny.cloud/1/YOUR_API_KEY/tinymce/5/tinymce.min.js" referrerpolicy="origin">
    <link rel="shortcut icon" type="image/x-icon" href="./template/assets/imgs/template/favicon.svg">

    <link href="./template/assets/css/plugins/animate.min.css" rel="stylesheet">
    <link href="./template/assets/css/plugins/magnific-popup.css" rel="stylesheet">
    <link href="./template/assets/css/plugins/perfect-scrollbar.css" rel="stylesheet">
    <link href="./template/assets/css/plugins/select2.min.css" rel="stylesheet">
    <link href="./template/assets/css/plugins/swiper-bundle.min.css" rel="stylesheet">
    
    <link href="/template/assets/css/stylecd4ee.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  </head>
  <body>
    <navbarAdmin/>
    <main class="main-2" style="margin-top: 0px">
      <div class="nav-2" style="border-right: 1px solid #dee2e6 ;   max-width: 310px;">
        <nav class="nav-main-menu-2">
          <ul class="main-menu-2">
            <li>
              <router-link to="/AdminOverview" class="dashboard2" href="candidates.html"
                ><img
                  src="template/assetss/imgs/template/icons/stack.svg"
                  alt="jobBox"
                /><span class="name">Overview</span></router-link
              >
            </li>
            <li   style=" width: 280px;">
              <router-link to="/EtuTable" class="dashboard2 active"
                ><img
                  src="template/assetss/imgs/template/icons/file-person.svg"
                  alt="jobBox"
                /><span class="name">Tous Les Etudiants</span></router-link
              >
            </li>
            <li>
              <router-link to="/EntTable" class="dashboard2" 
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
      <div class="form-section-2" style="background-color: #ffffff">
    
    <div class="tab-content">
      <div class="box-heading-2">
        <div class="box-title-2">
          <h3 class="mb-35">Etudiants</h3>
        </div>
      </div>
      <div class="row-2">
        <div class="col-lg-1222">
          <div class="section-box-2">
            <div class="container-22">
              <div class="panel-white-2 mb-30" style="width:1070px">
                <div class="box-padding-2 bg-postjob-2">
                  <div class="row mt-30">
                    <div class="col-lg-9" style="width:100%">
                        <table class="table">
  <thead>
    <tr>
        <th scope="col">Etudiant</th>
      <th scope="col">Nom</th>
      <th scope="col">Prénom</th>
      <th scope="col">Status</th>
      <th scope="col">Action</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="etudiant  in etudiants" :key="etudiant.id">
      <th scope="row" ><div class="image-box"><img  :src="this.baseUrl+etudiant.profile_photo" alt="jobBox" style="width: 40px;;"></div></th>
      <td class="cus-td "><a :href="'/EtudiantDetails/' + etudiant.id ">{{etudiant.last_name}}</a></td>
      <td class="cus-td"><a :href="'/EtudiantDetails/'+etudiant.id" class="name-job">{{etudiant.first_name}}</a></td>
      <td class="cus-td "><div class="mt-5">
        <span v-if="etudiant.blocked===false"  @click="block(etudiant.id)" style="color: rgb(57, 177, 77);">Actif</span>
          <span v-if="etudiant.blocked===true" @click="unblock(etudiant.id)" style="color: rgb(186, 45, 45);">Bloqué</span>
      </div></td>
      <td class="cus-td">
        <button v-if="etudiant.blocked===false"  @click="block(etudiant.id)"  class="btn-bloquer"> bloquer</button>
          <button v-if="etudiant.blocked===true" @click="unblock(etudiant.id)"  class="btn-debloquer">débloquer</button>
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
              <div
                class="col-md-6 col-sm-12 mb-25 text-center text-md-start"
              >
                <p class="font-lg color-text-paragraph-made-by">
                  © 2024 - Made By SwConnect
                </p>
              </div>
              <div class="col-md-6 col-sm-12 text-center text-md-end mb-25">
                <ul class="menu-footer-2">
                  <li><a href="#">About</a></li>
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
    </router>
</template>
<script>
import axios from "axios";
import navbarAdmin from'@/components/navbarAdmin.vue';
export default{
    name:"EtuTable",
    data(){
        return{
            etudiants:[],
            baseUrl: "http://127.0.0.1:8000/",
        }
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
    components:{navbarAdmin},
    mounted() {
    // Call a method to fetch all offers from the backend API
this.fetchAllEtudiants();
    },
    methods:{
      fetchAllEtudiants() {
    axios.get('http://127.0.0.1:8000/api/etudiants/getall/')
        .then(response => {
            // Set offers data
            this.etudiants = response.data;
        })
        .catch(error => {
            // Log error to console
            console.error('Error fetching etudiants:', error);
            // Display alert to the user
            alert('An error occurred while fetching etudiants. Please try again later.');
        });
},
block(id) {
  try {
    axios.put(`http://localhost:8000/api/etudiants/block/${id}/`)
      .then(response => {
        // Update the verified status in the frontend
        const blockedEtudiantIndex = this.etudiants.findIndex(etudiant => etudiant.id === id);
        if (blockedEtudiantIndex !== -1) {
          this.etudiants[blockedEtudiantIndex].blocked = true;
          console.log(response);
        }
        alert('Etudiant blocked successfully.');
      })
      .catch(error => {
        console.error('There was an error blocking etudiant:', error);
        alert('Error blocking etudiant.');
      });
  } catch (error) {
    console.error('There was an errorblocking etudiant:', error);
    alert('Error blocking etudiant.');
  }
},
unblock(id) {
  try {
    axios.put(`http://localhost:8000/api/etudiants/unblock/${id}/`)
      .then(response => {
        // Update the verified status in the frontend
        const unblockedEtudiantIndex = this.etudiants.findIndex(etudiant => etudiant.id === id);
        if (unblockedEtudiantIndex !== -1) {
          this.etudiants[unblockedEtudiantIndex].blocked = false;
          console.log(response);
        }
        alert('Etudiant unblocked successfully.');
      })
      .catch(error => {
        console.error('There was an error unblocking etudiant:', error);
        alert('Error unblocking etudiant.');
      });
  } catch (error) {
    console.error('There was an errorblocking etudiant:', error);
    alert('Error blocking etudiant.');
  }
},
}
}
</script>
<style scoped>
.btn-bloquer{
  color: #fff;
  cursor: pointer;
  background-color: rgb(186, 45, 45);
  border:rgb(186, 45, 45) solid 1px;
  border-radius: 4px;
}
.btn-debloquer{
  color: #fff;
  cursor: pointer;
  background-color: rgb(57, 177, 77);
  border:rgb(57, 177, 77) solid 1px;
  border-radius: 4px;
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

/* Styles for the tab content */
.tab-content {
  padding: 30px;
  border: 1px solid #dee2e6;
  border-top: none;
  border-right: none;
  background-color: #f2f4fa;
  border-radius: 9px;
  padding-top: 50px;
}
.tab-content.active {
  display: block;
}
.cus-td{
    padding-top: 15px;
    font-size:16px;
    padding-bottom: 15px;
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