const merge = require("webpack-merge");
const common = require("./webpack.common.js");
const webpack = require("webpack");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = merge(common, {
  // devtool: "eval",
  devServer: {
    historyApiFallback: true,
    noInfo: true
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: "./templates/index.html"
    }),
    new webpack.HotModuleReplacementPlugin()
  ],
  mode: 'development'
});
