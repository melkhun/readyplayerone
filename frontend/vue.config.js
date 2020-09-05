const GoogleFontsPlugin = require("google-fonts-webpack-plugin");

module.exports = {
  "transpileDependencies": [
    "vuetify"
  ], devServer: {
    proxy: 'https://localhost:8080'
}
}