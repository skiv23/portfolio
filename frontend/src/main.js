import Vue from 'vue'
import VueRouter from 'vue-router'
import VueSweetalert2 from 'vue-sweetalert2';
import App from './App.vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faHome, faUser, faEnvelope, faPaperPlane, faCogs, faLaptopCode, faGraduationCap, faBriefcase, faGlobe,
  faCalendar, faMapMarkerAlt, faSun, faMoon, faQuestion, faTerminal } from '@fortawesome/free-solid-svg-icons'
import { faLinkedinIn } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import SlideHome from './components/SlideHome.vue'
import SlideAbout from './components/SlideAbout.vue'
import SlideCV from './components/SlideCV.vue'
import SlidePortfolio from './components/SlidePortfolio.vue'
import SlideContact from './components/SlideContact.vue'

import HTTP from "../http-common.js";
import 'sweetalert2/dist/sweetalert2.min.css';

Vue.prototype.$http = HTTP;

Vue.use(VueRouter)
Vue.use(VueSweetalert2)

library.add(faLinkedinIn, faHome, faUser, faEnvelope, faPaperPlane, faCogs, faLaptopCode, faGraduationCap, faBriefcase,
  faGlobe, faCalendar, faMapMarkerAlt, faSun, faMoon, faQuestion, faTerminal)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

const routes = [
  { path: '/', component: SlideHome, name: 'home' },
  { path: '/about', component: SlideAbout, name: 'about' },
  { path: '/cv', component: SlideCV, name: 'cv' },
  { path: '/portfolio', component: SlidePortfolio, name: 'portfolio' },
  { path: '/contact', component: SlideContact, name: 'contact' },
]

const router = new VueRouter({
  routes
})


new Vue({
  render: h => h(App),
  router
}).$mount('#app')
