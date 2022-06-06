<template>
  <body v-bind:style="{ backgroundColor: color}">
    <h2 class="project">{{ this.palot.project }}</h2>
    <h2>{{this.counter}}</h2>
    <div class="container" v-if="isLoading">
        <div class="ring"></div>
    </div>
    <div class="errorMessage" v-if="errorMessage409">
      <p>Este codigo ya ha sido consumido</p>
    </div>
    <div class="errorMessage" v-if="errorMessage404">
      <p>Este palot no existe</p>
    </div>
    <div class="okMessage" v-if="okMessage">
      <p>Este palot a sido leido y guardado correctamente</p>
    </div>

    <input
      name="barcode"
      v-model="palot.lote_number"
      v-on:keyup.enter="sentData(palot)"
      ref="myInput"
      autofocus
      type="text"
      id="barCodeInput"
      placeholder="Codigo de barras"
      
    />
    <button @click="goToLines">ELEGIR LINEA</button>
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
      counter: 0,
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
      let response = await fetch("https://localhost:8080/api/barcode", settings);
      if (response.status == 200) {
        this.isLoading = false;
        this.errorMessage409 = false;
        this.errorMessage404 = false;
        this.okMessage = true;
        this.color= "green";
        document.getElementById("barCodeInput").disabled= false
        this.controlVariable = true;
        this.palot.lote_number = "";
        this.counter += 1;
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
        this.counter += 1;
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
        this.counter += 1;
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

<style>
body{
  justify-content: center;
  min-height: 100vh;
}
.correctBarCode {
  background-color: rgb(95, 207, 95);
  border: 2px solid green;
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
  background-image: radial-gradient(100% 100% at 100% 0, #5adaff 0, #5468ff 100%);
  border: 0;
  border-radius: 6px;
  box-shadow: rgba(45, 35, 66, .4) 0 2px 4px,rgba(45, 35, 66, .3) 0 7px 13px -3px,rgba(58, 65, 111, .5) 0 -3px 0 inset;
  box-sizing: border-box;
  color: #fff;
  cursor: pointer;
  display: inline-flex;
  font-family: "JetBrains Mono",monospace;
  height: 10vh;
  width: 100vw;
  justify-content: center;
  line-height: 1;
  list-style: none;
  overflow: hidden;
  padding-left: 16px;
  padding-right: 16px;
  position: relative;
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

</style>