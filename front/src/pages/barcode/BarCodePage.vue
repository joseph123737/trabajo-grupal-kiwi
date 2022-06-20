<template>
<div id="prueba">
  <body v-bind:style="{ backgroundColor: color}">

   
    <h2 class="project" v-bind:style="{color: lineColor}">-{{ this.palot.project }}-</h2>
    <p class="instruction" v-if="!selectMessage" >ESCANEE EL C.B. DEL PALOT</p>
    <p class="instruction " v-if="selectMessage" >ESCOJA UNA LINEA DE TRABAJO </p>
    
    <div class="container" v-if="isLoading">
        <div class="ring"></div>
    </div>

    
    <div class="errorMessage" v-if="errorMessage409">
      <p>DUPLICADO</p>
    </div>
    <div class="errorMessage" v-if="errorMessage404">
      <p>ERROR</p>
    </div>
    <div class="errorMessageNoLine" v-if="errorMessageNoLineSelected">
      <p>ERROR ESCANEE UN QR</p>
    </div>
    <div class="okMessage" v-if="okMessage">
      <p>OK</p>
    </div>
    <audio id="audio" controls><source type="audio/wav" src="@/assets/audio/grocery-scanning_1.wav"></audio>

    
    <input
      class="input"
      name="barcode"
      v-model="palot.lote_number"
      v-on:keyup.enter="inputData(palot)"
      @click="inputData(palot)"
      ref="myInput"
      autofocus
      type="text"
      id="barCodeInput"
      placeholder="Codigo de barras"
      autocomplete="off"
    />
   <button @click="prueba">aaaaaaaaaaaa</button>
  </body>
</div> 
</template>

<script>
import {config} from "@/config.js"
export default {
  name: "barcode",
  data() {
    return {
      palot: {
        project: "",
        lote_number: "",
      },
      lineColor:"",
      color: 'white',
      correctBarCode: false,
      isLoading: false,
      controlVariable:true,
      errorMessage409: false,
      errorMessage404: false,
      errorMessageNoLineSelected:false,
      okMessage: false,
      selectMessage:true,
    };
  },
  computed: {
    
  },
  mounted() {
    this.inputDisabledFalse();
    
    setInterval(()=>{
      this.setFocus();
    },500);
    setTimeout(() => {
      this.isLoading = false;
    }, 1500);

    
  },
  methods: {
    prueba(){
      let a = document.getElementById("prueba")
      a.disabled = true
    },
    inputData(palot){
      if (palot.lote_number == ("L.CESTAS")){this.palot.project = palot.lote_number;
       this.palot.lote_number = "";
       this.errorMessageNoLineSelected =false 
       this.color="white";
       this.lineColor="orange";
       this.errorMessage409=false;
      this.errorMessage404=false;
      this.okMessage= false;
      this.selectMessage = false;
      } 
      else if (palot.lote_number == ("L.CALIBRADO")){this.palot.project = palot.lote_number;
       this.palot.lote_number = "";
       this.errorMessageNoLineSelected = false
       this.color="white";
       this.lineColor="purple";
       this.errorMessage409=false;
      this.errorMessage404=false;
      this.okMessage= false;
      this.selectMessage = false;
      } 
     else{
        this.sentData(palot);
      }
    },
    async sentData(palot) {
        if(palot.project === ""){
          this.errorMessageNoLineSelected = true
          this.palot.lote_number = "";
        }else{
          
        let myAudio = document.getElementById("audio")
        myAudio.play()
        const settings = {
        method: "POST",
        body: JSON.stringify(palot),
        headers: {
          "Content-Type": "application/json",
        },
      };
      this.color="white"
      this.errorMessage409=false;
      this.errorMessage404=false;
      this.okMessage= false;
      this.controlVariable = false;
      this.isLoading= true
      this.errorMessage = false;
      this.okMessage = false;

      
      document.getElementById("barCodeInput").disabled = true
      
      let response = await fetch(`${config.API_PATH}api/barcode`, settings);
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
        this.color= "red";
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
        this.color="red";
        this.palot.lote_number = "";
        this.correctBarCode = true;
        this.setFocus();
      }
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
    goToLines(){
      this.$router.push("/selectLine")
    }
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@800&display=swap');
#audio{
  display: none;
}

body{
  justify-content: center;
  max-height: 100vh;
}
.project{
  color: rgb(3, 8, 70);
  margin-top: 0.7em;
  font-size: 3em;
}
.instruction{
  font-family: 'Open Sans', sans-serif;
  font-size: 3.5em;
  color: rgb(3, 8, 70);
}
.errorMessage>p{
  font-size: 3rem;
}
.okMessage>p{
  font-size: 3rem;
}

 
  .input[data-v-600ef54c] {
	text-align: center;
	margin: 5%;
	width: 60%;
	height: 2rem;
	border: 2px solid #00478d;
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
  margin: 5px;
  font-weight: 900;
  color: white;
}
.errorMessageNoLine>p{
  color: red;
  font-size: 3rem;
  font-weight: 900;
}
.okMessage{
  border: 1px solid green;
  background-color: green;
  margin: 5px;
  font-weight: 900;
  color: white;
}

/* button style */
button {
  margin-top: 20px;
  margin-left: 13px;
  align-items: center;
  appearance: none;
  background-image: radial-gradient(100% 100% at 100% 0, #00478d 0, #061150 100%);
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
  min-width: 85vw;
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




</style>