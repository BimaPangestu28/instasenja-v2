import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Home.vue"),
  },
  {
    path: "/bot-account",
    name: "BotAccount",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/BotAccount.vue"),
  },
  {
    path: "/fake-comment",
    name: "FakeComment",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/FakeComment.vue"),
  },
  {
    path: "/contact",
    name: "ContactScraping",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/ContactScraping.vue"),
  },
  {
    path: "/action",
    name: "Action",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/Action.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
