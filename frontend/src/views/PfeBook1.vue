<template>
    <head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="ie=edge" />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:400,600" />
  <link rel="stylesheet" href="/Book/book1/css/all.min.css" />
  <link href='https://fonts.googleapis.com/css?family=Concert One' rel='stylesheet'>
  <link rel="stylesheet" href="/Book/book1/css/bootstrap.min.css" />
  <link rel="stylesheet" href="/Book/book1/css/templatemo-style.css" />
  <title>Modèle 1</title>
  
  
<!--
Mini Profile Template
https://templatemo.com/tm-530-mini-profile
-->
</head>
<body>
  <main>
  <section>
<header>
  <img :src="book.profile_logo"  alt="company-logo" class="company-logo">
  <h1>{{book.entreprise_nom}}</h1>
</header>
<div class="container-containers">
<div class="container-left">
<h1>Bienvenue {{book.entreprise_nom}}</h1>
<p>{{book.entreprise_description}}</p>
<button class="shadow-button">En savoir plus</button>
</div>
<div class="container-right">
<div class="shadow-effect"> </div>
<div>
  <img src="/template/assets/imgs/design/page1.jpg" alt="cover-page" />
</div>
</div>
</div>
  </section>
  <section>
<div class="container-containers">
<div class="container-left">
<h1>Notre Vision</h1>
<p>{{book.entreprise_vision}}</p>

</div>
<div class="container-right">
<div 
      id="drop-area" 
      class="drop-area" 
      :class="{ 'highlight': isHighlighted, 'with-image': imagePreview }"
      @dragenter.prevent="highlight" 
      @dragover.prevent="highlight" 
      @dragleave.prevent="unhighlight" 
      @drop.prevent="handleDrop" 
      @click="triggerFileInput"
    >
      <p v-if="!imagePreview">Drag and drop an image here or click to select one</p>
      <input 
        type="file" 
        id="fileElem" 
        accept="image/*" 
        @change="handleFiles" 
        ref="fileInput" 
        style="display: none;"
      >
      <img v-if="imagePreview" :src="imagePreview" alt="cover-page" class="preview-img">
    </div>
</div>
</div>
  </section>
  <section>
    <div  class="description">
 <textarea v-model="book.titre" class="description-titre"></textarea>
<textarea v-model="book.text" class="description-paragraph" rows="8"></textarea>
</div>
  </section>
  <section v-for="(offer, index) in book.offer_details" :key="index" >
<div class="container-containers">
<div class="container-left">
<h1 class="offer-heading">  {{offer.title}}</h1>
<p>{{offer.description}}</p>
<button class="shadow-button" style="border:none;" @click="openOffre(offer.offer_id)">Voir Offre</button>
</div>
<div class="container-right">
<div class="card">
  <div class="column">
  <div class="icon">     <img
                      src="/Book/book1/icons/buildings-fill.svg"
                      alt="jobBox"
                    /></div>
  <div class="title">Domaine</div>
  <div class="text">{{ offer.domain }}</div>
  <div class="icon">    <img
                      src="/Book/book1/icons/award-fill.svg"
                      alt="jobBox"
                    /></div>
  <div class="title">Role</div>
  <div class="text">{{ offer.role }}</div>

</div>
<div class="column">
  <div class="icon">   <img
                      src="/Book/book1/icons/coin.svg"
                      alt="jobBox"
                    /></div>
  <div class="title">Salaire</div>
  <div class="text">{{ offer.minimal_payment }}DT -{{ offer.maximal_payment }}DT</div>
  <div class="icon">   <img
                      src="/Book/book1/icons/journal-bookmark-fill.svg"
                      alt="jobBox"
                    /></div>
  <div class="title">Education</div>
  <div class="text">{{offer.education}}</div>
</div>
<div class="column">
  <div class="icon">   <img
                      src="/Book/book1/icons/person-workspace.svg"
                      alt="jobBox"
                    /></div>
  <div class="title">Travail</div>
  <div class="text">{{offer.offer_type}}</div>
  <div class="icon"> <img
                      src="/Book/book1/icons/calendar-check-fill.svg"
                      alt="jobBox"
                    /></div>
  <div class="title">Durée</div>
  <div class="text">{{offer.duration }}</div>
</div>
<div class="column">
  <div class="icon"> <img
                      src="/Book/book1/icons/person-plus-fill.svg"
                      alt="jobBox"
                    /></div>
  <div class="title">Binome</div>
  <div class="text">{{ offer.binome }}</div>
  <div class="icon"> <img
                      src="/Book/book1/icons/people-fill.svg"
                      alt="jobBox"
                    /></div>
  <div class="title">Stagiaires</div>
  <div class="text">{{offer.number_of_interns }}</div>

</div>

</div>
</div>

</div>
  </section>
  <section>

<div class="container-containers-2">
<div class="container-left-switch">
  <img  :src="book.profile_logo"  alt="company-logo" />
  <h1> {{book.entreprise_nom}}</h1>
</div>
<div class="container-right-switch">
<div>
  <h1>Contact</h1>
<ul>
  <li>{{book.entreprise_telephone}}</li>
  <li>{{book.entreprise_location}}</li>
  <li>{{book.entreprise_email}}</li>
</ul>
</div>
<div class="icons">
  <a  v-if="this.entreprise.site_url"  :href="book.entreprise_site"  target="_blank">
<img  src="/Book/book1/img/globe.svg" alt="icon"  > 
</a>
<a  v-if="book.entreprise_link_lien"  :href="book.entreprise_link_lien"  target="_blank">
<img src="/Book/book1/img/linkedin.svg" alt="icon">
</a>
<a  v-if="book.entreprise_in_lien"  :href="book.entreprise_in_lien"  target="_blank">
<img src="/Book/book1/img/instagram (1).svg" alt="icon">
</a>
<a  v-if="book.entreprise_fb"  :href="book.entreprise_fb"  target="_blank">
<img src="/Book/book1/img/facebook.svg" alt="icon">
</a>
</div>
<button class="update-button" @click="updateBook(this.book.id)">Enregistrer</button>
</div>
</div>
  </section>
</main>
  <!-- Welcome Section -->
    <!--
              <h1 class="tm-brand-name">Pfe Book</h1>
              <p class="tm-brand-description mb-0">{{this.entreprise.nom}}</p>
              <h2 class="tm-welcome-title">Bienvenue chez {{ this.entreprise.nom }}</h2>
              <p class="pb-0">{{this.entreprise.description}}. </p>
        
              <img :src="this.entrepriseUrl" style="height:100px   ; margin-left: 130px; margin-bottom: 20px;">
              <p v-if="this.entreprise.vision" class="mb-0">
           {{this.entreprise.vision.slice(0,147)}}
          <div v-for="(offer, index)  in offerDetails" :key="offer.id" class="tm-portfolio-item">
            <div class="tm-portfolio-name text-white " :class="['tm-portfolio-name', dynamicClass(index)]">
             {{offer.title}}
            </div>
            <div class="tm-portfolio-description">
              <h3 class="tm-text-green" :class="['tm-text-green', dynamicClassText(index)]">
                  {{ this.entreprise.nom }}
                <span class="tm-title-small">{{offer.expirationDate}}</span>
                {{offer.description.slice(0,200)}}
section -->

</body>

</template>
<script>

import $ from 'jquery';
import axios from "axios";
import Parallax from 'parallax-js';
export default {
  data() {
      return{
        imagePreview: null,
    isHighlighted: false,
          baseUrl: "http://127.0.0.1:8000/",
          book: {
            id:null,
        offer_details: [],
        entreprise: null,
        titre:'',
        text:'',
        file:null
      },

  entrepriseUrl:null,

      };
},
  created() {
     
  console.log('Selected offers:', this.getSelectedOffers);
    const userId = localStorage.getItem("user_id");
  if (!userId) {
    // User ID not found in local storage, redirect to error interface
    alert("you have to log in");
    this.$router.push("/ConnexionView");
    return;
  }
  this.entreprise = {
      id: userId
  };
  this.fetchEntrepriseData();
  this.fetchOfferDetails(this.selectedOffers);
  this.fetchBook();
},
  computed: {
      selectedOffers() {
    const offers = this.$route.query.selectedOffers;
    return offers ? offers.split(',').map(decodeURIComponent) : [];
  }
  },
  mounted() {
  // Code to execute after the component is mounted
  this.setBrandMarginTop();
  this.detectMsBrowser();

  // Handle window resize event
  window.addEventListener('resize', this.setBrandMarginTop);
  const parallaxContainer = document.querySelector('.parallax-window');
  if (parallaxContainer) {
    new Parallax(parallaxContainer);
  }
},
beforeUnmount() {
  // Cleanup code before component is destroyed
  window.removeEventListener('resize', this.setBrandMarginTop);
},
methods: {
  openOffre(offreId) {
      const url = this.$router.resolve({ name: 'OffreDetails', params: { id: offreId }}).href;
      window.open(url, '_blank');
    },
  async fetchBook() {
      const bookId = this.$route.params.id;
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/books/${bookId}/`);
        this.book = response.data;
      } catch (error) {
        console.error('Error fetching book:', error);
        alert('An error occurred while fetching the book details.');
      }
    },
    async updateBook(bookId) {
      const template= "template1";
      const formData = new FormData();
      formData.append('text', this.book.text);
      formData.append('titre', this.book.titre);
      formData.append('template',template);

      if (this.book.file) {
        formData.append('file', this.book.file);
      }

      try {
        const response = await axios.put(`http://127.0.0.1:8000/api/update-book/${bookId}/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        console.log('Book updated successfully:', response.data);
        alert('Book updated successfully!');
        this.$router.push('/bookview1/'+bookId);
      } catch (error) {
        if (error.response) {
          console.error('Error response:', error.response.data);
          console.error('Error status:', error.response.status);
          console.error('Error headers:', error.response.headers);
        } else if (error.request) {
          console.error('Error request:', error.request);
        } else {
          console.error('Error message:', error.message);
        }
        console.error('Error config:', error.config);
        alert('An error occurred while updating the book.');
      }
    },
  highlight(event) {
    event.currentTarget.classList.add('highlight');
    console.log('Highlight event triggered');
  },
  unhighlight(event) {
    event.currentTarget.classList.remove('highlight');
    console.log('Unhighlight event triggered');
  },
  handleDrop(event) {
    console.log('Drop event triggered');
    const files = event.dataTransfer.files;
    console.log('Files dropped:', files);
    if (files.length) {
      this.handleFiles({ target: { files } });
    }
  },
  handleFiles(event) {
    console.log('Handle files event triggered');
    const files = event.target.files;
    console.log('Files selected:', files);
    if (files.length) {
      const file = files[0];
      this.book.file = file;
      if (file.type.startsWith('image/')) {
        const reader = new FileReader();
        reader.onload = (e) => {
          console.log('File reader loaded');
          this.imagePreview = e.target.result;
          console.log('Image preview set:', this.imagePreview);
        };
        reader.readAsDataURL(file);
      } else {
        alert('Please drop an image file.');
      }
    }
  },
  triggerFileInput() {
    console.log('Trigger file input');
    this.$refs.fileInput.click();
  },
  fetchOfferDetails(offerIds) {
    offerIds.forEach(offerId => {
      axios
        .get(`http://127.0.0.1:8000/api/offer/${offerId}/`)
        .then((response) => {
          this.offerDetails.push(response.data);
        })
        .catch((error) => {
          console.error("Error fetching offer details:", error);
        });
    });
  },
  detectMsBrowser() {
    let using_ms_browser =
      navigator.appName == "Microsoft Internet Explorer" ||
      (navigator.appName == "Netscape" &&
        navigator.appVersion.indexOf("Edge") > -1) ||
      (navigator.appName == "Netscape" &&
        navigator.appVersion.indexOf("Trident") > -1);

    if (using_ms_browser == true) {
      alert(
        "Please use Chrome or Firefox for the best browsing experience!"
      );
    }
  },
  setBrandMarginTop() {
    let bottomContainerHeight = $(".tm-welcome-container").height();

    $(".tm-brand-container-outer").css({
      "margin-top": -bottomContainerHeight + "px"
    });
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
  dynamicClass(index) {
      const classIndex = index % 5;
    return `offer-color-${classIndex}`;
  },
  dynamicClassText(index) {
      const classIndexText = index % 5;
    return `offer-color-${classIndexText}`;
  },
  loadScripts() {
    this.loadScript('/Book/book1/js/jquery.min.js', () => {
      console.log('jQuery loaded successfully');
      this.initializeJQueryFunctions();

      this.loadScript('/Book/book1/js/parallax.min.js', () => {
        console.log('Parallax loaded successfully');
        this.initializeParallax();
      });
    });
  },
  loadScript(src, callback) {
    const script = document.createElement('script');
    script.src = src;
    script.onload = callback;
    document.head.appendChild(script);
  },
  initializeJQueryFunctions() {
    $(document).ready(function() {
      console.log('jQuery is ready to use.');
      // Initialize your jQuery functions here
    });
  },

}
};
</script>

<style scoped>
.update-button{
  position: relative;
  left:200px;
  top:150px;
  padding:10px;
  border-radius: 10px;
  font-size:16px;
  color:#fff;
  background-color: #9340FF;
  font-family:'Concert One';
  cursor:pointer;
}
.card{
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  height: 380px;
  width: 480px;
  padding: 20px;
  padding-right: 20px;
  gap: 10px;
  background-color:  #101728;
  border: solid 1px #FF3C5F;
  border-radius: 20px;
  margin-right:100px;

}
.column {
  display: flex;
  flex-direction: column;
  align-items: center;
  width:70px;
  margin-right:30px;
  padding-left: 20px;
  align-content: center;
  justify-content: center;
  flex-wrap: wrap;
}

.icon img{
height:40px;
margin-top:0px !important;
margin-bottom:20px;
width: 40px !important;
border-radius: 0px  !important;
}

.title {
  color: #FF3C5F;
font-family:'Concert One';
}

.text {
margin-bottom:20px;
color: #ecebeb;
font-family:'Concert One';
}
.offer-heading{
  color:#9340FF !important;
}
.icons img{
margin-top:50px;
margin-left:20px;
}
ul {
      list-style-type: none; /* Remove bullets */
      text-align: left;
      color: #ecebeb;
      font-family:'Concert One';
  }
.container-left-switch img{
      height: 100px;
      margin-left:0px;
      padding-left:200px;
     margin-top:-300px;
    }
  .container-left-switch h1{
      padding-left:40px;
     margin-top:-300px;
    }
.container-right-switch h1{
  color:#9340FF;
  margin-left:-140px;
  text-align: left;
  margin-left:35px;
  margin-top: -150px;
  font-size:60px;
}
  .container-right-switch{
width:50%;
padding-right:50px;
padding-left:50px;
height:600px;
flex: 1;
justify-content: center;
box-sizing: border-box;
display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.container-left-switch{
width:50%;
background-color:  #101728;
height:600px;
flex: 1;
    display: flex;
align-items: center;
  box-sizing: border-box;
}
.container-left-switch h1{
    margin-top:0px;
    margin-bottom:300px;
    padding-right:0px;
    color: #ecebeb;
  }
.container-right-switch p{
  padding-right:200px;
  padding-left:50px;
  margin-bottom:35px;
  text-align: justify;
  color: #ecebeb;
font-family:'Concert One';
}
.description{
padding:200px;


  text-align: center
}
.description-titre{
  color:#9340FF;
  font-size: 46.5px;
  background-color: #101728;
  text-align: center;
  margin-bottom:40px;
  width:100%;
  font-family:'Concert One';
  height: 100px;
  overflow-x: hidden;
  overflow-y: hidden;
}
.description-paragraph{
  background-color: #101728;
  text-align: justify;
  width:100%;
  color: #ecebeb;
  text-align: center;
  font-family:'Concert One';
  font-size:22px;
  overflow-x: hidden;
  overflow-y: hidden;
}
.drop-area {
border: 2px dashed #9340FF;
border-radius: 10px;
padding: 20px;
text-align: center;
width: 70%;
height: 70%;
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
cursor: pointer;
}

.drop-area p {
margin: 0;
color: #9340FF;
font-family:'Concert One';
}

.preview-img {
max-width: 100%;
height: auto;
margin-bottom: -70px;
}

.highlight {
border-color: #9340FF;
}

.with-image {
border: none;
}

  .shadow-effect{
  position: relative;
  z-index:1;
position: absolute;
top: calc(50% - 80px);
left: 60%;
width: 380px;
height: 380px;
border-radius: 20%;
box-shadow:
  inset 0 0 50px #260E69,
  inset 20px 0 80px #1F41BB,
  inset -20px 0 80px #260E69,
  inset 20px 0 300px #1F41BB,
  inset -20px 0 300px #260E69,
  0 0 50px #260E69,
  -10px 0 80px #1F41BB,
  10px 0 80px #1F41BB;

}
.container-right img{
  z-index:2;
  position: relative;
  right:10%;
  border-radius: 22px;
  margin-top:-120px;
  width:380px;
}
.shadow-button{
background: linear-gradient(90deg, #9340FF, #FF3C5F);
font-size: 1.5rem;
border:none;
padding: 15px;
border-radius: 30px;
margin-left:-200px;
font-family: 'Concert One';
font-size: 18px;
width:200px;
cursor: pointer;
}
  .container-left h1{
    margin-top:-150px;
    margin-bottom:50px;
    padding-left:50px;
    color: #ecebeb;
  }
.container-left p{
  padding-right:50px;
  padding-left:100px;
  margin-bottom:35px;
  text-align: justify;
  color: #ecebeb;
font-family:'Concert One';
}
.container-containers{
  display: flex;
  margin-bottom: 100px;;
}
.container-containers-2{
  display: flex;

}
.container-left{
padding-top:50px;
width:50%;
padding-right:50px;
padding-left:50px;
height:600px;
flex: 1;
justify-content: center;
box-sizing: border-box;
display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.container-right{
width:50%;
background-color:  #101728;
height:600px;
flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
}
h1{
color: #ecebeb;
font-family:'Concert One';
margin-top:10px;
}
.company-logo{
height: 50px;
margin-left: 20px;
margin-right: 40px;
}
header{
padding-top:40px;
padding-bottom: 80px;
padding-left:60px;
display: flex;
align-items: center;
background-color: #101728 !important;
}
body {
  font-family: 'Arial', sans-serif;
  margin: 0;
  padding: 0;
  background-color: #101728 !important;
  height:auto;

}
main{
  width:100%;
  height:auto;
  background-color: #101728 !important;
}


.tm-portfolio-name.offer-color-0 {
background-color: #cc6733; /* Color 1 */
}
.tm-text-green.offer-color-0 {
color: #cc6733; /* Color 1 */
}

.tm-portfolio-name.offer-color-1 {
background-color: #3398cc; /* Color 2 */
}
.tm-text-green.offer-color-1 {
color: #3398cc; /* Color 1 */
}
.parallax-window {
min-height: 1100px; /* Adjust as needed */
/* background: transparent;*/
}

.tm-portfolio-name.offer-color-2 {
background-color: #33cc67; /* Color 3 */
}
.tm-text-green.offer-color-2 {
color: #33cc67; /* Color 1 */
}

.tm-portfolio-name.offer-color-3 {
background-color: #cc33cc; /* Color 4 */
}
.tm-text-green.offer-color-3 {
color: #cc33cc;/* Color 1 */
}

.tm-brand-container-outer {
  margin-top: -400px;
}

.tm-portfolio-name.offer-color-4 {
background-color: #cc3367; /* Color 5 */
}
.tm-text-green.offer-color-4 {
color: #cc3367;/* Color 1 */
}
.tm-welcome-container {
  min-height: 400px !important;
  position: absolute !important;
  bottom: 0 !important;
  left: 0 !important;
  width: 100% !important;
  display: flex !important;
  align-items: stretch !important;
}

.tm-bg-white-transparent {
  background-color: rgba(255, 255, 255, 0.8);
}
.tm-welcome-container-2{
top:700px !important;

padding-bottom: 100px !important;
}
</style>
