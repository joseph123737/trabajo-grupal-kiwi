<template>
  <body>
    <h1>{{ project }}</h1>

    <button @click="startProcess">Start</button>
    <div id="reader"></div>
  </body>
</template>
<script>
import { Html5QrcodeScanner } from "html5-qrcode";
export default {
  name: "QrCode",
  data() {
    return {
      palot: {
        project: localStorage.line,
        loteNumber: "",
      },
    };
  },
  mounted() {
    
  },
  methods: {
    startProcess(){
      this.barcodeReader()
    },
    repeatTheLoop(){
      setInterval(this.barcodeReader,3000);
    },
    barcodeReader() {
      console.log("hola")
      let html5QrcodeScanner = new Html5QrcodeScanner(
        "reader",
        { fps: 10, qrbox: { width: 250, height: 50 } },
        false
      );
      
      html5QrcodeScanner.render(this.onScanSuccess, this.onScanFailure);
    },
    onScanSuccess(decodedText, decodedResult) {
      this.palot.barCode = decodedText;
      if (this.decodedText != "") {
        this.sentData(this.palot);
        this.html5QrcodeScanner.clear()
      }

      console.log(`Code matched = ${decodedText}`, decodedResult);
      
    },
    onScanFailure(error) {
      console.warn(`Code scan error = ${error}`);
    },
    
    async sentData(palot) {
      const settings = {
        method: "POST",
        body: JSON.stringify(palot),
        headers: {
          "Content-Type": "application/json",
        },
      };
      console.log(palot);
      await fetch("https://192.168.21.62:8081/api/barcode", settings);
      // if (response == "200"){
      //   this.barcodeReader()
      
      // }else{
      //   this.barcodeReader()
      // }
    },
  },
};
</script>
