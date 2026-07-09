import { useState } from "react";
import api from "../services/api";


function ChatInterface() {

  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);


  const askAI = async () => {

    if (!question.trim()) return;


    const userMessage = {
      type: "user",
      text: question
    };


    setMessages((prev) => [
      ...prev,
      userMessage
    ]);


    setQuestion("");


    try {

      const response = await api.post("/ai/chat", {
        question: userMessage.text
      });


      const aiMessage = {
        type: "ai",
        text: response.data.answer
      };


      setMessages((prev) => [
        ...prev,
        aiMessage
      ]);


    } catch (error) {

      setMessages((prev) => [
        ...prev,
        {
          type: "ai",
          text: "Something went wrong"
        }
      ]);

    }

  };


  return (

    <div className="card">

      <h2>🤖 AI CRM Assistant</h2>


      <div>

        {
          messages.map((msg, index) => (

            <div
              key={index}
              style={{
                textAlign: msg.type === "user" ? "right" : "left",
                margin: "10px"
              }}
            >

              <span
                style={{
                  display: "inline-block",
                  padding: "10px",
                  borderRadius: "10px",
                  background:
                    msg.type === "user"
                    ? "#2563eb"
                    : "#e5e7eb",
                  color:
                    msg.type === "user"
                    ? "white"
                    : "black",
                  maxWidth:"70%"
                }}
              >

                {msg.text}

              </span>


            </div>

          ))
        }


      </div>



      <input
        placeholder="Ask AI about your CRM..."
        value={question}
        onChange={(e)=>setQuestion(e.target.value)}
      />


      <button onClick={askAI}>
        Send
      </button>


    </div>

  );

}


export default ChatInterface;
