<template>
  <body v-bind:style="{ backgroundColor: color}">

    <!-- Page text -->
    <h2 class="project">-{{ this.palot.project }}-</h2>
    <p class="instruction">ESCANEE EL CODIGO DE BARRAS</p>
    <!-- Page loading effect -->
    <div class="container" v-if="isLoading">
        <div class="ring"></div>
    </div>

    <!-- Feedback message -->
    <div class="errorMessage" v-if="errorMessage409">
      <p>Este codigo ya ha sido consumido</p>
    </div>
    <div class="errorMessage" v-if="errorMessage404">
      <p>Este palot no existe</p>
    </div>
    <div class="okMessage" v-if="okMessage">
      <p>Este palot a sido leido y guardado correctamente</p>
    </div>

    <!-- Barcode scanner input -->
    <input
      class="input"
      name="barcode"
      v-model="palot.lote_number"
      v-on:keyup.enter="sentData(palot)"
      ref="myInput"
      autofocus
      type="text"
      id="barCodeInput"
      placeholder="Codigo de barras"
    />
    <div class="btn bottom">
      <button @click="goToLines">Volver a Lineas</button>
    </div>
  </body>
</template>

<script>
export default {
  name: "barcode",
  data() {
    return {
      palot: {
        project: this.$route.params.line,
        lote_number: "",
      },
      color: 'white',
      correctBarCode: false,
      isLoading: false,
      controlVariable:true,
      errorMessage409: false,
      errorMessage404: false,
      okMessage: false,
    };
  },
  computed: {
    
  },
  mounted() {
    this.inputDisabledFalse();
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
      this.controlVariable = false;
      this.isLoading= true
      this.errorMessage = false;
      this.okMessage = false;

      
      document.getElementById("barCodeInput").disabled = true
      let response = await fetch("https://192.168.21.113:8081/api/barcode", settings);
      if (response.status == 200) {
        this.isLoading = false;
        this.errorMessage409 = false;
        this.errorMessage404 = false;
        this.okMessage = true;
        this.color= "green";
        document.getElementById("barCodeInput").disabled= false
        this.controlVariable = true;
        this.palot.lote_number = "";
        this.correctBarCode = true;
        this.setFocus();
      }
      if (response.status == 409) {
        this.isLoading = false;
        this.okMessage = false;
        document.getElementById("barCodeInput").disabled= false  
        this.controlVariable = true;
        this.errorMessage404 = false
        this.errorMessage409 = true;
        this.palot.lote_number = "";
        this.correctBarCode = true;
        this.setFocus();
      }
      if (response.status == 404) {
        this.isLoading = false;
        this.okMessage = false;
        this.errorMessage409 = false
        document.getElementById("barCodeInput").disabled= false  
        this.controlVariable = true;
        this.errorMessage404 = true;
        this.palot.lote_number = "";
        this.correctBarCode = true;
        this.setFocus();
      }
    },
    inputDisabledFalse(){
      var input = document.getElementById("barCodeInput")
      input.disabled= false
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
      
    },
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@800&display=swap');

body{
  justify-content: center;
  min-height: 100vh;
}
.project{
  color: rgb(3, 8, 70);
  margin-top: 2em;
  font-size: 3em;
}
.instruction{
  font-family: 'Open Sans', sans-serif;
  font-size: 4em;
  color: rgb(3, 8, 70);
}
.input{
  margin: 10%;
}


/* Loading effect */
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
/* Error mesage */
.errorMessage{
  border: 1px solid red;
  background-color: red;
  margin: 10px;
  font-weight: 900;
  color: white;
}
.okMessage{
  border: 1px solid green;
  background-color: green;
  margin: 10px;
  font-weight: 900;
  color: white;
}

/* button style */
button {
  align-items: center;
  appearance: none;
  background-image: radial-gradient(100% 100% at 100% 0, #00478d 0, #020c47 100%);
  border: 0;
  border-radius: 6px;
  box-shadow: rgb(0, 0, 0) 0 2px 4px,rgb(10, 7, 15) 0 7px 13px -3px,rgb(17, 19, 32) 0 -3px 0 inset;
  box-sizing: border-box;
  color: #fff;
  cursor: pointer;
  display: inline-flex;
  font-family: "JetBrains Mono",monospace;
  font-weight: 900;;
  height: 10vh;
  min-width: 95vw;
  justify-content: center;
  line-height: 1;
  list-style: none;
  overflow: hidden;
  padding-left: 16px;
  padding-right: 16px;
  position:relative;
  text-align: left;
  text-decoration: none;
  transition: box-shadow .15s,transform .15s;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  white-space: nowrap;
  will-change: box-shadow,transform;
  font-size: 18px;
}

button:focus {
  box-shadow: #3c4fe0 0 0 0 1.5px inset, rgba(45, 35, 66, .4) 0 2px 4px, rgba(45, 35, 66, .3) 0 7px 13px -3px, #3c4fe0 0 -3px 0 inset;
}

button:hover {
  box-shadow: rgba(45, 35, 66, .4) 0 4px 8px, rgba(45, 35, 66, .3) 0 7px 13px -3px, #3c4fe0 0 -3px 0 inset;
  transform: translateY(-2px);
}

button:active {
  box-shadow: #3c4fe0 0 3px 7px inset;
  transform: translateY(2px);
}
.bottom{
  position: absolute;
  bottom: 0;
}

</style>