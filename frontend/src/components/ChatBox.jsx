import { useState } from 'react';
import { sendMessage } from '../api';

export default function ChatBox() {
  const [chat, setChat] = useState([]);
  const [input, setInput] = useState('');

  const handleSend = async () => {
    if (!input.trim()) return;

    const userLine = `🧍 You: ${input}`;
    const reply = await sendMessage(input);
    const botLine = `🤖 Bot: ${reply}`;
    setChat([...chat, userLine, botLine]);
    setInput('');
  };

  return (
    <div className="bg-gray-900 p-4 rounded-xl shadow-md">
      <div className="h-64 overflow-y-auto bg-gray-800 p-3 rounded mb-3 text-sm scroll-smooth">
        {chat.map((line, i) => (
          <div key={i} className="mb-2">{line}</div>
        ))}
      </div>
      <textarea
        rows={3}
        className="w-full p-3 rounded-md bg-gray-700 text-white border border-purple-600 focus:outline-none focus:ring-2 focus:ring-purple-400"
        value={input}
        placeholder="Ask a question..."
        onChange={(e) => setInput(e.target.value)}
      />
      <button
        onClick={handleSend}
        className="w-full bg-purple-600 hover:bg-purple-700 text-white font-semibold py-2 mt-3 rounded-md transition-all duration-200"
      >
        Send
      </button>
    </div>
  );
}
