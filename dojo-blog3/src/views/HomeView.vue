<template>
  <div class="home">
    home
    <p>My name is {{ name }} and my age is {{ age }}</p>
    <button @click="handleClick">click me</button>
    </div>
</template>

<script>
export default {
  name: "Home",
  setup() {
    console.log("setup");

    let name = "kyle";
    let age = 16;

    const handleClick = () => {
      console.log('you clicked me')
    }

    return { name, age, handleClick };
  },
};
</script>
