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
    <title>S'inscrire</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css" rel="stylesheet">
    <link href="https://cdn.tiny.cloud/1/YOUR_API_KEY/tinymce/5/tinymce.min.js" referrerpolicy="origin">


    <link href="./template/assets/css/plugins/animate.min.css" rel="stylesheet">
    <link href="./template/assets/css/plugins/magnific-popup.css" rel="stylesheet">
    <link href="./template/assets/css/plugins/perfect-scrollbar.css" rel="stylesheet">
    <link href="./template/assets/css/plugins/select2.min.css" rel="stylesheet">
    <link href="./template/assets/css/plugins/swiper-bundle.min.css" rel="stylesheet">
    
    <link href="/template/assets/css/stylecd4e.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  </head>
  <body style="overflow:hidden;height:100%">
  <div class="containertem">
   
    <div class="row">
      <div class="col-md-6">
        <!-- Second division for signup form -->
        <div class="logo-container">
          <img src="template/assets/imgs/page/login-register/logo.png" alt="logo" class="img-fluid logo-img">
        </div>
        <div class="card" style="height:79%;padding-bottom:10px;">
          <div class="card-body">
            <h5 class="card-title">Créer Un Compte</h5>
            <div>
              <p>Vous avez déjà un compte ? <routerLink to ="/ConnexionView"> Connectez-vous</routerLink></p>
            </div>
            <div class="container-ent">
              <p>Créer un compte en tant que</p>
              <div class="button-container">
                <router-link to="/PageRegisterEtudiant" >
                <button class="btn btn-secondary btn-etu" >
                  <img src="template//assets/imgs/page/login-register/icon-Etu.png" alt="Etudiant Icon" class="icon-etu">
                  <p class="etu">Etudiant</p>
                </button>
              </router-link>
                <router-link to="/PageRegisterRH" >
                <button class="btn btn-secondary btn-ent">
                <img src="template//assets/imgs/page/login-register/icon-ent.png" alt="Entreprise Icon" class="icon-ent">
                <p class="entr">Entreprise</p>
                </button>
                 </router-link>

              </div>
            </div>
            <div class="form-group" style="display: flex;">
  <span style="flex: 1;">
    <input v-model="first_name" type="text" class="form-control" name="first_name" placeholder="Entrez votre prénom" style="height:40px; font-size:16px;">
  </span>
  <span style="flex: 1; margin-left: 10px;">
    <input v-model="last_name" type="text" class="form-control" name="last_name" placeholder="Entrez votre nom" style="height:40px; font-size:16px;">
  </span>
</div>
<div class="form-group">
  <input v-model="username" type="text" class="form-control" name="username" placeholder="Entez votre username" @blur="checkUsername" required style="height:40px; font-size:16px;">
  <div v-if="showUsernameExistsAlert" class="alert alert-danger">Le nom d'utilisateur existe déjà.</div>
</div>


<div class="form-group">
  <input v-model="email" type="email" class="form-control" name="email" placeholder="Entez votre email" @blur="validateEmail" :class="{ 'is-invalid': mailError }" required style="height:40px; font-size:16px;">
  <div v-if="mailError" class="invalid-feedback">Format email incorrect.</div>
</div>

<div class="form-group">
  <input v-model="password" @input="checkPassword" type="password" class="form-control" name="password" placeholder="Entez votre  mot_de_passe" @blur="validateMDP" :class="{ 'is-invalid': MDPError }" required>
  <div v-if="MDPError" class="invalid-feedback">Le mot de passe doit contenir au moins 6 caractères.</div>
</div>
<div class="form-group">
  <input v-model="confirm" type="password" class="form-control" name="confirm" placeholder="Confirmation" @blur="validateConfirmation" :class="{ 'is-invalid': ConfirmError }" required>
  <div v-if="ConfirmError" class="invalid-feedback">La confirmation du mot de passe ne correspond pas au mot de passe saisi.</div>
</div>


            <button type="submit" class="btn btn-secondary btn-fle" @click="creerCompte">
              <p class="creer">Créer un compte</p>
              <img src="template/assets/imgs/page/login-register/fleche.png" alt="fleche Icon" class="icon-fleche">
            </button>
        
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <!-- First division for image -->
       <!-- <img src="frontend/assets/imgs/page/login-register/image.png" alt="Your Image" class="img-fluid smaller-image">-->
        <div class="img-1 d-none d-lg-block" style="position: relative;left: 160px;top: 130px; "><img class="shape-1" src="template/assets/imgs/page/login-register/students.png" alt="Your Image"></div>
      </div>
    </div>
  </div>
  <!-- Fenêtre modale pour afficher le message d'erreur -->
  <div v-if="showErrorMessage" class="modal">
    <div class="modal-content">
      <span class="close" @click="hideErrorMessage">&times;</span>
      <p>Veuillez remplir tous les champs et cocher la case pour créer un compte.</p>
    </div>
  </div>
  </body>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PageRegister',
  data() {
    return {
      showUsernameExistsAlert: false,
      showErrorMessage: false, // Indicateur pour afficher ou masquer la fenêtre modale

     
      first_name: '', 
      last_name: '',
      username:'',
      email: '',
      password: '',
      confirm: '',

      mailError: false, 
      MDPError: false, 
      ConfirmError:false,
    };
  },
 
  methods: {

    creerCompte() {
   // Vérifier la validation du formulaire
   if (!this.first_name || !this.last_name ||! this.username || !this.email || !this.password || !this.confirm ) {
     // Afficher le message d'erreur
     this.showErrorMessage = true;
   } else {
     // Masquer la fenêtre modale d'erreur
     this.showErrorMessage = false;
     
     // Données à envoyer
     const userData = {
       first_name: this.first_name,
       last_name: this.last_name,
       username:this.username,
       email: this.email,
       password: this.password,
      
     };

     // Envoyer une requête POST au backend
     axios.post('http://127.0.0.1:8000/api/etudiant/', userData)


       .then(response => {
         // Gérer la réponse du backend si nécessaire
         console.log(response.data);
         this.$router.push('/ConnexionView');
       })
       .catch(error => {
         // Gérer les erreurs de la requête
         console.error('Erreur lors de la requête:', error);
         if (error.response && error.response.status === 400) {
                        // Set showUsernameExistsAlert to true
                        this.showUsernameExistsAlert = true;
                    }
       });
   }
 },
    validateEmail() {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      this.mailError = !emailRegex.test(this.email);
    },
    validateMDP(){
      this.MDPError = this.password.length < 6;
    },
    validateConfirmation() {
  this.ConfirmError = this.confirm !== this.password;
},


    hideErrorMessage() {
      // Masquer la fenêtre modale
      this.showErrorMessage = false;
    },
  
  }
  
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

</style>
