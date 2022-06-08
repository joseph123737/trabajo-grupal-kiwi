module.exports = {
    devServer: {
        proxy: {
          "^/api": {
            target: "http://192.168.21.143:5000/",
            ws: true,
            changeOrigin: true,
          },
        },
      },
 } 
