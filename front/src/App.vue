<template>
  
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
*{
  padding: 0 !important;
  margin: 0;
}

</style>