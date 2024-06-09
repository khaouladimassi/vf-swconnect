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
      <title> Mes offres</title>
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
    <body>
        <navbarEntreprise />

    <main class="main-2" style="margin-top: 0px">
      <div class="nav-2" style="border-right: 1px solid #dee2e6">
        <nav class="nav-main-menu-2">
          <ul class="main-menu-2">
            <li>
              <router-link :to="'/EntOverview/' + entreprise.id"   class="dashboard2"><img
                  src="../assets/imgs/template/icons/stack.svg"
                  alt="jobBox"
                /><span class="name">Overview</span></router-link
              >
            </li>
            <li>
              <router-link to="/BookGeneration" class="dashboard2" 
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
              <router-link to="/MesOffres" class="active dashboard2" 
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
            <div class="box-title-2" style="width:150%; display:flex;">
              <h3 class="mb-35">Mes Offres</h3>
            <router-link :to="`/PfeBook/${entreprise.id}`"> <h6 v-if="pfe_book && pfe_book.length > 0" class="mb-35" style="margin-left:750px;"  >Voir pfe book</h6></router-link>
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
                  <div v-for="offer in offers" :key="offer.id"  class="col-xl-12 col-12">
       
                    <div class="card-grid-2 hover-up"><span class="flash"></span>
                      <div class="row">
                        <div class="col-lg-6 col-md-6 col-sm-12">
                          <div class="card-grid-2-image-left">
                            <div class="image-box"><img  :src="this.entrepriseUrl" alt="jobBox" style="width: 52px;;"></div>
                            <div class="right-info"><a class="name-job">{{entreprise.nom}}</a><span class="location-small">{{offer.location}}</span></div>
                          </div>
                        </div>
                        <div class="col-lg-6 text-start text-md-end pr-60 col-md-6 col-sm-12">
                          <div class="pl-15 mb-15 mt-30">       <a v-for="(skill, index) in offer.skills" :key="index" class='btn btn-grey-small cus-mr mr-5' href='jobs-grid.html'>
                                    {{ skill }}
                                </a></div>
                        </div>
                      </div>
                      <div class="card-block-info">
                        <h4><a :href="'/OffreDetails/' + offer.id ">{{offer.title}}</a></h4>
                        <div class="mt-5"><span class="card-briefcase">{{offer.offer_type}}</span><span class="card-time">{{offer.created_at.slice(0,10)}}</span></div>
                        <p class="font-sm color-text-paragraph mt-10">{{offer.description}}</p>
                        <div class="card-2-bottom mt-20">
                          <div class="row">
                            <div class="col-lg-7 col-7"><span class="card-text-price">{{offer.maximal_payment}} DT</span></div>
                            <div class="col-lg-5 col-5 text-end">
                                <div class="btn btn-apply-now" style="color:#447AB8" type="submit" @click="openModal(offer.id)">Modifier</div>
                              <div class="btn btn-apply-now"  style="    margin-left: 14px;color:#447AB8" @click="deleteOffer(offer.id)">Supprimer</div>
                              <router-link :to="'/MesDemandes/'+offer.id" class="btn btn-apply-now"  style="    margin-left: 14px;color:#447AB8">Voir demandes</router-link>
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
            </div>
          </div>
       
          <div class="footer-2 mt-20">
            <div class="container">
              <div class="box-footer-2">
                <div class="row">
                  <div class="col-md-6 col-sm-12 mb-25 text-center text-md-start">
                    <p class="font-lg color-text-paragraph-made-by">
                      © 2024 - Made By SwConnect
                    </p>
                  </div>
                  <div class="col-md-6 col-sm-12 text-center text-md-end mb-25">
                    <ul class="menu-footer-2">
                      <li><a href="#">About</a></li>
                      <li><a href="#">Careers</a></li>
                      <li><a href="#">Policy</a></li>
                      <li><a href="#">Contact</a></li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
      </div>
    </main>
      <!-- Modal -->
      <div class="modal" v-if="showModal">
      <!-- Modal content -->
      <div class="modal-content" style="max-height: 70vh; overflow-y: auto;">
        <h5 class="modal-title">Modifier Offre</h5>
        <span class="close" @click="closeModal">&times;</span>
        <div class="col-lg-12">
                            <div class="form-group-2 mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Compétences</label
                                                        >
                                                                                                          <select
                                                      v-model="offer.skills"
                                                      name="competence"
                                                 
                                                      class="form-control"
                                                      multiple
                                                  >
                                                  <option value="algorithmique">Algorithmique</option>
    <option value="analyse-de-donnees">Analyse de données</option>
    <option value="analyse-de-marche">Analyse de marché</option>
    <option value="analyse-financiere">Analyse financière</option>
    <option value="animation">Animation</option>
    <option value="art-numerique">Art numérique</option>
    <option value="arts-plastiques">Arts plastiques</option>
    <option value="astrophysique">Astrophysique</option>
    <option value="banque-et-finance">Banque et finance</option>
    <option value="base-de-donnees">Base de données</option>
    <option value="biologie-moleculaire">Biologie moléculaire</option>
    <option value="branding">Branding</option>
    <option value="chimie-organique">Chimie organique</option>
    <option value="communication-digitale">Communication digitale</option>
    <option value="comptabilite">Comptabilité</option>
    <option value="conception-de-produits">Conception de produits</option>
    <option value="design-graphique">Design graphique</option>
    <option value="developpement-web">Développement web</option>
    <option value="economie-internationale">Économie internationale</option>
    <option value="econometrie">Économétrie</option>
    <option value="finance-d-entreprise">Finance d'entreprise</option>
    <option value="genetique">Génétique</option>
    <option value="genie-logiciel">Génie logiciel</option>
    <option value="gestion-de-projet-marketing">Gestion de projet marketing</option>
    <option value="gestion-des-risques">Gestion des risques</option>
    <option value="illustration">Illustration</option>
    <option value="intelligence-artificielle">Intelligence artificielle</option>
    <option value="investissements">Investissements</option>
    <option value="marketing-de-contenu">Marketing de contenu</option>
    <option value="marketing-strategique">Marketing stratégique</option>
    <option value="mathematiques-appliquees">Mathématiques appliquées</option>
    <option value="marches-financiers">Marchés financiers</option>
    <option value="mecanique-des-fluides">Mécanique des fluides</option>
    <option value="nanotechnologie">Nanotechnologie</option>
    <option value="peinture">Peinture</option>
    <option value="photographie">Photographie</option>
    <option value="programmation">Programmation</option>
    <option value="publicite-en-ligne">Publicité en ligne</option>
    <option value="relations-publiques">Relations publiques</option>
    <option value="reseaux-informatiques">Réseaux informatiques</option>
    <option value="reseaux-sociaux">Réseaux sociaux</option>
    <option value="sciences-de-la-terre">Sciences de la terre</option>
    <option value="sculpture">Sculpture</option>
    <option value="securite-informatique">Sécurité informatique</option>
    <option value="seo-et-sem">SEO et SEM</option>
    <option value="statistiques">Statistiques</option>
    <option value="systemes-d-exploitation">Systèmes d'exploitation</option>
    <option value="typographie">Typographie</option>
                                                  </select>
                            </div>
                          </div>
                          <div class="row">
  <div class="col-lg-6 col-md-6">
    <div class="form-group mb-30 mr-30">
      <label class="font-lg color-text-mutted-2 mb-10">Titre</label>
      <input
        v-model="offer.title"
        name="title"
        class="form-control-2"
        type="text"
      />
    </div>
  </div>
  <div class="col-lg-6 col-md-6">
    <div class="form-group mb-30 mr-30">
      <label class="font-lg color-text-mutted-2 mb-10">Role</label>
      <select
        class="form-control"
        v-model="offer.role"
        name="role"
      >
      <option value="Administrateur de base de données">Administrateur de base de données</option>
      <option value="Administrateur réseau">Administrateur réseau</option>
      <option value="Administrateur système">Administrateur système</option>
      <option value="Analyste de risques">Analyste de risques</option>
      <option value="Analyste financier">Analyste financier</option>
    <option value="Analyste marketing">Analyste marketing</option>
    <option value="Animateur 3D">Animateur 3D</option>
    <option value="Artiste numérique">Artiste numérique</option>
    <option value="Artiste peintre">Artiste peintre</option>
    <option value="Artiste plasticien">Artiste plasticien</option>
    <option value="Astrophysicien">Astrophysicien</option>
    <option value="Biologiste moléculaire">Biologiste moléculaire</option>
    <option value="Chef de projet marketing">Chef de projet marketing</option>
    <option value="Chimiste organique">Chimiste organique</option>
    <option value="Comptable">Comptable</option>
    <option value="Data analyst">Data analyst</option>
    <option value="Designer de produits">Designer de produits</option>
    <option value="Développeur logiciel">Développeur logiciel</option>
    <option value="Développeur web">Développeur web</option>
    <option value="Économiste international">Économiste international</option>
    <option value="Économètre">Économètre</option>
    <option value="Géologue">Géologue</option>
    <option value="Généticien">Généticien</option>
    <option value="Graphiste">Graphiste</option>
    <option value="Ingénieur logiciel">Ingénieur logiciel</option>
    <option value="Illustrateur">Illustrateur</option>
    <option value="Ingénieur en intelligence artificielle">Ingénieur en intelligence artificielle</option>
    <option value="Spécialiste en marketing de contenu">Spécialiste en marketing de contenu</option>
    <option value="Spécialiste en marketing stratégique">Spécialiste en marketing stratégique</option>
    <option value="Ingénieur en mécanique des fluides">Ingénieur en mécanique des fluides</option>
    <option value="Ingénieur en nanotechnologie">Ingénieur en nanotechnologie</option>
    <option value="Photographe">Photographe</option>
    <option value="Responsable des relations publiques">Responsable des relations publiques</option>
    <option value="Sculpteur">Sculpteur</option>
    <option value="Spécialiste en branding">Spécialiste en branding</option>
    <option value="Spécialiste en communication digitale">Spécialiste en communication digitale</option>
    <option value="Spécialiste en médias sociaux">Spécialiste en médias sociaux</option>
    <option value="Spécialiste en publicité en ligne">Spécialiste en publicité en ligne</option>
    <option value="Spécialiste en référencement">Spécialiste en référencement</option>
    <option value="Spécialiste en sécurité informatique">Spécialiste en sécurité informatique</option>
    <option value="Statisticien">Statisticien</option>
    <option value="Typographe">Typographe</option>
      </select>
    </div>
  </div>
</div>
<h5 style="    margin-left: -745px; margin-bottom:30px;">Paiement</h5>
<div class="row">
                          <div class="col-lg-6 col-md-6">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Paiement Minimal</label
                              >
                              <input
                                v-model="offer.minimal_payment"
                                name="minPayment"
                                class="form-control"
                                type="text"
                           
                              />
                         
                            </div>
                          </div>
                          <div class="col-lg-6 col-md-6" >
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Paiement Maximal</label
                              >
                              <input
                                v-model="offer.maximal_payment"
                                name="maxPayment"
                                class="form-control"
                                type="text"
                              
                              />
             
                            </div>
                          </div>
                        </div>
                          <h5 style="margin-left: -610px; margin-bottom:30px;">
                            Informations Avancées
                          </h5>
                          <div class="row">
                          <div class="col-lg-4 col-md-4">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Education</label
                              >
                              <select
                                v-model="offer.education"
                                name="education"
                                class="form-control"
                             
                              >
                                <option value="Bac+2">Bac+2</option>
                                <option value="Bac+3">Bac+3</option>
                                <option value="Bac+5">Bac+5</option>
                                <option value="Bac+6">Bac+6</option>
                              </select>
                 
                            </div>
                          </div>
                          <div class="col-lg-4 col-md-4">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Domaine</label
                              >
                              <select
                                v-model="offer.domain"
                                name="domain"
                                class="form-control"
                   
                              >
                              <option value="Agriculture">Agriculture</option>
  <option value="Automotive">Automotive</option>
  <option value="Construction">Construction</option>
  <option value="Consulting">Consulting</option>
  <option value="E-commerce">E-commerce</option>
  <option value="Education">Education</option>
  <option value="Energy">Energy</option>
  <option value="Finance">Finance</option>
  <option value="Génie Civil">Génie Civil</option>
  <option value="Informatique">Informatique</option>
  <option value="Legal">Legal</option>
  <option value="Logistics">Logistics</option>
  <option value="Manufacturing">Manufacturing</option>
  <option value="Media">Media</option>
  <option value="Real Estate">Real Estate</option>
  <option value="Retail">Retail</option>
  <option value="Santé">Santé</option>
  <option value="Telecommunications">Telecommunications</option>
  <option value="Tourisme">Tourisme</option>
  <option value="Transport">Transport</option>
                              </select>
                         
                            </div>
                          </div>
                          <div class="col-lg-4 col-md-4">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Espace de travail</label
                              >
                              <select
                                v-model="offer.offer_type"
                                name="workspace"
                                class="form-control"
                         
                              >
                                <option value="Télétravail">Télétravail</option>
                                <option value="Bureau">Bureau</option>
                              </select>
                       
                            </div>
                          </div>
                        </div>
                        <div class="row">
                          <div class="col-lg-6 col-md-6">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Nombre de stagiares</label
                              >
                              <input
                                v-model="offer.number_of_interns"
                                name="internCount"
                                class="form-control"
                                type="text"
                                
                              />
                           
                            </div>
                          </div>
                          <div class="col-lg-6 col-md-6">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Binome</label
                              >
                              <select
                                v-model="offer.binome"
                                name="binome"
                                class="form-control"
        
                              >
                                <option value="Oui">Oui</option>
                                <option value="Non">Non</option>
                              </select>
                        
                            </div>
                          </div>
                        </div>
                        <div class="row">
                          <div class="col-lg-6 col-md-6">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Date d'expiration</label
                              >
                              <input
                                v-model="this.expirationDate"
                                name="expirationDate"
                                class="form-control"
                                type="text"
                                placeholder="e.g. dd/mm/aaaa"
                             
                              />
             
                            </div>
                          </div>
                       
                      
                          <div class="col-lg-6 col-md-6">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Durée</label
                              >
                              <select
                                v-model="offer.duration"
                                name="duration"
                                class="form-control"
                           
                              >
                                <option value="1 mois">1 mois</option>
                                <option value="3 mois">3 mois</option>
                                <option value="4 mois">4 mois</option>
                                <option value="6 mois">6 mois</option>
                              </select>
                    
                            </div>
                          </div>
                        </div>
                  
                          <div class="col-lg-12">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Location</label
                              >
                              <input
                                class="form-control"
                                v-model="offer.location"
                                name="location">

                            </div>
                          </div>
                       
                          <div class="col-lg-12">
                            <div class="form-group-2 mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Description</label
                              >
                              <textarea
                                v-model="offer.description"
                                name="description"
                     
                                class="form-control-2"
                                rows="8"
                              >
 </textarea>
                            </div>
                           
                          </div>
                          <div class="col-lg-4 col-md-4">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Status</label
                              >
                              <select
                                v-model="offer.status"
                                name="status"
                          
                                class="form-control"
                              >
                                <option value="Soon">Soon</option>
                                <option value="En cours de recrutement">
                                  En cours de recrutement
                                </option>
                                <option value="Expirée">Expirée</option>
                              </select>
                             
                            </div>
                          </div>
                          <div class="col-lg-12">
                            <div class="form-group mt-10">
                              <button
                                class="btn btn-default-2 btn-brand-2"
                                type="submit"
                                @click="updateOffer(selectedOfferId)"
                              >
                                Modifier
                              </button><pre>{{offer.id}}</pre>
                            </div>
                          </div>

      </div>
    </div>
  </body>
    
  </template>
  <script>
  import axios from "axios";
  import navbarEntreprise from '@/components/navbarEntreprise.vue';
  export default {
    name: "MesOffres",
    components:{navbarEntreprise},
    data() {
      return {
        baseUrl: "http://localhost:8000",
        entrepriseUrl:null,
        userType:'',
        entreprise:{},
        offers:{},
        pfe_book:{},
        showModal: false,
        offer:{
id:'',
            skills: [],
            title: "",
           role: "",
         min_payment: "",
      max_payment: "",
      domain: "",
      offer_type: "",
      number_of_interns: "",
      binome: "",
      expirationDate: "",
      duration: "",
      description: "",
      status: "",
      education: "",
      location:""
        },
        
  
   
        
    
        //filesize control
        fileSizeError: false,
        //dropdownmenu
        showDropdown: false,
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
  
    this.entreprise.id = userId;
    console.log(this.entreprise.id);
    // Fetch entreprise data using the entreprise ID
    this.fetchEntrepriseData();
    const userType = localStorage.getItem('user_type');
    if (userType === 'entreprise') {
      this.userType = userType;}
  },
  mounted() {
    // Call a method to fetch all offers from the backend API
    this.fetchOffersData();
    this.fetchPfeBook();
  },

  
    methods: {
        openModal(offerId) {
      this.showModal = true;
      if (!offerId) {
        console.error("Offer ID is null or undefined in modal");
        return;}
        this.selectedOfferId = offerId;
    },
    closeModal(){
        this.showModal = false;
    },

async fetchPfeBook() {
        try {
          const response = await axios.get(
            `http://127.0.0.1:8000/api/pfebook/entreprise/${this.entreprise.id}/`
          );
          // Populate the etudiant object with data from the response
          this.pfe_book = response.data;
          console.log(this.pfe_book);
          
        } catch (error) {
          console.error("Error fetching pfebook data:", error);
        }
      },
      
      async fetchEntrepriseData() {
        try {
          const response = await axios.get(
            `http://127.0.0.1:8000/api/entreprises/get/${this.entreprise.id}/`
          );
          // Populate the etudiant object with data from the response
          this.entreprise = response.data;
          if (this.entreprise.profile_logo) {
            this.entrepriseUrl = this.baseUrl + this.entreprise.profile_logo;
          }
        } catch (error) {
          console.error("Error fetching entreprise data:", error);
        }
      },
      async fetchOffersData() {
        try {
          const response = await axios.get(
            `http://127.0.0.1:8000/api/offers/entreprise/${this.entreprise.id}/`
          );
          // Populate the etudiant object with data from the response
          this.offers = response.data;
        
        } catch (error) {
          console.error("Error fetching offer data:", error);
        }
      },
      async updateOffer(offerId) {
  if (!offerId) {
    console.error("Offer ID is null or undefined");
    return;
  }

  try {
    // Retrieve the existing offer data
    const existingOffer = this.offers.find(offer => offer.id === offerId);
    if (!existingOffer) {
      console.error("Offer not found in existing data");
      return;
    }

    // Construct the update request data by merging existing and new offer data
    const requestData = {
      id: offerId,
      entreprise: this.entreprise.id,
      title: this.offer.title || existingOffer.title,
      description: this.offer.description || existingOffer.description,
      minimal_payment: this.offer.minimal_payment || existingOffer.minimal_payment,
      maximal_payment: this.offer.maximal_payment || existingOffer.maximal_payment,
      number_of_interns: this.offer.number_of_interns || existingOffer.number_of_interns,
      skills: this.offer.skills || existingOffer.skills,
      binome: this.offer.binome || existingOffer.binome,
      domain: this.offer.domain || existingOffer.domain,
      role: this.offer.role || existingOffer.role,
      location: this.offer.location || existingOffer.location,
      offer_type: this.offer.offer_type || existingOffer.offer_type,
      duration: this.offer.duration || existingOffer.duration,
      education: this.offer.education || existingOffer.education,
      status: this.offer.status || existingOffer.status,
      expirationDate: this.offer.expirationDate || existingOffer.expirationDate
    };

    const response = await axios.put(
      `http://127.0.0.1:8000/api/entreprise/${this.entreprise.id}/update/${offerId}/`,
      requestData
    );

    this.showModal = false;
    console.log("Updated offer:", response.data);
    alert("Success, offer updated");
    // Instead of reloading the window, consider updating the offers data directly
    this.fetchOffersData();
  } catch (error) {
    console.error("Error updating offer:", error);
    console.log(offerId);
    this.showModal = false;
    let errorMessage =
      "An error occurred while updating offer. Please try again later.";
    if (error.response && error.response.data) {
      errorMessage = error.response.data.message || errorMessage;
    }
    alert(errorMessage);
  }
},
async deleteOffer(offerId) {
  if (!offerId) {
    console.error("Offer ID is null or undefined");
    return;
  }

  try {
    const response = await axios.delete(
      `http://127.0.0.1:8000/api/offer/delete/${offerId}/`
    );

    console.log("Deleted offer:", response.data);
    alert("Success, offer deleted");
    // Remove the deleted offer from the offers array
    this.offers = this.offers.filter(offer => offer.id !== offerId);
  } catch (error) {
    console.error("Error deleting offer:", error);
    alert("An error occurred while deleting offer. Please try again later.");
  }
},


      logout() {
            localStorage.removeItem('user_id');
            this.$router.push('/ConnexionView');
            console.log('Logout successful');
      },
      
    }
  };
  </script>
  <style scoped>
  .form-section-2{
    width:100%;
  }
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
  margin: 5% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 90%;
  max-width: 900px;
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
  .btn-grey-small{
    margin-bottom: 5px;
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
    height:85px;
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
    transform: translateY(18px);
  }
  /* Styles for the tab content */
  .tab-content {
    padding: 30px;
    border: 1px solid #dee2e6;
    border-top: none;
    border-right: none;
    background-color: #f2f4fa;
    border-radius: 9px;
    padding-top:50px;
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

  .card-grid-2:hover .btn-apply-now {
    background-color: #447AB8 !important;
    color: #E0E6F7 !important;
  }
  </style>
  