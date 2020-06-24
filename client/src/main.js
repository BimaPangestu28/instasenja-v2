import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";

import { BootstrapVue, IconsPlugin } from "bootstrap-vue";

Vue.use(require('vue-pusher'), {
  api_key: '81ac97583b4547cbf23a',
  options: {
      cluster: 'ap1',
      encrypted: true,
  }
});

// Install BootstrapVue
Vue.use(BootstrapVue);
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin);

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

import "./assets/styles/style.bundle.css";
import "./assets/styles/datatable.bundle.css";
import "./assets/styles/index.css";

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
