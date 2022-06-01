<template>
  <div id="nav">
    <p @click="goToLines">ELEGIR LINEA</p>
  </div>
  <router-view />
</template>

<script>
export default {
  methods: {
    goToLines() {
      this.$router.push("/");
    },
  }
}
</script>

<style scoped>
#nav{
  height: 10vh;
  background-color: grey;
  border-radius: 10px;
  color: white;
  padding: 0;
  display: flex;
  justify-content: center;
  }
p{
  font-size: 3em;
  margin: auto;
}
</style>