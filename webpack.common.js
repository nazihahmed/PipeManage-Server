const path = require("path");
const ManifestPlugin = require("webpack-manifest-plugin");
const CleanWebpackPlugin = require("clean-webpack-plugin");
const webpack = require("webpack");

module.exports = {
  entry: "./static/index.js",
  output: {
    filename: "main.js",
    path: path.resolve(__dirname, "dist")
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  },
  plugins: [
    new ManifestPlugin(),
    new CleanWebpackPlugin(["dist"])
  ],
  resolve: {
    modules: ["node_modules"],
    extensions: [".js", ".svg", ".gif", ".png"]
  }
};
