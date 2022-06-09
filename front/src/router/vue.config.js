import {back} from "config.js"
module.exports = {
    devServer: {
        proxy: {
          "^/api": {
            target: back,
            ws: true,
            changeOrigin: true,
          },
        },
      },
 } 
