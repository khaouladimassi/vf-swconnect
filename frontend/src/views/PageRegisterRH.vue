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

<link href="./template/assets/css/stylecd4e.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
</head>
<body>
<div class="container">

 <div class="row">
   <div class="col-md-6">
     <!-- First division for image -->
     <div class="img-1 d-none d-lg-block" style="position: relative; left: 90px;top: 140px;"><img class="shape-1" src="template/assets/imgs/page/login-register/RH.png" alt="Your Image"></div>
   </div>
   <div class="col-md-6">
     <!-- Second division for signup form -->
     <div class="logo-container" style="position: relative;right:25%;">
       <img src="template/assets/imgs/page/login-register/logo.png" alt="logo" class="img-fluid logo-img">
     </div>
     <div class="card" style="position: relative; left: 100px; top: 15px; height: auto;">
       <div class="card-body">
         <h5 class="card-title">Créer Un Compte</h5>
         <div><p>Vous avez déjà un compte ? <routerLink to ="/ConnexionView"> Connectez-vous</routerLink></p></div> 
         <div class="container-ent">
           <p>Créer un compte en tant que</p>
           <div class="button-container">
             <router-link to="/PageRegisterEtudiant" >
               <button class="btn btn-secondary btn-etu" >
                 <img src="template/assets/imgs/page/login-register/icon-Etu.png" alt="Etudiant Icon" class="icon-etu">
                 <p class="etu">Etudiant</p>
               </button>
             </router-link>
             <router-link to="/PageRegisterRH" >
               <button class="btn btn-secondary btn-ent">
                 <img src="template/assets/imgs/page/login-register/icon-ent.png" alt="Entreprise Icon" class="icon-ent">
                 <p class="entr">Entreprise</p>
               </button>
             </router-link>
           </div>
         </div>
         <div class="form-group">
           <input type="text" class="form-control" v-model="nom" name="nom" placeholder="Entez le nom de l'entreprise" required style="font-size:16px;">
         </div>
         <div class="form-group">
           <input type="text" class="form-control" v-model="username" name="username" placeholder="Entez le username de l'entreprise" required style="font-size:16px;">
           <div v-if="showUsernameExistsAlert" class="alert alert-danger">Le nom d'utilisateur existe déjà.</div>
         </div>
         <div class="form-group">
           <input type="email" class="form-control" v-model="email" name="email" placeholder="Entez votre email"  @blur="validateEmail" :class="{ 'is-invalid': mailError }" required style="font-size:16px;">
           <div v-if="mailError" class="invalid-feedback">Format email incorrect.</div>
         </div>
         <div class="form-group">
           <input type="text" class="form-control" v-model="numero" name="numero" placeholder="Entez votre Numéro de téléphone"  @blur="validateNumero" :class="{'is-invalid ':numeroError }" required style="font-size:16px;" >
           <div v-if="numeroError" class="invalid-feedback">Le numéro de téléphone doit contenir  8 chiffres</div>
           
         </div>
         <div class="form-group">
           <input type="password" class="form-control" v-model="password" name="password" placeholder="Entez votre mot_de_passe"  @blur="validateMDP" :class="{ 'is-invalid': MDPError }" required style="height:50px; font-size:16px;">
           <div v-if="MDPError" class="invalid-feedback">Le mot de passe doit contenir au moins 6 caractères.</div>
         </div>
         <div class="form-group">
           <input type="password" class="form-control" v-model="confirm" name="confirm" placeholder="Confirmation"  @blur="validateConfirmation" :class="{ 'is-invalid': ConfirmError }" required style="height:50px; font-size:16px;">
           <div v-if="ConfirmError" class="invalid-feedback">La confirmation du mot de passe ne correspond pas au mot de passe saisi.</div>
         </div>
         <button type="submit" class="btn btn-secondary btn-fle" @click="creerCompte">
           <p class="creer">Créer un compte</p>
           <img src="template/assets/imgs/page/login-register/fleche.png" alt="fleche Icon" class="icon-fleche">
         </button>
       </div>
     </div>
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
name: 'PageRegisterHR',
data() {
 return {
   showUsernameExistsAlert: false,
   showErrorMessage: false,
   username: '',
   nom:'',
   email: '',
   numero: '',
   password: '',
   confirm: '',
   mailError: false, 
   MDPError: false, 
   ConfirmError: false,
   numeroError: false
 };
},
methods: {
 creerCompte() {
if (!this.nom || !this.username || !this.email || !this.numero || !this.password || !this.confirm ) {
this.showErrorMessage = true;
} else {
this.showErrorMessage = false;
const RHData = {
 nom: this.nom,
 username: this.username,
 telephone: this.numero,
 email: this.email,
 password: this.password,
};
console.log(RHData);
axios.post('http://127.0.0.1:8000/api/entreprise/', RHData)
 .then(response => {
   console.log(response.data);
   this.$router.push('/ConnexionView');

   const nomEntreprise = this.nom;
   const message = `Un compte a été créé pour l'entreprise ${nomEntreprise}`;
   this.ajouterNotification(message);

 })
 .catch(error => {
   console.error('Erreur lors de la requête:', error);
   if (error.response && error.response.status === 400) {
     this.showUsernameExistsAlert = true;
   }
 });
}
},
ajouterNotification(message) {
// Envoyer la notification au serveur
axios.post('http://127.0.0.1:8000/creer-notif-admin/', {
message: message,
})
.then(response => {
console.log('Notification ajoutée avec succès:', response.data);
})
.catch(error => {
console.error('Erreur lors de l\'ajout de la notification:', error);
});
},

validateNumero() {
   const numeroRegex = /^\d{8}$/;
   this.numeroError = !numeroRegex.test(this.numero);
},
 validateEmail() {
   const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
   this.mailError = !emailRegex.test(this.email);
 },
 validateMDP() {
   this.MDPError = this.password.length < 6;
 },
 validateConfirmation() {
   this.ConfirmError = this.confirm !== this.password;
 },
 hideErrorMessage() {
   this.showErrorMessage = false;
 },
}
};
</script>

<style>
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
.container{
margin-bottom:100px;
}
</style>