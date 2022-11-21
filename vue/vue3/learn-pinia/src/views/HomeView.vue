<template>
  <div class="home">
    <counter />
    <div class="count">{{ storeCounter.count }}</div>
  </div>
  <div class="buttons">
    <button @click="storeCounter.increaseCount">+</button>
    <button @click="storeCounter.decreaseCount">-</button>
  </div>
  <hr />
  <div>This counter is: {{ storeCounter.oddOrEven }}</div>
  <hr />
  <div>
    <h3>Edit counter:</h3>
    <input v-model="storeCounter.count" type="number" />
  </div>
</template>

<script setup>
import Counter from "../components/Counter.vue";
import { useCounterStore } from "../stores/counter";
const storeCounter = useCounterStore();
</script>

<style>
.count {
  font-size: 60px;
  margin: 20px;
}
.buttons button {
  font-size: 40px;
  margin: 10px;
}
</style>
