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
      this.$router.push({name:"BarCode",params:{line:"L.CESTAS"}});
    },
    goToBarCodePageCalibrated() {
      localStorage.line = this.calibrated;
      this.$router.push({name:"BarCode",params:{line:"L.CALIBRADO"}});
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
  list-style-type: none;
}
li {
  list-style: none;
  border-radius: 30px;
  width: 80vw;
  height: 35vh;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 5%;
  margin-bottom: 10%;
  font-size: 2em;
  font-weight: bold;
  background-color: rgb(230, 227, 227);
  box-shadow: 5px 10px;
  
  
}
</style>
