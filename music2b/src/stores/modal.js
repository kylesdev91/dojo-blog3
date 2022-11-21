import { defineStore } from "pinia";
export default defineStore("modal", {
  isOpen: false,
  getters: {
    hiddenClass(state) {
      return !state.isOpen ? "hidden" : "";
    },
  },
});
