const GoogleFontsPlugin = require("google-fonts-webpack-plugin");

module.exports = {devServer: {
  proxy: 'https://localhost:8888'
},
  "transpileDependencies": [
    "vuetify"
  ], 
}