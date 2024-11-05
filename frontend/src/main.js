import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import * as bootstrap from 'bootstrap'

// Make bootstrap available globally
window.bootstrap = bootstrap

createApp(App).mount('#app')
