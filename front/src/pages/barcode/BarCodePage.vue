<template>
  <body>
    <h2>{{ palot.lineName }}</h2>
    <input
      v-bind:class="{ correctBarCode: correctBarCode }"
      v-model="palot.barCode"
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
        lineName: localStorage.line,
        barCode: "",
      },
      correctBarCode: false,
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
      let response = await fetch("http://localhost:5000/api/barCode", settings);
      if (response.status == 200) {
        this.palot.barCode = "";
        this.correctBarCode = true;
      }
    },
    checkingInput() {
      if (this.palot.barCode == "") {
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
</style>