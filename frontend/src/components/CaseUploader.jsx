import { useState } from 'react';
import { uploadCase } from '../api';

export default function CaseUploader() {
  const [caseText, setCaseText] = useState('');

  const handleUpload = async () => {
    const status = await uploadCase(caseText);
    alert(status);
    setCaseText('');
  };

  return (
    <div className="bg-gray-900 p-4 rounded-xl shadow-md mb-6">
      <textarea
        rows={6}
        className="w-full p-3 rounded-md bg-gray-700 text-white border border-purple-600 focus:outline-none focus:ring-2 focus:ring-purple-400"
        placeholder="Paste your case here..."
        value={caseText}
        onChange={(e) => setCaseText(e.target.value)}
      />
      <button
        onClick={handleUpload}
        className="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-2 mt-3 rounded-md transition-all duration-200"
      >
        Upload Case
      </button>
    </div>
  );
}
