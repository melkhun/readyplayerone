const GoogleFontsPlugin = require("google-fonts-webpack-plugin");

module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false
    }
  },
}