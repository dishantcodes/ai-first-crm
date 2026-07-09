import "./App.css";

import HCPForm from "./components/HCPForm";
import HCPList from "./components/HCPList";
import InteractionForm from "./components/InteractionForm";
import InteractionList from "./components/InteractionList";
import ChatInterface from "./components/ChatInterface";


function App() {

  return (
    <div className="container">

      <h1>🏥 AI-First CRM</h1>

      <p>
        Healthcare Professional Management
      </p>


      <hr />

      <HCPForm />


      <hr />

      <HCPList />


      <hr />

      <InteractionForm />


      <hr />

      <InteractionList />


      <hr />

      <ChatInterface />


    </div>
  );
}


export default App;
