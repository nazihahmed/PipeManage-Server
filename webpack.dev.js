const merge = require("webpack-merge");
const common = require("./webpack.common.js");
const webpack = require("webpack");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = merge(common, {
  devtool: "eval",
  devServer: {
    contentBase: "./public",
    port: 8444,
    proxy: {
      "/oauth": "http://localhost:8443",
      "/rest": "http://localhost:8443",
      "/mock": "http://localhost:8443",
      "/socket.io": {
        target: "ws://localhost:8443",
        ws: true,
        secure: false
      }
    }
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: "./public/index.ejs"
    }),
    new webpack.DefinePlugin({
      DEV: true
    })
  ]
});
