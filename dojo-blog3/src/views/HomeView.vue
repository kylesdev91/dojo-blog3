<template>
  <div class="home">
    home
    <p>My name is {{ name }} and my age is {{ age }}</p>
    <button @click="handleClick">click me</button>
  </div>
</template>

<script>
import { ref } from '@vue/reactivity';
export default {
  name: "Home",
  setup() {
    console.log(this);

    const p = ref(null)

    let name = "kyle";
    let age = 16;

    const handleClick = () => {
      console.log("you clicked me");
    };

    return { name, age, handleClick };
  },
};
</script>
