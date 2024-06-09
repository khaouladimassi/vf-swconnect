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
    <title>Portfolio</title>
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
  <body style="overflow-x: hidden;">
      <navbarEntreprise />

  <main class="main-2" style="margin-top: 0px">
    <div class="nav-2" style="border-right: 1px solid #dee2e6">
      <nav class="nav-main-menu-2">
          <ul class="main-menu-2">
            <li>
              <a class="dashboard2" :href="'/EntOverview/' + entreprise.id"
                ><img
                  src="../assets/imgs/template/icons/stack.svg"
                  alt="jobBox"
                /><span class="name">Overview</span></a
              >
            </li>
            <li>
              <router-link to="/BookGeneration" class="dashboard2 active" 
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
              <router-link to="/MesOffres" class=" dashboard2" 
                ><img
                  src="../assets/imgs/template/icons/briefcase2.svg"
                  alt="jobBox"
                /><span class="name">Mes Offres</span></router-link
              >
            </li>
            <li>
              <a class="dashboard2" :href="'/EtudDrive/' + entreprise.id">
                <img
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
            <h3 class="mb-35">Générer Pfe Book</h3>
          
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
       <h6>Modèle 1</h6>
        <div :class="['model-container', { selected: isSelected1 }]" @click="toggleSelection(1)" style="display: flex !important; height: 160px !important; position: relative;">
          <img src="/Book/book1/img/1.png" alt="model 1">
          <img src="/Book/book1/img/2.png" alt="model 1">
          <img src="/Book/book1/img/3.png" alt="model 1">
          <img src="/Book/book1/img/4.png" alt="model 1">
          <div class="preview-container" style="  height: 140px !important; width:447px;">
    <img src="/Book/book1/img/5.png" alt="model 5" style="  height: 140px !important;width:447px;">
    <span class="preview-text" @click="viewTemplate()">Voir preview</span>
  </div>
        </div>
        <h6>Modèle 2</h6>
        <div :class="['model-container', { selected: isSelected2 }]" @click="toggleSelection(2)" style="display: flex !important; height: 160px !important; position: relative;">
          <img src="/Book/book2/19.png" alt="model 2">
          <img src="/Book/book2/20.png" alt="model 2">
          <img src="/Book/book2/21.png" alt="model 2">
          <img src="/Book/book2/23.png" alt="model 2">
          <div class="preview-container" style="  height: 140px !important; width:447px;">
    <img src="/Book/book2/24.png" alt="model 5" style="  height: 140px !important;width:447px;">
    <span class="preview-text" @click="viewTemplate2()">Voir preview</span>
  </div>
        </div>
        <h6>Modèle 3</h6>
        <div :class="['model-container', { selected: isSelected3 }]" @click="toggleSelection(3)" style="display: flex !important; height: 160px !important; position: relative;">
          <img src="/Book/book3/14 (2).png" alt="model 2">
          <img src="/Book/book3/14 (1).png" alt="model 2">
          <img src="/Book/book3/14 (3).png" alt="model 2">
          <img src="/Book/book3/14 (4).png" alt="model 2">
          <div class="preview-container" style="  height: 140px !important; width:447px;">
    <img src="/Book/book3/14 (5).png" alt="model 5" style="  height: 140px !important;width:447px;">
    <span class="preview-text" @click="viewTemplate3()">Voir preview</span>
  </div>
        </div>
        <div class="col-lg-12">
                    <div class="form-group mt-10">
                                  <button
                                    class="btn btn-default-2 btn-brand-2"
                                    v-if="this.isSelected1===true  " 
                                    @click="generateBook"
                                  >
                                    Générer Pfe Book
                                  </button>
                                  <button
                                    class="btn btn-default-2 btn-brand-2"
                                    v-if=" this.isSelected2===true  " 
                                    @click="generateBook2"
                                  >
                                    Générer Pfe Book
                                  </button>
                                  <button
                                    class="btn btn-default-2 btn-brand-2"
                                    v-if=" this.isSelected3===true " 
                                    @click="generateBook3"
                                  >
                                    Générer Pfe Book
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
      </div>
    </div>
  </main>
  </body>

</template>

<script>
import axios from 'axios';
import router from '@/router';
import { mapGetters } from 'vuex';
  import navbarEntreprise from '@/components/navbarEntreprise.vue';
export default {
  data() {
      return{
        isSelected1: false,
        isSelected2: false,
        isSelected3:false,
        book:{},
        entreprise:{
          id:null
        }
      }
  },
  components:{navbarEntreprise},
  computed: {
    ...mapGetters(['getSelectedOffers']),
    selectedOffers() {
      return this.getSelectedOffers;
    }
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
    this.entreprise.id=userId;
    this.fetchBook(userId);
},
methods: {
  async fetchBook(entrepriseId) {
      try {
        console.log("entreprise",entrepriseId);
        const response = await axios.get(`http://127.0.0.1:8000/api/get-pfe-book-by-entreprise/${entrepriseId}/`);
        this.book = response.data;
    
      } catch (error) {
        console.error('Error fetching book:', error);
        alert('An error occurred while fetching the book details.');
      }
    },
  toggleSelection(model) {
    if (model === 1) {
      this.isSelected1 = !this.isSelected1;
      this.isSelected2 = false; // Déselectionner l'autre modèle
      this.isSelected3 = false; 
    } else if (model === 2) {
      this.isSelected2 = !this.isSelected2;
      this.isSelected1 = false; // Déselectionner l'autre modèle
      this.isSelected3 = false; 
    }
    else if (model === 3) {
      this.isSelected3 = !this.isSelected3;
      this.isSelected2 = false; // Déselectionner l'autre modèle
      this.isSelected1 = false; 
    }
  },
  async generateBook() {
    console.log("alert",this.book[0])
    if(this.book[0]){
      alert("vous avez déja généré un pfe book! Supprimer le si vous voulez générer un nouveau.")
    }
     else{
      const userId = localStorage.getItem('user_id');
      console.log(this.selectedOffers);
      const payload = {
        offer_ids: this.selectedOffers,
        entreprise: userId, // Assuming user ID is the entreprise ID
        text: 'Default text',  // Add text if needed
        titre: 'Default title', // Add title if needed
        template:'template1'
      };

      try {
        const response = await axios.post('http://127.0.0.1:8000/api/create-book/', payload);
        console.log(response.data);
        alert('Book created successfully!');
        const bookId = response.data.id;
    const bookUrl = this.$router.resolve({ name: 'PfeBook1', params: { id: bookId } }).href;

    // Open the new window with the book's URL
    window.open(bookUrl, '_blank');

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
        alert('An error occurred while creating the book.');
      }
     }
    },
    async generateBook2() {
      if(this.book[0]){
      alert("vous avez déja généré un pfe book! Supprimer le si vous voulez générer un nouveau.")
    }
    else{
      const userId = localStorage.getItem('user_id');
      console.log(this.selectedOffers);
      const payload = {
        offer_ids: this.selectedOffers,
        entreprise: userId, // Assuming user ID is the entreprise ID
        text: 'Default text',  // Add text if needed
        titre: 'Default title', // Add title if needed
        template:'template2'
      };

      try {
        const response = await axios.post('http://127.0.0.1:8000/api/create-book/', payload);
        console.log(response.data);
        alert('Book created successfully!');
        const bookId = response.data.id;
    const bookUrl = this.$router.resolve({ name: 'PfeBook2', params: { id: bookId } }).href;

    // Open the new window with the book's URL
    window.open(bookUrl, '_blank');

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
        alert('An error occurred while creating the book.');
      }
    }
     
    },
    async generateBook3() {
      if(this.book[0]){
      alert("vous avez déja généré un pfe book! Supprimer le si vous voulez générer un nouveau.")
    }
    else{
      const userId = localStorage.getItem('user_id');
      console.log(this.selectedOffers);
      const payload = {
        offer_ids: this.selectedOffers,
        entreprise: userId, // Assuming user ID is the entreprise ID
        text: 'Default text',  // Add text if needed
        titre: 'Default title', // Add title if needed
        template:'template3'
      };
console.log(payload);
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/create-book/', payload);
        console.log(response.data);
        alert('Book created successfully!');
        const bookId = response.data.id;
    const bookUrl = this.$router.resolve({ name: 'PfeBook3', params: { id: bookId } }).href;

    // Open the new window with the book's URL
    window.open(bookUrl, '_blank');

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
        alert('An error occurred while creating the book.');
      }
    }
      
    },
  viewTemplate() {
    const selectedOffers = this.selectedOffers.map(offer => encodeURIComponent(offer));
    const routeUrl = router.resolve({ 
      name: 'BookTemplate1', 
      query: { selectedOffers: selectedOffers.join(',') } 
    }).href;
  
    // Open a new window with the resolved URL
    window.open(routeUrl, '_blank');
   // this.selected=true;
  },
  viewTemplate3() {
    const selectedOffers = this.selectedOffers.map(offer => encodeURIComponent(offer));
    const routeUrl = router.resolve({ 
      name: 'BookTemplate3', 
      query: { selectedOffers: selectedOffers.join(',') } 
    }).href;
  
    // Open a new window with the resolved URL
    window.open(routeUrl, '_blank');
   // this.selected=true;
  },
  viewTemplate2() {
    const selectedOffers = this.selectedOffers.map(offer => encodeURIComponent(offer));
    const routeUrl = router.resolve({ 
      name: 'BookTemplate2', 
      query: { selectedOffers: selectedOffers.join(',') } 
    }).href;
  
    // Open a new window with the resolved URL
    window.open(routeUrl, '_blank');
   // this.selected=true;
  }

  }

};
</script>
<style scoped>
.model-container.selected {
  border: 3px solid #447AB8; /* Blue border when selected */
}
.preview-container {
  position: relative;
  height: 100px !important;
}
.preview-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white; /* or any color that contrasts with the image */
  background-color: rgba(0, 0, 0, 0.5); /* semi-transparent background */
  border-radius: 5px;
  cursor:pointer;
}
.model-container{
    padding-bottom: 10px;
    padding-top: 10px;
    margin-bottom: 20px;
}
.model-container img{
  width:20%;
}
  .form-section-2{
    width:100%;
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
