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
    <title>Admin</title>
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
    
    <link href="./template/assets/css/stylecd4ee.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  </head>
  <body>
<navbarAdmin/>
    <main class="main">
      <div class="banner-hero banner-image-single" style="margin-left:5px; "><img :src="this.baseUrl+this.admin.profile_cover" alt="jobbox" style="height:348px;"></div>
      <div class="box-company-profile" style="width:100px">
            <div class="image-compay" style="width:100px; margin-left:-596px;"><img :src="this.adminUrl" alt="jobbox">
            </div>
      </div>
      <section class="section-box-2">
        <div class="container">
          <div class="row mt-10">
            <div class="col-lg-8 col-md-12">
              <div class="inline-content">
                <h3 style="display: inline">
                  {{ admin.username }}
                </h3>
              </div>
              <p class="company-name" href="#">Administrateur     <span><img src="/template/assets/imgs/template/icons/patch-check-fill.svg"></span></p>
            </div>
            <div  v-if="userType === 'entreprise'"  class="col-lg-4 col-md-12 text-lg-end">
              <div class="btn-group" role="group" aria-label="Button group">
                <div class="icon-container-2 hover-up">
                  <i class="bi bi-bookmark custom-icon-3"  style="cursor: pointer"></i>
                </div>

                <div
                  class="btn btn-apply btn-apply-big hover-up"
                  style="border-radius: 8px"
                >
                  Contacter <i class="bi bi-chat-text custom-icon-4"></i>
                </div>
              </div>
            </div>
          </div>
          <div class="border-bottom pt-10 pb-10"></div>
        </div>
      </section>
      <section class="section-box mt-50">
        <div class="container">
          <div class="row">
            <div class="col-lg-8 col-md-12 col-sm-12 col-12">
              <div class="content-single">
    
                <p>Bonjour, je suis l'administrateur du site.</p>
              
              </div>
              <div class="author-single">
                <span>{{admin.username }}</span>
              </div>
            </div>
            <div
              class="col-lg-4 col-md-12 col-sm-12 col-12 pl-40 pl-lg-15 mt-lg-30"
            >
              <div class="sidebar-border">
                <div class="sidebar-heading">
                  <h5 class=" ">Coordonnées</h5>
                  <div class="avatar-sidebar">
                    <div class="sidebar-info"></div>
                  </div>
                </div>
                <div class="sidebar-list-job">
                  <ul>
                    <li>
                      <i class="bi bi-envelope custom-iconss"></i
                      >{{ admin.email }}
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      </main>
    </body>
  </template>
  <script>
  import axios from 'axios';
 import navbarAdmin from '@/components/navbarAdmin.vue';
  export default {
    components:{navbarAdmin},
    name: "DetailsAdmin",
    data() {
      return {
        admin:{},
        adminUrl:null,
        baseUrl: "http://127.0.0.1:8000/",
            showErrorMessage: false,
             showDropdown: false,
    }},

methods:{
      logout() {
          localStorage.removeItem('user_id');
          this.$router.push('/ConnexionView');
          console.log('Logout successful');
    },
      toggleDropdown() {
      this.showDropdown = !this.showDropdown;
    },
    async fetchAdminData() {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/admin/${this.admin.id}/`
        );
        // Populate the etudiant object with data from the response
        this.admin = response.data;
        if (this.admin.profile_photo) {
          this.adminUrl = this.baseUrl + this.admin.profile_photo;
        }
      } catch (error) {
        console.error("Error fetching admin data:", error);
      }
    },
  
  },
  created() {
    const userId = localStorage.getItem("user_id");
    
    if (!userId) {
      // User ID not found in local storage, redirect to error interface
      alert("you have to log in");
      this.$router.push("/ConnexionView");
      return;
    }
    this.admin.id = userId;
    this.fetchAdminData();
  },

};
  </script>
  <style scoped>
    .modal {
  display: block; /* Afficher la fenêtre modale */
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Fond semi-transparent */
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
  .h5 p{
font-size: 22px;
font-family: "Plus Jakarta Sans", sans-serif;
}
  .dropdown-menu a:hover span {
  color: #447AB8 !important;
}
.dropdown-menu a:hover img {
  filter: brightness(0) saturate(100%) invert(45%) sepia(30%) saturate(995%) hue-rotate(172deg) brightness(93%) contrast(87%);
}
.dropdown-menu a:hover {
  background-color: #E7F0FA !important;
  color: #447AB8 !important;
  border-left: 4px solid #447AB8;
}
  .dropdown-item{
    font-family: "Plus Jakarta Sans", sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 16px;
    line-height: 24px;
    color: #858585;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    height:40px;
  }
  .dropdown-item img{
    margin-right: 20px;
    width:25px;
  }
.dropdown-menu {
  display: block;
  left: auto !important;
  right: 0;
  min-width: 13rem;
}
  .icon-plus{
    padding:8px;
  }
  .btn-modal{
    width:100%;
    height:49.5px;
    background-color:#F2F4FA;
    color: #313131;
    border: 1px solid #dee2e6;
    font-size:18px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
    .custom-svg {
    width: 47px; /* Adjust width as needed */
    fill: #447AB8; /* Fill color */
    margin-right:14px;
    margin-left:10px;
  }
  .custom-png{
    width:62px;
    height:35px;
    margin-right: 10px;
    margin-top: 5px;
  }
  .input-group-prepend{
    display: flex;
    border-top: #dee2e6 solid 1px;
    border-bottom: #dee2e6 solid 1px;
    border-left: #dee2e6 solid 1px;
  }
  .input-group-prepend img{
    padding-left:21px;
  } 
.custom-iconss {
  font-size: 1.5rem;
  margin-right: 20px;
  color: #05264e;
}
  .btn-lien{
      width: 145px;
      padding-left:0px;
      font-size: 18px;
      display: flex;
    align-items: center;
}
.btn-lien-1{
      width: 135px;
      padding-left:0px;
      font-size: 18px;
      display: flex;
    align-items: center;
}
.col-lg-1222{
    flex: 0 0 auto;
    width: 100%;
   }
      .col-lg-9 {
    flex: 0 0 auto;
    width: 100%;
   }
 .panel-white-2 {
    height:1120px;
  }
  .col-md-3-2{
      flex:0 0 auto;
      width:35%;
  }
.col-md-7-2{
          flex:0 0 auto;
          width:65%;
}
.btn-pre-1{
    margin-left:30px;
  
  } 
  .btn-pre-2{
    margin-left:30px;
  }  
  .drag-drop-area {
    background-color: #f0f0f0; /* Background color */
    border: 2px dashed #ccc; /* Border style */
    border-radius: 10px; /* Rounded corners */
    height:  200px; /* Height */
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
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
      height:84px;
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
      color: #447AB8  !important;
      font-family: "Plus Jakarta Sans", sans-serif;
    font-style: normal;
    font-weight: 700;
    font-size: 17px;
    border-bottom: #447AB8 solid 3px;
    transform: translateY(18px);
    }
    /* Styles for the tab content */
    .tab-content {
      padding: 30px;
    border: 1px solid #dee2e6;
    border-top: none;
    border-right: none;
    background-color: #F2F4FA;
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
    .form-control{
      height: 50px;
    }
  
  </style>