<template>
<div id="prueba">
  <body v-bind:style="{ backgroundColor: color}">

  <div v-bind:class={selectedLineCestas:selectedLineCestas,selectedLineCalibrado:selectedLineCalibrado}>
    <h2 class="project">- {{ this.palot.project }} -</h2>
  </div>
  <div>
    <div class="instruccionDiv">
      <p class="instruction" v-if="!selectMessage" >ESCANEE EL PALOT</p>
      <p class="instruction " v-if="selectMessage" >ESCOJA UNA LINEA</p>
    </div>    
    
    
    <div class="container" v-if="isLoading">
        <div class="ring"></div>
    </div>

    <section >

    
    <div class="errorMessage" v-if="errorMessage409">
      <p>DUPLICADO</p>
    </div>
    <div class="errorMessage" v-if="errorMessage404">
      <p>ERROR</p>
    </div>
    <div class="errorMessageNoLine" v-if="errorMessageNoLineSelected">
      <p>DEBE SELECCIONAR UNA LINEA</p>
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
<<<<<<< HEAD
   <button @click="prueba">aaaaaaaaaaaa</button>
=======
    </section>
  </div>
  
>>>>>>> b4f90e124fb808c1cbd529fbd7fbda0dca182e71
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
      selectedLineCalibrado:false,
      selectedLineCestas:false,
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
       this.selectedLineCestas = true
       this.errorMessage409=false;
      this.errorMessage404=false;
      this.okMessage= false;
      this.selectMessage = false;
      } 
      else if (palot.lote_number == ("L.CALIBRADO")){this.palot.project = palot.lote_number;
       this.palot.lote_number = "";
       this.errorMessageNoLineSelected = false
       this.color="white";
       this.selectedLineCalibrado = true
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
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap');

*{
  font-family: 'Roboto', sans-serif;
  color:black;
}

#audio{
  display: none;
}
.selectedLineCestas{
  background-color: orange;
  color: white;
  align-items: center;
  padding: 0.3%;
  text-align: center;
}

.selectedLineCalibrado{
  background-color: rgb(38, 0, 255);
  text-align: center;
  margin: 0;
  color: white;
}
body{
  justify-content: center;
  min-height: 80vh;
  background-color:antiquewhite;
}

.instruction{
  font-size: 3.5em;
  margin-top: 1em;
}
.errorMessage>p{
  font-size: 3rem;
}
.okMessage>p{
  font-size: 3rem;
}

 
<<<<<<< HEAD
  .input[data-v-600ef54c] {
	text-align: center;
	margin: 5%;
	width: 60%;
	height: 2rem;
	border: 2px solid #00478d;
}
=======
>>>>>>> b4f90e124fb808c1cbd529fbd7fbda0dca182e71



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
.input{
  margin-left: -10000px !important;
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
  margin-top:em
  
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



.project {
  align-items: center;
  border: 0;
  box-sizing: border-box;
  color: #FFFFFF;
  display: flex;
  font-size: 3em;
  justify-content: center;
  line-height: 1em;
  height: 10vh;
  max-width: 100%;
  min-width: 140px;
  padding: 19px 24px;
  
  
}



@media (min-width: 768px) {
  .button-63 {
    font-size: 24px;
    min-width: 196px;
  }
}


</style>