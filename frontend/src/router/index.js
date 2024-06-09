import { createRouter, createWebHistory } from 'vue-router';

import MasterView from '../views/MasterView.vue'
import PageRegisterEtudiant from '../views/PageRegisterEtudiant.vue'
import PageRegisterRH from '../views/PageRegisterRH.vue'
import ConnexionView from '../views/ConnexionView.vue'
import GenerationPortfolio from '../views/GenerationPortfolio.vue'
import EtudDrive from '../views/EtudDrive.vue'
import testView from '../views/testView.vue'
import PostView from '../views/PostView.vue'
import OffreDetails from '../views/OffreDetails.vue'
import ProfilEntView from '../views/ProfilEntView.vue'
import OffreGrid from '../views/OffreGrid.vue'
import EntGrid from '../views/EntGrid.vue'
import PfeBook from '../views/PfeBook.vue';
import EtuGrid from '../views/EtuGrid.vue'
import ProfilEtuView from '../views/ProfilEtuView.vue';
import EtuConfig from '../views/EtuConfig.vue';
import EntConfig from '../views/EntConfig.vue';
import EtudiantDetails from '../views/EtudiantDetails.vue'
import EntrepriseDetails from '../views/EntrepriseDetails.vue'
import MesOffres from'../views/MesOffres.vue'
import AdminDetails from '../views/AdminDetails.vue'
import ProfilAdView from '../views/ProfilAdView.vue'
import ContenuProtected from '../views/ContenuProtected.vue'
import OffreTable from '../views/OffreTable.vue'
import EntTable from '../views/EntTable.vue'
import EtuTable from '../views/EtuTable.vue'
import chatView from '../views/chatView.vue'
import PortfolioTemplate1 from '../views/PortfolioTemplate1.vue'
import PortfolioTemplate2 from '../views/PortfolioTemplate2.vue'
import PortfolioTemplate3 from '../views/PortfolioTemplate3.vue'

import GenePortfo from '../views/GenePortfo.vue'
import GenePortfo2 from '../views/GenePortfo2.vue'

import PortTemplate1Choi from '../views/PortTemplate1Choi.vue'
import PortTemplate2Choi from '../views/PortTemplate2Choi.vue'
import PortTemplate3Choi from '../views/PortTemplate3Choi.vue'

import EtudOverview from '../views/EtudOverview.vue'
import OffreFavoris from '../views/OffreFavoris.vue'
import EntrepriseFavoris from '../views/EntrepriseFavoris.vue'
import Demandes from '../views/Demandes.vue'
import MesDemandes from '../views/MesDemandes.vue'
import HistoriqueView from '../views/HistoriqueView.vue'
import BookGeneration from '../views/BookGeneration.vue'
import BookGeneration2 from '../views/BookGeneration2.vue'

import BookTemplate1 from '../views/BookTemplate1.vue'
import PfeBook1 from '../views/PfeBook1.vue'
import PfeBook1View from '../views/PfeBook1View.vue'

import BookTemplate2 from '../views/BookTemplate2.vue'
import PfeBook2 from '../views/PfeBook2.vue'
import PfeBook2View from '../views/PfeBook2View.vue'

import BookTemplate3 from '../views/BookTemplate3.vue'
import PfeBook3 from '../views/PfeBook3.vue'
import PfeBook3View from '../views/PfeBook3View.vue'

import AdminOverview from '../views/AdminOverview.vue'
import EntOverview from '../views/EntOverview.vue'
import AdminDemandes from '../views/AdminDemandes.vue'





const routes = [
  {
    path: '/',
    name: 'MasterView',
    component: MasterView
  },
  {
    path: '/bookview1/:id',
    name: 'PfeBook1View',
    component: PfeBook1View
  },
  {
    path: '/bookview2/:id',
    name: 'PfeBook2View',
    component: PfeBook2View
  },
  {
    path: '/bookview3/:id',
    name: 'PfeBook3View',
    component: PfeBook3View
  },
  {
    path: '/book1/:id',
    name: 'PfeBook1',
    component: PfeBook1
  },
  {
    path: '/book3/:id',
    name: 'PfeBook3',
    component: PfeBook3
  },
  {
    path: '/book2/:id',
    name: 'PfeBook2',
    component: PfeBook2
  },
  {
    path: '/BookTemplate1',
    name: 'BookTemplate1',
    component: BookTemplate1,
    props: true
  },
  {
    path: '/BookTemplate2',
    name: 'BookTemplate2',
    component: BookTemplate2,
    props: true
  },
  {
    path: '/BookTemplate3',
    name: 'BookTemplate3',
    component: BookTemplate3,
    props: true
  },
  {
    path: '/BookGeneration2',
    name: 'BookGeneration2',
    component: BookGeneration2
  },
  {
    path: '/BookGeneration',
    name: 'BookGeneration',
    component: BookGeneration
  },
  {
    path: '/Demandes',
    name: 'Demandes',
    component: Demandes
  },
  {
    path: '/MesDemandes/:id',
    name: 'MesDemandes',
    component: MesDemandes
  },
  {
    path: '/AdminDemandes/:id',
    name: 'AdminDemandes',
    component: AdminDemandes
  },
  {
    path: '/EntrepriseFavoris',
    name: 'EntrepriseFavoris',
    component: EntrepriseFavoris
  },
  {
    path: '/OffreFavoris',
    name: 'OffreFavoris',
    component: OffreFavoris
  },
  {
    path:'/EtudOverview/:id',
    name:'EtudOverview',
    component:EtudOverview
  },
  {
    path:'/chatView/:username?', 
    name:'chatView',
    component:chatView
  },
  {
    path: '/EntTable',
    name: 'EntTable',
    component: EntTable
  },
{
    path: '/EtuTable',
    name: 'Etuable',
    component: EtuTable
  },
  {
    path: '/OffreTable',
    name: 'OffreTable',
    component: OffreTable
  },

  {
    path: '/ContenuProtected',
    name: 'ContenuProtected',
    component: ContenuProtected
  },
  {
    path: '/MesOffres',
    name: 'MesOffres',
    component: MesOffres
  },
  {
    path: '/PfeBook/:id',
    name: 'PfeBook',
    component: PfeBook
  },
  {
    path: '/EtuConfig',
    name: 'EtuConfig',
    component: EtuConfig
  },
  {
    path: '/EntConfig',
    name: 'EntConfig',
    component: EntConfig
  },
  {
    path: '/EntGrid',
    name: 'EntGrid',
    component: EntGrid
  },
  {
    path: '/EtuGrid',
    name: 'EtuGrid',
    component: EtuGrid
  },
  {
    path: '/OffreGrid',
    name: 'OffreGrid',
    component: OffreGrid
  },
  {
    path: '/ProfilEntView',
    name: 'ProfilEntView',
    component: ProfilEntView
  },
  {
    path: '/ProfilAdView',
    name: 'ProfilAdView',
    component: ProfilAdView
  },
  {
    path: '/ProfilEtuView',
    name: 'ProfilEtuView',
    component: ProfilEtuView
  },
  {
    path:'/testView',
    name:'testView',
    component : testView
  },
  {
    path: '/PageRegisterEtudiant',
    name: 'PageRegisterEtudiant',
    component: PageRegisterEtudiant
  },
  {
    path: '/PageRegisterRH',
    name: 'PageRegisterRH',
    component: PageRegisterRH
  },
  {
    path: '/ConnexionView',
    name: 'ConnexionView',
    component: ConnexionView
  },
  {
    path: '/GenerationPortfolio/:id',
    name: 'GenerationPortfolio',
    component: GenerationPortfolio
  },
  {
  path: '/PortfolioTemplate1',
  name: 'PortfolioTemplate1',
  component: PortfolioTemplate1
  },
  {
  path: '/EtudDrive/:id',
  name: 'EtudDrive',
  component: EtudDrive
},
{
  path: '/PortfolioTemplate1',
  name: 'PortfolioTemplate1',
  component: PortfolioTemplate1
},
{
  path:'/PostView',
  name:'PostView',
  component:PostView
},
{
  path:'/OffreDetails/:id',
  name:'OffreDetails',
  component:OffreDetails
},
{
path:'/EtudiantDetails/:id',
name:'EtudiantDetails',
component:EtudiantDetails
},
{
  path:'/EntrepriseDetails/:id',
  name:'EntrepriseDetails',
  component:EntrepriseDetails
  },
  {
    path:'/AdminDetails',
    name:'AdminDetails',
    component:AdminDetails
    },
    {
      path: '/PortfolioTemplate1/:id',
      name: 'PortfolioTemplate1',
      component: PortfolioTemplate1
      },
    
    {
      path: '/PortfolioTemplate2/:id',
      name: 'PortfolioTemplate2',
      component: PortfolioTemplate2
    },
    {
      path: '/PortfolioTemplate3/:id',
      name: 'PortfolioTemplate3',
      component: PortfolioTemplate3
    },
    {
      path:'/GenePortfo/:id',
      name:'GenePortfo',
      component:GenePortfo
    },
    {
      path:'/GenePortfo2/:id',
      name:'GenePortfo2',
      component:GenePortfo2
      
    },
    {
      path:'/PortTemplate2Choi',
      name:'PortTemplate2Choi',
      component:PortTemplate2Choi
    },
    {
      path:'/PortTemplate1Choi',
      name:'PortTemplate1Choi',
      component:PortTemplate1Choi
    },
    {
      path:'/PortTemplate3Choi',
      name:'PortTemplate3Choi',
      component:PortTemplate3Choi
    },
    {
      path:'/HistoriqueView/:id',
      name:'HistoriqueView',
      component:HistoriqueView
    },
    {
      path:'/AdminOverview',
      name:'AdminOverview',
      component:AdminOverview
    },
    {
      path:'/EntOverview/:id',
      name:'EntOverview',
      component:EntOverview
    },

];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;


