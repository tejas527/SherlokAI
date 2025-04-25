import ChatBox from './components/ChatBox';
import CaseUploader from './components/CaseUploader';

function App() {
  return (
    <div className="min-h-screen bg-black text-purple-100 p-4 flex flex-col items-center">
      <div className="w-full max-w-2xl">
        <h1 className="text-3xl font-extrabold mb-6 text-center text-purple-400">🕵️ SherlockAI</h1>
        <CaseUploader />
        <ChatBox />
      </div>
    </div>
  );
}

export default App;
