import "vuetify/styles";
import { createApp } from "vue";
import { createVuetify } from "vuetify";
import App from "./App.vue";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import router from "./router";

const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: "light",
  },
});

createApp(App).use(router).use(vuetify).mount("#app");
