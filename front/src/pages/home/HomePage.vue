<template>
  <body class="home">
    <ul>
      <li @click="goToBarCodePageBaskets">
        <p>LINEA CESTAS</p>
      </li>
      <li @click="goToBarCodePageCalibrated">
        <p>LINEA CALIBRADO</p>
      </li>

    </ul>
  </body>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      basket: "L.CESTAS",
      calibrated: "L.CALIBRADO",
    };
  },
  methods: {
    goToBarCodePageBaskets() {
      localStorage.line = this.basket;
      this.$router.push("/barcode");
    },
    goToBarCodePageCalibrated() {
      localStorage.line = this.calibrated;
      this.$router.push("/barcode");
    },
  },
};
</script>

<style scoped>
body {
  height: 100%;
  overflow-y: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}
ul {
  padding: 0;
  margin: 0;
}
li {
  list-style: none;
  border: 1px solid black;
  border-radius: 30px;
  width: 50vw;
  height: 25vh;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 3%;
}
</style>
