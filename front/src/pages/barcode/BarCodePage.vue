<template>
  <body>
    <h2 class="project">{{ this.palot.project }}</h2>
    <h2>{{this.counter}}</h2>
    <LoadingScreen v-if="isLoading"/>
    <input
      name="barcode"
      v-model="palot.lote_number"
      v-on:keyup.enter="sentData(palot)"
      ref="myInput"
      autofocus
      type="text"
      placeholder="Codigo de barras"
      
    />
  </body>
</template>

<script>
import LoadingScreen from "@/pages/components/LoadingScreen.vue";
export default {
  name: "barcode",
  components: {LoadingScreen},
  data() {
    return {
      palot: {
        project: localStorage.line,
        lote_number: "",
      },
      correctBarCode: false,
      counter: 0,
      isLoading: true
    };
  },
  computed: {},
  mounted() {
    this.setFocus();
    setTimeout(() => {
      this.isLoading = false;
    }, 1500);
  },
  methods: {
    async sentData(palot) {
      const settings = {
        method: "POST",
        body: JSON.stringify(palot),
        headers: {
          "Content-Type": "application/json",
        },
      };
      console.log(palot);
      let response = await fetch("https://localhost:8080/api/barcode", settings);
      if (response.status == 200) {
        this.isLoading = false;
        this.palot.lote_number = "";
        this.counter += 1;
        this.correctBarCode = true;
      }
      
      
    },
    checkingInput() {
      if (this.palot.lote_number == "") {
        return false;
      } else {
        return true;
      }
    },
    setFocus() {
      this.$refs.myInput.focus();
      // this.correctBarCode = false;
    },
  },
};
</script>

<style>
.correctBarCode {
  background-color: rgb(16, 212, 16);
  border: 2px solid green;
}
body{
  display:flex;
  flex-direction: column;
}
</style>