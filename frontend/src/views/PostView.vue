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
    <title>Publier offre</title>
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
    
    <link href="./template/assets/css/stylecd4ee.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  </head>
  <body>
<navbarEntreprise/>
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
              <router-link to="/PostView" class="active dashboard2" 
                ><img
                  src="../assets/imgs/template/icons/plus-circle.svg"
                  alt="jobBox"
                /><span class="name">Publier Un Offre</span></router-link
              >
            </li>
            <li>
              <router-link to="/MesOffres" class="dashboard2" 
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
      <div class="wrapper">
        <div class="icon">
          <i
            class="fas fa-angle-left"
            @click="scrollLeft"
            style="display: none"
          ></i>
        </div>
        <div class="tab-box" ref="tabBox">
          <div
            class="tab"
            v-for="(tab, index) in tabs"
            :key="index"
            @click="selectTab(index)"
            :class="{ active: activeTab === index }"
          >
            {{ tab }}
          </div>
        </div>
        <div class="icon">
          <i
            class="fas fa-angle-right"
            @click="scrollRight"
            style="display: none"
          ></i>
        </div>
      </div>
      <div class="tab-content" v-show="activeTab === 0">
        <div class="box-heading-2">
          <div class="box-title-2">
            <h3 class="mb-35">Publier Un Offre</h3>
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
                        <div class="row">
                          <div class="col-lg-12">
                            <div class="form-group-2 mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Compétences*    </label
                                                        ><p>  &nbsp; &nbsp; &nbsp; &nbsp; Ctrl+click à gauche pour sélectionner plus d'un choix </p>
                                                                                                          <select
                                                      v-model="competence"
                                                      name="competence"
                                                      @blur="validateCompetence"
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
    <option value="machine-learning">Machine learning</option>
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
                              <div
                                v-if="competenceTouched && !isCompetenceFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ.
                              </div>
                            
                            </div>
                          </div>
                          <div class="col-lg-6 col-md-6">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Titre*</label
                              >
                              <input
                                v-model="title"
                                name="title"
                                class="form-control-2"
                                type="text"
                                placeholder="e.g. Senior Product Designer"
                                @blur="validateTitre"
                              />
                              <div
                                v-if="titreTouched && !isTitreFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ.
                              </div>

                          
                            </div>
                          </div>
                          <div class="col-lg-6 col-md-6">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Role *</label
                              >
                              <select
                                class="form-control"
                                v-model="role"
                                name="role"
                                @blur="validateRole"
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
    <option value="Ingénieur en machine learning">Ingénieur en machine learning</option>
    <option value="Ingénieur en mécanique des fluides">Ingénieur en mécanique des fluides</option>
    <option value="Ingénieur en nanotechnologie">Ingénieur en nanotechnologie</option>
    <option value="Photographe">Photographe</option>
    <option value="Responsable des relations publiques">Responsable des relations publiques</option>
    <option value="Sculpteur">Sculpteur</option>
    <option value="Spécialiste en branding">Spécialiste en branding</option>
    <option value="Spécialiste en communication digitale">Spécialiste en communication digitale</option>
    <option value="Spécialiste en marketing de contenu">Spécialiste en marketing de contenu</option>
    <option value="Spécialiste en marketing stratégique">Spécialiste en marketing stratégique</option>
    <option value="Spécialiste en médias sociaux">Spécialiste en médias sociaux</option>
    <option value="Spécialiste en publicité en ligne">Spécialiste en publicité en ligne</option>
    <option value="Spécialiste en référencement">Spécialiste en référencement</option>
    <option value="Spécialiste en sécurité informatique">Spécialiste en sécurité informatique</option>
    <option value="Statisticien">Statisticien</option>
    <option value="Typographe">Typographe</option>
                              </select>
                              <div
                                v-if="roleTouched && !isRoleFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ.
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-12">
                            <div
                              class="form-check mb-30"
                              style="margin-left: 20px"
                            >
                              <input
                                class="form-check-input"
                                type="checkbox"
                                id="paiementCheckbox"
                                v-model="showSalary"
                              />
                              <h5
                                class="form-check-label"
                                for="paiementCheckbox"
                              >
                                Paiement
                              </h5>
                            </div>
                          </div>
                          <div class="col-lg-6 col-md-6" v-if="showSalary">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Paiement Minimal</label
                              >
                              <input
                                v-model="minPayment"
                                name="minPayment"
                                class="form-control"
                                type="text"
                                placeholder="e.g. 50000"
                                @blur="validateMin"
                              />
                              <div
                                v-if="minTouched && !isMinFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ.
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-6 col-md-6" v-if="showSalary">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Paiement Maximal</label
                              >
                              <input
                                v-model="maxPayment"
                                name="maxPayment"
                                class="form-control"
                                type="text"
                                placeholder="e.g. 100000"
                                @blur="validateMax"
                              />
                              <div
                                v-if="maxTouched && !isMaxFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ.
                              </div>
                            </div>
                          </div>
                          <h5 style="margin-bottom: 20px">
                            Informations Avancées
                          </h5>
                          <div class="col-lg-4 col-md-4">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Education *</label
                              >
                              <select
                                v-model="education"
                                name="education"
                                class="form-control"
                                @blur="validateEducation"
                              >
                                <option value="Bac+2">Bac+2</option>
                                <option value="Bac+3">Bac+3</option>
                                <option value="Bac+5">Bac+5</option>
                                <option value="Bac+6">Bac+6</option>
                              </select>
                              <div
                                v-if="educationTouched && !isEducationFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ.
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-4 col-md-4">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Domaine*</label
                              >
                              <select
                                v-model="domain"
                                name="domain"
                                class="form-control"
                                @blur="validateDomain"
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
                              <div
                                v-if="domainTouched && !isDomainFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ.
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-4 col-md-4">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Espace de travail *</label
                              >
                              <select
                                v-model="workspace"
                                name="workspace"
                                class="form-control"
                                @blur="validateWork"
                              >
                                <option value="Télétravail">Télétravail</option>
                                <option value="Bureau">Bureau</option>
                              </select>
                              <div
                                v-if="workTouched && !isWorkFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ.
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-6 col-md-6">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Nombre de stagiares*</label
                              >
                              <input
                                v-model="internCount"
                                name="internCount"
                                class="form-control"
                                type="text"
                                placeholder="e.g. 100”"
                                @blur="validateIntern"
                              />
                              <div
                                v-if="internTouched && !isInternFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ d'un nombre entier.
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-6 col-md-6">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Binome*</label
                              >
                              <select
                                v-model="binome"
                                name="binome"
                                class="form-control"
                                @blur="validateBinome"
                              >
                                <option value="Oui">Oui</option>
                                <option value="Non">Non</option>
                              </select>
                              <div
                                v-if="binomeTouched && !isBinomeFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ.
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-6 col-md-6">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Date d'expiration*</label
                              >
                              <input
                                v-model="expirationDate"
                                name="expirationDate"
                                class="form-control"
                                type="text"
                                placeholder="e.g. dd/mm/aaaa"
                                @blur="validateExpDate"
                              />
                              <div
                                v-if="dateExpTouched && !isExpDateFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ.
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-6 col-md-6">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Durée*</label
                              >
                              <select
                                v-model="duration"
                                name="duration"
                                class="form-control"
                                @blur="validateDuration"
                              >
                                <option value="1 mois">1 mois</option>
                                <option value="3 mois">3 mois</option>
                                <option value="4 mois">4 mois</option>
                                <option value="6 mois">6 mois</option>
                              </select>
                              <div
                                v-if="durationTouched && !isDurationFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ.
                              </div>
                            </div>
                          </div>
                          <h5 style="margin-bottom: 20px">Location</h5>
                          <div class="col-lg-122">
                              <div class="input-group mb-3"> 
                                <label class="font-lg color-text-mutted-2 mb-10">Location Map*</label>
                                <input v-model="location" name="location" @blur="validateLocation"  class="form-control-2" type="text" placeholder="e.g. Tunis">
                                <div v-if="locationTouched && !isLocationFilled" class="text-danger">Veuillez remplir ce champ.</div>
                              </div>
                            </div>
                
                          <div class="col-lg-12">
                            <div class="form-group-2 mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Description*</label
                              >
                              <textarea
                                v-model="description"
                                name="description"
                                @blur="validateDescription"
                                class="form-control-2"
                                rows="8"
                              >
 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at sem id enim suscipit commodo nec in ante. Sed viverra vel leo vitae pharetra. Morbi viverra venenatis neque, eu porttitor diam blandit nec. Etiam et volutpat magna, id molestie quam. Vestibulum vel libero gravida, scelerisque arcu eu, maximus mi. Suspendisse eu dolor lobortis, posuere enim venenatis, posuere quam.
  
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at sem id enim suscipit commodo nec in ante. Sed viverra vel leo vitae pharetra. Morbi viverra venenatis neque, eu porttitor diam blandit nec. Etiam et volutpat magna, id molestie quam. Vestibulum vel libero gravida, scelerisque arcu eu, maximus mi. Suspendisse eu dolor lobortis, posuere enim venenatis, posuere quam.</textarea
                              >
                            </div>
                            <div
                              v-if="descriptionTouched && !isdescriptionFilled"
                              class="text-danger"
                            >
                              Veuillez remplir ce champ.
                            </div>
                          </div>
                          <div class="col-lg-4 col-md-4">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Status*</label
                              >
                              <select
                                v-model="status"
                                name="status"
                                @blur="validateStatus"
                                class="form-control"
                              >
                                <option value="Soon">Soon</option>
                                <option value="En cours de recrutement">
                                  En cours de recrutement
                                </option>
                                <option value="Expirée">Expirée</option>
                              </select>
                              <div
                                v-if="statusTouched && !isStatusFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ.
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-12">
                            <div class="form-group mt-10">
                              <button
                                class="btn btn-default-2 btn-brand-2"
                                type="submit"
                                @click="creerOffre"
                              >
                                Publier Offre
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
                    <li><a href="#">Contact</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="tab-content" v-show="activeTab === 1" style="width: 1126px">
        <div class="box-heading-2">
          <div class="box-title-2">
            <h3 class="mb-35">Publier un pfe book</h3>
          </div>
        </div>
        <div class="row-2">
          <div class="col-lg-1222">
            <div class="section-box-2">
              <div class="container-22">
                <div class="panel-white-2 mb-30 mr-30">
                  <div class="box-padding-2 bg-postjob-2">
                    <div class="row mt-30">
                      <div class="col-lg-9">
                        <div class="row">
                          <div class="col-md-100">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Pfe book</label
                              >
                              <label
                                for="FileInput"
                                class="drag-drop-area"
                                @click="openFileInput"
                              >
                                Cliquez ici pour choisir un pfe book.<br />
                                Le format supporté est PDF. La taille maximum
                                est 10 MB.
                              </label>
                              <input
                                type="file"
                                id="FileInput"
                                accept=".pdf"
                                @change="handleFiles($event.target.files)"
                                style="display: none"
                              />
                              <p
                                v-if="selectedFileName"
                                class="selected-file-info"
                              >
                                Fichier sélectionné : {{ selectedFileName }}
                              </p>

                              <p v-if="fileSizeError" class="text-danger">
                                La taille du fichier dépasse 10 MB.
                              </p>
                            </div>
                          </div>
                          <div class="col-lg-12">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Titre*</label
                              >
                              <input
                                v-model="titre"
                                name="titre"
                                class="form-control-2"
                                type="text"
                                placeholder="e.g. Pfe Book Telecom Developpement"
                                @blur="validateTitreBook"
                              />
                              <div
                                v-if="titreBookTouched && !isTitreBookFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ.
                              </div>

                          
                            </div>
                          </div>
                          <div class="col-lg-122" style="margin-top: 41px;">
                            <div class="form-group mt-10">
                              <button
                              type="submit"
                                class="btn btn-default-2 btn-brand-2"
                                @click="uploadPfeBook"
                              >
                                Publier pfe book
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
  
</body>
   <!-- Fenêtre modale pour afficher le message d'erreur -->
   <div v-if="showErrorMessage" class="modal">
      <div class="modal-content">
        <span class="close" @click="hideErrorMessage">&times;</span>
        <p>Veuillez remplir tous les champs obligatoires *  pour publier un offre.</p>
      </div>
    </div>
</template>
<script>
import axios from "axios";
import navbarEntreprise from '@/components/navbarEntreprise.vue';
export default {
  name: "PostView",
  components:{navbarEntreprise},
  data() {
    return {
      baseUrl: "http://localhost:8000",
      entrepriseUrl:null,
      entreprise:{},
      competence: [],

      selectedFileName: "",
      file: null,
      showSalary: false,
    location:"",
      title: "",
      role: "",
      minPayment: null,
      maxPayment: null,
      domain: "",
      workspace: "",
      internCount: null,
      binome: "",
      expirationDate: "",
      duration: "",
      description: "",
      status: "",
      education: "",
      titre: "",
      
      tabs: ["Publier un offre", "Publier un pfe book"],
      activeTab: 0, // Default to Tab 2
      //error messages and validators
      descriptionTouched: false,
      isdescriptionFilled: false,
      educationTouched: false,
      isEducationFilled: false,
      competenceTouched: false,
      isCompetenceFilled: false,
      minTouched: false,
      isMinFilled: false,
      maxTouched: false,
      isMaxFilled: false,
      roleTouched: false,
      isRoleFilled: false,
      titreTouched: false,
      isTitreFilled: false,
      workTouched: false,
      isWorkFilled: false,
      domainTouched: false,
      isDomainFilled: false,
      internTouched: false,
      isInternFilled: false,
      binomeTouched: false,
      isBinomeFilled: false,
      durationTouched: false,
      isDurationFilled: false,
      dateExpTouched: false,
      isExpDateFilled: false,
    
      locationTouched:false,
      isLocationFilled:false,
      statusTouched: false,
      isStatusFilled: false,
      titreBookTouched:false,
      isTitreBookFilled:false,
      showErrorMessage: false,
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
},
  mounted() {
    const paiementCheckbox = document.getElementById("paiementCheckbox");
    if (paiementCheckbox) {
      paiementCheckbox.addEventListener("change", this.toggleSalaryInputGroup);
    } else {
      console.error("Checkbox element not found.");
    }
    },

  methods: {
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

    creerOffre() {
      //const competenceArray = [...this.competence];
  //console.log("Selected competence:", competenceArray);
  

      if (!this.title || !this.role || !this.competence  || !this.education || !this.domain || !this.workspace ||
        !this.binome || !this.internCount || !this.description || !this.duration || !this.status || !this.expirationDate ) {
          this.showErrorMessage = true;

        } else {
          this.showErrorMessage = false;
          const userId = localStorage.getItem("user_id");
 
          if(this.minPayment == null ){
            this.minPayment = 0;
          }
          if(this.maxPayment == null ){
            this.maxPayment = 0;
          }
         
      const offerData = {
        title: this.title,
        description: this.description,
        role: this.role,
        minimal_payment: this.minPayment,
        maximal_payment: this.maxPayment,
        number_of_interns: this.internCount,
        competence: this.competence, 
        binome: this.binome,
        domain: this.domain,
       location:this.location,
        duration: this.duration,
        education: this.education,
        status: this.status,
        expirationDate: this.expirationDate,
        offer_type: this.workspace,
         // Append each skill individually
       
      };
      
      console.log("offerData before sending:", offerData);
      axios
      .post(
          `http://127.0.0.1:8000/api/entreprise/${userId}/offers/`,
          offerData
        )
        .then((response) => {
          // Handle success response
          console.log("Offer created successfully:", response.data);
          alert('Offer created successfully');
          this.ajouterAction('Un offre a été publié');

        })
        .catch((error) => {
          // Handle error response
          
          console.error("Error creating offer:", error);
          alert('Error creating offer');
        });
    }
  },
  hideErrorMessage() {
        this.showErrorMessage = false;
      },
    uploadPfeBook() {
      
      const userId = localStorage.getItem("user_id");
  
      if (!this.file ||   !this.selectedFileName || !this.titre) {
        alert('File or filename not selected');
        return;
   
      }
  

      const formData = new FormData();

  formData.append('pfe_book', this.file);
  formData.append('titre',this.titre);

  

      axios.post(`http://127.0.0.1:8000/api/entreprise/${userId}/pfebook/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then(response => {
        // Handle success
        console.log('File uploaded successfully:', response.data);
         alert('File uploaded successfully');
         this.ajouterAction('Un PFE book a été publié');

      })
      .catch(error => {
        console.error('Error uploading file:', error);
        alert('Error uploading file, you already have pfe book',this.file);
      });
    },
    logout() {
          localStorage.removeItem('user_id');
          this.$router.push('/ConnexionView');
          console.log('Logout successful');
    },
    handleFiles(files) {
      // Check if any file is selected
      if (files.length > 0) {
        // Check if file size exceeds 10 MB (10 * 1024 * 1024 bytes)
        if (files[0].size > 10 * 1024 * 1024) {
          this.fileSizeError = true; // Set fileSizeError to true if file size exceeds 10 MB
          this.selectedFileName = ""; // Clear selectedFileName
        } else {
          this.file = files[0];
          this.fileSizeError = false; // Reset fileSizeError
          this.selectedFileName = files[0].name; // Set selectedFileName to the name of the selected file
        }
      } else {
        // No file selected, reset selectedFileName and fileSizeError
        this.selectedFileName = "";
        this.fileSizeError = false;
      }

      for (let i = 0; i < files.length; i++) {
        // Your code to handle the uploaded file goes here
        console.log("Uploaded file:", files[i]);
      }
    },
    openFileInput(event) {
      event.preventDefault(); // Prevent the default action of the label
      event.stopPropagation(); // Stop the event from propagating to the input element

      const inputId = event.currentTarget.getAttribute("for");
      const fileInput = document.getElementById(inputId);

      if (fileInput) {
        fileInput.click(); // Trigger click event on file input
      }
    },
    validateLocation() {
    this.locationTouched = true;
    if (this.location && this.location.trim() !== '') {
        this.isLocationFilled = true;
    } else {
        this.isLocationFilled = false;
    }
},
    validateTitreBook(){
      this.titreBookTouched = true;
      if(this.titre && this.titre.trim()!==""){
        this.isTitreBookFilled=true;
      }else{
        this.isTitreBookFilled=false;
      }
    },
    validateStatus() {
      this.statusTouched = true;
      if (this.status && this.status.trim() !== "") {
        this.isStatusFilled = true;
      } else {
        this.isStatusFilled = false;
      }
    },
    validateWork() {
      this.workTouched = true;
      if (this.workspace && this.workspace.trim() !== "") {
        this.isWorkFilled = true;
      } else {
        this.isWorkFilled = false;
      }
    },
    validateIntern() {
  this.internTouched = true;
  const internPattern = /^\d+$/; // Regular expression to check if the value is a whole number

  if (this.internCount && internPattern.test(this.internCount.trim()) && Number.isInteger(Number(this.internCount.trim()))) {
    this.isInternFilled = true;
  } else {
    this.isInternFilled = false;
  }
},
    validateBinome() {
      this.binomeTouched = true;
      if (this.binome && this.binome.trim() !== "") {
        this.isBinomeFilled = true;
      } else {
        this.isBinomeFilled = false;
      }
    },
    validateExpDate() {
      this.dateExpTouched = true;
      if (this.expirationDate && this.expirationDate.trim() !== "") {
        this.isExpDateFilled = true;
      } else {
        this.isExpDateFilled = false;
      }
    },
    validateDuration() {
      this.durationTouched = true;
      if (this.duration && this.duration.trim() !== "") {
        this.isDurationFilled = true;
      } else {
        this.isDurationFilled = false;
      }
    },
    validateDomain() {
      this.domainTouched = true;
      if (this.domain && this.domain.trim() !== "") {
        this.isDomainFilled = true;
      } else {
        this.isDomainFilled = false;
      }
    },
    validateEducation() {
      this.educationTouched = true;
      if (this.education && this.education.trim() !== "") {
        this.isEducationFilled = true;
      } else {
        this.isEducationFilled = false;
      }
    },
    validateMin() {
      this.minTouched = true;
      if (this.minPayment && this.minPayment.trim() !== "") {
        this.isMinFilled = true;
      } else {
        this.isMinFilled = false;
      }
    },
    validateMax() {
      this.maxTouched = true;
      if (this.maxPayment && this.maxPayment.trim() !== "") {
        this.isMaxFilled = true;
      } else {
        this.isMaxFilled = false;
      }
    },
    validateRole() {
      this.roleTouched = true;
      if (this.role && this.role.trim() !== "") {
        this.isRoleFilled = true;
      } else {
        this.isRoleFilled = false;
      }
    },
    validateTitre() {
      this.titreTouched = true;
      if (this.title && this.title.trim() !== "") {
        this.isTitreFilled = true;
      } else {
        this.isTitreFilled = false;
      }
    },
    validateCompetence() {
      this.competenceTouched = true;
      this.isCompetenceFilled = this.competence.length > 0;
    },
    validateDescription() {
      this.descriptionTouched = true;
      if (this.description && this.description.trim() !== "") {
        this.isdescriptionFilled = true;
      } else {
        this.isdescriptionFilled = false;
      }
    },
    toggleSalaryInputGroup(event) {
      this.showSalary = event.target.checked;
    },
    toggleDropdown() {
      
      this.showDropdown = !this.showDropdown;
    },
    selectTab(index) {
      this.activeTab = index;
    },
    scrollLeft() {
      this.$refs.tabBox.scrollLeft -= 100;
    },
    scrollRight() {
      this.$refs.tabBox.scrollLeft += 100;
    },
    updateVilles() {
      this.selectedVille = ""; // Reset selected ville
    },
    moveToNextTab() {
      if (this.activeTab < this.tabs.length - 1) {
        this.activeTab++; // Increment the activeTab index to move to the next tab
        this.scrollToActiveTab(); // Optionally scroll to the active tab if needed
      }
    },
    // Method to move to the previous tab
    moveToPreviousTab() {
      if (this.activeTab > 0) {
        this.activeTab--; // Decrement the activeTab index to move to the previous tab
        this.scrollToActiveTab(); // Optionally scroll to the active tab if needed
      }
    },
    // Method to scroll to the active tab
    scrollToActiveTab() {
      // Logic to scroll to the active tab if needed
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
};
</script>
<style scoped>
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
.col-lg-1222 {
  flex: 0 0 auto;
  width: 100%;
}
.col-lg-9 {
  flex: 0 0 auto;
  width: 100%;
}
.panel-white-2 {
  height: 1490px;
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
</style>
