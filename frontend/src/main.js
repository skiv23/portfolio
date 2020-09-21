import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faHome, faUser, faEnvelope, faPaperPlane, faCogs, faLaptopCode, faGraduationCap, faBriefcase, faGlobe, faCalendar } from '@fortawesome/free-solid-svg-icons'
import { faLinkedinIn } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import SlideHome from './components/SlideHome.vue'
import SlideAbout from './components/SlideAbout.vue'
import SlideCV from './components/SlideCV.vue'
import SlidePortfolio from './components/SlidePortfolio.vue'

Vue.use(VueRouter)

library.add(faLinkedinIn, faHome, faUser, faEnvelope, faPaperPlane, faCogs, faLaptopCode, faGraduationCap, faBriefcase, faGlobe, faCalendar)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

const routes = [
  { path: '/', component: SlideHome, name: 'home' },
  { path: '/about', component: SlideAbout, name: 'about' },
  { path: '/cv', component: SlideCV, name: 'cv' },
  { path: '/portfolio', component: SlidePortfolio, name: 'portfolio' },
]

const router = new VueRouter({
  routes
})

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
