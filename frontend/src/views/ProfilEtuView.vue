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
    <title>Paramètres</title>
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
 <navbarEtudiant/>
  <main class="main-2 " style="margin-top: 0px;">
        <div class="nav-2" style="border-right:1px solid #dee2e6;">
                <nav class="nav-main-menu-2">
          <ul class="main-menu-2">
            <li>
              <router-link :to="'/EtudOverview/' + this.etudiant.id" 
                ><img
                  src="../assets/imgs/template/icons/stack.svg"
                  alt="jobBox"
                /><span class="name">Overview</span></router-link
              >
            </li>
            <li>
              <router-link :to="'/GenerationPortfolio/' + this.etudiant.id" class=" dashboard2" exact
                ><img
                  src="../assets/imgs/template/icons/file-person.svg"
                  alt="jobBox"
                /><span class="name">Générer Portfolio</span></router-link>
              
            </li>
           
            <li>
              <router-link to="/Demandes"
                ><img
                  src="../assets/imgs/template/icons/briefcase2.svg"
                  alt="jobBox"
                /><span class="name">Mes Demades</span></router-link>
            </li>
            <li>
              <router-link :to="'/EtudDrive/' + this.etudiant.id"
                ><img
                  src="../assets/imgs/template/icons/folder.svg"
                  alt="jobBox"
                /><span class="name">Mon Drive</span></router-link>
              
            </li>
          </ul>
        </nav>
          <div class="border-bottom mb-20 mt-20"></div>
        </div>
   
       
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
                    
                            <div class="col-lg-6 col-md-3-2">
                              <div class="form-group mb-30"> 
                                <label class="font-lg color-text-mutted-2 mb-10">Photo de profil</label>
                                <label style="text-align:center;"  for="logoFileInput" class="drag-drop-area" @click="openFileInput">
                                            Cliquez ici pour choisir une photo de profil .<br>
                                            Les formats supportés est PNG et JPG.<br> La taille maximum est 300 KB.<br>
                                            Dimensions recommendées  :  320 x 320 pixels.
                                          </label>
                                          <input type="file" accept=".png, .jpg"  id="logoFileInput" @change="handleFiles($event.target.files)" style="display: none;" />
                                          <p v-if="selectedFileName" class="selected-file-info">
                                                Fichier sélectionné : {{ selectedFileName }}
                                              </p>

                                              <p v-if="fileSizeError" class="text-danger">
                                                La taille du fichier dépasse 300 KB.
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
    <input type="file" id="coverPhotoFileInput" accept=".png, .jpg"  @change="handleCoverPhotoFileChange($event.target.files)" style="display: none;" />
    <p v-if="selectedFileName3" class="selected-file-info">
  Fichier sélectionné : {{ selectedFileName3}}
</p>

<!-- Display error message if file size exceeds 50 KB -->
<p v-if="fileSizeError3" class="text-danger">
  La taille du fichier dépasse 50 KB.
</p>
      </div>
                              </div>
                          

                  

                            <div class="col-lg-122">
                              <div class="form-group-2 mb-30"> 
                                <label class="font-lg color-text-mutted-2 mb-10">Username</label>
                                <input v-model="etudiant.username" name="username" class="form-control-2" type="text" placeholder="e.g. SW Consulting">
                                <div v-if="usernameTouched && !isUsernameFilled" class="text-danger">Veuillez remplir ce champ.</div>
                                
                              </div>
                            </div>
                            
                            <div class="col-lg-6 col-md-6">
                              <div class="form-group-2 mb-30"> 
                                <label class="font-lg color-text-mutted-2 mb-10">Nom</label>
                                <input v-model="etudiant.first_name" name="nom"   class="form-control-2" type="text" placeholder="e.g. SW Consulting">
                                <div v-if="nomTouched && !isnomFilled" class="text-danger">Veuillez remplir ce champ.</div>
                                
                              </div>
                            </div>
                            <div class="col-lg-6 col-md-6">
                              <div class="form-group mb-30">
                                <label class="font-lg color-text-mutted-2 mb-10">Prénom</label>
                                <input v-model="etudiant.last_name" name="prenom" class="form-control" type="text" placeholder="e.g. Ahmed">
                                <div v-if="prenomTouched && !isPrenomFilled" class="text-danger">Veuillez remplir ce champ.</div>
                              </div>
                            </div>
                            <div class="col-lg-122 " style="margin-bottom:20px; margin-top: 10px;">
        
        <a class="link" @click="openModal" >changer mot de passe</a>

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
                            <h5 style="margin-bottom: 20px;">Cv & Certificats</h5>
                            <div class="col-lg-6 col-md-3-2">
                              <div class="form-group mb-30"> 
                                <label class="font-lg color-text-mutted-2 mb-10">CV</label>
                                <label style="text-align:center;" for="cvFileInput" class="drag-drop-area" @click="openFileInput">
                                            Cliquez ici pour choisir un CV.<br>
                                            Le format supporté est PDF.<br>
                                            La taille du fichierne doit pas dépasser 200 KB.
                                          </label>
                                          <input accept=".pdf" type="file" id="cvFileInput" @change="handleFiles1($event.target.files)" style="display: none;" />
                                          <p v-if="selectedFileName1" class="selected-file-info">
                                                Fichier sélectionné : {{ selectedFileName1 }}
                                              </p>

                                              <p v-if="fileSizeError1" class="text-danger">
                                                La taille du fichier dépasse 200 KB.
                                              </p>
                              </div>
                            </div>
                            <div class="col-lg-6 col-md-7-2">
                              <div class="form-group mb-30">
                                <label class="font-lg color-text-mutted-2 mb-10">Certificats & Attestations</label>
                                <label for="certifFileInput" class="drag-drop-area" @click="openFileInput">
                              Cliquez ici pour choisir des documents.<br>
                              Le format supporté est PDF. La taille maximum est 5 MB.
                            </label>
                            <input accept=".pdf" type="file" id="certifFileInput" @change="handleFiles2($event.target.files)" style="display: none;" />
                            <p v-if="selectedFileName2" class="selected-file-info">
                                                Fichier sélectionné : {{ selectedFileName2 }}
                                              </p>

                                              <p v-if="fileSizeError2" class="text-danger">
                                                La taille du fichier dépasse 5 MB.
                                              </p>
                              </div>
                      </div>
                      <div class="col-lg-4 col-md-4">
                              <div class="form-group mb-30"> 
                                <label class="font-lg color-text-mutted-2 mb-10">Date de naissance</label>
                                <input v-model="etudiant.date_naissance" name="dateNaissance"  class="form-control" type="text" placeholder="e.g. dd/mm/aaaa">
                                <div v-if="dateNaisTouched && !isDateNaisFilled" class="text-danger">Veuillez remplir ce champ.</div>
                              </div>
                            </div>
                            <div class="col-lg-4 col-md-4">
                              <div class="form-group mb-30"> 
                                <label class="font-lg color-text-mutted-2 mb-10">Sexe</label>
                                <select v-model="etudiant.sexe" name="sexe"  class="form-control" type="text" >
                                  <option value="Homme">Homme</option>
                                  <option value="Femme">Femme</option>
                                </select>
                                <div v-if="sexeTouched && !isSexeFilled" class="text-danger">Veuillez remplir ce champ.</div>
                              </div>
                            </div>
                            <div class="col-lg-4 col-md-4">
                              <div class="form-group mb-30">
                                <label class="font-lg color-text-mutted-2 mb-10">Education</label>
                                <select v-model="etudiant.education" name="education"  class="form-control" type="text" placeholder="e.g. 100" >
                                  <option value="Bac+2">Bac+2</option>
                                <option value="Bac+3">Bac+3</option>
                                <option value="Bac+5">Bac+5</option>
                                <option value="Bac+6">Bac+6</option>
                                </select>
                               <div v-if="educationTouched && !isEducationFilled" class="text-danger">Veuillez remplir ce champ.</div>
                              </div>
                            </div>
                            <div class="col-lg-6 col-md-6">
                              <div class="form-group mb-30">
                                <label class="font-lg color-text-mutted-2 mb-10">Role</label>
                                <select v-model="etudiant.role" name="role"  class="form-control" type="text" placeholder="Design UX/UI" >
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
                               <div v-if=" roleTouched && !isRoleFilled" class="text-danger">Veuillez remplir ce champ.</div>
                              </div>
                            </div>
                            <div class="col-lg-6 col-md-6">
                              <div class="form-group mb-30">
                                <label class="font-lg color-text-mutted-2 mb-10">Domaine</label>
                                <select
                                v-model="etudiant.domain"
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
                              <div
                                v-if="domainTouched && !isDomainFilled"
                                class="text-danger"
                              >
                                Veuillez remplir ce champ.
                              </div>
                            </div>
                          </div>
                            <div class="col-lg-122">
                              <div class="form-group mb-30"> 
                                <label class="font-lg color-text-mutted-2 mb-10">Compétences</label><p>  &nbsp; &nbsp; &nbsp; &nbsp; Ctrl+click à gauche pour sélectionner plus d'un choix </p>
                                <select
                                                      v-model="etudiant.skills"
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
                                <div v-if="competenceTouched && !isCompetenceFilled" class="text-danger">Veuillez remplir ce champ.</div>
                              </div>
                            </div>
                            <div class="col-lg-122"> 
                              <div class="form-group-2 mb-30"> 
                                <label class="font-lg color-text-mutted-2 mb-10">Biographie</label>
                                <textarea v-model="etudiant.bio" name="bio" class="form-control-2"  rows="8"> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at sem id enim suscipit commodo nec in ante. Sed viverra vel leo vitae pharetra. Morbi viverra venenatis neque, eu porttitor diam blandit nec. Etiam et volutpat magna, id molestie quam. Vestibulum vel libero gravida, scelerisque arcu eu, maximus mi. Suspendisse eu dolor lobortis, posuere enim venenatis, posuere quam.
  
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at sem id enim suscipit commodo nec in ante. Sed viverra vel leo vitae pharetra. Morbi viverra venenatis neque, eu porttitor diam blandit nec. Etiam et volutpat magna, id molestie quam. Vestibulum vel libero gravida, scelerisque arcu eu, maximus mi. Suspendisse eu dolor lobortis, posuere enim venenatis, posuere quam.</textarea>
                              </div>
                              <div v-if="bioTouched && !isBioFilled" class="text-danger">Veuillez remplir ce champ.</div>
                            </div>
                            <div class="col-lg-122"> 
                              <div class="form-group-2 mb-30"> 
                                <label class="font-lg color-text-mutted-2 mb-10">Lettre de motivation</label>
                                <textarea v-model="etudiant.lettre_motivation" name="lettre"  class="form-control-2"  rows="8"> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at sem id enim suscipit commodo nec in ante. Sed viverra vel leo vitae pharetra. Morbi viverra venenatis neque, eu porttitor diam blandit nec. Etiam et volutpat magna, id molestie quam. Vestibulum vel libero gravida, scelerisque arcu eu, maximus mi. Suspendisse eu dolor lobortis, posuere enim venenatis, posuere quam.
  
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
              <input v-model="etudiant.fb_lien" name="fbLien" type="url" class="form-control" aria-label="Text input with dropdown button">
            </div>
                                  </div>
                              
                                  <div class="col-lg-122">
                              <label class="font-lg color-text-mutted-2 mb-10">Lien Social 2</label>
                            <div class="input-group mb-3">
                                    <div class="input-group-prepend">
                                      <img src="template/assetss/imgs/template/icons/instagram.svg" class="custom-svg">
                                      <div class="btn-lien-1 " aria-haspopup="true" aria-expanded="false">Instagram</div>
                                    </div>
                                    <input v-model="etudiant.in_lien" name="inLien" type="url" class="form-control" aria-label="Text input with dropdown button">
                                  </div>
                                  </div>
                                  <div class="col-lg-122">
                              <label class="font-lg color-text-mutted-2 mb-10">Lien Social 3</label>
                            <div class="input-group mb-3">
                                    <div class="input-group-prepend">
                                      <img src="template/assetss/imgs/template/icons/linkedin.svg">
                                      <div class="btn-lien"  aria-haspopup="true" aria-expanded="false">Linkedin</div>
                                    </div>
                                    <input v-model="etudiant.link_lien" name="linkLien" type="url" class="form-control" aria-label="Text input with dropdown button">
                                  </div>
                                </div>
                            
                                  <div class="col-lg-122">
                              <label class="font-lg color-text-mutted-2 mb-10">Lien Social 4</label>
                            <div class="input-group mb-3">
                                    <div class="input-group-prepend">
                                      <img class="custom-svg"  src="template/assetss/imgs/template/icons/github.svg">
                                      <div class="btn-lien " aria-haspopup="true" aria-expanded="true">Github</div>    
                                    </div>
                                    <input v-model="etudiant.git_lien" name="gitLien" type="url" class="form-control" aria-label="Text input with dropdown button">
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
                            <div class="col-lg-122">
                              <div class="input-group mb-3"> 
                                <label class="font-lg color-text-mutted-2 mb-10">Location Map</label>
                                <input v-model="etudiant.location" name="location"   class="form-control-2" type="text" placeholder="e.g. Tunis">
                                <div v-if="locationTouched && !isLocationFilled" class="text-danger">Veuillez remplir ce champ.</div>
                              </div>
                            </div>
                            <div class="col-lg-122">
                            <div class="form-group-2 mb-30">
                              <label class="font-lg color-text-mutted-2 mb-10">Téléphone</label>
                              <div class="input-group input-group-lg">
                                <div class="input-group-prepend">
                                      <img class="custom-png"  src="template/assetss/imgs/template/icons/flag_tunisie.png">
                                      <div class="btn-lien " aria-haspopup="true" aria-expanded="true">+ 216</div>    
                                    </div>
                                      <input v-model="etudiant.telephone" name="telephone"  type="text" class="form-control" aria-label="Default" aria-describedby="inputGroup-sizing-default">
                                    </div>
                                    <div v-if="telephoneTouched && !isTelephoneFilled" class="text-danger">Veuillez remplir ce champ.</div>
                                    </div>
                                  </div>
                                  <div class="col-lg-122">
                                    <label class="font-lg color-text-mutted-2 mb-10">Email</label>
                              <div class="input-group mb-3"> 
                            
                                <div class="input-group-prepend">
                                      <img class="custom-svg"  src="template/assetss/imgs/template/icons/envelope-at.svg">
                                      <div class="btn-lien " aria-haspopup="true" aria-expanded="true">Email</div>    
                                    </div>
        
                                <input v-model="etudiant.email" name="email"  class="form-control" type="email" placeholder="e.g. mohamedkacem@gmail.com" required>
                                <div v-if="mailError" class="invalid-feedback">Format email incorrect.</div>
                              </div>
                            </div>
                     
                            <div class="col-lg-122"> 
                              <div class="form-group mt-10">
                                
                                <button class="btn btn-default-2 btn-brand-2 " @click="updateEtudiant">Enregistrer</button>
                                <button class="btn btn-default btn-brand " @click="moveToPreviousTab">Précédent</button>
                              </div>
                            </div>
                            <div class="col-lg-122">
                              <h5>Supprimer compte</h5><br>
                              <p>Si vous supprimez votre compte, vous ne pourrez plus obtenir d'informations sur vos offres de stages correspondantes,
                               vos demandes reçues, les notifications et plus encore. 
                              Vous serez exclu de tous les services de SW Connect.</p><br>
                              <a   style="color:red; cursor:pointer;" @click="deleteEtudiant">supprimer compte</a>

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
                      <li><a href="#">Contact</a></li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    <!-- Modal -->
    <div class="modal" v-if="showModal">
    <!-- Modal content -->
    <div class="modal-content">
      <h5 class="modal-title">Changer mot de passe</h5>
      <span class="close" @click="closeModal">&times;</span>
                              <div class="input-group mb-3"> 
                                <label class="font-lg color-text-mutted-2 mb-10">Nouveau mot de passe</label>
                                <input v-model="etudiant.password" name="password"  class="form-control-2" type="password"  @blur="validateMdpNouv">
                                <div v-if="mdpnouvTouched && !isMdpNouvFilled" class="text-danger">Veuillez remplir ce champ de 6 caractères au minimum.</div>
                              </div>
                         
                              <button class="btn btn-default-2 btn-brand-2 " @click="closeModal">Enregistrer</button>
                  
    </div>
  </div>
  
      </main>
   
    </body>
  </template>
  <script>

 import axios from "axios";
 import navbarEtudiant from '@/components/navbarEtudiant.vue';
  export default {
    name: "ProfilEntView",
    components:{navbarEtudiant},
    data() {
      return {
        etudiant: {
        first_name: '',
        last_name: '',
        email: '',
        password: '',
        bio: '',
        education: '',
        location: '',
        sexe: '',
        skills:[ ],
        lettre_motivation:'',
        telephone: '',
        fb_lien: '',
        git_lien: '',

        in_lien: '',
        link_lien: '',

        date_naissance: '',
        cv: '',
        certificats: '',
        role:'',
      domain:'',
      username:"",
      profile_cover: null,
        profile_photo: null,
        previousPhoto: null,
        previousCover: null,
                },
                
        originalUsername: '' ,
        tabs: ['Infos Etudiant', 'Infos Avancées', 'Réseaux sociaux', 'Contact'],
        activeTab: 0,// Default to Tab 2
        //error messages and validators
        mailError: false,
        nomTouched:false,
        isnomFilled:false,
        prenomTouched:false,
        isPrenomFilled:false,
        bioTouched:false,
        isBioFilled:false,
        usernameTouched:false,
        isUsernameFilled:false,
        sexeTouched:false,
        isSexeFilled:false,
        educationTouched:false,
        isEducationFilled:false,
        competenceTouched: false,
        isCompetenceFilled: false,
        dateNaisTouched: false,
        isDateNaisFilled:false,
        locationTouched: false,
        isLocationFilled:false,
        telephoneTouched: false,
        isTelephoneFilled:false,
             //dropdownmenu
       showDropdown: false,
       mdpnouvTouched: false,
       isMdpNouvFilled:false,
       mdpconfirmTouched: false,
       isMdpConfirmFilled:false,
    selectedFileName: '', // Initialize selectedFileName data property to store the selected file name
      fileSizeError: false ,
      selectedFileName1: '',
      fileSizeError1: false ,
      selectedFileName2: '',
      fileSizeError2: false ,
      selectedFileName3: '',
      fileSizeError3: false ,
      showModal:false,
      roleTouched:false,
      isRoleFilled:false,
      baseUrl: "http://localhost:8000",
      };
    },
    created() {
    // Retrieve etudiant ID from localStorage
    this.etudiant.id = localStorage.getItem('user_id');
    console.log(this.etudiant.id);
    // Fetch etudiant data using the etudiant ID
    this.fetchEtudiantData();
  },
    mounted(){
  this.setPreviousPhotos();
},

    methods: {
      
    handleCoverPhotoFileChange(files) {
      if (files.length > 0) {
        // Check if file size exceeds 50 kB (5 1024  bytes)
        if (files[0].size > 800*1024) {
          this.fileSizeError3 = true; // Set fileSizeError to true if file size exceeds 10 MB
          this.selectedFileName3 = ''; // Clear selectedFileName
          this.etudiant.profile_cover = null;
        } else {
         
          this.fileSizeError3 = false; // Reset fileSizeError
          this.selectedFileName3 = files[0].name; // Set selectedFileName to the name of the selected file
          this.etudiant.profile_cover=files[0];
      } 
      }else {
        // No file selected, reset selectedFileName and fileSizeError
        this.selectedFileName3 = '';
        this.fileSizeError3= false;
        this.etudiant.profile_cover=null;
      }

      for (let i = 0; i < files.length; i++) {
        // Your code to handle the uploaded file goes here
        console.log("Uploaded file:", files[i]);
      }
},
      setPreviousPhotos() {
        // Logic to retrieve previous logo and cover photo URLs or file data from your backend or wherever they are stored
        // For example:
        this.previousPhoto = this.etudiant.profile_photo; // Accessing as this.previousLogo
        this.previousCover = this.etudiant.profile_cover;
    },
      async fetchEtudiantData() {
      try {

        const response = await axios.get(`http://127.0.0.1:8000/api/etudiants/get/${this.etudiant.id}/`);
        // Populate the etudiant object with data from the response
        this.etudiant = response.data;
        this.originalUsername = response.data.username; 
        if (this.etudiant.profile_photo) {
          this.etudiantUrl = this.baseUrl + this.etudiant.profile_photo;
          console.log(this.etudiant.profile_photo);
        }
      } catch (error) {
        console.error('Error fetching etudiant data:', error);
      }
    },
    async updateEtudiant() {
    try {
        // Log etudiant data before FormData creation
        console.log('Etudiant data:', this.etudiant);
        console.log('Etudiant skills:', this.etudiant.skills);


        // Create FormData object
        const formData = new FormData();
        formData.append('skills', JSON.stringify(this.etudiant.skills));


        formData.append('id', this.etudiant.id);
        formData.append('first_name', this.etudiant.first_name);
formData.append('last_name', this.etudiant.last_name);
formData.append('email', this.etudiant.email);

formData.append('bio', this.etudiant.bio);
formData.append('education', this.etudiant.education);
formData.append('location', this.etudiant.location);
formData.append('sexe', this.etudiant.sexe);
formData.append('lettre_motivation', this.etudiant.lettre_motivation);
formData.append('telephone', this.etudiant.telephone);

formData.append('date_naissance', this.etudiant.date_naissance);
//formData.append('skills',this.etudiant.skills);
formData.append('role', this.etudiant.role);
formData.append('domain', this.etudiant.domain);

if (this.etudiant.username && this.etudiant.username !== this.originalUsername) {
            formData.append('username', this.etudiant.username);
        }
if (this.etudiant.fb_lien) {
    formData.append('fb_lien', this.etudiant.fb_lien);
} 
if (this.etudiant.git_lien) {
    formData.append('git_lien', this.etudiant.git_lien);
}

if (this.etudiant.in_lien) {
    formData.append('in_lien', this.etudiant.in_lien);
} 

if (this.etudiant.link_lien) {
    formData.append('link_lien', this.etudiant.link_lien);
} 
    
        if (this.etudiant.password) {
            formData.append('password', this.etudiant.password);
        }
        if (this.etudiant.cv instanceof File && this.etudiant.cv) {
            formData.append('cv', this.etudiant.cv);
        }
        if (this.etudiant.certificats instanceof File && this.etudiant.certificats) {
            formData.append('certificats', this.etudiant.certificats);
        }

        // Append profile_photo only if it's modified or new
        if (this.etudiant.profile_photo instanceof File && this.etudiant.profile_photo !== this.etudiant.previousPhoto) {
            formData.append('profile_photo', this.etudiant.profile_photo);
        }

        // Append profile_cover only if it's modified or new
        if (this.etudiant.profile_cover instanceof File && this.etudiant.profile_cover !== this.etudiant.previousCover) {
            formData.append('profile_cover', this.etudiant.profile_cover);
        }


        // Log FormData before sending the request
      // Log FormData before sending the request
      console.log('FormData:', formData);


        const response = await axios.put(`http://127.0.0.1:8000/api/etudiants/update/${this.etudiant.id}/`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
        console.log('Response skills:', response);



        // Log response data
        console.log('Response:', response.data);

// Redirect to another page after successful update
this.$router.push('/OffreGrid');
} catch (error) {
console.error('Error updating etudiant:', error);
let errorMessage = 'An error occurred while updating etudiant. Please try again later.';
if (error.response && error.response.data) {
    if (error.response.status === 400) {
        errorMessage = "Username already exists. Please choose a different username.";
    } else {
        errorMessage = error.response.data.message || errorMessage;
    }
}
alert(errorMessage);
}
},


      validateMdpNouv(){
        this.mdpnouvTouched = true;
    if (this.etudiant.password && this.etudiant.password.trim().length > 5) {
        this.isMdpNouvFilled = true;
    } else {
        this.isMdpNouvFilled = false;
    }

      },
 
      openModal() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
      logout() {
          localStorage.removeItem('user_id');
          this.$router.push('/ConnexionView');
          console.log('Logout successful');
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
 
      handleFiles(files) {
      // Check if any file is selected
      if (files.length > 0) {
        // Check if file size exceeds 50 kB (50 * 1024  bytes)
        if (files[0].size > 300 * 1024 ) {
          this.fileSizeError = true; // Set fileSizeError to true if file size exceeds 10 MB
          this.selectedFileName = ''; 
          this.etudiant.profile_photo=null;// Clear selectedFileName
        } else {
          this.fileSizeError = false; // Reset fileSizeError
          this.selectedFileName = files[0].name;
          this.etudiant.profile_photo=files[0]; // Set selectedFileName to the name of the selected file
        }
      } else {
        // No file selected, reset selectedFileName and fileSizeError
        this.selectedFileName = '';
        this.fileSizeError = false;
        this.etudiant.profile_photo=null;
      }

      for (let i = 0; i < files.length; i++) {
        // Your code to handle the uploaded file goes here
        console.log("Uploaded file:", files[i]);
      }
    },
    handleFiles1(files) {
      // Check if any file is selected
      if (files.length > 0) {
        // Check if file size exceeds 50 kB (5 1024  bytes)
        if (files[0].size > 200*1024) {
          this.fileSizeError1 = true; // Set fileSizeError to true if file size exceeds 10 MB
          this.selectedFileName1 = ''; // Clear selectedFileName
          this.etudiant.cv=null;
        } else {
          this.fileSizeError1 = false; // Reset fileSizeError
          this.selectedFileName1 = files[0].name; 
          this.etudiant.cv=files[0];// Set selectedFileName to the name of the selected file
        }
      } else {
        // No file selected, reset selectedFileName and fileSizeError
        this.selectedFileName1 = '';
        this.fileSizeError1= false;
        this.etudiant.cv=null;
      }

      for (let i = 0; i < files.length; i++) {
        // Your code to handle the uploaded file goes here
        console.log("Uploaded file:", files[i]);
      }
    },
    handleFiles2(files) {
      // Check if any file is selected
      if (files.length > 0) {
        // Check if file size exceeds 50 kB (5 1024  bytes)
        if (files[0].size > 50*1024*1024) {
          this.fileSizeError2 = true; // Set fileSizeError to true if file size exceeds 10 MB
          this.selectedFileName2 = ''; 
          this.etudiant.certificats=null;// Clear selectedFileName
        } else {
          this.fileSizeError1 = false; // Reset fileSizeError
          this.selectedFileName2 = files[0].name;
          this.etudiant.certificats=files[0]; // Set selectedFileName to the name of the selected file
        }
      } else {
        // No file selected, reset selectedFileName and fileSizeError
        this.selectedFileName2 = '';
        this.fileSizeError2= false;
        this.etudiant.certificats=null;
      }

      for (let i = 0; i < files.length; i++) {
        // Your code to handle the uploaded file goes here
        console.log("Uploaded file:", files[i]);
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
   updateVilles() {
        this.selectedVille = ''; // Reset selected ville
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
  async deleteEtudiant() {
    try {
      // Assuming this.entreprise.id contains the ID of the entreprise to delete
      const etudiantId = this.etudiant.id;

      const response = await axios.delete(
        `http://127.0.0.1:8000/api/etudiants/delete/${etudiantId}/`
      );

      console.log("Deleted etudiant:", response.data);
      alert("Success, etudiant deleted");

      // Redirect the user to a different page or perform other actions after deletion
      this.$router.push("/PageRegisterEtudiant");
    } catch (error) {
      console.error("Error deleting etudiant:", error);
      alert("An error occurred while deleting etudiant. Please try again later.");
    }
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
  .link {
    color: blue;
    text-decoration: underline;
    cursor: pointer; /* Change cursor to pointer on hover */
}

/* Modal styles (you can customize as needed) */
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
    margin: 10% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
    max-width: 500px;
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
    height: 40px;
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
  .form-control {
    height:53px;
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
    height:1318px;
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
      height: 84px;
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
  
  </style>