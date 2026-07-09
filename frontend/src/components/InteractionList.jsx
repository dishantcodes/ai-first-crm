import { useEffect, useState } from "react";
import api from "../services/api";


function InteractionList() {

  const [interactions, setInteractions] = useState([]);


  const fetchInteractions = async () => {

    try {

      const response = await api.get("/interaction/");

      setInteractions(response.data);

    } catch (error) {

      console.log(error);

    }

  };


  useEffect(() => {

    fetchInteractions();

  }, []);



  return (

    <div>

      <h2>📋 Interaction History</h2>


      {
        interactions.map((item) => (

          <div className="card" key={item.id}>


            <h3>
              🩺 {item.interaction_type}
            </h3>


            <p>
              <b>Notes:</b>
              <br />
              {item.notes}
            </p>


            <p>
              <b>🤖 AI Summary:</b>
              <br />
              {item.ai_summary || "Generating summary..."}
            </p>


            <p>
              <b>➡️ Next Action:</b>
              <br />
              {item.next_action || "No action suggested"}
            </p>


            <small>
              Created: {new Date(item.created_at).toLocaleString()}
            </small>


          </div>

        ))
      }


    </div>

  );

}


export default InteractionList;
