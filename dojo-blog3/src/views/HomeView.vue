<template>
  <div class="home">
    home
    <p ref="p">My name is {{ name }} and my age is {{ age }}</p>
    <button @click="handleClick">click me</button>
    <button @click="age++">add 1 to age</button>
    <input type="text" v-model="name" />
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  name: "Home",
  setup() {
    // const p = ref(null);

    const name = ref("kyle");
    const age = ref(16);

    const handleClick = () => {
      (name.value = "geesey"), (age.value = "13");
    };

    return { name, age, handleClick };
  },
};
</script>
