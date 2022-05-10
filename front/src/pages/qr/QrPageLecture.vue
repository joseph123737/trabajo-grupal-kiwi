<template>
  <body>
    <div id="reader" >
      
    </div>
  </body>
</template>
<script>
import { Html5QrcodeScanner } from "html5-qrcode";
export default {
  name: "QrCode",
  data() {
    return {
        palot: {
        lineName: localStorage.line,
        varCode: "",
      },
      
    };
  },
  mounted (){
      this.barcodeReader();
  },
  methods: {
    barcodeReader() {
      let html5QrcodeScanner = new Html5QrcodeScanner(
        "reader",
        { fps: 10, qrbox: { width: 250, height: 50 } },
        false
      );
      html5QrcodeScanner.render(this.onScanSuccess, this.onScanFailure);
    },
    onScanSuccess(decodedText, decodedResult) {
        this.palot.varCode = decodedText
        if (this.decodedText != ""){
            this.sentData(this.palot)
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
       await fetch("http://localhost:5000/api/barcode", settings);
    }
  },
};
</script>
