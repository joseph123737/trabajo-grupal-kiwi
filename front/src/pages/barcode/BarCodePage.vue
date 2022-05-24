<template>
  <body>
    <h2 class="project">{{ this.palot.project }}</h2>
    <h2>{{this.counter}}</h2>
    <div class="container" v-if="isLoading">
        <div class="ring"></div>
    </div>
    <!-- <LoadingScreen class="loading" v-if="isLoading"/> -->

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
.container{
  position:fixed;
  width:100%;
  display:flex;
  justify-content: center;
  align-items: center;
}
.container .ring{
  position:relative;
  width:150px;
  height: 150px;
  margin: -30px;
  border-radius:50%;
  border: 4px solid transparent;
  border-top: 4px solid #000000;
  animation: animate 4s linear infinite;
}
@keyframes animate {
  0%{
      transform: rotate(0deg)
  }
  100%{
      transform: rotate(360deg)
  }
}
.container .ring::before{
  content:"";
  position:absolute;
  top: 12px;
  right: 12px;
  border-radius: 50%;
  width:15px;
  height:15px;
  background: #000000;
  box-shadow: 0 0 0 15px #00000033,
  0 0 0 10px #00000022,
  0 0 0 20px #00000011,
  0 0  20px #000000,
  0 0 50px #000000;
}

</style>