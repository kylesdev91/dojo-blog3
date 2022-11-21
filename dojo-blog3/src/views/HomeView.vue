<template>
  <div class="home">
    home
    <p ref="p">My name is {{ name }} and my age is {{ age }}</p>
    <button @click="handleClick">click me</button>
  </div>
</template>

<script>
import { ref } from "@vue/reactivity";
export default {
  name: "Home",
  setup() {
    console.log(this);

    const p = ref("hello");
    console.log(p, p.value);

    let name = "kyle";
    let age = 16;

    const handleClick = () => {
      console.log(p, p.value);
      p.value.classList.add("test");
      p.value.textContent = "hello, wewos";
    };

    return { name, age, handleClick, p };
  },
};
</script>
