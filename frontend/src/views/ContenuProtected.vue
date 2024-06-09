<template>
    <router>
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
    <link href="/template/assets/css/stylecd4ee.css?version=4.1" rel="stylesheet">
    <title>Contenu protégé</title>
  </head>
  <body>
    <header class="header sticky-bar">
        <div class="container">
          <div class="main-header">
            <div class="header-left">
              <div class="header-logo"><a class='d-flex' href='index.html'><img alt="jobBox" src="/template/assetss/imgs/logo/logo-blanc.png"></a></div>
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
    <main class="main">
      <section class="pt-100 login-register">
        <div class="container"> 
          <div class="row login-register-cover pb-250">
            <div class="col-lg-4 col-md-6 col-sm-12 mx-auto">
              <div class="text-center"><img src="/template/assets/imgs/page/login-register/img-6.svg" alt="JobBox">
                <h2 class="mt-10 mb-5 text-brand-1">Contenu Protégé</h2>
                <p class="font-sm text-muted mb-30">
                   Ce contenu est protégé. 
                   Pour pouvoir accéder cette page, vous devez attendre la vérification de votre compte.
                   Merci d'essayer plus tard.
                </p>
                <div class="button-container">
                    <router-link to="/">
                        <button   class='btn btn-default btn-shadow  postbutt' style="margin-right: 20px;">Revenir à la page d'accueil</button>
                    </router-link>
                    <button class="btn btn-default-2 btn-brand-2 " @click="logout">Se déconnecter</button>
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
    </footer>

  </body>
</router>
</template>
<script>

export default{
    name:"ContentProtected",
    methods:{
        logout() {
          localStorage.removeItem('user_id');
          this.$router.push('/ConnexionView');
          console.log('Logout successful');
    },
    }

}
</script>
<style scoped>
.postbutt{
    border: none;
}
.button-container{
    display:inline-flex;
    align-items: center;
    width:160%;
    margin-left:-140px !important; 
}
.btn-default{
    width:fit-content;
}
.btn-default-2{
    width:fit-content;
    padding:10px 25px;
    height:fit-content;
}
</style>