<template>
  <router>
    <!DOCTYPE html>

    <meta http-equiv="content-type" content="text/html;charset=UTF-8" />
    <head>
      <meta charset="UTF-8" />
      <meta
        name="viewport"
        content="width=device-width, initial-scale=1, maximum-scale=1"
      />
      <meta http-equiv="X-UA-Compatible" content="ie=edge" />
      <meta name="msapplication-TileColor" content="#0E0E0E" />
      <meta name="template-color" content="#0E0E0E" />
      <link rel="manifest" href="manifest.html" crossorigin />
      <meta name="msapplication-config" content="browserconfig.html" />
      <meta name="description" content="Index page" />
      <meta name="keywords" content="index, page" />
      <meta name="author" content="" />
      <title>Etudiants</title>
      <link
        rel="shortcut icon"
        type="image/x-icon"
        href="assets/imgs/template/favicon.svg"
      />
      <link
        href="./template/assets/css/stylecd4ee.css?version=4.1"
        rel="stylesheet"
      />

      <title>SW Connect</title>
    </head>
    <body style="overflow-x: hidden;">
      <navbarEtudiant />
      <main class="main">
        <section class="section-box-2">
          <div class="container">
            <div class="banner-hero banner-single banner-single-bg">
              <div class="block-banner text-center">
                <h3 class="wow animate__animated animate__fadeInUp">
                  <span class="color-brand-2">Entreprises</span> actuellement
                  disponibles
                </h3>
                <!--<div class="font-sm color-text-paragraph-2 mt-10 wow animate__animated animate__fadeInUp" data-wow-delay=".1s">Trouvez facilement une opportunité qui correspond à vos intérêts et à votre localisation <br class="d-none d-xl-block"></div>-->
                <div
                  class="form-find text-start mt-40 wow animate__animated animate__fadeInUp"
                  data-wow-delay=".2s"
                >
                  <form>
                    <input
                      id="input-keysearch"
                      class="form-input input-keysearch mr-10"
                      type="text"
                      placeholder="mot clé... "
                    />
                    <button
                      class="btn btn-default btn-find font-sm"
                      @click.prevent="onSearchClick"
                    >
                      Rechercher
                    </button>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section class="section-box mt-30">
          <div class="container">
            <div class="row flex-row-reverse">
              <div
                class="col-lg-9 col-md-12 col-sm-12 col-12 float-right"
                style="width: 100%"
              >
                <div class="content-page">
                  <!-- <div class="box-filters-job">
              <div class="row">
                  <div class="col-xl-6 col-lg-5"><span class="text-small text-showing">Showing <strong>41-60 </strong>of <strong>944 </strong>jobs</span></div>
                  <div class="col-xl-6 col-lg-7 text-lg-end mt-sm-15">
               
                  </div>
                </div>
              </div>-->
                  <div class="row" style="position: relative; top: -45px">
                    <template v-if="searchResults.length === 0">
                      <div
                        v-for="entreprise in entreprises"
                        :key="entreprise.id"
                        class="col-xl-3 col-lg-4 col-md-6"
                      >
                        <div
                          class="card-grid-1 hover-up wow animate__animated animate__fadeIn"
                        >
                          <div class="image-box">
                            <a
                              ><img
                                :src="this.baseUrl + entreprise.profile_logo"
                                alt="jobBox"
                                style="height: 50px"
                            /></a>
                          </div>
                          <div class="info-text mt-10">
                            <h5 class="font-bold">
                              <a href="company-details.html">{{
                                entreprise.nom
                              }}</a>
                            </h5>
                            <div class="mt-5">
                              <span
                                class="font-xs color-text-mutted ml-10"
                              ></span>
                            </div>
                            <span
                              class="card-location"
                              style="font-size: 17px"
                              >{{ entreprise.location }}</span
                            ><br />
                            <span style="font-weight: 500">{{
                              entreprise.type_industrie
                            }}</span>
                            <div class="mt-30">
                              <a class="btn btn-grey-big"
                                ><span>{{ entreprise.total_offers || 0 }}</span
                                ><span> offres</span></a
                              >
                            </div>
                          </div>
                        </div>
                      </div>
                    </template>
                  </div>
                  <template v-if="searchResults.length">
                    <div
                      v-for="entreprise in searchResults"
                      :key="entreprise.id"
                      class="col-xl-3 col-lg-4 col-md-6"
                    >
                      <div
                        class="card-grid-1 hover-up wow animate__animated animate__fadeIn"
                      >
                        <div class="image-box">
                          <a
                            ><img
                              :src="entreprise.profile_logo"
                              alt="jobBox"
                              style="height: 50px"
                          /></a>
                        </div>
                        <div class="info-text mt-10">
                          <h5 class="font-bold">
                            <a href="company-details.html">{{
                              entreprise.nom
                            }}</a>
                          </h5>
                          <div class="mt-5">
                            <span
                              class="font-xs color-text-mutted ml-10"
                            ></span>
                          </div>
                          <span class="card-location" style="font-size: 17px">{{
                            entreprise.location
                          }}</span
                          ><br />
                          <span style="font-weight: 500">{{
                            entreprise.type_industrie
                          }}</span>
                          <div class="mt-30">
                            <a class="btn btn-grey-big"
                              ><span>{{ entreprise.total_offers || 0 }}</span
                              ><span> offres</span></a
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </template>
                </div>
                <!--<div class="paginations">
              <ul class="pager">
                <li><a class="pager-prev" href="#"></a></li>
                <li><a class="pager-number" href="#">1</a></li>
                <li><a class="pager-number" href="#">2</a></li>
                <li><a class="pager-number" href="#">3</a></li>
                <li><a class="pager-number" href="#">4</a></li>
                <li><a class="pager-number" href="#">5</a></li>
                <li><a class="pager-number active" href="#">6</a></li>
                <li><a class="pager-number" href="#">7</a></li>
                <li><a class="pager-next" href="#"></a></li>
              </ul>
            </div>-->
              </div>
            </div>
          </div>
        </section>
      </main>
      <footer class="footer-cnx">
        <p>@ 2024 SW Connect - Tous droits réservés</p>
      </footer>
      <!--<footer class="footer mt-50">
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
import navbarEtudiant from "@/components/navbarEtudiant.vue";
export default {
  components: { navbarEtudiant },
  name: "EntGrid",
  data() {
    return {
      baseUrl: "http://127.0.0.1:8000/",
      etudiant: {},
      entreprises: [],
      etudiantUrl: null,
      entreprisesUrl: null,
      //dropdownmenu
      showDropdown: false,
      searchQuery: "", // Ajout du champ de recherche
      searchResults: [],
    };
  },
  mounted() {
    // Call a method to fetch all offers from the backend API
    this.fetchAllEntreprises();
  },
  created() {
    const userId = localStorage.getItem("user_id");
    if (!userId) {
      // User ID not found in local storage, redirect to error interface
      alert("you have to log in");
      this.$router.push("/ConnexionView");
      return;
    }

    this.etudiant.id = userId;
    console.log(this.etudiant.id);
    // Fetch entreprise data using the entreprise ID
    this.fetchEtudiantData();
  },
  methods: {
    fetchAllEntreprises() {
      // Make an API request to fetch all offers from the backend
      // Assuming you have a method named getAllOffers in your API service
      // Replace 'apiService' with your actual API service
      axios
        .get("http://127.0.0.1:8000/api/entreprises/getall/")
        .then((response) => {
          // Assign the fetched offers to the offers array
          this.entreprises = response.data;
          this.gettotaloffrebyentreprise();
        })
        .catch((error) => {
          console.error("Error fetching entreprises:", error);
        });
    },
    async fetchEtudiantData() {
      try {
        const response = await axios.get(
          `http://127.0.0.1:8000/api/etudiants/get/${this.etudiant.id}/`
        );
        // Populate the etudiant object with data from the response
        this.etudiant = response.data;

        if (this.etudiant.profile_photo) {
          this.etudiantUrl = this.baseUrl + this.etudiant.profile_photo;
        }
      } catch (error) {
        console.error("Error fetching etudiant data:", error);
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
    gettotaloffrebyentreprise() {
      this.entreprises.forEach((entreprise) => {
        axios
          .get(
            `http://127.0.0.1:8000/entreprise/${entreprise.id}/total_offers/`
          )
          .then((response) => {
            console.log("entrepriseid: " + entreprise.id);
            console.log("total_offers: " + response.data.total_offers);
            entreprise.total_offers = response.data.total_offers; // Direct assignment
          })
          .catch((error) => {
            console.error("Total offres by entreprise:", error);
          });
      });
    },
    onSearchClick() {
      const keyword = document.getElementById("input-keysearch").value;
      this.searchEntreprises(keyword);
    },
    searchEntreprises(keyword) {
      if (keyword.trim() !== "") {
        // Requête GET à l'API pour récupérer les PFE books
        axios
          .get("http://localhost:8000/api/entreprisesbymc/", {
            params: {
              q: keyword,
            },
          })
          .then((response) => {
            const searchResults = response.data;
            console.log(searchResults);
            this.updateFilteredentreprises(searchResults);
          })
          .catch((error) => {
            console.error("Error searching offers:", error);
          });
      }
    },
    updateFilteredentreprises(searchResults) {
      this.entreprises = searchResults;
    },
  },
};
</script>
<style scoped>
.cus-mr {
  margin: 5px;
}
.btn-apply-now {
  background-color: #e0e6f7;
  color: #447ab8;
  padding: 12px 10px;
  min-width: 95px;
  border-radius: 4px;
  font-size: 12px;
  text-transform: capitalize;
}
.card-grid-2 .card-block-info .card-text-price {
  color: #447ab8;
}
.card-grid-2:hover .btn-apply-now {
  color: #ffffff;
  background-color: #447ab8;
}
.color-text-paragraph {
  color: #05264e;
}
.btn.btn-default {
  color: #447ab8;
  background-color: #ffffff;
  line-height: 26px;
  padding: 10px 25px;
}
.btn.btn-default:hover {
  background-color: #ffffff;
  transform: translateY(-2px);
  transition: 0.2s;
}
.postbutt {
  border: 1px solid #447ab8;
  margin-left: 10px;
  width: 200px;
}

.icon-fb {
  height: 50px;
  width: 50px;
}
.nav-li-cus {
  font-size: 16px;
}
.header-left-cus {
  margin-right: 54px;
}
.header-right-cus {
  min-width: 335px;
}
.header-logo-cus {
  height: 50px;
}
.header-cus {
  margin-bottom: 92px;
  padding-right: 40px;
  background-color: #fff;
  border-bottom: 1px solid #e0e6f7;
}
.grid-row-offer {
  padding-right: 32px;
}
.logo-site {
  height: 55px;
  width: 434px;
}
.cus-row {
  margin-right: 0px;
}
.header .main-menu li a:hover,
.header .main-menu li a.active {
  color: #fff;
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

.color-text-paragraph-2 {
  color: #05264e;
}
.color-brand-1 {
  color: #05264e;
}
.footer-cnx {
  position: relative;
  background-color: transparent;
  height: 20px;
  width: 150%;
  overflow-x: hidden;
}
</style>
