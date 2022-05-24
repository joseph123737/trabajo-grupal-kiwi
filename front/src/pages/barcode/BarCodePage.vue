<template>
  <body>
    <h2 class="project">{{ this.palot.project }}</h2>
    <h2>{{this.counter}}</h2>
    <input
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
export default {
  name: "barcode",
  data() {
    return {
      palot: {
        project: localStorage.line,
        lote_number: "",
      },
      correctBarCode: false,
      counter: 0,
    };
  },
  computed: {},
  mounted() {
    this.setFocus();
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
      let response = await fetch("https://192.168.21.62:8080/api/barcode", settings);
      if (response.status == 200) {
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
.project{
  font-size: 75px;

}
</style>