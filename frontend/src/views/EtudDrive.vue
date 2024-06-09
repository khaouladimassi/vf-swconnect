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
      <title>Drive</title>
      <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css" rel="stylesheet">
      <link href="https://cdn.tiny.cloud/1/YOUR_API_KEY/tinymce/5/tinymce.min.js" referrerpolicy="origin">
      <link rel="shortcut icon" type="image/x-icon" href="/template/assets/imgs/template/favicon.svg">
  
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
    <main class="main-2" style="margin-top: 0px;position:sticky;height: 750px;">
      <div class="nav-2" style="border-right: 1px solid #dee2e6;position: relative;top: 27px;">
        <nav v-if="userType === 'entreprise'" class="nav-main-menu-2">
          <ul class="main-menu-2">
            <li>
                <a class="  dashboard2" :href="'/EntOverview/' + entreprise.id">

                <img src="../assets/imgs/template/icons/stack.svg" alt="jobBox" />
                <span class="name">Overview</span>
                </a>
            </li>
            <li>
              <router-link to="/BookGeneration"  class="dashboard2">
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
              <a class=" dashboard2" :href="'/MesOffres/' + entreprise.id">
                <img src="../assets/imgs/template/icons/briefcase2.svg" alt="jobBox" />
                <span class="name">Mes Offres</span>
              </a>
            </li>
            <li>
              <a class=" active dashboard2" :href="'/EtudDrive/' + entreprise.id">
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
              <router-link  :to="'/EtudDrive/' + etudiant.id"  class="active dashboard2">
                <img src="../assets/imgs/template/icons/folder.svg" alt="jobBox" />
                <span class="name">Mon Drive</span>
              </router-link>
            </li>
          </ul>
        </nav>
        <div class="border-bottom mb-20 mt-20"></div>
      </div>
  
      <div class="offrepublie" style="position: relative; left: 55px; top: 35px; height: auto;">
  <div style="font-size: 23px; color: #666; font-weight: 600; font-family: Arial, sans-serif; position: relative; left: 4px; top: -10px;">
    Mes fichiers
  </div>
  <div style="max-height: 600px; overflow-y: auto;">
    <table class="table">
      <thead style="background-color: #E5E8F3;">
        <tr>
          <th scope="col">Nom du fichier</th>
          <th scope="col">Date de stockage</th>
          <th scope="col"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="file in files" :key="file.id">
          <td scope="row">
            <span style="color: #6C6B6B; font-size: 15px; line-height: 1;">{{ file.nomfichier }}</span>
          </td>
          <td>
            <span style="color: #818181; font-size: 16px; padding: 7px;">{{ file.date_stockage }}</span>
          </td>
          <td>
            <div class="dropdown" @click="toggleDropdown3(file)">
              <button class="dropdown-button" type="button">
                &#8942; <!-- Code Unicode pour les trois points verticaux -->
              </button>
              <ul class="dropdown-menu" v-if="file.isDropdownOpen3" style="z-index: 10;"> <!-- Increased z-index value -->
                <li><a class="dropdown-item" @click="ouvrirFichier(file.id)"><i class="fas fa-eye" style="color: green; padding: 10px;"></i> Ouvrir</a></li>
                <li><a class="dropdown-item" href="#" @click="supprimerFichier(file.id)"><i class="fas fa-trash" style="color: red; padding: 10px;"></i> Supprimer</a></li>
              </ul>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>



<button type="submit" class="btn btn-secondary btn-fle" style="position: sticky; top: 300vh; width: 20%; border-color: white; left: -15px;"  @click="OpenModal">
  <p class="creer" style="position: relative; left: 2px;"><i class="fas fa-plus fa-1x" style="padding: 5px;"></i> </p>
</button>



<div class="modal"  id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" v-if="showModal" style="display: flex;">
  <div class="modal-dialog" style="position: relative;left: 40px;">
    <div class="modal-content" style="height: 400px;">
      
      <div class="modal-header">
        <button type="button" class="btn-close"  @click="CloseModal"></button>
      </div>

      <div class="modal-body" >
      
        <form method="post" enctype="multipart/form-data">
    <div class="upload-container" style="width: 320px;height: 150px;top: 8px;left: -5px;">
        <label for="imageUpload" class="upload-label">
            <i class="fas fa-cloud-download-alt fa-3x" style="position: relative;color: #828282; opacity: 0.2; left:10px;padding: 10px;bottom: 12px;" ></i>
            <p class="upload-info" style="left: 3%;bottom: 25px;font-weight: 700;">Téléchargez votre fichier</p>
            <p class="upload-info" style="left: 5%;bottom: 27px;">Les fichiers PDF seulement !</p>
        </label>
        <input type="file" id="imageUpload" name="imageUpload" accept=".pdf" style="display: none;" @change="displayFileName">
        <p v-if="uploadedFileName" class="upload-info" style="position:relative;top: 24px; color: #99C9FE ;font-size: 20px;"><strong>Fichier sélectionné : </strong>{{ uploadedFileName }}</p>
        <p v-if="invalidFile" class="upload-info" style="position:relative;top: 17px; color: red; font-size: 16px;">Erreur : Veuillez sélectionner un fichier PDF !</p>
    </div>
</form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn " @click="ajouterFichier" style="position: relative;top: 27px;left: 18px;background-color: #447AB8;"><p style="color: white;">Ajouter</p></button>
      </div>
    </div>
  </div>
</div>


    </main>
    <div class="footer-2 mt-20"  style="height: 99px;">
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
 
 export default {
  components: { navbarEntreprise, navbarEtudiant },

   data() {
     return {
       showModal: false,
       fichier: null,
       uploadedFileName: '',
       invalidFile: false,
       files: [],
       isDropdownOpen1: false,
       isDropdownOpen2: false,
       userType: null,
        entreprise: {},
        etudiant: {},



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

    // Fetch entreprise data using the entreprise ID

    const userType = localStorage.getItem("user_type");
    // Set userType only if it's valid

      this.userType = userType;


  },

mounted() {
    // Appeler la méthode recupererFichiers lors du montage du composant
    this.recupererFichiers();
},
   methods: {
     OpenModal() {
       this.showModal = true;
     },
     CloseModal() {
       this.showModal = false;
     },
     displayFileName(event) {
       const input = event.target;
       if (input.files.length > 0) {
         this.fichier = input.files[0];
         this.uploadedFileName = input.files[0].name;
       } else {
         this.fichier = null;
         this.uploadedFileName = '';
       }
     },
     ajouterAction() {
      const userId = localStorage.getItem("user_id");
  if (!userId) {
    alert("Vous devez être connecté.");
    return;
  }
  axios.post(`http://127.0.0.1:8000/creer-action/${userId}/`, {
    action_message: 'Ajout de fichier dans le drive',
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

ajouterFichier() {
  const userId = localStorage.getItem("user_id");
  if (!userId) {
    alert("Vous devez être connecté.");
    return;
  }

  if (!this.fichier) {
    alert('Veuillez sélectionner un fichier.');
    return;
  }
  
  let formData = new FormData();
  formData.append('fichier', this.fichier); // Ajouter le fichier
  formData.append('nomfichier', this.fichier.name); // Ajouter le nom du fichier
  formData.append('user', userId); // Ajouter l'ID de l'utilisateur

  axios.post(`http://127.0.0.1:8000/creer-fichier/${userId}`, formData)
    .then(() => {
      alert('Fichier ajouté avec succès !');
      this.CloseModal();
      this.ajouterAction();
      
      // Récupérer immédiatement les fichiers après l'ajout réussi du fichier
      this.recupererFichiers();
    })
    .catch(error => {
      console.error('Erreur lors de la requête :', error);
      alert('Une erreur est survenue lors de l\'ajout du fichier.');
    });
},

recupererFichiers() {
    // Récupérer l'ID de l'utilisateur
    const userId = localStorage.getItem("user_id");
    if (!userId) {
        alert("Vous devez être connecté.");
        return;
    }

    // Envoyer une requête GET pour récupérer tous les fichiers
    axios.get(`http://127.0.0.1:8000/get-all-fichiers/${userId}`)
        .then(response => {
            // Traiter la réponse et afficher les fichiers récupérés
            this.files = response.data;
            // Vous pouvez traiter les fichiers récupérés ici, par exemple, les afficher dans une liste ou une table
        })
        .catch(error => {
            console.error('Erreur lors de la récupération des fichiers :', error);
            alert('Une erreur est survenue lors de la récupération des fichiers.');
        });
},
supprimerFichier(pk) {
  const userId = localStorage.getItem("user_id");
    if (!userId) {
        alert("Vous devez être connecté.");
        return;
    }
    // Envoyer la requête DELETE pour supprimer le fichier avec l'ID spécifié
    axios.delete(`http://127.0.0.1:8000/supprimer-fichier/${pk}/${userId}`)
      .then(() => {
        // Supprimer 'response' de la fonction de rappel
        // Afficher un message de succès ou effectuer d'autres actions si nécessaire
        alert('Fichier supprimé avec succès !');
        // Mettre à jour la liste des fichiers après la suppression
        this.recupererFichiers();
      })
      .catch(error => {
        // Gérer les erreurs ici
        console.error('Erreur lors de la suppression du fichier :', error);
        alert('Une erreur est survenue lors de la suppression du fichier.');
      });
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
     toggleDropdown3(file) {
    file.isDropdownOpen3 = !file.isDropdownOpen3;
  },
 
  ouvrirFichierPDF(fichierId) {
  // Construire l'URL vers la vue Django pour servir le fichier
  const url = `http://127.0.0.1:8000/servir-fichier/${fichierId}/`;
  // Ouvrir le fichier dans une nouvelle fenêtre ou un nouvel onglet
  window.open(url, '_blank');
},
ouvrirFichier(fichierId) {
  // Appel à la méthode ouvrirFichierPDF avec l'identifiant du fichier
  this.ouvrirFichierPDF(fichierId);
},



   }


 };
 </script>
 

  <style scoped>
    
   
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
.table {

width: 980px;
}
.dropdown-button {
border: none;
background: none;
padding: 0;
font-size: 24px;
line-height: 1;
}
.modal {
    display: none;
    position: fixed;
    z-index: 1;
    left: 50%;
    top: 60%;
    transform: translate(-50%, -50%);
    width: 40%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0); /* Ajoutez une légère opacité pour l'arrière-plan */
}
  </style>
  