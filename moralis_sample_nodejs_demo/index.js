require('dotenv').config();

const express = require("express");
// Import Moralis
const Moralis = require("moralis").default;
// Import the EvmChain dataType
const { EvmChain } = require("@moralisweb3/common-evm-utils");

const app = express();
const port = 3000;

// Add a variable for the api key, address and chain
const MORALIS_API_KEY = process.env.MORALIS_API_KEY;
const address = process.env.EHTEREUM_ADDRESS;
const chain = EvmChain.ETHEREUM;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

// Add this a startServer function that initialises Moralis
const startServer = async () => {
  await Moralis.start({
    apiKey: process.env.MORALIS_API_KEY,
  });

  app.listen(port, () => {
    console.log(`Example app listening on port ${port}; http://localhost:3000/`);
  });
};

// Call startServer()
startServer();


async function getDemoData() {
  // Get native balance
  const nativeBalance = await Moralis.EvmApi.balance.getNativeBalance({
    address,
    chain,
  });

  // Format the native balance formatted in ether via the .ether getter
  const native = nativeBalance.result.balance.ether;

  return { native };
}

app.get("/demo", async (req, res) => {
  try {
    // Get and return the crypto data
    const data = await getDemoData();
    res.status(200);
    res.json(data);
  } catch (error) {
    // Handle errors
    console.error(error);
    res.status(500);
    res.json({ error: error.message });
  }
});