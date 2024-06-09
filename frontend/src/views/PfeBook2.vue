<template>
      <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link href="https://fonts.cdnfonts.com/css/garet" rel="stylesheet">
                
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:400,600" />
    <link rel="stylesheet" href="/Book/book1/css/all.min.css" />
    <link href='https://fonts.googleapis.com/css?family=Concert One' rel='stylesheet'>
    <link rel="stylesheet" href="/Book/book1/css/bootstrap.min.css" />
    <link rel="stylesheet" href="/Book/book1/css/templatemo-style.css" />
    <title>Modèle 2</title>
    
    
<!--
Mini Profile Template
https://templatemo.com/tm-530-mini-profile
-->
  </head>
  <body>
    <main>
    <section class="cover-1">
      <header>
    <img :src="book.profile_logo"  alt="company-logo" class="company-logo">
    <h1>{{book.entreprise_nom}}</h1>
</header>
<div class="container-containers">
  <div class="container-left">
  <h1 style=" margin-right: 900px;">Bienvenue chez {{book.entreprise_nom}}</h1>
  <p style=" margin-right: 650px;">{{book.entreprise_description}}</p>
<button style=" margin-right: 700px;" class="shadow-button">En savoir plus</button>
</div>
</div> 

    </section>
    <section class="cover-2">
<div class="container-containers">
  <div class="container-left">
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
        <p v-if="!imagePreview"  style="padding-left: 100px;color: #000000;" >Drag and drop an image here or click to select one</p>
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
<div class="container-right" 
style="display:flex;
flex: 1;
  justify-content: center;
  box-sizing: border-box;
  display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding-right:50px;
padding-left:50px;
background-color: #DDD8D3;">
  <textarea rows="3" v-model="book.titre" style=" font-family: 'Garet'; font-weight:bold;
    margin-top: 10px;   text-align: justify; width:400px; color: #000000;   font-size: 1.5rem;
    overflow-x:hidden; overflow-y:hidden;">Proxym est une entreprise qui cherche à changer la façon dont les gens se connectent.</textarea>
  <textarea v-model="book.text" rows="8"  style="width:400px; color:#000000;  
      overflow-x:hidden; overflow-y:hidden;
     text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</textarea>
</div>
</div>
    </section>
    <section v-for="offer  in book.offer_details" :key="offer.id" class="cover-3" >
<div class="container-containers">
  <div class="container-left" style="padding-top:150px">
  <h1 class="offer-heading">  {{offer.title}}</h1>
      <table class="table">
  <tbody>
    <tr>
      <th scope="row" >    <div class="title">Role</div></th>
      <td class="cus-td ">    <div class="text">{{ offer.role }}</div></td>
    </tr>
    <tr>
      <th scope="row" >    <div class="title">Domaine</div></th>
      <td class="cus-td ">    <div class="text">{{ offer.domain }}</div></td>
    </tr>
    <tr>
      <th scope="row" >    <div class="title">Education</div></th>
      <td class="cus-td ">    <div class="text">{{offer.education}}</div></td>
    </tr>
    <tr>
      <th scope="row" >    <div class="title">Salaire</div></th>
      <td class="cus-td ">    <div class="text">{{ offer.minimal_payment }}DT -{{ offer.maximal_payment }}DT</div></td>
    </tr>
    <tr>
      <th scope="row" >    <div class="title">Stagiaires</div></th>
      <td class="cus-td ">    <div class="text">{{offer.number_of_interns }}</div></td>
    </tr>
    <tr>
      <th scope="row" >    <div class="title">Travail</div></th>
      <td class="cus-td ">    <div class="text">{{offer.offer_type}}</div></td>
    </tr>
    <tr>
      <th scope="row" >    <div class="title">Durée</div></th>
      <td class="cus-td ">    <div class="text">{{offer.duration }}</div></td>
    </tr>
    <tr>
      <th scope="row" >    <div class="title">Binôme</div></th>
      <td class="cus-td ">    <div class="text">{{ offer.binome }}</div></td>
    </tr>
  </tbody>
</table>
  <button class="shadow-button" style="padding:10px;border-radius: 10px;  margin-left:-200px;     position: relative;
    bottom: -30px;"  @click="openOffre(offer.offer_id)">Voir Offre</button>
</div>
<div class="container-right">
<div class="content">
  <div style="font-weight: bold"  class="title">Description</div>
  <p style="    width: 400px; color:#fff;     text-align: justify;">{{offer.description}}</p>
  <div style="font-weight: bold"  class="title">Compétences</div>
  <div style="display: flex;">
                    <p v-for="(skill, index) in offer.skills"
                    :key="index"  class="skills"> {{ skill }}</p>
                  </div>
</div>
    </div>

</div>
    </section>
    <section class="cover-4">

<div class="container-containers-2">
  <div class="container-left-switch" style="   background-color:  #FDFDFD;">
<img src="/Book/book2/cover2.png" alt="cover2" style="height:100%; position: relative; bottom: -200px; left:-100px;">
</div>
<div class="container-right-switch">
  <div>
    <h1 style="position: relative;
    bottom: -100px;">Contactez-nous</h1>
    <div class="column"> 
    <div class="title" style="color: #000000;     text-align: left; position: relative;
    left: -50px;"><b>Téléphone</b></div>
    <div class="text" style="color: #000000; margin-bottom:50px;    text-align: left;">{{book.entreprise_telephone}}</div>
    <div class="title" style="color: #000000;    text-align: left;     position: relative;
    left: -50px;"><b>Email</b></div>
    <div class="text" style="color: #000000;    text-align: left;">{{book.entreprise_email}}</div>

  </div>
  <div class="column" style="    left: 350px;
    bottom: -51px;"> 
    <div class="title" style="color: #000000;     text-align: left; position: relative;
    left: -50px;"><b>Location</b></div>
    <div class="text" style="color: #000000; margin-bottom:50px;    text-align: left;">{{book.entreprise_location}}</div>

  </div>
  </div>
  <div class="icons">
    <img :src="book.profile_logo"  alt="company-logo" class="company-logo">
    <p style="color:#000000; font-family: 'Garet'; position: relative;
        left: 150px;
    bottom: -140px;"> {{book.entreprise_nom}}</p>
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


      entrepriseUrl:null,
      book: {
            id:null,
        offer_details: [],
        entreprise: null,
        titre:'',
        text:'',
        file:null
      },
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
      const formData = new FormData();
      const template= "template2";
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
        this.$router.push('/bookview2/'+bookId);
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
  color:#DDD8D3;
  background-color: #474747;
  font-family:'Garet';
  cursor:pointer;
}
  textarea{
    background-color: #DDD8D3;
  }
  .cover-4{
   background-color:  #FDFDFD;
   height:700px;
  }
  .content{
    position: relative;
    bottom: -70px;
  }
  .skills{
    color:#474747;
    margin-right: 10px;
    background-color: #DDD8D3;
    border-radius: 5px;
    padding: 5px;
    font-family:'Garet';
  }
  th{
    height:40px !important;
  }
  .cus-td{
    height:40px !important;
  }
  tr{
    height:40px !important;
  }
  .cover-3{
    background-color: #474747;
    height:700px;
  }
  .cover-2{
    background-color: #DDD8D3;
      background-size: cover; /* Ajuste l'image pour couvrir tout l'élément */
  background-repeat: no-repeat; /* Empêche la répétition de l'image */
  background-position: center center;
  height:800px;
  }
.cover-1{
  width:100%;
  background-image: url('/public/Book/book2/cover1.png');
  background-size: cover; /* Ajuste l'image pour couvrir tout l'élément */
  background-repeat: no-repeat; /* Empêche la répétition de l'image */
  background-position: center center;
  height:800px;
}
  .card{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    height: 200px;
    width: 480px;
    padding: 20px;
    padding-right: 20px;
    gap: 10px;
    background-color:   #474747;
    border: solid 1px  #474747;
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
    position: relative;
    bottom: -200px;

  }

  .icon img{
height:40px;
margin-top:0px !important;
margin-bottom:20px;
width: 40px !important;
border-radius: 0px  !important;
  }

  .title {
    color: #DDD8D3;
    font-family:'Garet';
    width: 150px !important;
    text-align: left;
  }

  .text {
color: #fff;
font-family:'Garet';
width: 250px !important;
text-align: left;
  }
  .offer-heading{
    color:#fff !important;
    padding-top: 50px;
  }
.icons img{
  margin-top:50px;
  margin-left:20px;
  position: relative;
  bottom: -200px;
}
ul {
        list-style-type: none; /* Remove bullets */
        text-align: left;
        color: #ecebeb;
        font-family:'Garet';
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
    color:#474747;
    margin-left:-140px;
    text-align: left;
    margin-left:35px;
    margin-top: -150px;
    font-size:50px;
    font-weight:normal;
    font-family: 'Garet';
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
    font-family:'Garet';
}
  .description{
 padding:200px;


    text-align: center
  }
  .description h1{
    color:#9340FF;
    font-size: 46.5px;
    text-align: center;
    margin-bottom:40px;
  }
  .description p{
    text-align: justify;
    color: #ecebeb;
    text-align: center;
    font-family:'Garet';
    font-size:22px;
  }
.drop-area {
  border: 2px dashed #000000;
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
  font-family:'Garet';
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
  background: none;
font-size: 1.5rem;
color:#fff;
border: #fff 1px solid;
padding: 15px;
  margin-left:-200px;
  font-family:'Garet';
  font-size: 18px;
  width:200px;
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
    font-family:'Garet';
}
  .container-containers{
  display: flex;
  position: relative ;
  z-index:  2;
  margin-bottom: 100px;
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
  height:600px;
  flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;
  }
h1{
  color: #ecebeb;
font-family:'Garet';
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

}
 body {
    font-family: 'Garet', sans-serif;
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
