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
    <title>Configuration</title>
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
  <header class="header sticky-bar">
        <div class="container">
          <div class="main-header">
            <div class="header-left">
              <div class="header-logo"><a class='d-flex' href='index.html'><img alt="jobBox" src="template/assetss/imgs/logo/logo-blanc.png"></a></div>
            </div>
            <div class="header-nav">
              <nav class="nav-main-menu">
                <ul class="main-menu">
                  <li class="has-children"><router-link to="/">Accueil</router-link></li>
               <li class="has-children"><router-link to="/ContenuProtected">Trouver un candidat</router-link></li>
                  <li class="has-children"><router-link to="/ContenuProtected">Tableau de bord</router-link></li>
                  <li class="has-children"><router-link to="/ContenuProtected">Mes Offres</router-link></li>
                  <li class="has-children"><router-link to="/ContenuProtected">Mes Demandes</router-link></li>
                  <li class="has-children"><router-link to="/ContenuProtected">Aide & Support</router-link></li>
                </ul>
              </nav>
              <div class="burger-icon burger-icon-white"><span class="burger-icon-top"></span><span class="burger-icon-mid"></span><span class="burger-icon-bottom"></span></div>
            </div>
            
          </div>
        </div>
      </header>
      <div class=" header-2 sticky-bar2 d-flex">
      <div class="container2">
       
        <div class="right-bar">
          <div class="icon-container hover-up" style="cursor:pointer;display: flex;
    align-items: center;">
            <i class="bi bi-bell custom-icon"></i>
          </div> 
          <router-link  :to="'/chatView'" class="icon-container hover-up">
            <img style="width: 28px; fill: #447AB8;"  src="template/assetss/imgs/template/icons/envelope-arrow-up.svg">
          </router-link>
          <router-link to="/ContenuProtected"  class='btn btn-default btn-shadow  postbutt' style="margin-right: 20px;">Publier Offre</router-link>
          <div class="icon-container hover-up" style="cursor:pointer;">
    <img class="icon-fb" alt="profile-fb" :src="this.entrepriseUrl"  @click="toggleDropdown">
    <div class="dropdown-menu dropdown-menu-left" v-if="showDropdown" @click="toggleDropdown">
      <router-link to="/ContenuProtected" class="dropdown-item" ><img src="template/assetss/imgs/template/icons/person-circle.svg" alt="jobBox"><span>Profil</span></router-link>
        <router-link to="/ContenuProtected" class="dropdown-item" >
              <img src="../assets/imgs/template/icons/bookmark.svg" alt="jobBox" />
              <span>Favoris</span>
            </router-link>
        <router-link to="/ContenuProtected" class="dropdown-item" ><img src="template/assetss/imgs/template/icons/clock-history.svg" alt="jobBox"><span>Historique</span></router-link>
        <router-link to="/ContenuProtected" class="dropdown-item"  ><img src="template/assetss/imgs/template/icons/gear.svg" alt="jobBox"><span>Paramètres</span></router-link>
        <a class="dropdown-item" href="#" @click="logout"><img src="template/assetss/imgs/template/icons/box-arrow-right.svg" alt="jobBox"><span>Déconnexion</span></a>
    </div>
  </div>
        </div>
      </div>    
    </div>
  <main class="main-2 " style="margin-top: 0px;">
      
       
        <div class="form-section-2" style="background-color:#ffffff">
          <div class="wrapper">
   
        <div class="tab-box" ref="tabBox">
          <div class="tab" v-for="(tab, index) in tabs" :key="index" @click="selectTab(index)" :class="{ 'active': activeTab === index }">{{ tab }}</div>
        </div>

      </div>
        
      <div class="tab-content" v-show="activeTab === 0">
            <div class="box-heading-2">
            <div class="box-title-2"> 
              <h3 class="mb-35">Paramètres</h3>
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
                             <h5 style="margin-bottom: 20px;">Logo & Photo de Couverture</h5>
                            <div class="col-lg-6 col-md-3-2">
                              <div class="form-group mb-30"> 
                                <label class="font-lg color-text-mutted-2 mb-10">Logo</label>
                                <label style="text-align:center;" for="logoFileInput" class="drag-drop-area" @click="openFileInput">
                                            Cliquez ici pour choisir un logo.<br>
                                            Les formats supportés est PNG et JPG.<br> La taille maximum est 50 KB.<br>
                                            Dimensions recommendées  :  320 x 320 pixels.
                                          </label>
                                          <input type="file" accept=".png, .jpg,.jpeg"  id="logoFileInput" @change="handleLogoFileChange($event)" style="display: none;" />
                                          <p v-if="selectedFileName" class="selected-file-info">
  Fichier sélectionné : {{ selectedFileName }}
</p>

<!-- Display error message if file size exceeds 50 KB -->
<p v-if="fileSizeError" class="text-danger">
  La taille du fichier dépasse 50 KB.
</p>
                              </div>
                            </div>
                            <div class="col-lg-6 col-md-7-2">
                              <div class="form-group mb-30">
                                <label class="font-lg color-text-mutted-2 mb-10">Photo de couverture</label>
                                <label style="text-align:center;" for="coverPhotoFileInput" class="drag-drop-area" @click="openFileInput">
      Cliquez ici pour choisir une photo de couverture.<br>
      Les formats supportés est PNG et JPG. La taille maximum est 800 KB.<br>
                                            Dimensions recommendées  :  851 x 315 pixels.
    </label>
    <input type="file" id="coverPhotoFileInput" @change="handleCoverPhotoFileChange($event)" style="display: none;" />
    <p v-if="selectedFileName1" class="selected-file-info">
  Fichier sélectionné : {{ selectedFileName1 }}
</p>

<!-- Display error message if file size exceeds 50 KB -->
<p v-if="fileSizeError1" class="text-danger">
  La taille du fichier dépasse 800 KB.
</p>
      </div>
                              </div>
                          
                           
                            <div class="col-lg-122"> 
                              <div class="form-group-2 mb-30"> 
                                <label class="font-lg color-text-mutted-2 mb-10">A propos de nous*</label>
                                <textarea v-model="entreprise.description" name="description" @blur="validateDescription"  class="form-control-2"  rows="8"> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at sem id enim suscipit commodo nec in ante. Sed viverra vel leo vitae pharetra. Morbi viverra venenatis neque, eu porttitor diam blandit nec. Etiam et volutpat magna, id molestie quam. Vestibulum vel libero gravida, scelerisque arcu eu, maximus mi. Suspendisse eu dolor lobortis, posuere enim venenatis, posuere quam.
  
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at sem id enim suscipit commodo nec in ante. Sed viverra vel leo vitae pharetra. Morbi viverra venenatis neque, eu porttitor diam blandit nec. Etiam et volutpat magna, id molestie quam. Vestibulum vel libero gravida, scelerisque arcu eu, maximus mi. Suspendisse eu dolor lobortis, posuere enim venenatis, posuere quam.</textarea>
                              </div>
                              <div v-if="descriptionTouched && !isdescriptionFilled" class="text-danger">Veuillez remplir ce champ.</div>
                            </div>
                            <div class="col-lg-122"> 
                              <div class="form-group mt-10">
                                <button class="btn btn-default-2 btn-brand-2 " @click="moveToNextTab">Suivant</button>
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
                    <p class="font-lg color-text-paragraph-made-by">© 2024 - Made By SwConnect </p>
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
        <div class="tab-content" v-show="activeTab === 1">
          <div class="box-heading-2">
            <div class="box-title-2"> 
              <h3 class="mb-35">Paramètres</h3>
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
                            
                        
                    
                      <div class="col-lg-4 col-md-4">
                              <div class="form-group mb-30"> 
                                <label class="font-lg color-text-mutted-2 mb-10">Type de l'Organisation*</label>
                                <select v-model="entreprise.type_organisation" name="typeOrg" @blur="validateTypeOrg" class="form-control" type="text" placeholder="e.g. public, privé”">
                                  <option value="privée">Privée</option>
                                  <option value="privée">Public</option>

                                </select>
                                <div v-if="typeOrgTouched && !isTypeOrgFilled" class="text-danger">Veuillez remplir ce champ.</div>
                              </div>
                            </div>
                            <div class="col-lg-4 col-md-4">
                              <div class="form-group mb-30"> 
                                <label class="font-lg color-text-mutted-2 mb-10">Type de l'Industrie*</label>
                                <select v-model="entreprise.type_industrie" name="typeInd" @blur="validateTypeInd" class="form-control" type="text" placeholder="e.g. technologique, informatique">
                          
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
                                <div v-if="typeIndTouched && !isTypeIndFilled" class="text-danger">Veuillez remplir ce champ.</div>
                              </div>
                            </div>
                            <div class="col-lg-4 col-md-4">
                              <div class="form-group mb-30">
                                <label class="font-lg color-text-mutted-2 mb-10">Nombre de l'Equipe*</label>
                                <input v-model="entreprise.nombre_equipe" @blur="validateTeamInput" class="form-control-2" type="text" placeholder="e.g. 100" >
                               <div v-if="teamInputTouched && !isTeamInputFilled" class="text-danger">Veuillez remplir ce champ.</div>
                              </div>
                            </div>
                            
                            <div class="col-lg-6 col-md-6">
                              <div class="form-group mb-30"> 
                                <label class="font-lg color-text-mutted-2 mb-10">Date d'Etablissement*</label>
                                <input v-model="entreprise.date_etablissement" name="dateEtab" @blur="validateDateEtab" class="form-control" type="text" placeholder="e.g. dd/mm/aaaa">
                                <div v-if="dateEtabTouched && !isDateEtabFilled" class="text-danger">Veuillez remplir ce champ.</div>
                              </div>
                            </div>
                            <div class="col-lg-6 col-md-6">
                              <div class="form-group mb-30">
                                <label class="font-lg color-text-mutted-2 mb-10">Site Web</label>
                                <input v-model="entreprise.site_url" name="site" class="form-control" type="url" placeholder="e.g. dd/mm/aaaa">
                              </div>
                            </div>
                            
                            <div class="col-lg-122"> 
                              <div class="form-group-2 mb-30"> 
                                <label class="font-lg color-text-mutted-2 mb-10">Vision de l'entreprise</label>
                                <textarea v-model="entreprise.vision" name="vision"  class="form-control-2"  rows="8"> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at sem id enim suscipit commodo nec in ante. Sed viverra vel leo vitae pharetra. Morbi viverra venenatis neque, eu porttitor diam blandit nec. Etiam et volutpat magna, id molestie quam. Vestibulum vel libero gravida, scelerisque arcu eu, maximus mi. Suspendisse eu dolor lobortis, posuere enim venenatis, posuere quam.
  
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at sem id enim suscipit commodo nec in ante. Sed viverra vel leo vitae pharetra. Morbi viverra venenatis neque, eu porttitor diam blandit nec. Etiam et volutpat magna, id molestie quam. Vestibulum vel libero gravida, scelerisque arcu eu, maximus mi. Suspendisse eu dolor lobortis, posuere enim venenatis, posuere quam.</textarea>
                              </div>
                            </div>
                            <div class="col-lg-122"> 
                              <div class="form-group mt-10">
                                
                                <button class="btn btn-default-2 btn-brand-2 " @click="moveToNextTab">Suivant</button>
                                <button class="btn btn-default btn-brand btn-pre-1  " @click="moveToPreviousTab">Précédent</button>
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
                    <p class="font-lg color-text-paragraph-made-by">© 2024 - Made By SwConnect </p>
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
        
        <div class="tab-content" v-show="activeTab === 2">
          <div class="box-heading-2">
            <div class="box-title-2"> 
              <h3 class="mb-35">Paramètres</h3>
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
                            <div class="col-lg-122">
                              <label class="font-lg color-text-mutted-2 mb-10">Lien Social 1</label>
                              <div class="input-group mb-3">
              <div class="input-group-prepend">
                <img src="template/assetss/imgs/template/icons/facebook.svg">
                <div class=" btn-lien">Facebook</div>
              </div>
              <input v-model="entreprise.fb_lien" name="fbLien" type="url" class="form-control" aria-label="Text input with dropdown button">
            </div>
                                  </div>
                              
                                  <div class="col-lg-122">
                              <label class="font-lg color-text-mutted-2 mb-10">Lien Social 2</label>
                            <div class="input-group mb-3">
                                    <div class="input-group-prepend">
                                      <img src="template/assetss/imgs/template/icons/instagram.svg" class="custom-svg">
                                      <div class="btn-lien-1 " aria-haspopup="true" aria-expanded="false">Instagram</div>
                                    </div>
                                    <input v-model="entreprise.in_lien" name="inLien" type="url" class="form-control" aria-label="Text input with dropdown button">
                                  </div>
                                  </div>
                                  <div class="col-lg-122">
                              <label class="font-lg color-text-mutted-2 mb-10">Lien Social 4</label>
                            <div class="input-group mb-3">
                                    <div class="input-group-prepend">
                                      <img src="template/assetss/imgs/template/icons/linkedin.svg">
                                      <div class="btn-lien"  aria-haspopup="true" aria-expanded="false">Linkedin</div>
                                    </div>
                                    <input v-model="entreprise.link_lien" name="linkLien" type="url" class="form-control" aria-label="Text input with dropdown button">
                                  </div>
                                </div>
                            <div class="col-lg-122"> 
                              <div class="form-group mt-10">
                                
                                <button class="btn btn-default-2 btn-brand-2 " @click="moveToNextTab">Suivant</button>
                                <button class="btn btn-default btn-brand btn-pre-2 " @click="moveToPreviousTab">Précédent</button>
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
                    <p class="font-lg color-text-paragraph-made-by">© 2024 - Made By SwConnect </p>
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
        <div class="tab-content" v-show="activeTab === 3">
      
          <div class="box-heading-2">
            <div class="box-title-2"> 
              <h3 class="mb-35">Paramètres</h3>
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
                            <div class="col-lg-6 col-md-6">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Gouvernorat*</label
                              >
                              <select
                                class="form-control"
                                v-model="selectedGouvernorat"
                                name="selectedGouvernorat"
                                @change="updateVilles"
                                @blur="validateGouv"
                              >
                                <option value="">Select Gouvernorat</option>
                                <option
                                  v-for="(gouvernorat, index) in gouvernorats"
                                  :key="index"
                                  :value="gouvernorat"
                                >
                                  {{ gouvernorat }}
                                </option>
                              </select>
                              <div
                                v-if="gouvTouched && !isgouvFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ.
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-6 col-md-6">
                            <div class="form-group mb-30 mr-30">
                              <label class="font-lg color-text-mutted-2 mb-10"
                                >Ville*</label
                              >
                              <select
                                class="form-control"
                                v-model="selectedVille"
                                name="selectedVille"
                                @blur="validateVille"
                              >
                                <option
                                  v-for="(ville, index) in villes"
                                  :key="index"
                                  :value="ville"
                                >
                                  {{ ville }}
                                </option>
                              </select>
                              <div
                                v-if="villeTouched && !isVilleFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ.
                              </div>
                            </div>
                          </div>
                           
                            <h5 style="margin-bottom: 20px;">Responsable de stage</h5>
                            
                            <div class="col-lg-6 col-md-6">
                              <div class="form-group mb-30"> 
                                <label class="font-lg color-text-mutted-2 mb-10">Nom*</label>
                                <input v-model="entreprise.nom_rh" name="nomR" @blur="validateNomR" class="form-control" type="text" placeholder="e.g. Ben Salem">
                                <div v-if="nomRTouched && !isNomRFilled" class="text-danger">Veuillez remplir ce champ.</div>
                               
                              </div>
                            </div>
                            <div class="col-lg-6 col-md-6">
                              <div class="form-group mb-30">
                                <label class="font-lg color-text-mutted-2 mb-10">Prénom*</label>
                                <input v-model="entreprise.prenom_rh" name="prenom" @blur="validatePrenom" class="form-control" type="text" placeholder="e.g. Ahmed">
                                <div v-if="prenomTouched && !isPrenomFilled" class="text-danger">Veuillez remplir ce champ.</div>
                              </div>
                            </div>
                            <div class="col-lg-122">
                            <div class="form-group-2 mb-30">
                              <label class="font-lg color-text-mutted-2 mb-10">Téléphone*</label>
                              <div class="input-group input-group-lg">
                                <div class="input-group-prepend">
                                      <img class="custom-png"  src="template/assetss/imgs/template/icons/flag_tunisie.png">
                                      <div class="btn-lien " aria-haspopup="true" aria-expanded="true">+ 216</div>    
                                    </div>
                                      <input v-model="entreprise.telephone_rh" name="telephoneR" @blur="validateTelephoneR" type="text" class="form-control" aria-label="Default" aria-describedby="inputGroup-sizing-default">     
                                        </div>
                                        <div v-if="telephoneRTouched && !isTelephoneRFilled" class="text-danger">Veuillez remplir ce champ.</div> 
                                    </div>
                                    
                                  </div>
                    
                                  <div class="col-lg-122">
                              <label class="font-lg color-text-mutted-2 mb-10">Email*</label>
                            <div class="input-group mb-3">
                                    <div class="input-group-prepend">
                                      <img class="custom-svg"  src="template/assetss/imgs/template/icons/envelope-at.svg">
                                      <div class="btn-lien " aria-haspopup="true" aria-expanded="true">Email</div>    
                                    </div>
                                    <input v-model="entreprise.email_rh" name="emailR"  class="form-control" type="email" placeholder="e.g. ahmedbensalem@gmail.com" @blur="validateEmailR" :class="{ 'is-invalid': mailErrorR}" required>
                                    <div v-if="mailErrorR" class="invalid-feedback">Format email incorrect.</div>
                                  </div>
                                  </div>
                            <div class="col-lg-122"> 
                              <div class="form-group mt-10">
                                
                                <button class="btn btn-default-2 btn-brand-2 " @click="updateEntreprise">Enregistrer</button>
                                <button class="btn btn-default btn-brand " @click="moveToPreviousTab">Précédent</button>
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
                    <p class="font-lg color-text-paragraph-made-by">© 2024 - Made By SwConnect </p>
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
      <div v-if="showErrorMessage" class="modal">
    <div class="modal-content">
      <span class="close" @click="hideErrorMessage">&times;</span>
      <p>Veuillez remplir tous les champs obligatoire * pour créer un compte.</p>
    </div>
  </div>
    </body>
  </template>
  <script>
  import axios from "axios";
  export default {
    name: "EntConfig",
    data() {
      return {
        baseUrl: "http://localhost:8000",
        entreprise: 
        {
        nom_rh:'',
        prenom_rh:'',
        description:'',
        type_organisation:'',
        type_industrie:'',
        date_etablissement:'',
        site_url:'',
        vision:'',
        fb_lien:'',

        in_lien:'',
        link_lien:'',

        location:'',
        telephone:'',
        telephone_rh:'',
        email_rh:'',
        email:'',
        nombre_equipe:'',
        profile_cover:null,
        profile_logo:null,
        previousLogo: null,
      previousCover: null,
        },
        selectedVille: "",
      selectedGouvernorat: "",
      gouvernorats: ["Ariana","Béja","Ben_Arous","Bizerte","Gabés","Gafsa","Jendouba","Kairouan","Kasserine",
      "Kébili","Kef","Mahdia", "Manouba","Médenine","Monastir", "Nabeul", "Sfax","Sidi_Buzid","Siliana", "Sousse",
      "Tataouine","Tozeur","Tunis","Zeghouan"],
      villeByGouvernorat: {
        Zeghouan:["Bir Mchergua","El Fahs","El Zerbia","Zaghouan"],
        Tozeur:["Dagach","Hazoua","Nerfta","Tamaghza","Tozeur"],
        Tataouine:["Remada","Sammar","Tataouine Nord","Tataouine Sud"],
        Siliana:["Bou Rouis","El Aroussa","Gaafour","Siliana Nord","Siliana Sud"],
        Sidi_Bouzid:["Jelma","Sidi Bouzid Est","Sidi Bouzid Ouest","Souk Jedid"],
        Nabeul:["Bou Agroub","Grombalia","Hammamet","Menzel Bouzelfa"],
        Médenine:["Beni Khedech","Médenine Nord","Médenine Sud","Sidi Makhlouf"],
        Manouba:["Borj El Amri","Djedaida","El Battan","El Mournaguia"],
        Kef:["Kef Est","Kef Ouest","Nebeur","Sakiet Sidi Youssef","Tajerouine"],
        Kébili:["Douz Nord","Douz Sud","Faouar","Kebili Nord","Kébili Sud"],
        Kasserine:["Feriana","Kasserine Nord","Kasserine Sud","Sbeitla","Thala"],
        Kairouan:["Chébika","haffouz","Kairouan Nord","Kairouan Sud","Sbikha"],
        Jendouba:["Ain Drahem","Balta Bouawene","Fernana","Jendouba Nord","Tabarka"],
        Gafsa:["Gafsa Nord","Gafsa Sud","Metlaoui","Om El Araies","Redayef"],
        Gabés:["El Hamma","Gabés Ville","Matmata","Menzel El Habib","Nouvelle Matmata"],
        Bizerte:["Bizerte Nord","Bizerte Sud","El Alia","Mateur","Menzel Bourguiba"],
        Ben_Arous:["Ben Arous","El Mourouj","Hammam Chott","Medina Jedida"],
        Béja:["Amdoun","Beja Nord","Beja Sud","Mjaz El Bab","Nefza","Testour"],
        Mahdia: ["Boumerdes","Chebba","Chorbane","El Jem","Essouassi", "Ksour El Sef","Mahdia"],
        Monastir: ["Bouhjar","Bembia","Jammel", "Ksar Hlel","Moknine","Monastir","Sahline","Zeramdine"],
        Sousse: ["Akouda","Hammam Sousse","Hergla","Kalaa Kebira","Kalaa Sghira","Msaken","Sidi El Heni","Sousse Ville"],
        Tunis:["Carthage","El Bouhaira","El Manzah","La Marsa","Sabket Sijoumi","Sidi Hassine","Tunis"],
        Ariana:["Ariana ville","Cité Tadhamon","Kalaat Andalos","La Soukra","M'nihla","Raoued","Sidi Thabet"],
        Sfax:["Agareb","El Hencha","Menzel Chaker","Sfax ville"]
      },
        tabs: ['Infos Entreprise', 'Fondation', 'Réseaux sociaux', 'Contact' ],
        activeTab: 0,// Default to Tab 2
        //error messages and validators
        mailError: false,
        mailErrorR: false,
        nomTouched:false,
        isnomFilled:false,
        nomRTouched:false,
        isNomRFilled:false,
        prenomTouched:false,
        isPrenomFilled:false,
        descriptionTouched:false,
        isdescriptionFilled:false,
        typeOrgTouched:false,
        isTypeOrgFilled:false,
        typeIndTouched:false,
        isTypeIndFilled:false,
        teamInputTouched: false,
        isTeamInputFilled: false,
        dateEtabTouched: false,
        isDateEtabFilled:false,
        gouvTouched: false,
      isgouvFilled: false,
      villeTouched: false,
      isVilleFilled: false,
        telephoneTouched: false,
        isTelephoneFilled:false,
        telephoneRTouched:false,
        isTelephoneRFilled:false,
        usernameTouched: false,
        isUsernameFilled:false,
        //dropdownmenu
        showDropdown: false,
        selectedFileName: '', // Initialize selectedFileName data property to store the selected file name
      fileSizeError: false ,
      selectedFileName1: '',
      fileSizeError1: false ,
      showErrorMessage: false,
      
  

      };
    },
    created() {
    // Retrieve etudiant ID from localStorage
    this.entreprise.id = localStorage.getItem('user_id');
    console.log(this.entreprise.id);
    // Fetch etudiant data using the etudiant ID
    this.fetchEntrepriseData();
  },
  mounted() {
    // Call the method to set previousLogo and previousCover when the component is mounted
    this.setPreviousPhotos();
},
 

    methods: {
      setPreviousPhotos() {
        // Logic to retrieve previous logo and cover photo URLs or file data from your backend or wherever they are stored
        // For example:
        this.previousLogo = this.entreprise.profile_logo; // Accessing as this.previousLogo
        this.previousCover = this.entreprise.profile_cover;
    },
      async fetchEntrepriseData() {
      try {

        const response = await axios.get(`http://127.0.0.1:8000/api/entreprises/get/${this.entreprise.id}/`);
        // Populate the etudiant object with data from the response
        this.entreprise = response.data;
        this.setPreviousPhotos();
        if (this.entreprise.profile_logo) {
          this.entrepriseUrl = this.baseUrl + this.entreprise.profile_logo;
        }
      } catch (error) {
        console.error('Error fetching entreprise data:', error);
      }
    },
    async updateEntreprise() {
      try {
        if (!this.entreprise.description || !this.entreprise.type_organisation ||! this.entreprise.type_industrie || !this.entreprise.nombre_equipe || !this.entreprise.date_etablissement  ||
       !this.selectedGouvernorat  || !this.selectedVille || !this.entreprise.nom_rh || !this.entreprise.prenom_rh || !this.entreprise.telephone_rh || !this.entreprise.email_rh) {
            // Afficher le message d'erreur
            this.showErrorMessage = true;
        } else {
            this.showErrorMessage = false;
            const formData = new FormData();
            formData.append('id', this.entreprise.id);
            formData.append('nom_rh', this.entreprise.nom_rh);
            formData.append('prenom_rh', this.entreprise.prenom_rh);
            formData.append('telephone_rh', this.entreprise.telephone_rh);
            formData.append('email_rh', this.entreprise.email_rh);
            formData.append('description', this.entreprise.description);
       
            formData.append('type_organisation', this.entreprise.type_organisation);
            formData.append('type_industrie',this.entreprise.type_industrie);
            formData.append('date_etablissement',this.entreprise.date_etablissement);
            formData.append('vision',this.entreprise.vision);
           formData.append('location', this.selectedGouvernorat + "," + this.selectedVille);
            formData.append('nombre_equipe',this.entreprise.nombre_equipe);
            if (this.entreprise.fb_lien) {
    formData.append('fb_lien', this.entreprise.fb_lien);
} 
if (this.entreprise.site_url) {
    formData.append('site_url', this.entreprise.site_url);
}

if (this.entreprise.in_lien) {
    formData.append('in_lien', this.entreprise.in_lien);
} 

if (this.entreprise.link_lien) {
    formData.append('link_lien', this.entreprise.link_lien);
} 
    
        
            // Check if logo file exists
            if(this.entreprise.profile_logo instanceof File && this.entreprise.profile_logo !== this.entreprise.previousLogo) {
                formData.append('profile_logo', this.entreprise.profile_logo);
            }

            // Append profile_cover only if it's modified or new
            if (this.entreprise.profile_cover instanceof File &&
                this.entreprise.profile_cover !== this.entreprise.previousCover) {
                formData.append('profile_cover', this.entreprise.profile_cover);
            }

            // Convert skills to an Array if it's not already one
            const response = await axios.put(`http://127.0.0.1:8000/api/entreprises/update/${this.entreprise.id}/`, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            console.log('Updated entreprise:', response.data);
            alert('success');
            this.$router.push('/ConnexionView');
            alert("Merci d'attendre la vérification de votre compte pour se connecter ");
            localStorage.removeItem('user_id');
        }
    } catch (error) {
        console.error('Error updating entreprise:', error);
        let errorMessage = 'An error occurred while updating entreprise. Please try again later.';
        if (error.response && error.response.data) {
            errorMessage = error.response.data.message || errorMessage;
        }
        alert(errorMessage);
    }
    },
      logout() {
          localStorage.removeItem('user_id');
          this.$router.push('/ConnexionView');
          console.log('Logout successful');
    },
      toggleDropdown() {
      this.showDropdown = !this.showDropdown;
    },
      validateEmailR() {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      this.mailErrorR = !emailRegex.test(this.entreprise.email_rh);
      },
      validateGouv() {
      this.gouvTouched = true;
      if (this.selectedGouvernorat && this.selectedGouvernorat.trim() !== "") {
        this.isgouvFilled = true;
      } else {
        this.isgouvFilled = false;
      }
    },
    validateVille() {
      this.villeTouched = true;
      if (this.selectedVille && this.selectedVille.trim() !== "") {
        this.isVilleFilled = true;
      } else {
        this.isVilleFilled = false;
      }
    },
      

    validateTeamInput() {
    this.teamInputTouched = true;
    const equipePattern = /^\d+$/; 
    if (this.entreprise.nombre_equipe &&  equipePattern.test(this.entreprise.nombre_equipe.trim()) && Number.isInteger(Number(this.entreprise.nombre_equipe.trim()))) {
        this.isTeamInputFilled = true;
    } else {
        this.isTeamInputFilled = false;
    }
},
validateNomR(){
  this.nomRTouched = true;
    if (this.entreprise.nom_rh && this.entreprise.nom_rh.trim() !== '') {
        this.isNomRFilled = true;
    } else {
        this.isNomRFilled = false;
    }
},
validatePrenom(){
  this.prenomTouched = true;
    if (this.entreprise.prenom_rh && this.entreprise.prenom_rh.trim() !== '') {
        this.isPrenomFilled = true;
    } else {
        this.isPrenomFilled = false;
    }
},
validateDescription(){
  this.descriptionTouched = true;
    if (this.entreprise.description && this.entreprise.description.trim() !== '') {
        this.isdescriptionFilled = true;
    } else {
        this.isdescriptionFilled = false;
    }
},
validateTypeOrg(){
  this.typeOrgTouched = true;
    if (this.entreprise.type_organisation && this.entreprise.type_organisation.trim() !== '') {
        this.isTypeOrgFilled = true;
    } else {
        this.isTypeOrgFilled = false;
    }
},
validateTypeInd(){
  this.typeIndTouched = true;
    if (this.entreprise.type_industrie &&  this.entreprise.type_industrie.trim() !== '') {
        this.isTypeIndFilled = true;
    } else {
        this.isTypeIndFilled = false;
    }
},
validateDateEtab(){
  this.dateEtabTouched = true;
    if (this.entreprise.date_etablissement && this.entreprise.date_etablissement.trim() !== '') {
        this.isDateEtabFilled = true;
    } else {
        this.isDateEtabFilled = false;
    }
},
validateTelephoneR(){
  this.telephoneRTouched = true;
    if (this.entreprise.telephone_rh && this.entreprise.telephone_rh.trim() !== '') {
        this.isTelephoneRFilled = true;
    } else {
        this.isTelephoneRFilled = false;
    }
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
 
      handleLogoFileChange(event) {
    const file = event.target.files[0];
    if (file.size <= 800 * 1024) { // Check if file size is less than or equal to 50 KB
      this.entreprise.profile_logo = file;
        this.selectedFileName=file.name;
        this.fileSizeError = false;
    } else {
        // Handle error, such as showing a message to the user
        this.fileSizeError=true;
        // Optionally, clear the input field
        event.target.value = '';
    }
   
},
 handleCoverPhotoFileChange(event) {
    const file = event.target.files[0];
    if (file.size <= 800 * 1024) { // Check if file size is less than or equal to 50 KB
        this.entreprise.profile_cover = file;
        this.selectedFileName1=file.name;
    } else {
        // Handle error, such as showing a message to the user
        this.fileSizeError1=true;
        // Optionally, clear the input field
        event.target.value = '';
    }
  },

    openFileInput(event) {
      event.preventDefault(); // Prevent the default action of the label
      event.stopPropagation(); // Stop the event from propagating to the input element
      
      const inputId = event.currentTarget.getAttribute('for');
      const fileInput = document.getElementById(inputId);
      
      if (fileInput) {
        fileInput.click(); // Trigger click event on file input
      }
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
  hideErrorMessage() {
      // Masquer la fenêtre modale
      this.showErrorMessage = false;
    },
  
  },
    computed: {
      villes() {
        return this.villeByGouvernorat[this.selectedGouvernorat] || [];
      },
   
    }
  }
  </script>
  <style scoped>
.h5 p{
font-size: 22px;
font-family: "Plus Jakarta Sans", sans-serif;
}
.dropdown-menu a:hover span {
  color: #447AB8 !important;
}
.dropdown-menu a:hover img {
  filter: brightness(0) saturate(100%) invert(45%) sepia(30%) saturate(995%) hue-rotate(172deg) brightness(93%) contrast(87%);
}
.dropdown-menu a:hover {
  background-color: #E7F0FA !important;
  color: #447AB8 !important;
  border-left: 4px solid #447AB8;
}
  .dropdown-item{
    font-family: "Plus Jakarta Sans", sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 16px;
    line-height: 24px;
    color: #858585;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    height:40px;
  }
  .dropdown-item img{
    margin-right: 20px;
    width:25px;
  }
.dropdown-menu {
  display: block;
  left: auto !important;
  right: 0;
  min-width: 13rem;
}
  .icon-plus{
    padding:8px;
  }
  .modal {
  display: block; /* Afficher la fenêtre modale */
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Fond semi-transparent */
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
  .btn-modal{
    width:100%;
    height:49.5px;
    background-color:#F2F4FA;
    color: #313131;
    border: 1px solid #dee2e6;
    font-size:18px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
    .custom-svg {
    width: 47px; /* Adjust width as needed */
    fill: #447AB8; /* Fill color */
    margin-right:14px;
    margin-left:10px;
  }
  .custom-png{
    width:62px;
    height:35px;
    margin-right: 10px;
    margin-top: 5px;
  }
  .input-group-prepend{
    display: flex;
    border-top: #dee2e6 solid 1px;
    border-bottom: #dee2e6 solid 1px;
    border-left: #dee2e6 solid 1px;
  }
  .input-group-prepend img{
    padding-left:21px;
  } 
  .btn-lien{
      width: 145px;
      padding-left:0px;
      font-size: 18px;
      display: flex;
    align-items: center;
}
.btn-lien-1{
      width: 135px;
      padding-left:0px;
      font-size: 18px;
      display: flex;
    align-items: center;
}
.col-lg-1222{
    flex: 0 0 auto;
    width: 100%;
   }
      .col-lg-9 {
    flex: 0 0 auto;
    width: 100%;
   }
 .panel-white-2 {
    height:1000px;
  }
  .col-md-3-2{
      flex:0 0 auto;
      width:35%;
  }
.col-md-7-2{
          flex:0 0 auto;
          width:65%;
}
.btn-pre-1{
    margin-left:30px;
  
  } 
  .btn-pre-2{
    margin-left:30px;
  }  
  .drag-drop-area {
    background-color: #f0f0f0; /* Background color */
    border: 2px dashed #ccc; /* Border style */
    border-radius: 10px; /* Rounded corners */
    height:  200px; /* Height */
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
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
      height:84px;
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
      color: #447AB8  !important;
      font-family: "Plus Jakarta Sans", sans-serif;
    font-style: normal;
    font-weight: 700;
    font-size: 17px;
    border-bottom: #447AB8 solid 3px;
    transform: translateY(18px);
    }
    /* Styles for the tab content */
    .tab-content {
      padding: 30px;
    border: 1px solid #dee2e6;
    border-top: none;
    border-right: none;
    background-color: #F2F4FA;
    border-radius: 9px;
    padding-top: 50px ;
    }
    .tab-content.active {
      display: block;
    }
    /* Styles for the draggable tab */
    .icon {
      cursor: pointer;
      margin: 0 10px;
    }
  .form-control{
    height: 50px;
  }
  </style>