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
    <title>Offre</title>
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
    <navbarEntreprise v-if="userType === 'entreprise'" />
    <navbarEtudiant v-if="userType === 'etudiant'" />
    <navbarAdmin v-if="userType === 'admin'" />

    <main class="main">
      <div class="banner-hero banner-image-single" style="margin-left: 5px">
        <img :src="offer.entreprise_cover" alt="jobbox" style="height: 348px" />
      </div>
      <div class="box-company-profile" style="width: 100px">
        <div class="image-compay" style="width: 100px; margin-left: -596px">
          <img :src="offer.entreprise_logo" alt="jobbox" />
        </div>
      </div>
      <section class="section-box-2">
        <div class="container">
          <div class="row mt-10">
            <div class="col-lg-8 col-md-12">
              <div class="inline-content">
                <h3 style="display: inline">
                  {{ offer.title }}
                </h3>
                <div class="container-time">
                  Expire le {{ offer.expirationDate }}
                </div>
              </div>
              <a
                class="company-name"
                :href="'/EntrepriseDetails/' + offer.entreprise_id"
              >
                {{ offer.nom }}
              </a>
            </div>
            <div
              v-if="userType === 'etudiant'"
              class="col-lg-4 col-md-12 text-lg-end"
            >
              <div
                class="btn-group"
                role="group"
                aria-label="Button group"
                style="cursor: pointer"
              >
                <div class="icon-container-2 hover-up">
                  <i
                    v-if="!isOfferInFavorites"
                    class="bi bi-bookmark custom-icon-3"
                    @click="addFavoriteOffer(offer.id)"
                  ></i>
                  <i
                    v-if="isOfferInFavorites"
                    class="bi bi-bookmark-fill custom-icon-3"
                    @click="deleteFavoriteOffer(favoriteOfferId)"
                  ></i>
                </div>
                <div
                  v-if="this.demandeId === null"
                  class="btn btn-apply-icon btn-apply btn-apply-big hover-up btn-postuler"
                  @click="addDemande(offer.id)"
                >
                  Postuler maintenant
                </div>
                <div
                  v-else-if="this.demande.status === 'en attente'"
                  class="btn en-attente-btn"
                  @click="deleteDemande(demandeId)"
                >
                  En attente
                </div>
                <div
                  v-else-if="this.demande.status === 'refused'"
                  class="btn refused-btn"
                >
                  Refusé
                </div>
                <div
                  v-else-if="this.demande.status === 'accepted'"
                  class="btn accepted-btn"
                >
                  Accepté
                </div>
              </div>
            </div>
          </div>
          <div class="border-bottom pt-10 pb-10"></div>
        </div>
      </section>
      <section class="section-box mt-50">
        <div class="container">
          <div class="row">
            <div class="col-lg-8 col-md-12 col-sm-12 col-12">
              <div class="content-single">
                <h5>Description</h5>
                <p>{{ offer.description }}</p>
              </div>
              <div class="author-single">
                <span>{{ offer.nom }}</span>
              </div>
              <div class="single-apply-jobs">
                <div class="row align-items-center">
                  <div class="col-md-5">
                    <a
                      v-if="userType === 'etudiant'"
                      class="btn btn-default mr-15"
                      href="#"
                      >Postuler</a
                    ><a
                      v-if="userType === 'etudiant' && !isOfferInFavorites"
                      class="btn btn-border"
                      href="#"
                      >Ajouter aux favoris</a
                    >
                  </div>
                  <div class="col-md-7 text-lg-end social-share">
                    <h6
                      class="color-text-paragraph-2 d-inline-block d-baseline mr-10"
                    >
                      Partager
                    </h6>
                    <a class="mr-5 d-inline-block d-middle" href="#"
                      ><img
                        alt="jobBox"
                        src="../assets/imgs/template/icons/share-fb.svg" /></a
                    ><a class="mr-5 d-inline-block d-middle" href="#"
                      ><img
                        alt="jobBox"
                        src="../assets/imgs/template/icons/share-tw.svg" /></a
                    ><a class="mr-5 d-inline-block d-middle" href="#"
                      ><img
                        alt="jobBox"
                        src="../assets/imgs/template/icons/share-red.svg" /></a
                    ><a class="d-inline-block d-middle" href="#"
                      ><img
                        alt="jobBox"
                        src="../assets/imgs/template/icons/share-whatsapp.svg"
                    /></a>
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
                      >{{ offer.location }}
                    </li>
                    <li>
                      <i class="bi bi-telephone custom-iconss"></i
                      >{{ offer.telephone }}
                    </li>
                    <li>
                      <i class="bi bi-envelope custom-iconss"></i
                      >{{ offer.email }}
                    </li>
                    <li v-if="offer.site_url">
                      <i class="bi bi-globe custom-iconss"></i
                      >{{ offer.site_url }}
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
                        src="../assets/imgs/page/job-single/industry.svg"
                        alt="jobBox"
                      />
                    </div>
                    <div class="sidebar-text-info ml-10">
                      <span class="text-description industry-icon mb-10"
                        >Domaine</span
                      >
                      <strong class="small-heading">{{ offer.domain }}</strong>
                    </div>
                  </div>
                  <div class="col-md-6 mt-sm-15">
                    <div class="sidebar-icon-item">
                      <img
                        src="../assets/imgs/page/job-single/job-level.svg"
                        alt="jobBox"
                      />
                    </div>
                    <div class="sidebar-text-info ml-10">
                      <span class="text-description joblevel-icon mb-10"
                        >Role</span
                      >
                      <strong class="small-heading">{{ offer.role }}</strong>
                    </div>
                  </div>
                </div>
                <div class="row mt-25">
                  <div class="col-md-6 mt-sm-15">
                    <div class="sidebar-icon-item">
                      <img
                        src="../assets/imgs/page/job-single/salary.svg"
                        alt="jobBox"
                      />
                    </div>
                    <div class="sidebar-text-info ml-10">
                      <span class="text-description salary-icon mb-10"
                        >Salaire</span
                      ><strong class="small-heading"
                        >{{ offer.minimal_payment }}DT -
                        {{ offer.maximal_payment }}DT</strong
                      >
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="sidebar-icon-item">
                      <img
                        src="../assets/imgs/page/job-single/experience.svg"
                        alt="jobBox"
                      />
                    </div>
                    <div class="sidebar-text-info ml-10">
                      <span class="text-description experience-icon mb-10"
                        >Education</span
                      ><strong class="small-heading">{{
                        offer.education
                      }}</strong>
                    </div>
                  </div>
                </div>
                <div class="row mt-25">
                  <div class="col-md-6 mt-sm-15">
                    <div class="sidebar-icon-item">
                      <img
                        src="../assets/imgs/page/job-single/job-type.svg"
                        alt="jobBox"
                      />
                    </div>
                    <div class="sidebar-text-info ml-10">
                      <span class="text-description jobtype-icon mb-10"
                        >Travail</span
                      ><strong class="small-heading">{{
                        offer.offer_type
                      }}</strong>
                    </div>
                  </div>
                  <div class="col-md-6 mt-sm-15">
                    <div class="sidebar-icon-item">
                      <img
                        src="../assets/imgs/page/job-single/deadline.svg"
                        alt="jobBox"
                      />
                    </div>
                    <div class="sidebar-text-info ml-10">
                      <span class="text-description mb-10">Durée</span
                      ><strong class="small-heading">{{
                        offer.duration
                      }}</strong>
                    </div>
                  </div>
                </div>
                <div class="row mt-25">
                  <div class="col-md-6 mt-sm-15">
                    <div class="sidebar-icon-item">
                      <img
                        src="../assets/imgs/page/job-single/updated.svg"
                        alt="jobBox"
                      />
                    </div>
                    <div class="sidebar-text-info ml-10">
                      <span class="text-description jobtype-icon mb-10"
                        >Binome</span
                      ><strong class="small-heading">{{ offer.binome }}</strong>
                    </div>
                  </div>
                  <div class="col-md-6 mt-sm-15">
                    <div class="sidebar-icon-item">
                      <img
                        src="../assets/imgs/page/job-single/people-fill.svg"
                        alt="jobBox"
                      />
                    </div>
                    <div class="sidebar-text-info ml-10">
                      <span class="text-description mb-10">Stagiares</span
                      ><strong class="small-heading">{{
                        offer.number_of_interns
                      }}</strong>
                    </div>
                  </div>
                </div>
              </div>
              <div class="sidebar-border">
                <h5 class="border-bottom pb-15 mb-30">Compétences</h5>
                <div class="comp-bar">
                  <div
                    v-for="(skill, index) in offer.skills"
                    :key="index"
                    class="container-competences"
                  >
                    {{ skill }}
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
                      <img
                        src="/template/assets/imgs/template/icons/person-vcard.svg"
                        class="custom-iconss"
                      />{{ offer.nom_rh }} {{ offer.prenom_rh }}
                    </li>
                    <li>
                      <i class="bi bi-telephone custom-iconss"></i
                      >{{ offer.telephone_rh }}
                    </li>
                    <li>
                      <i class="bi bi-envelope custom-iconss"></i
                      >{{ offer.email_rh }}
                    </li>
                  </ul>
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
import navbarEntreprise from "@/components/navbarEntreprise.vue";
import navbarEtudiant from "@/components/navbarEtudiant.vue";
import navbarAdmin from "@/components/navbarAdmin.vue";
export default {
  name: "OffreDetails",
  components: { navbarEntreprise, navbarEtudiant, navbarAdmin },
  data() {
    return {
      etudiantUrl: null,
      baseUrl: "http://127.0.0.1:8000/",
      userType: "",
      favoriteOffers: [],
      favoriteOfferId: null,
      demande: [],
      demandeId: null,
      demandeAdded: false,

      entrepriseUrl: null,
      offer: {},
    };
  },
  mounted() {
    // Fetch offer details data from your API
    // Assuming you have a method to fetch offer details by ID
    const offerId = this.$route.params.id; // Assuming you pass the offer ID through route params
    this.fetchOfferDetails(offerId);
    console.log(offerId, "details");
    console.log(this.demandeAdded);
    this.fetchFavoriteOffers();
    this.fetchDemande(offerId);
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
  methods: {
    logout() {
      localStorage.removeItem("user_id");
      this.$router.push("/ConnexionView");
      console.log("Logout successful");
    },
    redirectToCompanyDetails(companyId) {
      // Navigate to the company details view using the company ID
      this.$router.push({ name: "company-details", params: { id: companyId } });
    },
    fetchOfferDetails(offerId) {
      // Make an API request to fetch offer details by ID
      axios
        .get(`http://127.0.0.1:8000/api/offer/${offerId}/`)
        .then((response) => {
          // Assign the fetched offer data to the 'offer' property
          this.offer = response.data;
        })
        .catch((error) => {
          console.error("Error fetching offer details:", error);
        });
    },
    addDemande(offerId) {
      const userId = localStorage.getItem("user_id");
      axios
        .post(`http://127.0.0.1:8000/api/demande/${userId}/add/${offerId}/`)
        .then((response) => {
          // Handle successful response if needed
          console.log("Demande added :", response.data);
          this.fetchDemande(offerId);
          this.demandeAdded = true;
          this.demandeId = this.demande.id;
          this.ajouterAction('Candidature dans les détails d\'une offre');

          // You can update the UI to reflect that the offer is now favorited
        })
        .catch((error) => {
          console.error("Error adding demande:", error);
          // Handle error response if needed
        });
    },
    fetchDemande(offerId) {
      const userId = localStorage.getItem("user_id");
      axios
        .get(`http://127.0.0.1:8000/api/demande/${userId}/get/${offerId}/`)
        .then((response) => {
          // Handle successful response if needed
          console.log("Fetched demande:", response.data);
          this.demande = response.data;
          this.demandeId = this.demande.id;
          console.log(this.demandeId);
          console.log(this.demande);
          // You can update the UI to reflect that the offer is now favorited
        })
        .catch((error) => {
          console.error("Error fetching demande:", error);
          if (error.response && error.response.status === 404) {
            // Demande not found, set demandeId to null
            this.demande = {};
            this.demandeId = null;
          }
        });
    },
    addFavoriteOffer(offerId) {
      const userId = localStorage.getItem("user_id");
      axios
        .post(
          `http://127.0.0.1:8000/api/etudiant/${userId}/addFavoris/${offerId}/`
        )
        .then((response) => {
          // Handle successful response if needed
          console.log("Offer added to favorites:", response.data);
          this.fetchFavoriteOffers();
          this.ajouterAction('Offre ajoutée aux favoris');

          // You can update the UI to reflect that the offer is now favorited
        })
        .catch((error) => {
          console.error("Error adding offer to favorites:", error);
          // Handle error response if needed
        });
    },
    async deleteFavoriteOffer(favoriteOfferId) {
      if (!favoriteOfferId) {
        console.error(
          "Favorite offer ID is null or undefined",
          favoriteOfferId
        );
        return;
      }
      try {
        await axios
          .delete(
            `http://127.0.0.1:8000/api/etudiant/deleteFavoris/${favoriteOfferId}/`
          )
          .then(() => {
            // Handle successful response if needed
            console.log("Offer removed from favorites");
            // You can update the UI to reflect that the offer is now removed from favorites
            this.fetchFavoriteOffers(); // Fetch the student's favorite offers again after removing a favorite
          });
      } catch (error) {
        console.error("Error removing offer from favorites:", error);
        // Handle error response if needed
      }
    },
    async deleteDemande(demandeId) {
      if (!demandeId) {
        console.error("Favorite offer ID is null or undefined", demandeId);
        return;
      }
      try {
        await axios
          .delete(`http://127.0.0.1:8000/api/demande/${demandeId}/delete/`)
          .then(() => {
            // Handle successful response if needed
            console.log("Demande canceled");
            // You can update the UI to reflect that the offer is now removed from favorites
            // Fetch the student's favorite offers again after removing a favorite
            this.demandeAdded = false;
            console.log(this.demandeAdded);

            window.location.reload();
          });
      } catch (error) {
        console.error("Error removing demande:", error);
        // Handle error response if needed
      }
    },
    fetchFavoriteOffers() {
      const userId = localStorage.getItem("user_id");
      axios
        .get(`http://127.0.0.1:8000/api/etudiant/${userId}/getFavoris/`)
        .then((response) => {
          // Store the fetched favorite offers in the data property
          this.favoriteOffers = response.data;
          this.updateFavoriteOfferId();
          console.log("Fetched favorite offers", this.favoriteOffers);
        })
        .catch((error) => {
          console.error("Error fetching favorite offers:", error);
          // Handle error response if needed
        });
    },
    updateFavoriteOfferId() {
      const favorite = this.favoriteOffers.find(
        (favoriteOffer) => favoriteOffer.offer === this.offer.id
      );
      this.favoriteOfferId = favorite ? favorite.id : null;
    },
    ajouterAction(message) {
  const userId = localStorage.getItem("user_id");
  if (!userId) {
    alert("Vous devez être connecté.");
    return;
  }
  axios.post(`http://127.0.0.1:8000/creer-action/${userId}/`, {
    action_message: message,
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
  },
  computed: {
    isOfferInFavorites() {
      // Check if the current offer is in the student's favorite offers
      return this.favoriteOffers.some(
        (favoriteOffer) => favoriteOffer.offer === this.offer.id
      );
    },
  },
  watch: {
    favoriteOffers() {
      this.updateFavoriteOfferId();
    },
  },
};
</script>
<style scoped>
.custom-iconss {
  font-size: 1.5rem !important;
  margin-right: 20px;
  color: #05264e;
}
.en-attente-btn {
  color: #fff;
  background-color: #dca11d;
  border: #dca11d solid 1px;
  border-radius: 12px !important;
  display: flex;
  align-items: center;
}
.refused-btn {
  color: #fff;
  background-color: #D00711;
  border: #D00711 solid 1px;
  border-radius: 12px !important;
  display: flex;
  align-items: center;
}
.btn-postuler {
  border-radius: 17px !important;
}
.accepted-btn{
  color: #fff;
  background-color: #00901D;
  border: #00901D solid 1px;
  border-radius: 12px !important;
  display: flex;
  align-items: center;
}
</style>
