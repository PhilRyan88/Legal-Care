const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const dotenv = require("dotenv");

dotenv.config(); // ✅ load env FIRST

const authRoutes = require("./routes/auth");
const chatRoutes = require("./routes/chat.js");
const chat2Routes = require("./routes/chat2.js"); // ✅ now env is ready when this runs

const app = express();

app.use(cors());
app.use(express.json());

app.use("/api", chatRoutes);
app.use("/api", authRoutes);
app.use("/api", chat2Routes);

const PORT = process.env.PORT || 5000;
mongoose
  .connect(
    "mongodb+srv://crispyfingers:crispyDB@cluster0.k22ya.mongodb.net/legalAD?retryWrites=true&w=majority&appName=Cluster0"
  )
  .then(() => {
    app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
  })
  .catch((err) => console.error("Error connecting to MongoDB:", err));
