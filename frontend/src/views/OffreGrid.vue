<template>
  <router>

<meta http-equiv="content-type" content="text/html;charset=UTF-8" />
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <meta name="msapplication-TileColor" content="#0E0E0E">
  <meta name="template-color" content="#0E0E0E">
  <link rel="manifest" href="manifest.html" crossorigin>
  <meta name="msapplication-config" content="browserconfig.html">
  <meta name="description" content="Index page">
  <meta name="keywords" content="index, page">
  <meta name="author" content="">
  <link rel="shortcut icon" type="image/x-icon" href="assets/imgs/template/favicon.svg">
  <link href="./template/assets/css/stylecd4ee.css?version=4.1" rel="stylesheet">
  <title>SW Connect </title>
</head>
<body style="overflow-x: hidden;">
 <navbarEtudiant/>
  <main class="main">
    <section class="section-box-2">
      <div class="container">
        <div class="banner-hero banner-single banner-single-bg">
          <div class="block-banner text-center">
            <h3 class="wow animate__animated animate__fadeInUp"><span class="color-brand-2">Stages</span>  actuellement disponibles</h3>
            <div class="font-sm color-text-paragraph-2 mt-10 wow animate__animated animate__fadeInUp" data-wow-delay=".1s">Trouvez facilement une opportunité qui correspond à vos intérêts et à votre localisation <br class="d-none d-xl-block"></div>
            <div class="form-find text-start mt-40 wow animate__animated animate__fadeInUp" data-wow-delay=".2s">
              <form>
                <input id="input-keysearch" class="form-input input-keysearch mr-10" type="text" placeholder="mot clé... ">
                <button class="btn btn-default btn-find font-sm" @click.prevent="onSearchClick">Rechercher</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="section-box mt-30" >
      <div class="container">
        <div class="row flex-row-reverse" >
          <div class="col-lg-9 col-md-12 col-sm-12 col-12 float-right grid-row-offer" >
            <div class="content-page"  >
              <div class="box-filters-job">
                <div class="row cus-row">
                  <!--<div class="col-xl-6 col-lg-5"><span class="text-small text-showing">Showing <strong>41-60 </strong>of <strong>944 </strong>jobs</span></div>-->
                  <div class="col-xl-6 col-lg-7 text-lg-end mt-sm-15">
                  
                  </div>
                </div>
              </div>
              <div class="row" >
                <template v-if="searchClicked === false && FilterClick === false">
                  <div  v-for="offer in offers" :key="offer.id" class="col-xl-4 col-lg-4 col-md-6 col-sm-12 col-12">
                  <div class="card-grid-2 hover-up"  >
                    <div class="card-grid-2-image-left"><span class="flash"></span>
                      <div class="image-box"><img :src="offer.profile_logo" alt="jobBox" style="width:50px"></div>
                      <pre>{{offer.entreprise.profile_logo}}</pre>
                      

                      <div class="right-info">
  <a class='name-job' :href="'/EntrepriseDetails/'+offer.entreprise_id" >
      {{ offer.nom }}
  </a>
  <span class="location-small">{{ offer.location }}</span>
</div>
                    </div>
                    <div class="card-block-info">
                      <h6><a href="#" @click="redirectToOfferDetails(offer.id)">{{ offer.title }}</a></h6>
                      <div class="mt-5"><span class="card-briefcase">{{offer.offer_type}}</span><span class="card-time">{{offer.created_at.slice(0, 10)}}</span></div>
                      <div class="mt-5"><div class='btn btn-grey-small cus-mr mr-5' >{{offer.status}}</div></div>
                      <p class="font-sm color-text-paragraph mt-15">{{offer.description.slice(0, 100)}}</p>
                                              <div class="mt-30">
                              <!-- Loop through each skill in the offer.skills array -->
                              <a v-for="(skill, index) in offer.skills" :key="index" class='btn btn-grey-small cus-mr mr-5' href='jobs-grid.html'>
                                  {{ skill }}
                              </a>
                          </div>
                      <div class="card-2-bottom mt-30">
                        <div class="row">
                          <div class="col-lg-7 col-7"><span class="card-text-price">{{offer.maximal_payment}}</span><span class="text-muted">DT</span></div>
                          <div class="col-lg-5 col-5 text-end">
                            <div class="btn btn-apply-now"  @click="addDemande(offer.id)">Postuler</div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </template>
              <template v-if="searchClicked && filteredOffers.length">

                <!--offres recherchées-->
                <div  v-for="offer in filteredOffers" :key="offer.id" class="col-xl-4 col-lg-4 col-md-6 col-sm-12 col-12" id="offers-container">
                  <div class="card-grid-2 hover-up"  >
                    <div class="card-grid-2-image-left"><span class="flash"></span>
                      <div class="image-box"><img :src="offer.profile_logo" alt="jobBox" style="width:50px"></div>
                      <pre>{{offer.entreprise.profile_logo}}</pre>
                      

                      <div class="right-info">
  <a class='name-job' :href="'/EntrepriseDetails/'+offer.entreprise_id" >
      {{ offer.nom }}
  </a>
  <span class="location-small">{{ offer.location }}</span>
</div>
                    </div>
                    <div class="card-block-info">
                      <h6><a href="#" @click="redirectToOfferDetails(offer.id)">{{ offer.title }}</a></h6>
                      <div class="mt-5"><span class="card-briefcase">{{offer.offer_type}}</span><span class="card-time">{{offer.created_at.slice(0, 10)}}</span></div>
                      <div class="mt-5"><div class='btn btn-grey-small cus-mr mr-5' >{{offer.status}}</div></div>
                      <p class="font-sm color-text-paragraph mt-15">{{offer.description.slice(0, 100)}}</p>
                                              <div class="mt-30">
                              <!-- Loop through each skill in the offer.skills array -->
                              <a v-for="(skill, index) in offer.skills" :key="index" class='btn btn-grey-small cus-mr mr-5' href='jobs-grid.html'>
                                  {{ skill }}
                              </a>
                          </div>
                      <div class="card-2-bottom mt-30">
                        <div class="row">
                          <div class="col-lg-7 col-7"><span class="card-text-price">{{offer.maximal_payment}}</span><span class="text-muted">DT</span></div>
                          <div class="col-lg-5 col-5 text-end">
                            <div class="btn btn-apply-now" >Postuler</div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </template>
              <template v-if="FilterClick && filteredOffers2.length">

                <!--offres recherchées-->
                <div  v-for="offer in filteredOffers2" :key="offer.id" class="col-xl-4 col-lg-4 col-md-6 col-sm-12 col-12" id="offers-container">
                  <div class="card-grid-2 hover-up"  >
                    <div class="card-grid-2-image-left"><span class="flash"></span>
                      <div class="image-box"><img :src="offer.profile_logo" alt="jobBox" style="width:50px"></div>
                      <pre>{{offer.entreprise.profile_logo}}</pre>
                      

                      <div class="right-info">
  <a class='name-job' :href="'/EntrepriseDetails/'+offer.entreprise_id" >
      {{ offer.nom }}
  </a>
  <span class="location-small">{{ offer.location }}</span>
</div>
                    </div>
                    <div class="card-block-info">
                      <h6><a href="#" @click="redirectToOfferDetails(offer.id)">{{ offer.title }}</a></h6>
                      <div class="mt-5"><span class="card-briefcase">{{offer.offer_type}}</span><span class="card-time">{{offer.created_at.slice(0, 10)}}</span></div>
                      <div class="mt-5"><div class='btn btn-grey-small cus-mr mr-5' >{{offer.status}}</div></div>
                      <p class="font-sm color-text-paragraph mt-15">{{offer.description.slice(0, 100)}}</p>
                                              <div class="mt-30">
                              <!-- Loop through each skill in the offer.skills array -->
                              <a v-for="(skill, index) in offer.skills" :key="index" class='btn btn-grey-small cus-mr mr-5' href='jobs-grid.html'>
                                  {{ skill }}
                              </a>
                          </div>
                      <div class="card-2-bottom mt-30">
                        <div class="row">
                          <div class="col-lg-7 col-7"><span class="card-text-price">{{offer.maximal_payment}}</span><span class="text-muted">DT</span></div>
                          <div class="col-lg-5 col-5 text-end">
                            <div class="btn btn-apply-now" >Postuler</div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </template>
              <template v-if="searchClicked===false">
                <div v-for="book in books" :key="book.id" class="col-xl-4 col-lg-4 col-md-6 col-sm-12 col-12" >
                  <div class="card-grid-2 hover-up">
                    <div class="card-grid-2-image-left"><span class="flash"></span>
                      <div class="image-box"><img :src="book.profile_logo" alt="jobBox" style="width:50px"></div>
                      <div class="right-info"><a class='name-job'  :href="'/EntrepriseDetails/'+book.entreprise_id">{{ book.entreprise_nom}}</a><span class="location-small">{{book.entreprise_location}}</span></div>
                    </div>
                    <div class="card-block-info">
                      <h6>{{book.titre}}</h6>
                      <div class="mt-5"><span class="card-time">{{book.created_at.slice(0, 10)}}</span></div>
                      <div class="mt-5"><div class='btn btn-grey-small cus-mr mr-5' >PFE BOOK</div></div>
                      <div class="card-2-bottom mt-30">
                        <div class="row">
                          <div class="col-lg-7 col-7"></div>
                          <div class="col-lg-5 col-5 text-end">
                            <div  class="btn btn-apply-now" style="width: 100px;" 
                            @click="openBOOK(book.id)">Voir Pfe Book</div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </template>
              <template v-if="searchClicked && filteredpfebooks.length">
                <div v-for="book in filteredpfebooks" :key="book.id" class="col-xl-4 col-lg-4 col-md-6 col-sm-12 col-12" id="pfebooks-container" >
                  <div class="card-grid-2 hover-up">
                    <div class="card-grid-2-image-left"><span class="flash"></span>
                      <div class="image-box"><img :src="book.profile_logo" alt="jobBox" style="width:50px"></div>
                      <div class="right-info"><a class='name-job'  :href="'/EntrepriseDetails/'+book.entreprise_id">{{ book.entreprise_nom}}</a><span class="location-small">{{book.entreprise_location}}</span></div>
                    </div>
                    <div class="card-block-info">
                      <h6>{{book.titre}}</h6>
                      <div class="mt-5"><span class="card-time">{{book.created_at.slice(0, 10)}}</span></div>
                      <div class="mt-5"><div class='btn btn-grey-small cus-mr mr-5' >PFE BOOK</div></div>
                      <div class="card-2-bottom mt-30">
                        <div class="row">
                          <div class="col-lg-7 col-7"></div>
                          <div class="col-lg-5 col-5 text-end">
                            <div  class="btn btn-apply-now" style="width: 100px;" 
                            @click="openBOOK(book.id)">Voir Pfe Book</div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </template>
                

                

              </div>
            </div>
            
           
          </div>
          <div class="col-lg-3 col-md-12 col-sm-12 col-12" style="margin-top:-30px">
            <div class="sidebar-shadow none-shadow mb-30">
              <div class="sidebar-filters">
                <div class="filter-block head-border mb-30">
                  <h5>Filtrage Avancé</h5>
                </div>
        
                <div class="filter-block mb-20">
                  <h5 class="medium-heading mb-15">Domaines</h5>
                  <div class="form-group">
                      <ul class="list-checkbox">
                          <li>
                              <label class="cb-container">
                                  <input type="radio" name="domain" value="informatique" @change="toggleDomain('Informatique')" checked>
                                  <span class="text-small">Informatique</span>
                                  <span class="checkmark"></span>
                              </label>
                          </li>
                          <li>
                              <label class="cb-container">
                                  <input type="radio" name="domain" value="finance" @change="toggleDomain('Finance')">
                                  <span class="text-small">Finance</span>
                                  <span class="checkmark"></span>
                              </label>
                          </li>
                          <li>
                              <label class="cb-container">
                                  <input type="radio" name="domain" value="marketing" @change="toggleDomain('Marketing et publicité')">
                                  <span class="text-small">Marketing et publicité</span>
                                  <span class="checkmark"></span>
                              </label>
                          </li>
                          <li>
                              <label class="cb-container">
                                  <input type="radio" name="domain" value="E-commerce" @change="toggleDomain('E-commerce')">
                                  <span class="text-small">E-commerce</span>
                                  <span class="checkmark"></span>
                              </label>
                          </li>
                          <li>
                              <label class="cb-container">
                                  <input type="radio" name="domain" value="transport" @change="toggleDomain('Transport et logistique')">
                                  <span class="text-small">Transport et logistique</span>
                                  <span class="checkmark"></span>
                              </label>
                          </li>
                      </ul>
                  </div>
              </div>
              
                <div class="list-checkbox pb-20" id="scrollable">
                  <h5 class="medium-heading mb-15" style="position:relative;top:-25px;">Payant ou non</h5>
                  <div class="row position-relative mt-10 mb-20">
                    <div class="col-sm-12 box-slider-range">
                      <div id="slider-range"></div>
                    </div>
                    <div class="box-input-money">
                      <input class="input-disabled form-control min-value-money" type="text" name="min-value-money" disabled="disabled" value="">
                      <input class="form-control min-value" type="hidden" name="min-value" value="">
                    </div>
                  </div>
                  <div class="box-number-money">
                    <div class="row mt-30">
                      <div class="col-sm-6 col-6"><span class="font-sm color-brand-1">0dt</span></div>
                      <div class="col-sm-6 col-6 text-end"><span class="font-sm color-brand-1">500dt</span></div>
                    </div>
                  </div>
                </div>
        
                <div class="filter-block mb-30">
                  <div class="form-group">
                    <ul class="list-checkbox">
                      <li>
                        <label class="cb-container">
                          <input type="radio" name="stage" value="Bureau" checked="checked" @change="updateTypeStage('Bureau')">
                          <span class="text-small">Bureau</span>
                          <span class="checkmark"></span>
                        </label>
                      </li>
                      <li>
                        <label class="cb-container">
                          <input type="radio" name="stage" value="distance" @change="updateTypeStage('distance')">
                          <span class="text-small">Stage à distance</span>
                          <span class="checkmark"></span>
                        </label>
                      </li>
                    </ul>
                  </div>
                </div>
        
                <div class="filter-block mb-30">
                  <h5 class="medium-heading mb-10">Binome</h5>
                  <div class="form-group">
                    <ul class="list-checkbox">
                      <li>
                        <label class="cb-container">
                          <input type="radio" name="binome" value="oui" @change="updateBinome('oui')">
                          <span class="text-small">Oui</span>
                          <span class="checkmark"></span>
                        </label>
                      </li>
                      <li>
                        <label class="cb-container">
                          <input type="radio" name="binome" value="non" checked="checked" @change="updateBinome('non')">
                          <span class="text-small">Non</span>
                          <span class="checkmark"></span>
                        </label>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <button class="btn btn-default btn-find font-sm" style="position: relative; right: 1070px; width: 90px; top: -50px;" @click.prevent="onFilterClick"><span style="font-weight: 900;font-size: 30;">Filtrer</span></button>

        </div>
      </div>
    </section>
  </main>
  <footer class="footer-cnx">
        <p>@ 2024 SW Connect - Tous droits réservés</p>
      </footer>

 <!-- <footer class="footer mt-50">
    <div class="container">
      <div class="row">
        <div class="footer-col-1 col-md-3 col-sm-12"><a href='index.html'><img alt="jobBox" src="assets/imgs/template/jobhub-logo.svg"></a>
          <div class="mt-20 mb-20 font-xs color-text-paragraph-2">JobBox is the heart of the design community and the best resource to discover and connect with designers and jobs worldwide.</div>
          <div class="footer-social"><a class="icon-socials icon-facebook" href="#"></a><a class="icon-socials icon-twitter" href="#"></a><a class="icon-socials icon-linkedin" href="#"></a></div>
        </div>
        <div class="footer-col-2 col-md-2 col-xs-6">
          <h6 class="mb-20">Resources</h6>
          <ul class="menu-footer">
            <li><a href="#">About us</a></li>
            <li><a href="#">Our Team</a></li>
            <li><a href="#">Products</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </div>
        <div class="footer-col-3 col-md-2 col-xs-6">
          <h6 class="mb-20">Community</h6>
          <ul class="menu-footer">
            <li><a href="#">Feature</a></li>
            <li><a href="#">Pricing</a></li>
            <li><a href="#">Credit</a></li>
            <li><a href="#">FAQ</a></li>
          </ul>
        </div>
        <div class="footer-col-4 col-md-2 col-xs-6">
          <h6 class="mb-20">Quick links</h6>
          <ul class="menu-footer">
            <li><a href="#">iOS</a></li>
            <li><a href="#">Android</a></li>
            <li><a href="#">Microsoft</a></li>
            <li><a href="#">Desktop</a></li>
          </ul>
        </div>
        <div class="footer-col-5 col-md-2 col-xs-6">
          <h6 class="mb-20">More</h6>
          <ul class="menu-footer">
            <li><a href="#">Privacy</a></li>
            <li><a href="#">Help</a></li>
            <li><a href="#">Terms</a></li>
            <li><a href="#">FAQ</a></li>
          </ul>
        </div>
        <div class="footer-col-6 col-md-3 col-sm-12">
          <h6 class="mb-20">Download App</h6>
          <p class="color-text-paragraph-2 font-xs">Download our Apps and get extra 15% Discount on your first Order&mldr;!</p>
          <div class="mt-15"><a class="mr-5" href="#"><img src="assets/imgs/template/icons/app-store.png" alt="joxBox"></a><a href="#"><img src="assets/imgs/template/icons/android.png" alt="joxBox"></a></div>
        </div>
      </div>
      <div class="footer-bottom mt-50">
        <div class="row">
          <div class="col-md-6"><span class="font-xs color-text-paragraph">Copyright &copy; 2022. JobBox all right reserved</span></div>
          <div class="col-md-6 text-md-end text-start">
            <div class="footer-social"><a class="font-xs color-text-paragraph" href="#">Privacy Policy</a><a class="font-xs color-text-paragraph mr-30 ml-30" href="#">Terms &amp; Conditions</a><a class="font-xs color-text-paragraph" href="#">Security</a></div>
          </div>
        </div>
      </div>
    </div>
  </footer>-->

</body>


  </router>
</template>
<script>
import axios from "axios";

import navbarEtudiant from '@/components/navbarEtudiant.vue';
export default {
components:{navbarEtudiant},
name: "OffreGrid",
data() {
  return {
    baseUrl: "http://127.0.0.1:8000/",
    offers: [],
    etudiant: null,
    showDropdown: false,
    books:[],
    entreprise: [],  
    filteredOffers: [],
    filteredOffers2: [],
    searchClicked: false,
    FilterClick:false,
    filteredpfebooks:[],
    selectedDomains: [],
    selectedTypeStage: [],
    selectedBinome:[],
    minPrice: 0,
    maxPrice: 500,
   
}
  },
 mounted() {
  // Call a method to fetch all offers from the backend API
this.fetchAllOffers();
this.fetchEtudiantDetails();
this.offers.forEach(offer => {
    console.log('Profile Logo Path:', offer.entreprise.profile_logo);
  });
this.fetchAllBooks();
console.log(this.searchClicked);


},
  methods:{
    fetchAllOffers() {
  axios.get('http://127.0.0.1:8000/api/offers/')
      .then(response => {
          // Set offers data
          this.offers = response.data;
      })
      .catch(error => {
          // Log error to console
          console.error('Error fetching offers:', error);
          // Display alert to the user
          alert('An error occurred while fetching offers. Please try again later.');
      });
},
    fetchAllBooks() {

    axios.get('http://127.0.0.1:8000/api/pfebooks/')
      .then(response => {
        // Assign the fetched offers to the offers array
        this.books = response.data;
        console.log(this.books);
      })
      .catch(error => {
        console.error('Error fetching books:', error);
      });
    },
    openBOOK(bookId) {
const book = this.books.find(book => book.id === bookId);

if (book) {
  const pfeBookId = book.id; // Use the pfe_book data
  console.log(pfeBookId);
  const baseUrl = 'http://127.0.0.1:8000'; // Replace with your API base URL
  const fileUrl = baseUrl + book.file; // Assuming pfe_book is an array

  // Open a new window or tab to display the file content
  window.open(fileUrl, '_blank');
} else {
  console.error("PFE book data is not available");
}
}
,
    fetchEtudiantDetails() {
    // Fetch etudiant details from backend API
    const etudiantId = localStorage.getItem('user_id'); // Replace with the actual etudiant ID
    axios.get(`http://127.0.0.1:8000/api/etudiants/get/${etudiantId}/`)
      .then(response => {
        this.etudiant = response.data;
        
      if (this.etudiant.profile_photo) {
        this.etudiantUrl = this.baseUrl + this.etudiant.profile_photo;
        console.log(this.etudiantUrl)
      }
        
      })
      .catch(error => {
        console.error('Error fetching etudiant details:', error);
      });
  },
      toggleDropdown() {
    
    this.showDropdown = !this.showDropdown;
  },
  logout() {
        localStorage.removeItem('user_id');
        this.$router.push('/ConnexionView');
        console.log('Logout successful');
  },
  addDemande(offerId) {
const userId = localStorage.getItem("user_id");
axios
  .post(`http://127.0.0.1:8000/api/demande/${userId}/add/${offerId}/`)
  .then((response) => {
    // Handle successful response if needed
    console.log("Demande added :", response.data);
    alert("Demande sent successfully");
    this.ajouterAction();

    const etudiant = this.etudiant; 
    const offre = this.offers.find(offer => offer.id === offerId);

   
      const message = `L'étudiant ${etudiant.last_name} ${etudiant.first_name} postule dans l'offre ${offre.title}`; 
      this.ajouterNotification(offerId, message);
  })
  .catch((error) => {
    console.error("Error adding demande:", error);
    alert("You already sent demande");
    // Handle error response if needed
  });
},
ajouterNotification(offer_id, message) {
  axios.post(`http://127.0.0.1:8000/creer-notif-entre/${offer_id}/`, {
    message: message
  })
  .then(response => {
    console.log("Notification ajoutée avec succès:", response.data);
  })
  .catch(error => {
    if (error.response) {
      console.error("Erreur lors de l'ajout de la notification:", error.response.data);
    } else {
      console.error("Erreur lors de l'ajout de la notification:", error.message);
    }
  });
},
  redirectToOfferDetails(offerId) {
      // Navigate to the offer details view using the offer ID
      this.$router.push({ name: 'OffreDetails', params: { id: offerId } });
      console.log(offerId,'grids');
  },
  rechercherOffre(keyword) {
  if (keyword.trim() !== '') {
    // Requête GET à l'API pour récupérer les offres
    axios.get('http://localhost:8000/api/offersbymc/', {
      params: {
        q: keyword
      }
    })
    .then(response => {
      const offers = response.data;
      // Mettre à jour la liste filteredOffers avec les résultats
      this.updateFilteredOffers(offers);
    })
    .catch(error => {
      console.error('Une erreur s\'est produite lors de la récupération des offres!', error);
    });
  }
},

// Méthode pour mettre à jour la liste filteredOffers avec les offres filtrées
updateFilteredOffers(offers) {
  this.filteredOffers = offers;
},

// Méthode pour rechercher des PFE books en fonction du mot-clé saisi
rechercherpfebook(keyword) {
  if (keyword.trim() !== '') {
    // Requête GET à l'API pour récupérer les PFE books
    axios.get('http://localhost:8000/api/pfebooksbymc/', {
      params: {
        q: keyword
      }
    })
    .then(response => {
      const pfebooks = response.data;
      // Mettre à jour la liste filteredpfebooks avec les résultats
      this.updateFilteredpfebooks(pfebooks);
    })
    .catch(error => {
      console.error('Une erreur s\'est produite lors de la récupération des PFE books!', error);
    });
  }
},

// Méthode pour mettre à jour la liste filteredpfebooks avec les PFE books filtrés
updateFilteredpfebooks(pfebooks) {
  this.filteredpfebooks = pfebooks;
},

// Écouteur d'événement pour le clic sur le bouton de recherche
onSearchClick() {
  const keyword = document.getElementById('input-keysearch').value;
  this.rechercherOffre(keyword);
  this.rechercherpfebook(keyword);
  this.searchClicked = true;
},
onFilterClick() {
  const domain = document.querySelector('input[name="domain"]:checked').value;
  const stageType = document.querySelector('input[name="stage"]:checked').value;
  const binome = document.querySelector('input[name="binome"]:checked').value;
  const minPrice = this.minPrice; // Si vous avez besoin de minPrice
  this.FilterClick =true;

  this.filterOffers(domain, stageType, binome, minPrice);
},
filterOffers(domain, stageType, binome, minPrice) {
  const url = `http://localhost:8000/api/offers/filter/${domain}/${stageType}/${binome}/${minPrice}/`;
  axios.get(url)
    .then(response => {
      const filteredOffers2 = response.data;
      console.log('Offres filtrées reçues :', filteredOffers2);
      this.updateFilteredOffers2(filteredOffers2);
    })
    .catch(error => {
      console.error('Une erreur s\'est produite lors du filtrage des offres!', error);
    });
},
 // Méthode pour mettre à jour la liste filteredOffers avec les offres filtrées
 updateFilteredOffers2(offers) {
  this.filteredOffers2 = offers;
},
toggleDomain(domain) {
console.log('Domaine sélectionné :', domain);
this.selectedDomains = domain;
},
updateBinome(binome) {
this.selectedBinome = binome;
},
updateTypeStage(stage) {
this.selectedTypeStage = stage;
},
ajouterAction() {
    const userId = localStorage.getItem("user_id");
if (!userId) {
  alert("Vous devez être connecté.");
  return;
}
axios.post(`http://127.0.0.1:8000/creer-action/${userId}/`, {
  action_message: 'Candidature pour une offre',
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



}
  
  }
  
</script>
<style scoped>
.cus-mr{
  margin:5px;
}
.btn-apply-now {
  background-color: #E0E6F7;
  color: #447AB8;
  padding: 12px 10px;
  min-width: 95px;
  border-radius: 4px;
  font-size: 12px;
  text-transform: capitalize;
}
.card-grid-2 .card-block-info .card-text-price {
  color: #447AB8;
}
.card-grid-2:hover .btn-apply-now {
  color: #ffffff;
  background-color: #447AB8;
}
.color-text-paragraph{
  color: #05264E;
}
.btn.btn-default {
color: #447AB8;
background-color: #ffffff;
line-height: 26px;
padding: 10px 25px;
}
.btn.btn-default:hover {
background-color: #ffffff;
transform: translateY(-2px);
transition: 0.2s;
}
.postbutt{
border : 1px solid #447AB8;
margin-left: 10px;
width:200px;
}
.icon-fb{
  height: 50px;
  width: 50px;
}
.nav-li-cus{
  font-size: 16px;
}
.header-left-cus{
  margin-right: 275px;
}
.header-right-cus{
  min-width: 335px;
}
.header-logo-cus{
  height:50px;
}
.header-cus{
  margin-bottom: 92px;
  padding-right: 40px;
  background-color: #fff;
  border-bottom: 1px solid #E0E6F7;
}
.grid-row-offer{
  padding-right: 32px;
}
.logo-site{
  height: 49px; 
  width: 199px;
}
.cus-row{
  margin-right:0px;
}
.header .main-menu li a:hover, .header .main-menu li a.active{
  color:#fff;
}
.dropdown-menu a:hover span {
color: #447ab8 !important;

}
.dropdown-menu a span {
margin-left: 42px;
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
.section-box-2 {
  display: inline-block;
  width: 100%;
  overflow: visible;
  margin-bottom: -60px;
}
.box-slider-range {
  padding-right: 75px;
  position: relative;
}
.noUi-base, .noUi-handle {
  transform: translate3d(0, 0, 0);
}
.noUi-base {
  width: 100%;
  height: 100%;
  position: relative;
  z-index: 1;
}
.noUi-background {
  background: #3C65F5;
}
.noUi-horizontal {
  height: 6px;
}
.noUi-target {
  border-radius: 12px;
}
.footer-cnx {
  position: relative;
  background-color: transparent;
  height: 20px;
  width: 150%;
  overflow-x: hidden;
}
</style>