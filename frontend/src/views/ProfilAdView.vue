<template>
  <router-view></router-view>
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, maximum-scale=1"
    />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <meta name="msapplication-TileColor" content="#0E0E0E" />
    <meta name="template-color" content="#0E0E0E" />
    <meta name="msapplication-config" content="browserconfig.html" />
    <meta name="description" content="Index page" />
    <meta name="keywords" content="index, page" />
    <meta name="author" content="" />
    <title>Paramètres</title>
    <link
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
      rel="stylesheet"
    />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
    />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css"
      rel="stylesheet"
    />
    <link
      href="https://cdn.tiny.cloud/1/YOUR_API_KEY/tinymce/5/tinymce.min.js"
      referrerpolicy="origin"
    />
    <link
      rel="shortcut icon"
      type="image/x-icon"
      href="./template/assets/imgs/template/favicon.svg"
    />

    <link
      href="./template/assets/css/plugins/animate.min.css"
      rel="stylesheet"
    />
    <link
      href="./template/assets/css/plugins/magnific-popup.css"
      rel="stylesheet"
    />
    <link
      href="./template/assets/css/plugins/perfect-scrollbar.css"
      rel="stylesheet"
    />
    <link
      href="./template/assets/css/plugins/select2.min.css"
      rel="stylesheet"
    />
    <link
      href="./template/assets/css/plugins/swiper-bundle.min.css"
      rel="stylesheet"
    />

    <link href="./template/assets/css/stylecd4ee.css" rel="stylesheet" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
    />
  </head>
  <body>
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
                  <li>
                <router-link to="/OffreTable">Offres</router-link>
              </li>
              <li>
                <router-link to="/EntTable">Entreprises</router-link>
              </li>
              <li>
                <router-link to="/EtuTable">Etudiants</router-link>
              </li>
              <li >
                    <router-link to="/Dashboard" >Tableau de bord</router-link>
                  </li>
                  <li >
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
              />
            </div>
            <router-link  :to="'/chatView'" class="icon-container hover-up">
              <img
                style="width: 28px; fill: #447ab8"
                src="../assets/imgs/template/icons/envelope-arrow-up.svg"
              />
            </router-link>
       
            <div class="icon-container hover-up" style="">
      <img  class="icon-fb" alt="profile-fb" :src="this.adminUrl" @click="toggleDropdown" />
      <div class="dropdown-menu dropdown-menu-left" v-if="showDropdown"  >
        <router-link to="/AdminDetails"   class="dropdown-item" ><img
                src="../assets/imgs/template/icons/person-circle.svg"
                alt="jobBox"
              /><span>Profil</span></router-link> 
            
        
          <a class="dropdown-item" href="#">
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
    <main class="main-2" style="margin-top: 0px">
      <div class="nav-2" style="border-right: 1px solid #dee2e6 ;   max-width: 310px;">
        <nav class="nav-main-menu-2">
          <ul class="main-menu-2">
            <li>
              <a class="dashboard2" href="candidates.html"
                ><img
                  src="template/assetss/imgs/template/icons/stack.svg"
                  alt="jobBox"
                /><span class="name">Overview</span></a
              >
            </li>
            <li>
            <router-link to="/EtuTable" class="dashboard2 "
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
              <h3 class="mb-35">Paramètres</h3>
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
                          <div class="row">
                            <h5 style="margin-bottom: 20px">
                              Photo de Profil && Couverture
                            </h5>
                            <div class="col-lg-6 col-md-3-2">
                              <div class="form-group mb-30">
                                <label class="font-lg color-text-mutted-2 mb-10"
                                  >Photo de profil</label
                                >
                                <label
                                  style="text-align: center"
                                  for="logoFileInput"
                                  class="drag-drop-area"
                                  @click="openFileInput"
                                >
                                  Cliquez ici pour choisir un logo.<br />
                                  Les formats supportés est PNG et JPG.<br />
                                  La taille maximum est 50 KB.<br />
                                  Dimensions recommendées : 320 x 320 pixels.
                                </label>
                                <input
                                  type="file"
                                  accept=".png, .jpg"
                                  id="logoFileInput"
                                  @change="handleLogoFileChange($event)"
                                  style="display: none"
                                />
                                <p
                                  v-if="selectedFileName"
                                  class="selected-file-info"
                                >
                                  Fichier sélectionné : {{ selectedFileName }}
                                </p>

                                <!-- Display error message if file size exceeds 50 KB -->
                                <p v-if="fileSizeError" class="text-danger">
                                  La taille du fichier dépasse 50 KB.
                                </p>
                              </div>
                            </div>
                            <div class="col-lg-6 col-md-7-2">
                              <div class="form-group mb-30">
                                <label class="font-lg color-text-mutted-2 mb-10"
                                  >Photo de couverture</label
                                >
                                <label
                                  style="text-align: center"
                                  for="coverPhotoFileInput"
                                  class="drag-drop-area"
                                  @click="openFileInput"
                                >
                                  Cliquez ici pour choisir une photo de
                                  couverture.<br />
                                  Les formats supportés est PNG et JPG. La
                                  taille maximum est 800 KB.<br />
                                  Dimensions recommendées : 851 x 315 pixels.
                                </label>
                                <input
                                  type="file"
                                  id="coverPhotoFileInput"
                                  @change="handleCoverPhotoFileChange($event)"
                                  style="display: none"
                                />
                                <p
                                  v-if="selectedFileName1"
                                  class="selected-file-info"
                                >
                                  Fichier sélectionné : {{ selectedFileName1 }}
                                </p>

                                <!-- Display error message if file size exceeds 50 KB -->
                                <p v-if="fileSizeError1" class="text-danger">
                                  La taille du fichier dépasse 800 KB.
                                </p>
                              </div>
                            </div>

                            <div class="col-lg-122">
                              <div class="form-group mb-30">
                                <label class="font-lg color-text-mutted-2 mb-10"
                                  >Username</label
                                >
                                <input
                                  v-model="admin.username"
                                  name="username"
                                  @blur="validateUsername"
                                  class="form-control"
                                  type="text"
                                />
                                <div
                                  v-if="usernameTouched && !isUsernameFilled"
                                  class="text-danger"
                                >
                                  Veuillez remplir ce champ.
                                </div>
                              </div>
                            </div>
                            <div class="col-lg-122">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Email</label
                              >
                              <div class="input-group mb-3">
                                <div class="input-group-prepend">
                                  <img
                                    class="custom-svg"
                                    src="template/assetss/imgs/template/icons/envelope-at.svg"
                                  />
                                  <div
                                    class="btn-lien"
                                    aria-haspopup="true"
                                    aria-expanded="true"
                                  >
                                    Email
                                  </div>
                                </div>
                                <input
                                  v-model="admin.email"
                                  name="email"
                                  class="form-control"
                                  type="email"
                                  placeholder="e.g. swconnect@gmail.com"
                                  @blur="validateEmail"
                                  :class="{ 'is-invalid': mailError }"
                                  required
                                />
                                <div v-if="mailError" class="invalid-feedback">
                                  Format email incorrect.
                                </div>
                              </div>
                            </div>
                            <div
                              class="col-lg-122"
                              style="margin-bottom: 20px; margin-top: 10px"
                            >
                              <a class="link" @click="openModal"
                                >changer mot de passe</a
                              >
                            </div>
                            <div class="col-lg-122">
                              <div class="form-group mt-10">
                                <button
                                  class="btn btn-default-2 btn-brand-2"
                                  @click="updateAdmin"
                                >
                                  Enregistrer
                                </button>
                              </div>
                            </div>
                          </div>
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
    <!-- Modal -->
    <div class="modal" v-if="showModal">
      <!-- Modal content -->
      <div class="modal-content">
        <h5 class="modal-title">Changer mot de passe</h5>
        <span class="close" @click="closeModal">&times;</span>
        <div class="input-group mb-3">
          <label class="font-lg color-text-mutted-2 mb-10"
            >Nouveau mot de passe</label
          >
          <input
            v-model="admin.password"
            name="password"
            class="form-control-2"
            type="password"
            @blur="validateMdpNouv"
          />
          <div v-if="mdpnouvTouched && !isMdpNouvFilled" class="text-danger">
            Veuillez remplir ce champ de 6 caractères au minimum.
          </div>
        </div>
        <button class="btn btn-default-2 btn-brand-2" @click="closeModal">Enregistrer</button>
      </div>
    </div>
  </body>
</template>
<script>
import axios from "axios";
export default {
  name: "ProfilAdView",
  data() {
    return {
      baseUrl: "http://localhost:8000",
      admin: {
        username: "",
        email: "",
        profile_cover: null,
        profile_photo: null,
        previousPhoto: null,
        previousCover: null,
        password:''
      },
      mailError: false,
      usernameTouched: false,
      isUsernameFilled: false,
      //dropdownmenu
      showDropdown: false,
      selectedFileName: "", // Initialize selectedFileName data property to store the selected file name
      fileSizeError: false,
      selectedFileName1: "",
      fileSizeError1: false,
      mdpnouvTouched: false,
      isMdpNouvFilled: false,
      mdpconfirmTouched: false,
      isMdpConfirmFilled: false,
      showModal: false,
      

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

  this.admin.id = userId;

  // Fetch entreprise data using the entreprise ID
  this.fetchAdminData();
},
  mounted() {
    // Call the method to set previousLogo and previousCover when the component is mounted
    this.setPreviousPhotos();
  },
  methods: {

    setPreviousPhotos() {
      // Logic to retrieve previous logo and cover photo URLs or file data from your backend or wherever they are stored
      // For example:
      this.previousPhoto = this.admin.profile_photo; // Accessing as this.previousLogo
      this.previousCover = this.admin.profile_cover;
    },
    async fetchAdminData() {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/admin/${this.admin.id}/`
        );
        // Populate the etudiant object with data from the response
        this.admin = response.data;
        this.setPreviousPhotos();
        if (this.admin.profile_photo) {
          this.adminUrl = this.baseUrl + this.admin.profile_photo;
        }
      } catch (error) {
        console.error("Error fetching admin data:", error);
      }
    },
    async updateAdmin() {
      try {
          const formData = new FormData();
          formData.append("id", this.admin.id);
            formData.append('email', this.admin.email);
            formData.append('username', this.admin.username);
            if(this.admin.password){
              formData.append('password', this.admin.password);
            }
            // Check if logo file exists
          if (
            this.admin.profile_photo instanceof File &&
            this.admin.profile_photo  !== this.admin.previousPhoto
          ) {
            formData.append("profile_photo", this.admin.profile_photo);
          }
          // Append profile_cover only if it's modified or new
          if (
            this.admin.profile_cover instanceof File &&
            this.admin.profile_cover !== this.admin.previousCover
          ) {
            formData.append("profile_cover", this.admin.profile_cover);
          }
          // Convert skills to an Array if it's not already one
          const response = await axios.put(
            `http://127.0.0.1:8000/api/admin/update/${this.admin.id}/`,
            formData,
            {
              headers: {
                "Content-Type": "multipart/form-data",
              },
            }
          );
          console.log("Updated admin:", response.data);
          alert("success, you are updated");
          window.location.reload();
  
      }  catch (error) {
    console.error("Error updating admin:", error);
    let errorMessage =
      "An error occurred while updating admin. Please try again later.";
    if (error.response && error.response.data) {
      if (error.response.status === 400 ) {
        errorMessage = "Username already exists. Please choose a different username.";
      } else {
        errorMessage = error.response.data.message || errorMessage;
      }
    }
    alert(errorMessage);
  }
},

    validateMdpNouv() {
      this.mdpnouvTouched = true;
      if (
        this.admin.password &&
        this.admin.password.trim().length > 5
      ) {
        this.isMdpNouvFilled = true;
      } else {
        this.isMdpNouvFilled = false;
      }
    },

    openModal() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    logout() {
      localStorage.removeItem("user_id");
      this.$router.push("/ConnexionView");
      console.log("Logout successful");
    },
    toggleDropdown() {
      this.showDropdown = !this.showDropdown;
    },

    validateEmail() {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      this.mailError = !emailRegex.test(this.admin.email);
    },


    handleLogoFileChange(event) {
      const file = event.target.files[0];
      if (file.size <= 50 * 1024) {
        // Check if file size is less than or equal to 50 KB
        this.admin.profile_photo = file;
        this.fileSizeError = false;
        this.selectedFileName = file.name;
      } else {
          this.fileSizeError = true;
        event.target.value = "";
      }
    },

    handleCoverPhotoFileChange(event) {
    const file = event.target.files[0];
    if (file.size <= 800 * 1024) { // Check if file size is less than or equal to 50 KB
        this.admin.profile_cover = file;
        this.fileSizeError1 = false;
        this.selectedFileName1 = file.name;
    } else {
        // Handle error, such as showing a message to the user
        this.fileSizeError1=true;
        // Optionally, clear the input field
        event.target.value = '';
    }
  },
    openFileInput(event) {
      event.preventDefault(); // Prevent the default action of the label
      event.stopPropagation(); // Stop the event from propagating to the input element

      const inputId = event.currentTarget.getAttribute("for");
      const fileInput = document.getElementById(inputId);

      if (fileInput) {
        fileInput.click(); // Trigger click event on file input
      }
    },
  },
};
</script>
<style scoped>
.link {
  color: blue;
  text-decoration: underline;
  cursor: pointer; /* Change cursor to pointer on hover */
}

/* Modal styles (you can customize as needed) */
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
  margin: 10% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  max-width: 500px;
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
.h5 p {
  font-size: 22px;
  font-family: "Plus Jakarta Sans", sans-serif;
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
.col-lg-1222 {
  flex: 0 0 auto;
  width: 100%;
}
.col-lg-9 {
  flex: 0 0 auto;
  width: 100%;
}
.panel-white-2 {
  height: 1000px;
}
.col-md-3-2 {
  flex: 0 0 auto;
  width: 35%;
}
.col-md-7-2 {
  flex: 0 0 auto;
  width: 65%;
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
  height: 84px;
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
  padding-top: 50px;
}
.tab-content.active {
  display: block;
}
/* Styles for the draggable tab */
.icon {
  cursor: pointer;
  margin: 0 10px;
}
</style>
