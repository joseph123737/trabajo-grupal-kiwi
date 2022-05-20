<template>
  <body>
    <div class="container">
        <div class="ring"></div>
        <p>Loading...</p>
    </div>
  </body>
  
</template>

<script>
export default {
    name: "LoadingScreen"

}
</script>

<style>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
    display:flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}
.container{
    position:relative;
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

.container p{
    position:absolute;
    color: #fff;
    font-size: 1.5em;
    font-family: consolas, "Courier New", monospace;
    bottom: -80px;
    letter-spacing: 0.15em;
}
</style>