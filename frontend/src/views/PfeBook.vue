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
      <title>Pfe Book</title>
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
        <navbarEntreprise v-if="userType === 'entreprise' " />
 <navbarEtudiant v-if="userType==='etudiant'" />
    <main class="main-2" style="margin-top: 0px">
      <div class="nav-2" style="border-right: 1px solid #dee2e6">
        <nav class="nav-main-menu-2">
          <ul class="main-menu-2">
            <li>
              <a class="dashboard2" href="candidates.html"
                ><img
                  src="../assets/imgs/template/icons/stack.svg"
                  alt="jobBox"
                /><span class="name">Overview</span></a
              >
            </li>
            <li>
              <a class="dashboard2" href="candidates.html"
                ><img
                  src="../assets/imgs/template/icons/file-person.svg"
                  alt="jobBox"
                /><span class="name">Générer Pfe Book</span></a
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
              <a class="active dashboard2" :href="'/MesOffres/' + entreprise.id"
                ><img
                  src="../assets/imgs/template/icons/briefcase2.svg"
                  alt="jobBox"
                /><span class="name">Mes Offres</span></a
              >
            </li>
            <li>
              <a class="dashboard2" href="my-tasks-list.html"
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
              <h3 class="mb-35">Pfe Book</h3>
       
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
                            <div class="row display-list">
                  <div   class="col-xl-12 col-12">
       
                    <div class="card-grid-2 hover-up " style="    height: 249px;"><span class="flash"></span>
                      <div class="row">
                        <div class="col-lg-6 col-md-6 col-sm-12">
                          <div class="card-grid-2-image-left">
                            <div class="image-box"><img  :src="this.entrepriseUrl" alt="jobBox" style="width: 52px;;"></div>
                            <div class="right-info"><a class="name-job">{{entreprise.nom}}</a></div>
                          </div>
                        </div>
                      </div>
                      <div class="card-block-info">
                        <h4>{{titre}}</h4>
                        <p style="cursor:pointer" class="font-sm color-text-paragraph mt-10" @click="openBOOK">pfebook.pdf</p>
                        <div class="card-2-bottom mt-20">
                          <div class="row">
                            <div class="col-lg-7 col-7"><span class="card-text-price">
                            </span></div>
                            <div class="col-lg-5 col-5 text-end">
                              <div v-if="pfe_book && pfe_book.length > 0" class="btn btn-apply-now" style="color:#447AB8" type="submit" @click="openModal(pfe_book[0].id)">Modifier</div>

                              <div class="btn btn-apply-now"  style="    margin-left: 14px;color:#447AB8" @click="deletePfebook(pfe_book[0].id)">Supprimer</div>
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
      <!-- Modal -->
      <div class="modal" v-if="showModal">
      <!-- Modal content -->
      <div class="modal-content" style="max-height: 70vh; overflow-y: auto;">
        <h5 class="modal-title">Modifier Pfe Book</h5>
        <span class="close" @click="closeModal">&times;</span>
        <div class="col-md-100">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10" style="margin-right: 700px;"
                                >Pfe book</label
                              >
                              <label
                                for="FileInput"
                                class="drag-drop-area"
                                @click="openFileInput"
                              >
                                Cliquez ici pour choisir un pfe book.<br />
                                Le format supporté est PDF. La taille maximum
                                est 10 MB.
                              </label>
                              <input
                                type="file"
                                id="FileInput"
                                accept=".pdf"
                                @change="handleFiles($event.target.files)"
                                style="display: none"
                              />
                              <p
                                v-if="selectedFileName"
                                class="selected-file-info"
                              >
                                Fichier sélectionné : {{ selectedFileName }}
                              </p>

                              <p v-if="fileSizeError" class="text-danger">
                                La taille du fichier dépasse 10 MB.
                              </p>
                            </div>
                          </div>
                          <div class="col-lg-12">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10" style="margin-right: 720px;"
                                >Titre*</label
                              >
                              <input
                                v-model="this.titre"
                                name="titre"
                                class="form-control-2"
                                type="text"
                                @blur="validateTitreBook"
                              />
                              <div
                                v-if="titreBookTouched && !isTitreBookFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ.
                              </div>

                          
                            </div>
                          </div>
                          <div class="col-lg-12">
                            <div class="form-group mt-10">
                              <button
                                class="btn btn-default-2 btn-brand-2"
                                type="submit"
                                @click="updatePfebook(selectedBookId)"
                              >
                                Modifier
                              </button>
                            </div>
                          </div>

      </div>
    </div>
  </body>
    
  </template>
  <script>
  import axios from "axios";
  import navbarEntreprise from '@/components/navbarEntreprise.vue';
  export default {
    name: "PfeBook",
    components:{navbarEntreprise},
    data() {
      return {
        selectedFileName: "",
      file: null,

        baseUrl: "http://localhost:8000",
        entrepriseUrl:null,
        userType:'',
        entreprise:{},
          titre:'',
        pfe_book:{
        },
        pfebooks:{},
        showModal: false,
        titreBookTouched:false,
        isTitreBookFilled:false,
        
       
        //filesize control
        fileSizeError: false,
        //dropdownmenu
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
  
    this.entreprise.id = userId;
    console.log(this.entreprise.id);
    // Fetch entreprise data using the entreprise ID
    this.fetchEntrepriseData();
    const userType = localStorage.getItem('user_type');
    if (userType === 'entreprise') {
      this.userType = userType;}
  },
  mounted() {
    // Call a method to fetch all offers from the backend API

    this.fetchPfeBook();
  },

  
    methods: {
      updatePfebook(pfebookId) {
    // Check if a file is selected
    if (!this.file || !this.selectedFileName || !this.titre) {
        console.log('File or filename not selected');
        return;
    }

    // Create FormData object and append form fields
    const formData = new FormData();
    formData.append('id', pfebookId);
    formData.append('entreprise', this.entreprise.id);
    formData.append('file', this.file);
    formData.append('titre',this.titre);

    // Send PUT request to update Pfebook
    axios.put(`http://127.0.0.1:8000/api/entreprise/${this.entreprise.id}/update/pfebook/${pfebookId}/`, formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
    .then(response => {
        // Handle success
        console.log('File uploaded successfully:', response.data);
        alert('File uploaded successfully');
    })
    .catch(error => {
        // Handle error
        console.error('Error uploading file:', error);
        alert('Error uploading file', this.file);
    });
},
async deletePfebook(pfebookId) {
  if (!pfebookId) {
    console.error("Pfebook ID is null or undefined");
    return;
  }

  try {
    const response = await axios.delete(
      `http://127.0.0.1:8000/api/pfebook/delete/${pfebookId}/`
    );

    console.log("Deleted pfebook:", response.data);

    // If pfebooks is an array, remove the deleted pfebook from it
    if (Array.isArray(this.pfebooks)) {
      this.pfebooks = this.pfebooks.filter(pfebook => pfebook.id !== pfebookId);
    } else if (this.pfebooks && this.pfebooks.id === pfebookId) {
      // If pfebooks is not an array but matches the deleted pfebook, set it to null
      this.pfebooks = null;
    }

    alert("Success, pfebook deleted");

    // Navigate to the appropriate route
    this.$router.push(`/MesOffres/${this.entreprise.id}`);
    
  } catch (error) {
    console.error("Error deleting pfebook:", error);
    alert("An error occurred while deleting pfebook. Please try again later.");
  }
},


    handleFiles(files) {
      // Check if any file is selected
      if (files.length > 0) {
        // Check if file size exceeds 10 MB (10 * 1024 * 1024 bytes)
        if (files[0].size > 10 * 1024 * 1024) {
          this.fileSizeError = true; // Set fileSizeError to true if file size exceeds 10 MB
          this.selectedFileName = ""; // Clear selectedFileName
        } else {
          this.file = files[0];
          this.fileSizeError = false; // Reset fileSizeError
          this.selectedFileName = files[0].name; // Set selectedFileName to the name of the selected file
        }
      } else {
        // No file selected, reset selectedFileName and fileSizeError
        this.selectedFileName = "";
        this.fileSizeError = false;
      }

      for (let i = 0; i < files.length; i++) {
        // Your code to handle the uploaded file goes here
        console.log("Uploaded file:", files[i]);
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
      openBOOK() {
  // Check if entreprise and pfe_book are available
  if (this.entreprise && this.pfe_book && this.pfe_book.length > 0) {
    // Construct the full URL to the file
    const baseUrl = 'http://127.0.0.1:8000'; // Replace with your API base URL
    const fileUrl = baseUrl + this.pfe_book[0].file; // Assuming pfe_book is an array

    // Open a new window or tab to display the file content
    window.open(fileUrl, '_blank');
  } 
},
openModal(pfebookId) {

    if (pfebookId) {
    this.showModal = true;
    this.selectedBookId = pfebookId;}
    else {
        console.error('pfebookId is undefined or null');
    }
},
    closeModal(){
        this.showModal = false;
    },

async fetchPfeBook() {
        try {
          const response = await axios.get(
            `http://127.0.0.1:8000/api/pfebook/entreprise/${this.entreprise.id}/`
          );
          // Populate the etudiant object with data from the response
          this.pfe_book = response.data;
          console.log(this.pfe_book);
          const pfebookId=this.pfe_book[0].id;
          this.titre = this.pfe_book[0].titre;
          console.log(pfebookId);
       
          
        } catch (error) {
          console.error("Error fetching pfebook data:", error);
        }
      },
      validateTitreBook(){
      this.titreBookTouched = true;
      if(this.titre && this.titre.trim()!==""){
        this.isTitreBookFilled=true;
      }else{
        this.isTitreBookFilled=false;
      }
    },
      
      async fetchEntrepriseData() {
        try {
          const response = await axios.get(
            `http://127.0.0.1:8000/api/entreprises/get/${this.entreprise.id}/`
          );
          // Populate the etudiant object with data from the response
          this.entreprise = response.data;
          if (this.entreprise.profile_logo) {
            this.entrepriseUrl = this.baseUrl + this.entreprise.profile_logo;
          }
        } catch (error) {
          console.error("Error fetching entreprise data:", error);
        }
      },


      logout() {
            localStorage.removeItem('user_id');
            this.$router.push('/ConnexionView');
            console.log('Logout successful');
      },
      
    }
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
  .col-lg-1222 {
    flex: 0 0 auto;
    width: 100%;
  }
  .col-lg-9 {
    flex: 0 0 auto;
    width: 100%;
  }
  .panel-white-2 {
    height: 1490px;
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
  </style>
  