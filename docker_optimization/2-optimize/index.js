const express = require("express");
const app = express();
const PORT = 3000;

app.get("/", (req, res) => res.send("Optimize me, now smaller! test test \n"));

app.listen(PORT, () => console.log(`Listening on port ${PORT}`));
