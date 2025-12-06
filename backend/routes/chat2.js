// routes/chat2.js
const express = require('express');
const { GoogleGenerativeAI } = require('@google/generative-ai');

const router = express.Router();

// ✅ Use API key from backend .env
const apiKey = process.env.GEMINI_API_KEY;

if (!apiKey) {
  console.error('❌ GEMINI_API_KEY is not set in backend .env');
}

const genAI = new GoogleGenerativeAI(apiKey);

// ✅ Use a currently available model (1.5 is giving 404 now)
const model = genAI.getGenerativeModel({
  // model: 'gemini-1.5-flash',          // ⛔ OLD – gives 404
  // model: 'gemini-2.0-flash',          // ✅ option 1
  model: 'gemini-2.5-flash',             // ✅ option 2 (newer, often recommended)
  systemInstruction:
    'You are pretending to be a legal advisor. You will provide answers to queries based on the ruleset used in India. Do not answer vaguely. Give clear steps on how the user can proceed in that situation. Refer to yourself as legal advisor. Only provide the legal side of the queries.',
  generationConfig: {
    maxOutputTokens: 8192,
    temperature: 1,
    topP: 0.95,
    topK: 40,
  },
});

// POST /api/vertex  → generate legal answer
router.post('/vertex', async (req, res) => {
  try {
    const { message } = req.body;

    if (!message) {
      return res.status(400).json({ error: 'Message is required' });
    }

    const result = await model.generateContent(message);
    const response = result.response;
    const text = response.text();

    res.json({ content: text });
  } catch (error) {
    console.error('Gemini backend error:', error);
    res.status(500).json({
      error: 'Failed to get response from Gemini',
      details: error.message,
    });
  }
});

// Health check
router.get('/vertex/health', (req, res) => {
  res.status(200).json({ status: 'OK' });
});

module.exports = router;
