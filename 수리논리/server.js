const express = require("express");
const bodyParser = require("body-parser");
const path = require('path');
const app = express();
const port = 8081;
const apiKey = "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"; // 여기에 OpenAI API 키를 입력하세요

app.use(bodyParser.json());

app.post("/chat", async (req, res) => {
    const message = req.body.message;
    const openaiURL = "https://api.openai.com/v1/chat/completions";

    try {
        const { default: fetch } = await import("node-fetch");

        const response = await fetch(openaiURL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                "model": "gpt-3.5-turbo",
                "messages": [
                    { "role": "system", "content": "You are a helpful assistant." },
                    { "role": "user", "content": message }
                ]
            })
        });

        const data = await response.json();
        const botReply = data.choices[0].message.content;
        res.json({ message: botReply });
    } catch (error) {
        console.error("Error:", error);
        res.status(500).json({ error: "An error occurred" });
    }
});

app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname, 'index.html'));
  });
  

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});