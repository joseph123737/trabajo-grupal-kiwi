<template>
  <body class="home">
    <ul>
      <li @click="goToVarCodePage">
        <p>LINEA CESTAS</p>
      </li>
      <li @click="goToVarCodePage">
        <p>LINEA CALIBRADO</p>
      </li>
      <li @click="goToVarCodePage">
        <p>CUADRE EXISTENCIAS</p>
      </li>
    </ul>
  </body>
</template>

<script>

export default {
  name: 'Home',
  methods: {
    goToVarCodePage(){
     this.$router.push("/varcode")
    }
  }


}
</script>

<style scoped>
body {
  height: 100%;
  overflow-y: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}
ul{
  padding: 0;
  margin: 0;
}
li{
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
