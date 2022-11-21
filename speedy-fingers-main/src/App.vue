<template>
  <h1>Speedy Fingers</h1>
  <h5>by Kyle</h5>
  <Block
    v-if="isPlaying"
    :blockMsgP="blockMsg"
    :delayProps="delay"
    @end="endGame"
  ></Block>
  <Results class="results" v-if="showResults" :scoreProps="score" />
  <button v-if="showButton" @click="start">{{ buttonLbl }}</button>
  <h2 @click="msgFoul" class="blockRed" v-if="showRed">{{ blockMsg }}</h2>
</template>

<script>
import Block from "./components/Block.vue";
import Results from "./components/Results.vue";

export default {
  name: "App",
  components: { Block, Results },
  data() {
    return {
      isPlaying: false,
      isTimerRunning: false,
      blockMsg: "",
      delay: null,
      showRed: false,
      score: 0,
      showResults: false,
      buttonLbl: "Play",
      showButton: true,
    };
  },
  methods: {
    start() {
      this.isPlaying = true;
      this.blockMsg = "Don't click yet... Wait for it!";
      this.showRed = true;
      this.delay = 2000 + Math.random() * 5000;
      this.disableRedBlock();
      console.log(this.delay);
      this.showResults = false;
      this.buttonLbl = "Play";
      this.showButton = false;
    },
    msgFoul() {
      this.isPlaying = false;
      this.blockMsg =
        "Foul! Pls don't click until it's green... Click Play to restart";
      this.showButton = true;
      this.buttonLbl = "Play";
    },
    disableRedBlock() {
      setTimeout(() => {
        if (this.isPlaying === false) {
          console.log("firstif");
        } else {
          console.log("elseif");
          this.showRed = false;
          // this.isPlaying = false;
        }
      }, this.delay);
    },
    endGame(reactiontimeEM) {
      this.score = reactiontimeEM;
      this.isPlaying = false;
      this.showResults = true;
      console.log(this.score);
      this.buttonLbl = "Play again?";
      this.showButton = true;
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.blockRed {
  color: white;
  background: red;
  margin: 40px auto;
  text-align: center;
  padding: 100px 0;
  border-radius: 20px;
  width: 400px;
}
h1 {
  color: black;
}
button {
  background-color: blue;
  color: white;
  font-size: 25px;
  border: none;
  padding: 16px 32px;
  border-radius: 20px;
  font-size: 25px;
  letter-spacing: 1px;
  cursor: pointer;
  margin: 10px;
}
p {
  background: purple;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 15px;
  font-size: 20px;
  letter-spacing: 3px;
  cursor: pointer;
  margin: 10px;
}

results {
  font-weight: bold;
}
</style>
