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
    <title>Portfolio</title>
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
  <body style="overflow: hidden">
    <NavbarEtudiant />
    <main class="main-2" style="margin-top: 0px; height: 700px">
      <div
        class="nav-2"
        style="border-right: 1px solid #dee2e6; position: relative; top: 27px"
      >
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
              <router-link
                :to="'/GenerationPortfolio/' + this.etudiant.id"
                class="active dashboard2"
                exact
                ><img
                  src="../assets/imgs/template/icons/file-person.svg"
                  alt="jobBox"
                /><span class="name">Générer Portfolio</span></router-link
              >
            </li>

            <li>
              <router-link to="/Demandes"
                ><img
                  src="../assets/imgs/template/icons/briefcase2.svg"
                  alt="jobBox"
                /><span class="name">Mes Demades</span></router-link
              >
            </li>
            <li>
              <router-link :to="'/EtudDrive/' + this.etudiant.id">
                <img
                  src="../assets/imgs/template/icons/folder.svg"
                  alt="jobBox"
                /><span class="name">Mon Drive</span></router-link
              >
            </li>
          </ul>
        </nav>
        <div class="border-bottom mb-20 mt-20"></div>
      </div>

      <div class="form-section-2" style="background-color: #ffffff"></div>

      <h4 style="position: relative; left: 25px; top: 25px; color: #858585">
        Sélectionner un Portfolio
      </h4>

      <div style="position: relative; top: 75px; left: -280px">
        <section style="position: relative; top: 35px; left: 180px">
          <div class="image-modele-container">
            <img src="/DevFolio/assets/img/Template1.png" alt="Image" />
            <div class="form-check">
              <input
                class="form-check-input"
                type="radio"
                name="modele"
                value="modele1"
                id="modele1"
                style="position: relative; top: -255px; left: 177px"
              />
              <label
                class="form-check-label"
                for="modele1"
                style="
                  position: relative;
                  top: -255px;
                  left: 177px;
                  color: #4d4c4c;
                  font-size: 20px;
                  margin-bottom: 35px;
                "
                >Modele1</label
              >
            </div>
            <div class="overlay">
              <router-link
                :to="'/PortfolioTemplate1/' + this.etudiant.id"
                style="text-decoration: none"
              >
                <p class="message">Voir preview</p>
              </router-link>
            </div>
          </div>
        </section>

        <section style="position: relative; left: 750px; top: -177px">
          <div class="image-modele-container">
            <img src="/DevFolio/assets/img/Template2.png" alt="Image" />
            <div class="form-check">
              <input
                class="form-check-input"
                type="radio"
                name="modele"
                value="modele2"
                id="modele2"
                style="position: relative; top: -255px; left: 177px"
              />
              <label
                class="form-check-label"
                for="modele2"
                style="
                  position: relative;
                  top: -255px;
                  left: 177px;
                  color: #4d4c4c;
                  font-size: 20px;
                  margin-bottom: 35px;
                "
                >Modele2</label
              >
            </div>
            <div class="overlay">
              <router-link
                :to="'/PortfolioTemplate2/' + this.etudiant.id"
                style="text-decoration: none"
              >
                <p class="message">Voir preview</p>
              </router-link>
            </div>
          </div>
        </section>

        <section style="position: relative; left: 440px; bottom: 100px">
          <div class="image-modele-container">
            <img src="/DevFolio/assets/img/Template3.png" alt="Image" />
            <div class="form-check">
              <input
                class="form-check-input"
                type="radio"
                name="modele"
                value="modele3"
                id="modele3"
                style="position: relative; top: -255px; left: 177px"
              />
              <label
                class="form-check-label"
                for="modele3"
                style="
                  position: relative;
                  top: -255px;
                  left: 177px;
                  color: #4d4c4c;
                  font-size: 20px;
                  margin-bottom: 35px;
                "
                >Modele3</label
              >
            </div>
            <div class="overlay">
              <router-link
                :to="'/PortfolioTemplate3/' + this.etudiant.id"
                style="text-decoration: none"
              >
                <p class="message">Voir preview</p>
              </router-link>
            </div>
          </div>
        </section>
      </div>

      <router-link to="" @click="generatePortfolio">
        <button
          type="submit"
          class="btn btn-secondary btn-fle"
          style="
            position: relative;
            width: 100%;
            border-color: white;
            top: 650px;
            left: 85px;
          "
          @click="sendFileToBackend"
        >
          <p class="creer">Générer le Portfolio</p>
          <img
            src="/template/assets/imgs/page/login-register/fleche.png"
            alt="fleche Icon"
            class="icon-fleche"
          />
        </button>
      </router-link>
    </main>
    <div class="footer-2 mt-20" style="height: 99px">
      <div class="container">
        <div class="box-footer-2">
          <div class="row">
            <div
              class="col-md-6 col-sm-12 mb-25 text-center text-md-start"
              style="position: relative; left: 14px"
            >
              <p class="font-lg color-text-paragraph-made-by">
                © 2024 - Made By SwConnect
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </body>
</template>
<script>
import NavbarEtudiant from "@/components/navbarEtudiant.vue";
import axios from "axios";

export default {
  components: { NavbarEtudiant },

  data() {
    return {
      isDropdownOpen1: false,
      isDropdownOpen2: false,
      etudiant: {
        id: null,
      },
    };
  },
  created() {
    const userId = localStorage.getItem("user_id");
    if (!userId) {
      alert("Vous devez vous connecter.");
      this.$router.push("/ConnexionView");
    } else {
      // Initialisez la propriété etudiant avec l'ID de l'utilisateur
      this.etudiant = { id: userId };
    }
  },
  methods: {
    // Envoyer une requête POST au backend
    stopPropagation(event) {
      event.stopPropagation();
    },
    toggleDropdown1() {
      this.isDropdownOpen1 = !this.isDropdownOpen1;
      if (this.isDropdownOpen1 && this.isDropdownOpen2) {
        this.isDropdownOpen2 = false; // Ferme le dropdown 2 si ouvert
      }
    },
    toggleDropdown2() {
      this.isDropdownOpen2 = !this.isDropdownOpen2;
      if (this.isDropdownOpen2 && this.isDropdownOpen1) {
        this.isDropdownOpen1 = false; // Ferme le dropdown 1 si ouvert
      }
    },
    generatePortfolio() {
      // Récupérer la valeur du bouton radio sélectionné
      var selectedModele = document.querySelector(
        'input[name="modele"]:checked'
      );

      // Vérifier si un modèle est sélectionné
      if (selectedModele) {
        this.ajouterAction();

        // Rediriger l'utilisateur vers la page de génération de portfolio en fonction du modèle sélectionné
        switch (selectedModele.value) {
          case "modele1":
            this.$router.push("/PortTemplate1Choi");
            break;
          case "modele2":
            this.$router.push("/PortTemplate2Choi");
            break;
          case "modele3":
            this.$router.push("/PortTemplate3Choi");
            break;
          default:
            // Si aucun modèle n'est sélectionné, afficher une alerte
            alert("Aucun modèle sélectionné");
        }
      } else {
        // Si aucun modèle n'est sélectionné, afficher une alerte
        alert("Aucun modèle sélectionné");
      }
    },
    ajouterAction() {
      const userId = localStorage.getItem("user_id");
      if (!userId) {
        alert("Vous devez être connecté.");
        return;
      }
      axios
        .post(`http://127.0.0.1:8000/creer-action/${userId}/`, {
          action_message: "Portfolio généré ",
        })
        .then(() => {
          // Traiter la réponse si nécessaire
          console.log("Action ajoutée avec succès !");
        })
        .catch((error) => {
          console.error("Erreur lors de l'ajout de l'action :", error);
          alert("Une erreur est survenue lors de l'ajout de l'action.");
        });
    },
  },
};
</script>
<style scoped>
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
  margin-left: 20px;
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
  height: 1440px;
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
  margin-bottom: 35px;
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
}
/* Styles for the tab content */
.tab-content {
  padding: 30px;
  border: 1px solid #dee2e6;
  border-top: none;
  border-right: none;
  background-color: #f2f4fa;
  border-radius: 9px;
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
.header .main-menu li a {
  font-family: "Plus Jakarta Sans", sans-serif;
  font-style: normal;
  font-weight: 600;
  font-size: 20px;
  line-height: 18px;
  color: #ffffff;
  display: block;
  padding: 0px;
  text-decoration: none;
  position: relative;
}
.main-2 {
  height: 550px;
}
.upload-container {
  position: relative;
  border: 2px dashed #ccc;
  width: 80%;
  height: 220px;
  top: 50px;
  padding: 10px;
  left: -45px;
}
.container2 {
  max-width: 1330px;
  width: 100%;
  margin: 0 auto;
  align-items: center;
  justify-content: space-between;
  position: relative;
  top: 15px;
}
.footer-2 .box-footer-2 {
  padding: 25px 0px 0px 0px;
  border-top: 1px solid #e0e6f6;
}
.image-modele-container {
  position: relative;
  height: 210px;
  width: 420px;
  right: 120px;
  top: 25px;
}
.image-modele-container:hover img {
  opacity: 0.2; /* L'image devient transparente au survol */
}

.image-modele-container:hover .overlay {
  opacity: 1; /* L'overlay devient opaque au survol */
}
.message {
  position: relative;
  font-size: 22px;
  font-weight: bolder;
  text-transform: uppercase;
  left: 95px;
  color: #717171;
}
.message:hover {
  color: #447ab8;
}
.overlay {
  position: absolute;
  top: 50%;
  left: 30%;
  transform: translate(-50%, -50%);
  text-align: center;
  opacity: 0; /* L'overlay est transparent par défaut */
  transition: opacity 0.5s ease; /* Animation de transition */
}
.image-modele-container:hover .overlay {
  opacity: 1; /* L'overlay devient opaque au survol */
}
.titremodele {
  color: #4d4c4c;
  font-size: 20px;
  margin-bottom: 35px;
}
/* Style pour la checkbox */
.form-check-input[type="checkbox"] {
  width: 15px;
  height: 15px;
  border-radius: 3px;
  background-color: transparent;
  border: 2px solid #447ab8;
}

/* Style pour la coche à l'intérieur de la checkbox */
.form-check-input[type="checkbox"]:checked {
  background-color: #447ab8;
}
</style>
