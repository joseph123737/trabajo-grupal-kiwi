import {backUrl} from "@/config.js"
module.exports = {
    devServer: {
        proxy: {
          "^/api": {
            target: backUrl,
            ws: true,
            changeOrigin: true,
          },
        },
      },
 } 
