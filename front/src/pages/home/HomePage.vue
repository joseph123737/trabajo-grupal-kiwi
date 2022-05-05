<template>
  <body class="home">
    <ul>
      <li>
        <button>
          LINEA CESTAS
        </button>
      </li>
      <li>
        <button>
          LINEA CALIBRADO
        </button>
      </li>
      <li>
        <button>
          CUADRE EXISTENCIAS
        </button>
      </li>
    </ul>
  </body>
</template>

<script>

export default {
  name: 'Home',
  


}
</script>

<style scoped>
body {
  height: 100%;
  overflow-y: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}
ul{
  padding: 0;
  margin: 0;
}
li{
  list-style: none;
  border: 1px solid black;
  border-radius: 30px;
  width: 50vw;
  height: 25vh;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 3%;
}
button {
  background: none;
	color: inherit;
	border: none;
	padding: 0;
	font: inherit;
	cursor: pointer;
	outline: inherit;
}
</style>
