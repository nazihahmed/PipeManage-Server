const merge = require("webpack-merge");
const common = require("./webpack.common.js");
const webpack = require("webpack");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = merge(common, {
  devtool: "eval",
  devServer: {
    contentBase: "./static",
    port: 5000
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: "./static/index.js"
    })
  ]
});
