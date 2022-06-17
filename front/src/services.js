
export function createdBodyXml(lineName,loteNumber){
    let Body = `<?xml version="1.0" encoding="UTF-8"?>
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:app="urn:microsoft-dynamics-schemas/codeunit/APP_MGMT">
    <soapenv:Header/>
    <soapenv:Body>
        <app:CheckConsumption>
          <app:pJobNo>${lineName}</app:pJobNo>
          <app:pBarcode>${loteNumber}</app:pBarcode>
          <app:pResourceNo >IK</app:pResourceNo >
        </app:CheckConsumption>
    </soapenv:Body>
    </soapenv:Envelope>`


    return Body

}
export function sendDataToErp(body){

  const settings = {
    method: "POST",
    body: body,
    headers: {
      "Content-Type": "text/xml; charset=utf-8",
      "Connection": "Keep-Alive",
      "User-Agent": "PHP-SOAP-CURL",
      'SOAPAction':'"CheckConsumption"',
      'Authorization': "GARAIAKOOP\\navision:Navi@GaraiaKoop"
    }
  };
  let response =   fetch("http://80.24.99.155:9074/NutriNav2016GaraiaReal/WS/2002%2004%2010%20COPIA%20IK/Codeunit/APP_MGMT",settings)
  console.log(response)

}