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
      <title>Entreprise</title>
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
        href="/template/assets/imgs/template/favicon.svg"
      />
  
      <link
        href="/template/assets/css/plugins/animate.min.css"
        rel="stylesheet"
      />
      <link
        href="/template/assets/css/plugins/magnific-popup.css"
        rel="stylesheet"
      />
      <link
        href="/template/assets/css/plugins/perfect-scrollbar.css"
        rel="stylesheet"
      />
      <link
        href="/template/assets/css/plugins/select2.min.css"
        rel="stylesheet"
      />
      <link
        href="/template/assets/css/plugins/swiper-bundle.min.css"
        rel="stylesheet"
      />
  
      <link href="/template/assets/css/stylecd4ee.css" rel="stylesheet" />
  
      <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
      />
    </head>
    <body>
      <navbarEntreprise v-if="userType === 'entreprise' " />
 <navbarEtudiant v-if="userType==='etudiant'" />
 <navbarAdmin v-if="userType==='admin'" />
  
      <main class="main">
        <div class="banner-hero banner-image-single" style="margin-left:5px; "><img :src="this.baseUrl+this.entreprise.profile_cover" alt="jobbox" style="height:348px;"></div>
        <div class="box-company-profile" style="width:100px">
              <div class="image-compay" style="width:100px; margin-left:-596px;"><img :src="this.baseUrl+this.entreprise.profile_logo" alt="jobbox">
              </div>
  
                      
        </div>
        <section class="section-box-2">
          <div class="container">
            <div class="row mt-10">
              <div class="col-lg-8 col-md-12">
                <div class="inline-content">
                  <h3 style="display: inline">
                    {{ entreprise.nom}} 
                  </h3>
                </div>
                <p class="company-name" href="#">{{ entreprise.type_industrie }}</p>
              </div>
              <div v-if="userType==='etudiant' || userType==='admin' "   class="col-lg-4 col-md-12 text-lg-end">
                <div class="btn-group" role="group" aria-label="Button group">
                 <!-- <div  v-if="userType==='etudiant'" class="icon-container-2 hover-up" >
                    <i class="bi bi-bookmark custom-icon-3"  style="cursor: pointer"></i>
                  </div>-->
  
                  <router-link :to="'/chatView/'+ entreprise.username"
                    class="btn btn-apply btn-apply-big hover-up"
                    style="border-radius: 8px"
                  >
                    Contacter <i class="bi bi-chat-text custom-icon-4"></i>
                </router-link>
                </div>
              </div>
            </div>
            <div class="border-bottom pt-10 pb-10"></div>
          </div>
        </section>
        <section class="section-box">
          <div class="container">
            <div class="row">
              <div class="col-lg-8 col-md-12 col-sm-12 col-12">
                <div class="content-single">
                  <h5>Description</h5>
                  <p>{{ entreprise.description }}</p>
                  <h5 v-if="entreprise.vision">Vision</h5>
                  <p v-if="entreprise.vision">{{ entreprise.vision }}</p>
                </div>
                <div class="author-single">
                  <span>{{ entreprise.nom }}</span>
                </div>
                <div class="single-apply-jobs">
                  <div class="row align-items-center">
                    <div v-if="userType==='etudiant' || userType==='admin'" class="col-md-5" style="width: 380px">
                      <a class="btn btn-default mr-15"  :href="'/chatView/'+ entreprise.username">Contacter</a
                      ><a v-if="userType==='etudiant'" class="btn btn-border" href="#">Ajouter aux favoris</a>
                    </div>
                    <div
                      class="text-lg-end social-share"
                      style="width: 500px; margin-right: 0px; margin-left:360px;"
                    >
                      <h6
                        class="color-text-paragraph-2 d-inline-block d-baseline mr-10"
                      >
                        Suivre sur
                      </h6>
                      <a v-if="entreprise.fb_lien"  class="mr-5 d-inline-block d-middle" :href="entreprise.fb_lien" target="_blank"
                        ><img v-if="entreprise.fb_lien"
                          alt="jobBox"
                          src="/template/assets/imgs/template/icons/facebook-colored.svg" /></a
                      >
                      <a v-if="entreprise.link_lien"
                        class="mr-5 d-inline-block d-middle"
                        :href="entreprise.link_lien"
                        target="_blank"
                        ><img v-if="entreprise.link_lien"
                          alt="jobBox"
                          src="/template/assets/imgs/template/icons/linkedin-colored.svg" /></a
                      >
                      <a v-if="entreprise.in_lien" class="mr-5 d-inline-block d-middle"  :href="entreprise.in_lien"
                        target="_blank"
                        ><img  v-if="entreprise.in_lien"
                          alt="jobBox"
                          src="/template/assets/imgs/template/icons/instagram-colored.svg" /></a
                      >
                    </div>
                  </div>
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
                        <i class="bi bi-geo-alt custom-iconss"></i
                        >{{ entreprise.location }}
                      </li>
                      <li>
                        <i class="bi bi-telephone custom-iconss"></i
                        >{{ entreprise.telephone }}
                      </li>
                      <li>
                        <i class="bi bi-envelope custom-iconss"></i
                        >{{ entreprise.email }}
                      </li>
                      <li v-if="entreprise.site_url">
                        <i class="bi bi-globe custom-iconss"></i
                        >{{ entreprise.site_url }}
                      </li>
                    </ul>
                  </div>
                </div>
                <div class="job-overview">
                  <h5 class="border-bottom pb-15 mb-30">Informations</h5>
                  <div class="row">
                    <div class="col-md-6">
                      <div class="sidebar-icon-item">
                        <img
                          src="/template/assets/imgs/template/icons/journal-bookmark.svg"
                          alt="jobBox"
                        />
                      </div>
                      <div class="sidebar-text-info ml-10">
                        <span class="text-description industry-icon mb-10"
                          >Domaine</span
                        >
                        <strong class="small-heading">{{
                          entreprise.type_industrie
                        }}</strong>
                      </div>
                    </div>
                    <div class="col-md-6 mt-sm-15">
                      <div class="sidebar-icon-item">
                        <img
                        src="../assets/imgs/page/job-single/job-type.svg"
                          alt="jobBox"
                        />
                      </div>
                      <div class="sidebar-text-info ml-10">
                        <span class="text-description joblevel-icon mb-10"
                          >Organisation</span
                        >
                        <strong class="small-heading">{{ entreprise.type_organisation }}</strong>
                      </div>
                    </div>
                  </div>
                  <div class="row mt-25">
                    <div class="col-md-6">
                      <div class="sidebar-icon-item">
                        <img
                          src="../assets/imgs/page/job-single/people-fill.svg"
                          alt="jobBox"
                        />
                      </div>
                      <div class="sidebar-text-info ml-10">
                        <span class="text-description experience-icon mb-10"
                          >Nombre d'équipe</span
                        ><strong class="small-heading">{{
                          entreprise.nombre_equipe
                        }}</strong>
                      </div>
                    </div>
                    <div class="col-md-6 mt-sm-15">
                      <div class="sidebar-icon-item">
                        <img
                          src="/template/assets/imgs/page/job-single/calendar-check.svg"
                          alt="jobBox"
                        />
                      </div>
                      <div class="sidebar-text-info ml-10">
                        <span class="text-description salary-icon mb-10"
                          >Date d'établissement</span
                        ><strong class="small-heading">{{
                          entreprise.date_etablissement
                        }}</strong>
                      </div>
                    </div>
                  </div>
                
                </div>
                <div class="sidebar-border">
                <div class="sidebar-heading">
                    <h5 class=" ">Responsable de stages</h5>
                    <div class="avatar-sidebar">
                      <div class="sidebar-info"></div>
                    </div>
                  </div>
                  <div class="sidebar-list-job">
                    <ul>
                      <li>
                        <img src="/template/assets/imgs/template/icons/person-vcard.svg" class="custom-iconss">{{ entreprise.nom_rh }} {{ entreprise.prenom_rh }}
                      </li>
                      <li>
                        <i class="bi bi-telephone custom-iconss"></i
                        >{{ entreprise.telephone_rh }}
                      </li>
                      <li>
                        <i class="bi bi-envelope custom-iconss"></i
                        >{{ entreprise.email_rh }}
                      </li>
                    </ul>
                  </div>
                </div>

                <div v-if="this.entreprise && this.pfe_book && this.pfe_book.length > 0" class="sidebar-border">
                  <div class="sidebar-heading">
                    <div class="row">
                      <div class="col-md-6">
                        <div class="avatar-sidebar">
                          <figure>
                            <img
                              alt="jobBox"
                              src="\template\assets\imgs\page\job-single\file-earmark-person.svg"
                            />
                          </figure>
                          <div class="sidebar-info">
                            <span class="sidebar-company" style="width:80px">Pfe book</span
                            ><span>PDF</span><br>
                            <span style="color:#b2b2b2">{{pfe_book[0].titre}}</span>
                          </div>
                        </div>
                      </div>
                      <div class="col-md-6 mt-sm-15">
                        <div class="sidebar-text-info ml-10">
                          <span
                            class="btn btn-border comp-bar mb-10 mt-90 container-competences custom-file"
                            style="
                              padding-bottom: 26px;
                              border: none;
                              font-size: 14px;
                              font-weight: normal;
                            "
                            @click="openBOOK"
                          >
                            Voir Pfe Book</span
                          >
                 
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div v-if="this.book" class="sidebar-border">
                <div class="sidebar-heading">
                  <div class="row">
                    <div class="col-md-6">
                      <div class="avatar-sidebar">
                        <figure>
                          <img
                            alt="jobBox"
                            src="\template\assets\imgs\page\job-single\filetype-ai.svg"
                          />
                        </figure>
                        <div class="sidebar-info">
                          <span class="sidebar-company">Pfe book </span
                          ><span>AI</span>
                        </div>
                      </div>
                    </div>
                    <div class="col-md-6 mt-sm-15">
                      <div class="sidebar-text-info ml-10">
                        <span
                          class="btn btn-border comp-bar  container-competences custom-file"
                          style="
                            padding-bottom: 26px;
                            border: none;
                            font-size: 14px;
                            font-weight: normal;
                          "
                          @click="open(this.book[0].id)"
                        >
                          Voir Pfe Book</span
                        >
                        <span  v-if="this.userType==='entreprise'"
                          class="btn btn-border comp-bar mt-60 container-competences custom-file"
                          style="
                            padding-bottom: 26px;
                            border: none;
                            font-size: 14px;
                            font-weight: normal;
             
                            
                          "
                          @click="deleteBook(this.book[0].id)"
                        >
                         Supprimer</span
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              </div>
            </div>
            
          </div>
        </section>
     
      </main>
      <footer class="footer mt-50">
        <div class="container">
          <div class="row">
            <div class="footer-col-1 col-md-3 col-sm-12">
              <a href="index.html"
                ><img
                  class="img-footer"
                  alt="jobBox"
                  src="../assets/imgs/logo/logo-blanc.png"
              /></a>
              <ul class="menu-footer">
                <li><a href="#">Téléphone : +216 27 351 589</a></li>
                <li><a href="#">Email : SWConnect@gmail.com</a></li>
                <li><a href="#">Addresse : Bouhjar, Monastir</a></li>
              </ul>
              <div class="footer-social">
                <a class="icon-socials icon-facebook" href="#"></a
                ><a class="icon-socials icon-twitter" href="#"></a
                ><a class="icon-socials icon-linkedin" href="#"></a>
              </div>
            </div>
            <div class="footer-col-2 col-md-2 col-xs-6">
              <h6 class="mb-20 footer-h6">Etudiant</h6>
              <ul class="menu-footer">
                <li><a href="#">Génération de portfolio</a></li>
                <li><a href="#">Consultation des offres</a></li>
                <li><a href="#">Filtrage des offres</a></li>
                <li><a href="#">Contacter entreprise</a></li>
              </ul>
            </div>
            <div class="footer-col-3 col-md-2 col-xs-6">
              <h6 class="mb-20 footer-h6">Entreprise</h6>
              <ul class="menu-footer">
                <li><a href="#">Génération de PFE book</a></li>
                <li><a href="#">Pulication des offres</a></li>
                <li><a href="#">Filtrage des stagiaires</a></li>
                <li><a href="#">Contacter Etudiant</a></li>
              </ul>
            </div>
            <div class="footer-col-4 col-md-2 col-xs-6">
              <h6 class="mb-20 footer-h6">Liens Rapides</h6>
              <ul class="menu-footer">
                <li><a href="#">Accueil</a></li>
                <li><a href="#">A propos</a></li>
                <li><a href="#">Equipe</a></li>
                <li><a href="#">Contact</a></li>
              </ul>
            </div>
            <div class="footer-col-5 col-md-2 col-xs-6">
              <h6 class="mb-20 footer-h6">Support</h6>
              <ul class="menu-footer">
                <li><a href="#">FAQ</a></li>
                <li><a href="#">Aide</a></li>
                <li><a href="#">Conditions générales</a></li>
                <li><a href="#">Politique de confidentialité</a></li>
              </ul>
            </div>
          </div>
          <div class="footer-bottom mt-50">
            <div class="row">
              <div class="col-md-6">
                <span class="font-xs color-text-paragraph-2-2"
                  >Copyright &copy; 2022. JobBox all right reserved</span
                >
              </div>
              <div class="col-md-6 text-md-end text-start">
                <div class="footer-social">
                  <a class="font-xs color-text-paragraph-2-2" href="#"
                    >Privacy Policy</a
                  ><a
                    class="font-xs color-text-paragraph-2-2 mr-30 ml-30"
                    href="#"
                    >Terms &amp; Conditions</a
                  ><a class="font-xs color-text-paragraph-2-2" href="#"
                    >Security</a
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
      </footer>
    </body>
  </template>
  <script>
  import axios from "axios";
  import navbarEtudiant from '@/components/navbarEtudiant.vue';
import navbarEntreprise from '@/components/navbarEntreprise.vue';
import navbarAdmin from '@/components/navbarAdmin.vue';
  export default {
    name: "EntrepriseDetails",
    components:{navbarEtudiant,navbarEntreprise,navbarAdmin},
    data() {
      return {
        showDropdown: false,
        entrepriseUrl: null,
        userType:'',
  
        baseUrl: "http://127.0.0.1:8000/",
        entreprise: {},
        pfe_book:{},
        book:{},
      };
    },
    mounted() {
      const entrepriseId = this.$route.params.id; // Assuming you pass the offer ID through route params
    this.fetchEntrepriseDetails(entrepriseId);
    console.log(entrepriseId);
    this.fetchPfeBook(entrepriseId);
    this.fetchBook(entrepriseId);

  },
    created() {
      const userId = localStorage.getItem("user_id");


      if (!userId) {
        // User ID not found in local storage, redirect to error interface
        alert("you have to log in");
        this.$router.push("/ConnexionView");
        return;
      }
      const userType = localStorage.getItem('user_type');
      this.userType = userType;
      console.log(userType);
      this.fetchPfeBook()

    },
    
    methods: {
       deleteBook(bookId) {
        console.error("Book ID is null or undefined");
  if (!bookId) {
    console.error("Book ID is null or undefined");
    return;
  }

  try {
    const response = axios.delete(
      `http://127.0.0.1:8000/api/book/${bookId}/`
    );

    console.log("Deleted book:", response.data);
    alert("Success, book deleted");
    this.fetchBook(this.entreprise.id);

    // Remove the deleted offer from the offers array
    
  } catch (error) {
    console.error("Error deleting book:", error);
    alert("An error occurred while deleting book. Please try again later.");
  }
},
      async fetchBook(entrepriseId) {
      try {
        console.log("entreprise",entrepriseId);
        const response = await axios.get(`http://127.0.0.1:8000/api/get-pfe-book-by-entreprise/${entrepriseId}/`);
        this.book = response.data;
        console.log("book",this.book[0].id);
      } catch (error) {
        console.error('Error fetching book:', error);
        alert('An error occurred while fetching the book details.');
      }
    },
    open(bookId){
      if(this.book[0].template==='template1'){
      this.$router.push('/bookview1/'+bookId);
    }else   if(this.book[0].template==='template2'){
      this.$router.push('/bookview2/'+bookId);
    }else   if(this.book[0].template==='template3'){
      this.$router.push('/bookview3/'+bookId);
    }
    },
      fetchEntrepriseDetails(entrepriseId) {
      // Make an API request to fetch offer details by ID
      axios
        .get(`http://127.0.0.1:8000/api/entreprises/get/${entrepriseId}/`)
        .then((response) => {
          // Assign the fetched offer data to the 'offer' property
          this.entreprise = response.data;
 
        })
        .catch((error) => {
          console.error("Error fetching entreprise details:", error);
        });
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

      
      async fetchPfeBook(entrepriseId) {
        try {
          const response = await axios.get(
            `http://127.0.0.1:8000/api/pfebook/entreprise/${entrepriseId}/`
          );
          // Populate the etudiant object with data from the response
          this.pfe_book = response.data;
          console.log(this.pfe_book);
          
        } catch (error) {
          console.error("Error fetching pfebook data:", error);
        }
      },
      toggleDropdown() {
        this.showDropdown = !this.showDropdown;
      },
      logout() {
        localStorage.removeItem("user_id");
        this.$router.push("/ConnexionView");
        console.log("Logout successful");
      },
      
    },
  };
  </script>
  <style scoped>
  .custom-file {
    padding-bottom: 0px;
    width: 126px;
    text-align: center;
    justify-content: center;
  }
  .custom-iconss {
    font-size: 1.5rem !important;
    margin-right: 20px;
    color: #05264e;
  }
  .custom-icon-4 {
    color: #fff;
    font-size: 1.5rem;
    margin-left: 8px;
  }
  .dropdown-menu {
    display: block;
    left: auto !important;
    right: 0;
    min-width: 13rem;
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
    z-index: 9999; /* Set a high z-index value */
  }
  
  .show-dropdown .dropdown-menu {
    display: block;
  }
  </style>
  