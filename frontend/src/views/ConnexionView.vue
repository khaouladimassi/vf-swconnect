<template>
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
    <title>Connexion</title>
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
      href="./template/assets/css/plugins/animate.min.css"
      rel="stylesheet"
    />
    <link
      href="./template/assets/css/plugins/magnific-popup.css"
      rel="stylesheet"
    />
    <link
      href="./template/assets/css/plugins/perfect-scrollbar.css"
      rel="stylesheet"
    />
    <link
      href="./template/assets/css/plugins/select2.min.css"
      rel="stylesheet"
    />
    <link
      href="./template/assets/css/plugins/swiper-bundle.min.css"
      rel="stylesheet"
    />

    <link href="/template/assets/css/stylecd4e.css" rel="stylesheet" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
    />
  </head>
  <body>
    <div class="container">
      <!-- Votre contenu principal ici -->
      <router-view></router-view>
      <div class="row">
        <img
          style="width: 200px"
          src="template/assets/imgs/page/login-register/welcome2.jpg"
          class="welcome-image"
        />

        <div class="col-md-6">
          <!-- Second division for signup form -->
          <div
            class="logo-container"
            style="position: relative; width: 20%; left: 90%; top: 10%"
          >
            <img
              class="logo-image"
              src="template/assets/imgs/page/login-register/logo.png"
              alt="SW Connect Logo"
            />
          </div>
          <div class="card-cnx">
            <div class="card-body">
              <!-- Votre formulaire de connexion -->
              <h5 class="card-title">Se connecter</h5>
              <div>
                <p>
                  Vous n'avez pas de compte.<router-link
                    to="/PageRegisterEtudiant"
                    >Créer un compte</router-link
                  >
                </p>
              </div>
              <form>
                <div class="form-group">
                  <input
                    v-model="username"
                    name="username"
                    type="text"
                    class="form-control"
                    id="username"
                    placeholder="Entez votre username"
                    style="height: 40px; font-size: 16px"
                  />
                </div>

                <div class="form-group">
                  <input
                    v-model="password"
                    name="password"
                    type="password"
                    class="form-control"
                    id="password"
                    placeholder="Entez votre mot_de_passe"
                    @blur="validateMDP"
                    :class="{ 'is-invalid': MDPError }"
                    required
                  />
                  <div v-if="MDPError" class="invalid-feedback">
                    Le mot de passe doit contenir au moins 6 caractères.
                  </div>
                </div>
              </form>

              <button
                type="submit"
                class="btn btn-secondary btn-fle"
                @click="login"
              >
                <p class="creer">Se Connecter</p>
                <img
                  src="template/assets/imgs/page/login-register/fleche.png"
                  alt="fleche Icon"
                  class="icon-fleche"
                />
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Pied de page -->
      <footer class="footer-cnx">
        <p>@ 2024 SW Connect - Tous droits réservés</p>
      </footer>
    </div>
    <!-- Fenêtre modale pour afficher le message d'erreur -->
    <div v-if="showErrorMessage" class="modal">
      <div class="modal-content">
        <span class="close" @click="hideErrorMessage">&times;</span>
        <p>
          Veuillez remplir tous les champs et cocher la case pour créer un
          compte.
        </p>
      </div>
    </div>
  </body>
</template>

<script>
import axios from "axios";

export default {
  name: "ConnexionView",
  data() {
    return {
      username: "",
      password: "",
      MDPError: false,
      showErrorMessage: false,
    };
  },
  methods: {
    validateMDP() {
      this.MDPError = this.password.length < 6;
    },
    validateConfirmation() {
      this.ConfirmError = this.confirm !== this.password;
    },

    login() {
      if (!this.username || !this.password) {
        this.showErrorMessage = true;
      } else {
        this.showErrorMessage = false;

        const userData = {
          username: this.username,
          password: this.password,
        };

        // Make a POST request to authenticate the user

        axios
          .post("http://127.0.0.1:8000/api/login/", userData)
          .then((response) => {
            console.log("Login response:", response);
            const { user_type, user_id, is_configured, verified, blocked } =
              response.data; // Destructure response.data to extract token and user_type

            localStorage.setItem("user_id", user_id);
            //localStorage.setItem('token', response.data.token);
            localStorage.setItem("user_type", response.data.user_type);

            // Redirect the user based on their user type
            if (user_type === "etudiant") {
              localStorage.setItem("blocked", blocked);
              if (blocked) {
                alert("Vous êtes bloqué pour le moment");
              } else {
                if (is_configured) {
                  this.$router.push("/EtudOverview/" + user_id);
                } else {
                  this.$router.push("/EtuConfig");
                }
              }
            } else if (user_type === "entreprise") {
              localStorage.setItem("verified", verified);
              if (is_configured) {
                if (verified) {
                  this.$router.push("/EntOverview/" + user_id);
                } else {
                  alert("Votre compte n'est pas encore vérifié");
                }
              } else {
                this.$router.push("/EntConfig");
              }
            } else if (user_type === "admin") {
              this.$router.push("/AdminOverview");
            }
          })

          .catch((error) => {
            console.error("Error occurred:", error);
            if (error.response) {
              if (error.response.status === 404) {
                alert("User not found. Please check your username.");
              } else if (error.response.status === 401) {
                alert("Incorrect username or password. Please try again.");
              } else {
                alert("An error occurred. Please try again later.");
              }
            } else {
              alert(
                "An error occurred. Please check your internet connection."
              );
            }
          });
      }
    },
    hideErrorMessage() {
      this.showErrorMessage = false;
    },
  },
};
</script>

<style>
.card-cnx {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 78%;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(0, 0, 0, 0.125);
  border-radius: 0.25rem;
  left: 350px;
  top: 15%;
  height: auto;
  overflow-y: hidden;
  overflow-x: hidden;
}
.footer-cnx {
  position: relative;
  height: 20px;
  width: 150%;
}
.welcome-image {
  position: relative;
  top: 25px;
  width: 15%;
  left: 30%;
  max-height: 96vh;
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
.icon-fleche {
  position: relative;
  height: 23px;
  width: 23px;
  left: 40%;
  bottom: 20px;
}
.btn-fle {
  background-color: #447ab8;
  width: 100%;
  height: 40px;
}
.btn-fle .creer {
  position: relative;
  bottom: 5px;
  right: 25px;
  color: white;
  font-size: 16px;
  font-weight: 700;
}
</style>
