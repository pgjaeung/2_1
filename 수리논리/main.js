const openai = require('openai');

const api_key = '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';
openai.api_key = api_key;

const messages = [
  { role: 'system', content: 'You are an intelligent assistant.' }
];

async function runChat() {
  while (true) {
    let userFinished = false;

    while (true) {
      const message = prompt('User: ');
      if (message === 'exit') {
        userFinished = true;
        break;
      } else if (message) {
        messages.push({ role: 'user', content: message });
      } else {
        userFinished = true;
      }
    }

    const chat = await openai.ChatCompletion.create({
      model: 'gpt-3.5-turbo',
      messages: messages
    });

    const reply = chat.choices[0].message.content;

    console.log(`ChatGPT: ${reply}`);

    messages.push({ role: 'assistant', content: reply });

    if (userFinished) {
      break;
    }
  }
}

runChat();