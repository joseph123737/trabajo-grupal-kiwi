module.exports = {
    devServer: {
        https: true,
        proxy: {
          "^/api": {
            target: "http://192.168.21.143:5000/",
            ws: true,
            changeOrigin: true,
          },
        },
      },
 } 
