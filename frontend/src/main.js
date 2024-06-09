import { createApp } from 'vue';
import App from './App.vue';
import router from './router'
import axios from 'axios';
import store from './store'; // Import the store

const app = createApp(App);
app.use(router); // Utilisez le routeur configuré dans votre application
app.use(store); 
app.mount('#app');
axios.defaults.baseURL = 'http://localhost:3000';
