<template>
  <p>Reaction Time: {{ scoreProps }} ms</p>
  <h2 class="feed">{{ feed }}</h2>
</template>

<script>
export default {
  props: ["scoreProps"],
  data() {
    return {
      feed: null,
    };
  },
  mounted() {
    if (this.scoreProps < 200) {
      this.feed = "Speedy Fingers! Now, try for a new record!";
    } else if (this.scoreProps < 450) {
      this.feed = "Good... can you do better?";
    } else {
      this.feed = "Too slow...";
    }
  },
};
</script>

<style>
.feed {
  font-size: 2.3rem;
  color: black;
  font-weight: 10050;
}
</style>
